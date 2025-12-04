import copy
from typing import List, Dict

from .ast_nodes import *


class WATEmitter:
    def __init__(self):
        self.lines = []
        self.indent = "  "
        self.funcs_emitted = set()
        self.extra_imports = [
            # '(import "env" "out_i32" (func $out_i32 (param i32)))',
            # '(import "env" "out_f32" (func $out_f32 (param f32)))',
            # '(import "env" "in_i32" (func $in_i32 (result i32)))'
        ]
        self.func_index = {}
        self.loop_stack = []
        self.var_types = {}

    def emit(self, program: ProgramNode) -> str:
        self.func_index = {}
        self.funcs_emitted = set()
        self.lines = []
        
        for f in program.subprograms:
            self.func_index[f.name] = f

        self.lines.append('(module')
        for imp in self.extra_imports:
            self.lines.append(f'{self.indent}{imp}')

        for f in program.subprograms:
            self.func_index[f.name] = f

        for f in program.subprograms:
            self.emit_func(f)

        for stmt in program.statements:
            self.emit_stmt(stmt)

        self.lines.append(')')
        return '\n'.join(self.lines)

    def _collect_calls_in_expr(self, e):
        res = []
        if isinstance(e, FuncCall):
            res.append(e)
            for a in e.args: res.extend(self._collect_calls_in_expr(a))
        elif isinstance(e, BinaryOp):
            res.extend(self._collect_calls_in_expr(e.left))
            res.extend(self._collect_calls_in_expr(e.right))
        elif isinstance(e, UnaryOp):
            res.extend(self._collect_calls_in_expr(e.expr))
        elif isinstance(e, CastExpr):
            res.extend(self._collect_calls_in_expr(e.expr))
        return res

    def _mangle(self, name, templ_args):
        safe = [t.replace(' ', '').replace('<','').replace('>','') for t in templ_args]
        return name + "__" + "_".join(safe)

    def _map_type(self, t):
        if t == 'float': return 'f32'
        return 'i32'

    def _get_expr_type(self, e):
        if isinstance(e, IntLiteral): return 'int'
        if isinstance(e, FloatLiteral): return 'float'
        if isinstance(e, StringLiteral): return 'int'
        if isinstance(e, VarRef):
            return self.var_types.get(e.name, 'int')
        if isinstance(e, BinaryOp):
            if e.op == '=': return self._get_expr_type(e.left)
            if e.op in ['==', '!=', '<', '<=', '>', '>=', '&&', '||']: return 'int'
            t_left = self._get_expr_type(e.left)
            t_right = self._get_expr_type(e.right)
            if t_left == 'float' or t_right == 'float': return 'float'
            return 'int'
        if isinstance(e, SubprogramCall):
            f = self.func_index.get(e.name)
            if f:
                return f.ret_type # может вернуть 'void'
            return 'int'
        if isinstance(e, UnaryOp):
            return self._get_expr_type(e.expr)
        return 'int'

    def emit_func(self, func: SubprogramNode):
        if func.name in self.funcs_emitted: return
        self.funcs_emitted.add(func.name)
        self.var_types = {}

        wasm_params_parts = []
        for i, pname in enumerate(func.params):
            ptype = 'int'
            if func.param_types and i < len(func.param_types):
                ptype = func.param_types[i]
            self.var_types[pname] = ptype
            wtype = self._map_type(ptype)
            wasm_params_parts.append(f'(param ${pname} {wtype})')
        
        wasm_params = ' '.join(wasm_params_parts)
        wasm_ret = ''
        if func.ret_type and func.ret_type != 'void':
            wasm_ret = f'(result {self._map_type(func.ret_type)})'
            
        self.lines.append(f'{self.indent}(func ${func.name} {wasm_params} {wasm_ret}')
        
        locals_ = self._collect_locals_with_types(func)
        for name, type_ in locals_.items():
            self.var_types[name] = type_
            if name not in func.params:
                self.lines.append(f'{self.indent*2}(local ${name} {self._map_type(type_)})')
        
        for s in func.body.body:
            self.emit_stmt(s)
            
        if func.ret_type and func.ret_type != 'void':
            wtype = self._map_type(func.ret_type)
            zero = '0.0' if wtype == 'f32' else '0'
            const_instr = 'f32.const' if wtype == 'f32' else 'i32.const'
            self.lines.append(f'{self.indent*2}{const_instr} {zero}')

        self.lines.append(f'{self.indent})')
        self.lines.append(f'{self.indent}(export "{func.name}" (func ${func.name}))')

    def _collect_locals_with_types(self, func):
        locs = {}
        def walk(stmts: list[StatementNode]):
            if not stmts: return
            for s in stmts:
                if isinstance(s, VarDecl):
                    locs[s.name] = s.type if s.type else 'int'
                elif isinstance(s, IfStmt):
                    walk(s.then_body.body)
                    if s.else_body:
                        walk(s.else_body.body)
                elif isinstance(s, WhileStmt):
                    walk(s.body.body)
                elif isinstance(s, UntilStmt):
                    walk(s.body.body)
                elif isinstance(s, ForStmt):
                    if s.init and isinstance(s.init, VarDecl):
                         locs[s.init.name] = s.init.type
                    walk(s.body.body)
        walk(func.body.body)
        return locs

    def emit_stmt(self, s):
        indent = self.indent * 2
        
        if isinstance(s, VarDecl):
            if s.init:
                target_type = s.type if s.type else 'int'
                expr_type = self._get_expr_type(s.init)
                self.emit_expr(s.init)
                
                if target_type == 'float' and (expr_type == 'int' or expr_type == 'char'):
                    self.lines.append(f'{indent}f32.convert_i32_s')
                elif (target_type == 'int' or target_type == 'char') and expr_type == 'float':
                    self.lines.append(f'{indent}i32.trunc_f32_s')
                    
                self.lines.append(f'{indent}local.set ${s.name}')
        
        elif isinstance(s, Expr):
            self.emit_expr(s)
            # FIX: Делаем drop только если выражение что-то вернуло (не void)
            if self._get_expr_type(s) != 'void':
                self.lines.append(f'{indent}drop')
        
        elif isinstance(s, Return):
            self.emit_expr(s)
            self.lines.append(f'{indent}return')
            
        elif isinstance(s, IfStmt):
            s: IfStmt
            self.emit_expr(s.cond)
            if self._get_expr_type(s.cond) == 'float':
                 self.lines.append(f'{indent}f32.const 0.0')
                 self.lines.append(f'{indent}f32.ne')
            self.lines.append(f'{indent}if')
            for ts in s.then_body.body:
                self.emit_stmt(ts)
            if s.else_body:
                self.lines.append(f'{indent}else')
                for es in s.else_body.body:
                    self.emit_stmt(es)
            self.lines.append(f'{indent}end')
        
        elif isinstance(s, WhileStmt):
            lb, lc = f"break_{len(self.lines)}", f"cont_{len(self.lines)}"
            self.lines.append(f'{indent}block ${lb}')
            self.lines.append(f'{indent}loop ${lc}')
            self.emit_expr(s.cond)
            self.lines.append(f'{indent}i32.eqz')
            self.lines.append(f'{indent}br_if ${lb}')
            self.loop_stack.append((lb, lc))
            for bs in s.body.body:
                self.emit_stmt(bs)
            self.loop_stack.pop()
            self.lines.append(f'{indent}br ${lc}')
            self.lines.append(f'{indent}end')
            self.lines.append(f'{indent}end')
        
        elif isinstance(s, ForStmt):
            s: ForStmt
            if s.init:
                self.emit_stmt(s.init)
            lb, lc = f"break_{len(self.lines)}", f"cont_{len(self.lines)}"
            self.lines.append(f'{indent}block ${lb}')
            self.lines.append(f'{indent}loop ${lc}')
            if s.cond:
                self.emit_expr(s.cond)
                self.lines.append(f'{indent}i32.eqz')
                self.lines.append(f'{indent}br_if ${lb}')
            self.loop_stack.append((lb, lc))
            for bs in s.body.body:
                self.emit_stmt(bs)
            self.loop_stack.pop()
            if s.step:
                self.emit_expr(s.step)
                self.lines.append(f'{indent}drop')
            self.lines.append(f'{indent}br ${lc}')
            self.lines.append(f'{indent}end')
            self.lines.append(f'{indent}end')

    def emit_expr(self, e):
        indent = self.indent * 2
        
        if isinstance(e, IntLiteral):
            self.lines.append(f'{indent}i32.const {e.value}')
        elif isinstance(e, FloatLiteral):
            self.lines.append(f'{indent}f32.const {e.value}')
        elif isinstance(e, StringLiteral):
            self.lines.append(f'{indent}i32.const 0')
        elif isinstance(e, VarRef):
            self.lines.append(f'{indent}local.get ${e.name}')

        elif isinstance(e, CastExpr):
            self.emit_expr(e.expr)
            src = self._get_expr_type(e.expr)
            dst = e.target_type
            
            if src == dst: pass
            elif (src == 'int' or src == 'char') and dst == 'float':
                self.lines.append(f'{indent}f32.convert_i32_s')
            elif src == 'float' and (dst == 'int' or dst == 'char'):
                self.lines.append(f'{indent}i32.trunc_f32_s')

        elif isinstance(e, BinaryOp):
            if e.op == '=':
                if not isinstance(e.left, VarRef): raise NotImplementedError("Assign to rvalue")
                var_type = self._get_expr_type(e.left)
                val_type = self._get_expr_type(e.right)
                self.emit_expr(e.right)
                
                if var_type == 'float' and (val_type == 'int' or val_type == 'char'):
                    self.lines.append(f'{indent}f32.convert_i32_s')
                elif (var_type == 'int' or var_type == 'char') and val_type == 'float':
                    self.lines.append(f'{indent}i32.trunc_f32_s')
                
                self.lines.append(f'{indent}local.tee ${e.left.name}')
                return

            t_left = self._get_expr_type(e.left)
            t_right = self._get_expr_type(e.right)
            is_float_op = (t_left == 'float' or t_right == 'float')

            if e.op == '^':
                if isinstance(e.right, IntLiteral) and e.right.value == 2 and isinstance(e.left, VarRef):
                     self.emit_expr(e.left)
                     if t_left != 'float': self.lines.append(f'{indent}f32.convert_i32_s')
                     self.emit_expr(e.left)
                     if t_left != 'float': self.lines.append(f'{indent}f32.convert_i32_s')
                     self.lines.append(f'{indent}f32.mul')
                     return
                self.emit_expr(e.left)
                if t_left != 'float': self.lines.append(f'{indent}f32.convert_i32_s')
                self.emit_expr(e.right)
                self.lines.append(f'{indent}drop')
                self.lines.append(f'{indent}f32.sqrt')
                return

            self.emit_expr(e.left)
            if is_float_op and t_left != 'float': self.lines.append(f'{indent}f32.convert_i32_s')
            
            self.emit_expr(e.right)
            if is_float_op and t_right != 'float': self.lines.append(f'{indent}f32.convert_i32_s')

            if is_float_op:
                op_map = {
                    '+': 'f32.add', '-': 'f32.sub', '*': 'f32.mul', '/': 'f32.div',
                    '==': 'f32.eq', '!=': 'f32.ne', '<': 'f32.lt', '<=': 'f32.le', '>': 'f32.gt', '>=': 'f32.ge'
                }
                self.lines.append(f'{indent}{op_map.get(e.op, "f32.add")}')
            else:
                op_map = {
                    '+': 'i32.add', '-': 'i32.sub', '*': 'i32.mul', '/': 'i32.div_s',
                    '==': 'i32.eq', '!=': 'i32.ne', '<': 'i32.lt_s', '<=': 'i32.le_s', '>': 'i32.gt_s', '>=': 'i32.ge_s',
                    '&&': 'i32.and', '||': 'i32.or'
                }
                self.lines.append(f'{indent}{op_map.get(e.op, "i32.add")}')

        elif isinstance(e, UnaryOp):
            e: UnaryOp
            self.emit_expr(e.expr)
            t = self._get_expr_type(e.expr)
            if e.op == '-':
                if t == 'float': self.lines.append(f'{indent}f32.neg')
                else:
                    self.lines.append(f'{indent}i32.const -1')
                    self.lines.append(f'{indent}i32.mul')
            elif e.op == '!':
                self.lines.append(f'{indent}i32.eqz')

        elif isinstance(e, SubprogramCall):
            e: SubprogramCall
            if e.name == 'in':
                self.lines.append(f'{indent}call $in_i32')
            elif e.name == 'out':
                arg_t = 'int'
                if e.args: arg_t = self._get_expr_type(e.args[0])
                for a in e.args: self.emit_expr(a)
                if arg_t == 'float': self.lines.append(f'{indent}call $out_f32')
                else: self.lines.append(f'{indent}call $out_i32')
                self.lines.append(f'{indent}i32.const 0')
            elif e.name == 'str':
                if e.args: self.emit_expr(e.args[0])
                else: self.lines.append(f'{indent}i32.const 0')
            else:
                target_func = self.func_index.get(e.name)
                for i, arg in enumerate(e.args):
                    self.emit_expr(arg)
                    expr_t = self._get_expr_type(arg)
                    param_t = 'int'
                    
                    if target_func and i < len(target_func.param_types):
                        param_t = target_func.param_types[i]
                    
                    if param_t == 'float' and expr_t != 'float':
                        self.lines.append(f'{indent}f32.convert_i32_s')
                    elif param_t != 'float' and expr_t == 'float':
                        self.lines.append(f'{indent}i32.trunc_f32_s')
                
                sub_name = e.name
                self.lines.append(f'{indent}call ${sub_name}')
        else:
            raise NotImplementedError(f'Unknown expr {type(e)}')