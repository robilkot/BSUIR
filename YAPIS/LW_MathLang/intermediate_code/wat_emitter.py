from typing import Dict

from intermediate_code.ast_nodes import *


class WatGenerator:
    def __init__(self):
        self.indent_level = 0
        self.code_lines = []
        self.current_function: str = 'main'
        self.function_locals: dict[str, dict[str, Type]] = {}  # function_name -> Dict[var_name: type]
        self.function_params = {}  # function_name -> Dict[param_name: type]
        self.function_types = {}
        self.label_counter = 0
        self.loop_stack = []
        self.math_functions = {'sin', 'cos', 'tan', 'asin', 'acos', 'atan',
                               'exp', 'log', 'sqrt', 'ceil', 'floor', 'abs'}
        self.__current_address: int = 1  # preserving 0 for null
        self.__module_begin_line_idx: int = 0
        self.string_constants: dict[str, tuple[int, int]] = {}  # string_value -> (address, length)

    def get_next_free_address(self, alloc_size: int) -> int:
        free_addr = self.__current_address
        self.__current_address += alloc_size
        return free_addr

    def indent(self):
        self.indent_level += 1

    def dedent(self):
        self.indent_level -= 1

    def emit(self, line: str):
        self.code_lines.append("  " * self.indent_level + line)

    def emit_local(self, var_name: str):
        line = f'(local ${var_name} i32)'
        # Find the index of the last line starting with '(func ' (all locals are next to sub decl)
        target_index = -1
        for i in range(len(self.code_lines) - 1, self.__module_begin_line_idx - 1, -1):
            if self.code_lines[i].__contains__(f'(func ${self.current_function}'):
                target_index = i
                break

        if target_index != -1:
            # Skip params for sub decls
            while target_index < len(self.code_lines) - 1 and self.code_lines[target_index + 1].__contains__('(param '):
                target_index += 1

            insert_pos = target_index + 1
            self.code_lines.insert(insert_pos, "  " * self.indent_level + line)
        else:
            # Fallback: just append like emit if no local found
            self.code_lines.append("  " * self.indent_level + line)

    def get_unique_label(self, prefix: str) -> str:
        self.label_counter += 1
        return f"${prefix}_{self.label_counter}"

    def _collect_string_constants(self, program: 'ProgramNode'):
        for stmt in program.statements:
            self._collect_strings_from_statement(stmt)

        for subprogram in program.subprograms:
            for stmt in subprogram.body.body:
                self._collect_strings_from_statement(stmt)

        # Generate data section
        if self.string_constants:
            self.emit(';; String constants')
            for string_value, (address, length) in sorted(self.string_constants.items(), key=lambda x: x[1][0]):
                # Encode string for WAT data section (escape special characters)
                encoded = string_value.replace('"', '\\"').replace('\\x', '\\')
                self.emit(f'(data (i32.const {address}) "{encoded}\\00")')

    def _collect_strings_from_statement(self, stmt):
        if isinstance(stmt, AssignNode):
            self._collect_strings_from_expr(stmt.value)
        elif isinstance(stmt, IfStmt):
            self._collect_strings_from_expr(stmt.cond)
            for s in stmt.then_body.body:
                self._collect_strings_from_statement(s)
            if stmt.else_body:
                for s in stmt.else_body.body:
                    self._collect_strings_from_statement(s)
        elif isinstance(stmt, (WhileStmt, UntilStmt)):
            self._collect_strings_from_expr(stmt.cond)
            for s in stmt.body.body:
                self._collect_strings_from_statement(s)
        elif isinstance(stmt, ForStmt):
            if stmt.cond:
                self._collect_strings_from_expr(stmt.cond)
            for s in stmt.body.body:
                self._collect_strings_from_statement(s)
        elif isinstance(stmt, Expr) and not isinstance(stmt, (VarRef, ReturnNode, BreakNode, ContinueNode)):
            self._collect_strings_from_expr(stmt)
        elif isinstance(stmt, BlockNode):
            for s in stmt.body:
                self._collect_strings_from_statement(s)

    def _collect_strings_from_expr(self, expr):
        """Helper to collect strings from expressions"""
        if isinstance(expr, StringLiteral):
            if expr.value not in self.string_constants:
                length = len(expr.value.encode('utf-8'))
                self.string_constants[expr.value] = (self.get_next_free_address(length + 1), length)
        elif isinstance(expr, BinaryOp):
            self._collect_strings_from_expr(expr.left)
            self._collect_strings_from_expr(expr.right)
        elif isinstance(expr, UnaryOp):
            self._collect_strings_from_expr(expr.expr)
        elif isinstance(expr, SubprogramCall):
            for arg in expr.args:
                self._collect_strings_from_expr(arg)
        elif isinstance(expr, CastExpr):
            self._collect_strings_from_expr(expr.expr)

    def generate(self, program: 'ProgramNode') -> str:
        self.code_lines = []

        # Start module
        self.emit("(module")
        self.indent()

        self._emit_io_imports()
        self._emit_js_math_imports()

        self.emit('(memory $memory 1)')

        self._collect_string_constants(program)

        # Collect function signatures first
        self._collect_function_info(program)

        self.__module_begin_line_idx = len(self.code_lines) - 1 if len(self.code_lines) > 0 else 0

        # Generate all subprograms
        for subprogram in program.subprograms:
            self._generate_subprogram(subprogram)

        self.current_function = 'main'

        # Generate main program (global statements)
        self._generate_main_program(program.statements)

        # Export the main function
        self.emit('(export "memory" (memory $memory))')
        self.emit('(export "main" (func $main))')

        self.dedent()
        self.emit(")")

        return "\n".join(self.code_lines)

    def _emit_io_imports(self):
        self.emit('(import "console" "write_int" (func $console_write_int (param i32)))')
        self.emit('(import "console" "write_float" (func $console_write_float (param f32)))')
        self.emit('(import "console" "write_bool" (func $console_write_bool (param i32)))')
        self.emit('(import "console" "write_string" (func $console_write_string (param i32)))')
        self.emit('(import "console" "read_int" (func $console_read_int (result i32)))')
        self.emit('(import "console" "read_float" (func $console_read_float (result f32)))')
        self.emit('(import "console" "read_bool" (func $console_read_bool (result i32)))')

    def _emit_js_math_imports(self):
        for func in self.math_functions:
            self.emit(f'(import "Math" "{func}" (func $Math_{func} (param f32) (result f32)))')
        self.emit(f'(import "Math" "pow" (func $Math_pow (param f32) (param f32) (result f32)))')

    def _collect_function_info(self, program: 'ProgramNode'):
        for subprogram in program.subprograms:
            param_types = [p.to_wat() for p in subprogram.param_types]
            return_type = subprogram.type.to_wat()
            self.function_types[subprogram.name] = (param_types, return_type)


    def _generate_main_program(self, statements: List['StatementNode']):
        self.emit('(func $main')
        self.indent()

        main_locals: dict[str, Type] = {}
        self._collect_local_vars_with_types(statements, main_locals)
        if main_locals:
            for var_name in main_locals.keys():
                self.__allocate_local_var(var_name)

        self.function_locals[self.current_function] = main_locals

        # Generate statements
        for stmt in statements:
            self._generate_statement(stmt)

        self.dedent()
        self.emit(')')

    def _generate_subprogram(self, subprogram: 'SubprogramNode'):
        self.current_function = subprogram.name

        # Store parameter types for this function
        param_types = {}
        for name, typ in zip(subprogram.param_names, subprogram.param_types):
            param_types[name] = typ
        self.function_params[subprogram.name] = param_types

        # Collect local variables with their types
        local_vars = {}
        self._collect_local_vars_with_types(subprogram.body.body, local_vars)
        self.function_locals[subprogram.name] = local_vars


        # Emit function header
        self.emit(f'(func ${subprogram.name}')
        self.indent()


        # Build parameter declarations (all passed by reference as i32 pointers)
        param_decls = []
        for name in subprogram.param_names:
            param_decls.append(f"(param ${name} i32)")

        # Emit parameters and locals
        for param_decl in param_decls:
            self.emit(param_decl)

        return_type = subprogram.type.to_wat()
        return_decl = f"(result {return_type})" if return_type else ""
        if return_decl:
            self.emit(return_decl)


        for var_name in local_vars.keys():
            if var_name not in self.function_params[subprogram.name]:
                self.__allocate_local_var(var_name)

        for stmt in subprogram.body.body:
            self._generate_statement(stmt)

        # Add implicit return for void functions if not already present
        if return_type == "" and not self._contains_return(subprogram.body.body):
            self.emit('return')

        self.dedent()
        self.emit(')')

        self.current_function = None

    def _contains_return(self, statements: List['StatementNode']) -> bool:
        for stmt in statements:
            if isinstance(stmt, ReturnNode):
                return True
            elif isinstance(stmt, BlockNode):
                if self._contains_return(stmt.body):
                    return True
            elif isinstance(stmt, IfStmt):
                if self._contains_return(stmt.then_body.body):
                    return True
                if stmt.else_body and self._contains_return(stmt.else_body.body):
                    return True
            # todo loops
        return False

    def _generate_assign(self, stmt: AssignNode):
        if stmt.name not in self.function_locals.get(self.current_function, {}):
            self.function_locals[self.current_function][stmt.name] = stmt.value.type
            self.__allocate_local_var(stmt.name)

        self.emit(f'local.get ${stmt.name}')
        self._generate_expr(stmt.value)

        var_type = self.function_locals[self.current_function][stmt.name]
        if var_type == Type.string():
            # For strings, just store the address (no .store needed)
            pass
        else:
            self.emit(f'{stmt.value.type.to_wat()}.store')


    def _generate_statement(self, stmt: 'StatementNode'):
        if isinstance(stmt, GlobalVarDeclaration):
            self._generate_global_var_decl(stmt)
        elif isinstance(stmt, AssignNode):
            self._generate_assign(stmt)
        elif isinstance(stmt, ReturnNode):
            self.emit('return')
        elif isinstance(stmt, BlockNode):
            self._generate_block(stmt)
        elif isinstance(stmt, IfStmt):
            self._generate_if(stmt)
        elif isinstance(stmt, WhileStmt):
            self._generate_while(stmt)
        elif isinstance(stmt, UntilStmt):
            self._generate_until(stmt)
        elif isinstance(stmt, ForStmt):
            self._generate_for(stmt)
        elif isinstance(stmt, (BreakNode, ContinueNode, ReturnNode)):
            self._generate_control_flow(stmt)
        elif isinstance(stmt, Expr):
            result = self._generate_expr(stmt)
            if result and stmt.type != Type.void():
                # Discard the result
                self.emit('drop')
        else:
            raise NotImplementedError(stmt)

    def _collect_local_vars_with_types(self, statements: List['StatementNode'], var_dict: Dict[str, Type]):
        for stmt in statements:
            if isinstance(stmt, GlobalVarDeclaration):
                var_dict[stmt.name] = stmt.type
            elif isinstance(stmt, AssignNode):
                var_dict[stmt.name] = stmt.value.type
            elif isinstance(stmt, BlockNode):
                self._collect_local_vars_with_types(stmt.body, var_dict)
            elif isinstance(stmt, IfStmt):
                self._collect_local_vars_with_types(stmt.then_body.body, var_dict)
                if stmt.else_body:
                    self._collect_local_vars_with_types(stmt.else_body.body, var_dict)
            elif isinstance(stmt, (WhileStmt, UntilStmt)):
                self._collect_local_vars_with_types(stmt.body.body, var_dict)
            elif isinstance(stmt, ForStmt):
                if stmt.init and isinstance(stmt.init, GlobalVarDeclaration):
                    var_dict[stmt.init.name] = stmt.init.type
                self._collect_local_vars_with_types(stmt.body.body, var_dict)

    # todo
    def _generate_global_var_decl(self, decl: 'GlobalVarDeclaration'):
        pass

    def _generate_block(self, block: 'BlockNode'):
        self.indent()
        for stmt in block.body:
            self._generate_statement(stmt)
        self.dedent()

    def _generate_if(self, if_stmt: 'IfStmt'):
        self._generate_expr(if_stmt.cond)

        if if_stmt.else_body:
            self.emit('if')
            self.indent()
            self._generate_block(if_stmt.then_body)
            self.dedent()
            self.emit('else')
            self.indent()
            self._generate_block(if_stmt.else_body)
            self.dedent()
            self.emit('end')
        else:
            self.emit('if')
            self.indent()
            self._generate_block(if_stmt.then_body)
            self.dedent()
            self.emit('end')

    def _generate_while(self, while_stmt: 'WhileStmt'):
        loop_start = self.get_unique_label("loop_start")
        loop_end = self.get_unique_label("loop_end")

        self.loop_stack.append((loop_start, loop_end))

        self.emit(f'block {loop_end}')
        self.emit(f'loop {loop_start}')
        self.indent()

        # Generate condition (continue if true)
        self._generate_expr(while_stmt.cond)

        self.emit(f'i32.eqz')
        self.emit(f'br_if {loop_end}')

        # Generate body
        self._generate_block(while_stmt.body)

        self.emit(f'br {loop_start}')
        self.dedent()
        self.emit('end')
        self.emit('end')

        self.loop_stack.pop()

    def _generate_until(self, until_stmt: 'UntilStmt'):
        loop_start = self.get_unique_label("loop_start")
        loop_end = self.get_unique_label("loop_end")

        self.loop_stack.append((loop_start, loop_end))

        self.emit(f'block {loop_end}')
        self.emit(f'loop {loop_start}')
        self.indent()

        self._generate_block(until_stmt.body)

        self._generate_expr(until_stmt.cond)
        self.emit(f'br_if {loop_end}')

        self.emit(f'br {loop_start}')
        self.dedent()
        self.emit('end')
        self.emit('end')

        self.loop_stack.pop()

    def _generate_for(self, for_stmt: 'ForStmt'):
        loop_start = self.get_unique_label("loop_start")
        loop_end = self.get_unique_label("loop_end")

        self.loop_stack.append((loop_start, loop_end))

        # Generate initialization
        if for_stmt.init:
            self._generate_statement(for_stmt.init)

        self.emit(f'block {loop_end}')
        self.emit(f'loop {loop_start}')
        self.indent()

        # Generate condition if present
        if for_stmt.cond:
            self._generate_expr(for_stmt.cond)
            self.emit(f'i32.eqz')
            self.emit(f'br_if {loop_end}')

        # Generate body
        self._generate_block(for_stmt.body)

        # Generate step
        if for_stmt.step:
            result = self._generate_statement(for_stmt.step)
            if result:
                self.emit('drop')

        self.emit(f'br {loop_start}')
        self.dedent()
        self.emit('end')
        self.emit('end')

        self.loop_stack.pop()

    def _generate_control_flow(self, stmt: 'StatementNode'):
        """Generate break/continue/return"""
        if isinstance(stmt, BreakNode):
            if self.loop_stack:
                _, loop_end = self.loop_stack[-1]
                self.emit(f'br {loop_end}')
        elif isinstance(stmt, ContinueNode):
            if self.loop_stack:
                loop_start, _ = self.loop_stack[-1]
                self.emit(f'br {loop_start}')

    def _generate_expr(self, expr: 'Expr') -> bool:
        """Generate expression code, returns True if expression leaves value on stack"""
        if isinstance(expr, IntLiteral):
            self.emit(f'i32.const {expr.value}')
            return True
        elif isinstance(expr, FloatLiteral):
            self.emit(f'f32.const {expr.value}')
            return True
        elif isinstance(expr, BoolLiteral):
            self.emit(f'i32.const {1 if expr.value else 0}')
            return True
        elif isinstance(expr, StringLiteral):
            # For strings, return the address in memory
            address, _ = self.string_constants[expr.value]
            self.emit(f'i32.const {address}')
            return True
        elif isinstance(expr, VarRef):
            self.emit(f'local.get ${expr.name}')
            if expr.type == Type.float():
                self.emit('f32.load')
            elif expr.type == Type.int():
                self.emit('i32.load')
            elif expr.type == Type.bool():
                self.emit('i32.load')
            elif expr.type == Type.string():
                # For strings, we store the address, so just return it
                # No need to load - the local contains the address directly
                pass
            else:
                raise NotImplementedError(expr)
            return True
        elif isinstance(expr, BinaryOp):
            return self._generate_binary_op(expr)
        elif isinstance(expr, UnaryOp):
            return self._generate_unary_op(expr)
        elif isinstance(expr, SubprogramCall):
            return self._generate_subprogram_call(expr)
        elif isinstance(expr, CastExpr):
            return self._generate_cast(expr)
        return False

    def _generate_binary_op(self, expr: 'BinaryOp') -> bool:
        int_codes: dict[str, list[str]] = {
            '+': ['i32.add'],
            '-': ['i32.sub'],
            '*': ['i32.mul'],
            '/': ['i32.div_s'],
            '%': ['i32.rem_s'],
            '==': ['i32.eq'],
            '!=': ['i32.ne'],
            '<': ['i32.lt_s'],
            '<=': ['i32.le_s'],
            '>': ['i32.gt_s'],
            '>=': ['i32.ge_s'],
            'and': ['i32.and'],
            'or': ['i32.or'],
        }
        float_codes: dict[str, list[str]] = {
            '+': ['f32.add'],
            '-': ['f32.sub'],
            '*': ['f32.mul'],
            '/': ['f32.div'],
            '%': ['f32.rem'],
            '==': ['f32.eq'],
            '!=': ['f32.ne'],
            '<': ['f32.lt'],
            '<=': ['f32.le'],
            '>': ['f32.gt'],
            '>=': ['f32.ge'],
            '^': ['f32.mul'] # TODO
        }
        self._generate_expr(expr.left)
        self._generate_expr(expr.right)

        op = expr.op
        if expr.left.type == Type.int() or expr.left.type == Type.bool():
            for code in int_codes[op]:
                self.emit(code)
        elif expr.left.type == Type.float():
            for code in float_codes[op]:
                self.emit(code)
        else:
            raise NotImplementedError(op, expr.left.type, expr.right.type)

        return True

    def _generate_unary_op(self, expr: 'UnaryOp') -> bool:
        self._generate_expr(expr.expr)

        op = expr.op
        if expr.expr.type == Type.int() or expr.expr.type == Type.bool():
            if op == '-':
                self.emit('i32.const -1')
                self.emit('i32.mul')
            elif op == 'not':
                self.emit('i32.eqz')
        elif expr.expr.type == Type.float():
            if op == '-':
                self.emit('f32.neg')

        return True

    def __allocate_local_var(self, var_name: str) -> None:
        # print("Allocation for", var_name, 'in', self.current_function)
        self.emit_local(var_name)
        self.emit(f'i32.const {self.get_next_free_address(4)}')
        self.emit(f'local.set ${var_name}')

    def _generate_subprogram_call(self, call: 'SubprogramCall') -> bool:
        if call.name == 'write':
            return self._generate_write_call(call)
        elif call.name == 'read':
            return self._generate_read_call(call)
        elif call.name in self.math_functions:
            return self._generate_math_call(call)
        elif call.name == 'pow':
            return self._generate_pow_call(call)

        for arg in call.args:
            if isinstance(arg, VarRef):
                self.emit(f'local.get ${arg.name}')
            else:
                # Create a temporary local
                temp_name = self.get_unique_label("temp")
                temp_type = arg.type.to_wat()

                self.function_locals[self.current_function][temp_name] = temp_type
                self.__allocate_local_var(temp_name)

                # Evaluate expression and store in temp
                self.emit(f'local.get ${temp_name}')
                self._generate_expr(arg)
                self.emit(f'{temp_type}.store')

                # Get pointer
                self.emit(f'local.get ${temp_name}')

        self.emit(f'call ${call.name}')

        if call.name in self.function_types:
            _, return_type = self.function_types[call.name]
            return return_type != ""

        return False

    def _generate_write_call(self, call: 'SubprogramCall') -> bool:
        if len(call.args) != 1:
            raise ValueError("write takes exactly one argument")

        arg = call.args[0]
        arg_type = arg.type

        self._generate_expr(arg)

        # Call appropriate console function
        if arg_type == Type.int():
            self.emit('call $console_write_int')
        elif arg_type == Type.float():
            self.emit('call $console_write_float')
        elif arg_type == Type.bool():
            self.emit('call $console_write_bool')
        elif arg_type == Type.string():
            self.emit('call $console_write_string')

        # write returns void
        return False

    def _generate_read_call(self, call: 'SubprogramCall') -> bool:
        if len(call.args) != 0:
            raise ValueError("read takes no arguments")

        if call.type == Type.int():
            self.emit('call $console_read_int')
        elif call.type == Type.float():
            self.emit('call $console_read_float')
        elif call.type == Type.bool():
            self.emit('call $console_read_bool')
            # Convert to boolean (0/1)
            self.emit('i32.const 0')
            self.emit('i32.ne')
        else:
            raise ValueError(f"read cannot read type {call.type}")

        return True

    def _generate_math_call(self, call: 'SubprogramCall') -> bool:
        if len(call.args) != 1:
            raise ValueError(f"{call.name} takes exactly one argument")

        arg = call.args[0]
        if arg.type != Type.float():
            raise ValueError(f"{call.name} requires float argument")

        self._generate_expr(arg)

        self.emit(f'call $Math_{call.name}')

        return True


    def _generate_pow_call(self, call: 'SubprogramCall') -> bool:
        if len(call.args) != 2:
            raise ValueError(f"Pow takes exactly two arguments")

        if call.args[0].type != Type.float() and call.args[1].type != Type.int():
            raise ValueError(f"Pow requires float argument")

        self._generate_expr(call.args[0])
        self._generate_expr(call.args[1])

        self.emit(f'call $Math_{call.name}')

        return True

    def _generate_cast(self, expr: CastExpr) -> bool:
        self._generate_expr(expr.expr)

        src_type = expr.expr.type
        dst_type = expr.type

        if src_type == dst_type:
            return True

        if src_type == Type.int() and dst_type == Type.float():
            self.emit('f32.convert_i32_s')
        elif src_type == Type.float() and dst_type == Type.int():
            self.emit('f32.trunc')
            self.emit('i32.trunc_f32_s')
        elif src_type == Type.bool() and dst_type == Type.int():
            # bool is already i32 in our representation
            pass
        elif src_type == Type.int() and dst_type == Type.bool():
            self.emit('i32.const 0')
            self.emit('i32.ne')
        elif src_type == Type.float() and dst_type == Type.bool():
            self.emit('f32.const 0.0')
            self.emit('f32.ne')
            self.emit('i32.trunc_f32_s')
        else:
            print("Invalid cast from", src_type, "to", dst_type)

        return True