from dataclasses import dataclass, field, InitVar
from typing import List, Optional, Dict, Set, Tuple
import math

from intermediate_code.ast_nodes import *


class WatGenerator:
    def __init__(self):
        self.indent_level = 0
        self.code_lines = []
        self.current_function = None
        self.function_locals = {}  # function_name -> Dict[var_name: type]
        self.function_params = {}  # function_name -> Dict[param_name: type]
        self.function_types = {}
        self.string_constants = {}
        self.string_counter = 0
        self.label_counter = 0
        self.loop_stack = []
        self.math_functions = {'sin', 'cos', 'tan', 'asin', 'acos', 'atan',
                               'exp', 'log', 'sqrt', 'ceil', 'floor', 'abs'}

    def indent(self):
        self.indent_level += 1

    def dedent(self):
        self.indent_level -= 1

    def emit(self, line: str):
        self.code_lines.append("  " * self.indent_level + line)

    def get_unique_label(self, prefix: str) -> str:
        self.label_counter += 1
        return f"${prefix}_{self.label_counter}"

    def generate(self, program: 'ProgramNode') -> str:
        """Main entry point to generate WAT from AST"""
        self.code_lines = []

        # Start module
        self.emit("(module")
        self.indent()

        # Import console functions
        self._emit_imports()

        # Import math functions
        self._emit_math_imports()

        # Generate memory for strings
        self.emit('(memory $memory 1)')

        # Generate string constants
        self._generate_string_constants(program)

        # Collect function signatures first
        self._collect_function_info(program)

        # Generate all subprograms
        for subprogram in program.subprograms:
            self._generate_subprogram(subprogram)

        # Generate main program (global statements)
        self._generate_main_program(program.statements)

        # Start the main function
        self.emit('(start $main)')

        self.dedent()
        self.emit(")")

        return "\n".join(self.code_lines)

    def _emit_imports(self):
        """Import console I/O functions"""
        self.emit('(import "console" "write_int" (func $console_write_int (param i32)))')
        self.emit('(import "console" "write_float" (func $console_write_float (param f32)))')
        self.emit('(import "console" "write_bool" (func $console_write_bool (param i32)))')
        self.emit('(import "console" "write_string" (func $console_write_string (param i32) (param i32)))')
        self.emit('(import "console" "read_int" (func $console_read_int (result i32)))')
        self.emit('(import "console" "read_float" (func $console_read_float (result f32)))')
        self.emit('(import "console" "read_bool" (func $console_read_bool (result i32)))')

    def _emit_math_imports(self):
        """Import math functions from JS Math module"""
        for func in self.math_functions:
            self.emit(f'(import "Math" "{func}" (func $Math_{func} (param f32) (result f32)))')

    def _collect_function_info(self, program: 'ProgramNode'):
        """Collect function signatures for type checking"""
        for subprogram in program.subprograms:
            param_types = [p.to_wat() for p in subprogram.param_types]
            return_type = subprogram.type.to_wat()
            self.function_types[subprogram.name] = (param_types, return_type)

    def _generate_string_constants(self, program: 'ProgramNode'):
        """Collect and generate string constants in data section"""
        # We'll need to traverse the AST to find all string literals
        # For now, we'll generate an empty data section
        self.emit('(data (i32.const 0) "")')

    def _generate_main_program(self, statements: List['StatementNode']):
        """Generate main program as a function"""
        self.emit('(func $main')
        self.indent()

        # Declare all local variables used in main
        main_locals: dict[str, Type] = {}
        self._collect_local_vars_with_types(statements, main_locals)
        if main_locals:
            local_decls = " ".join([f"(local ${var} {type.to_wat()})" for var, type in main_locals.items()])
            self.emit(local_decls)

        # Generate statements
        for stmt in statements:
            self._generate_statement(stmt)

        self.dedent()
        self.emit(')')

    def _collect_local_vars(self, statements: List['StatementNode'], var_set: Set[str]):
        """Collect all local variable names from statements"""
        for stmt in statements:
            if isinstance(stmt, VarDecl):
                var_set.add(stmt.name)
            if isinstance(stmt, AssignNode):
                var_set.add(stmt.name)
            elif isinstance(stmt, BlockNode):
                self._collect_local_vars(stmt.body, var_set)
            elif isinstance(stmt, IfStmt):
                self._collect_local_vars(stmt.then_body.body, var_set)
                if stmt.else_body:
                    self._collect_local_vars(stmt.else_body.body, var_set)
            elif isinstance(stmt, (WhileStmt, UntilStmt)):
                self._collect_local_vars(stmt.body.body, var_set)
            elif isinstance(stmt, ForStmt):
                if stmt.init:
                    self._collect_local_vars([stmt.init], var_set)
                self._collect_local_vars(stmt.body.body, var_set)

    def _generate_subprogram(self, subprogram: 'SubprogramNode'):
        """Generate a subprogram/function"""
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

        # Build parameter declarations (all passed by reference as i32 pointers)
        param_decls = []
        for name in subprogram.param_names:
            param_decls.append(f"(param ${name} i32)")

        # Build local variable declarations with correct types
        local_decls = []
        for var_name, var_type in sorted(local_vars.items()):
            if var_name not in param_types:  # Don't redeclare parameters
                wat_type = var_type.to_wat()
                local_decls.append(f"(local ${var_name} {wat_type})")

        # Build return type
        return_type = subprogram.type.to_wat()
        return_decl = f"(result {return_type})" if return_type else ""

        # Emit function header
        self.emit(f'(func ${subprogram.name}')
        self.indent()

        # Emit parameters and locals
        for param_decl in param_decls:
            self.emit(param_decl)

        if return_decl:
            self.emit(return_decl)

        if local_decls:
            self.emit(f"{' '.join(local_decls)}")

        # Generate function body
        for stmt in subprogram.body.body:
            self._generate_statement(stmt)

        # Add implicit return for void functions if not already present
        if return_type == "" and not self._has_return(subprogram.body.body):
            self.emit('return')

        self.dedent()
        self.emit(')')

        self.current_function = None

    def _has_return(self, statements: List['StatementNode']) -> bool:
        """Check if statements contain a return"""
        for stmt in statements:
            if isinstance(stmt, Return):
                return True
            elif isinstance(stmt, BlockNode):
                if self._has_return(stmt.body):
                    return True
            elif isinstance(stmt, IfStmt):
                if self._has_return(stmt.then_body.body):
                    return True
                if stmt.else_body and self._has_return(stmt.else_body.body):
                    return True
        return False

    def _generate_statement(self, stmt: 'StatementNode'):
        """Generate code for a statement"""
        if isinstance(stmt, VarDecl):
            self._generate_var_decl(stmt)
        elif isinstance(stmt, Return):
            self._generate_return(stmt)
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
            # Expression statement (function call, assignment, etc.)
            result = self._generate_expr(stmt)
            if result and stmt.type.name != "void":
                # Discard the result
                self.emit('drop')

    def _collect_local_vars_with_types(self, statements: List['StatementNode'], var_dict: Dict[str, Type]):
        """Collect all local variable names with their types from statements"""
        for stmt in statements:
            if isinstance(stmt, VarDecl):
                var_dict[stmt.name] = stmt.type
            elif isinstance(stmt, AssignNode):
                var_dict[stmt.name] = stmt.type
            elif isinstance(stmt, BlockNode):
                self._collect_local_vars_with_types(stmt.body, var_dict)
            elif isinstance(stmt, IfStmt):
                self._collect_local_vars_with_types(stmt.then_body.body, var_dict)
                if stmt.else_body:
                    self._collect_local_vars_with_types(stmt.else_body.body, var_dict)
            elif isinstance(stmt, (WhileStmt, UntilStmt)):
                self._collect_local_vars_with_types(stmt.body.body, var_dict)
            elif isinstance(stmt, ForStmt):
                if stmt.init and isinstance(stmt.init, VarDecl):
                    var_dict[stmt.init.name] = stmt.init.type
                self._collect_local_vars_with_types(stmt.body.body, var_dict)

    def _generate_var_decl(self, decl: 'VarDecl'):
        """Generate variable declaration"""
        var_name = decl.name
        var_type = decl.type

        if decl.init:
            # Generate initialization expression
            self._generate_expr(decl.init)
            # Store in local variable
            self.emit(f'local.set ${var_name}')
        else:
            # Initialize with default value
            if decl.type == Type.int():
                self.emit(f'i32.const 0')
                self.emit(f'local.set ${var_name}')
            elif decl.type == Type.float():
                self.emit(f'f32.const 0.0')
                self.emit(f'local.set ${var_name}')
            elif decl.type == Type.bool():
                self.emit(f'i32.const 0')
                self.emit(f'local.set ${var_name}')
            elif decl.type == Type.string():
                self.emit(f'i32.const 0')  # Null pointer
                self.emit(f'local.set ${var_name}')

    def _generate_return(self, ret: 'Return'):
        """Generate return statement"""
        self.emit('return')

    def _generate_block(self, block: 'BlockNode'):
        """Generate a block of statements"""
        self.indent()
        for stmt in block.body:
            self._generate_statement(stmt)
        self.dedent()

    def _generate_if(self, if_stmt: 'IfStmt'):
        """Generate if statement"""
        # Generate condition
        self._generate_expr(if_stmt.cond)

        # Generate then branch
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
        """Generate while loop"""
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
        """Generate until loop (do-while with inverted condition)"""
        loop_start = self.get_unique_label("loop_start")
        loop_end = self.get_unique_label("loop_end")

        self.loop_stack.append((loop_start, loop_end))

        self.emit(f'loop {loop_start}')
        self.indent()

        # Generate body
        self._generate_block(until_stmt.body)

        # Generate condition (break if true)
        self._generate_expr(until_stmt.cond)
        self.emit(f'br_if {loop_end}')

        self.emit(f'br {loop_start}')
        self.dedent()
        self.emit('end')
        self.emit(f'block {loop_end}')
        self.emit('end')

        self.loop_stack.pop()

    def _generate_for(self, for_stmt: 'ForStmt'):
        """Generate for loop"""
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
            result = self._generate_expr(for_stmt.step)
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
            self.emit(f'i32.const 0')  # Placeholder
            return True
        elif isinstance(expr, VarRef):
            # For pass-by-reference parameters, we need to dereference
            if self.current_function and expr.name in self.function_params.get(self.current_function, {}):
                # It's a parameter passed by reference - load from memory
                self.emit(f'local.get ${expr.name}')
                param_type = self.function_params[self.current_function][expr.name]
                if param_type == Type.float():
                    self.emit('f32.load')
                elif param_type == Type.int():
                    self.emit('i32.load')
                elif param_type == Type.bool():
                    self.emit('i32.load')
                else:
                    self.emit('i32.load')
            else:
                # It's a local variable - get directly
                self.emit(f'local.get ${expr.name}')
            return True
        elif isinstance(expr, AssignNode):
            # Check if assigning to a parameter (by reference) or local
            if self.current_function and expr.name in self.function_params.get(self.current_function, {}):
                # It's a parameter passed by reference - store to memory
                # First push the address (parameter value)
                self.emit(f'local.get ${expr.name}')
                # Then push the value to store
                self._generate_expr(expr.value)
                # Store with correct type
                param_type = self.function_params[self.current_function][expr.name]
                if param_type == Type.float():
                    self.emit('f32.store')
                elif param_type == Type.int():
                    self.emit('i32.store')
                elif param_type == Type.bool():
                    self.emit('i32.store')
                else:
                    self.emit('i32.store')
                # For assignment expression, we want to leave the stored value on stack
                # So we need to load it back
                self.emit(f'local.get ${expr.name}')
                if param_type == Type.float():
                    self.emit('f32.load')
                else:
                    self.emit('i32.load')
            else:
                # It's a local variable - store directly
                # First push the value to store
                self._generate_expr(expr.value)
                # Then store in local
                self.emit(f'local.set ${expr.name}')
                # Load back for expression value
                self.emit(f'local.get ${expr.name}')
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
        """Generate binary operation"""
        # Generate left operand
        self._generate_expr(expr.left)

        # Generate right operand
        self._generate_expr(expr.right)

        # Emit operation based on type and operator
        op = expr.op
        if expr.left.type == Type.int() or expr.left.type == Type.bool():
            if op == '+':
                self.emit('i32.add')
            elif op == '-':
                self.emit('i32.sub')
            elif op == '*':
                self.emit('i32.mul')
            elif op == '/':
                self.emit('i32.div_s')
            elif op == '%':
                self.emit('i32.rem_s')
            elif op == '==':
                self.emit('i32.eq')
            elif op == '!=':
                self.emit('i32.ne')
            elif op == '<':
                self.emit('i32.lt_s')
            elif op == '<=':
                self.emit('i32.le_s')
            elif op == '>':
                self.emit('i32.gt_s')
            elif op == '>=':
                self.emit('i32.ge_s')
            elif op == 'and':
                self.emit('i32.and')
            elif op == 'or':
                self.emit('i32.or')
        elif expr.left.type == Type.float():
            if op == '+':
                self.emit('f32.add')
            elif op == '-':
                self.emit('f32.sub')
            elif op == '*':
                self.emit('f32.mul')
            elif op == '/':
                self.emit('f32.div')
            elif op == '==':
                self.emit('f32.eq')
            elif op == '!=':
                self.emit('f32.ne')
            elif op == '<':
                self.emit('f32.lt')
            elif op == '<=':
                self.emit('f32.le')
            elif op == '>':
                self.emit('f32.gt')
            elif op == '>=':
                self.emit('f32.ge')

        return True

    def _generate_unary_op(self, expr: 'UnaryOp') -> bool:
        """Generate unary operation"""
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

    def _generate_subprogram_call(self, call: 'SubprogramCall') -> bool:
        """Generate function call with pass-by-reference semantics"""
        # Handle special functions
        if call.name == 'write':
            return self._generate_write_call(call)
        elif call.name == 'read':
            return self._generate_read_call(call)
        elif call.name in self.math_functions:
            return self._generate_math_call(call)

        # Regular function call with pass-by-reference
        # For pass-by-reference, we need to pass addresses of arguments
        for arg in call.args:
            if isinstance(arg, VarRef):
                # Pass the address (already in local)
                self.emit(f'local.get ${arg.name}')
            else:
                # For non-variable expressions, we need to:
                # 1. Evaluate the expression
                # 2. Store it in a temporary local
                # 3. Get the address of that temporary

                # Create a temporary local
                temp_name = self.get_unique_label("temp")
                temp_type = arg.type.to_wat()

                # Allocate local
                self.emit(f'(local ${temp_name} {temp_type})')

                # Evaluate expression and store in temp
                self._generate_expr(arg)
                self.emit(f'local.set ${temp_name}')

                # Get address (we need memory for true pass-by-reference)
                # For now, just pass the value
                self.emit(f'local.get ${temp_name}')

        # Call the function
        self.emit(f'call ${call.name}')

        # Check if function returns a value
        if call.name in self.function_types:
            _, return_type = self.function_types[call.name]
            return return_type != ""

        return False

    def _generate_write_call(self, call: 'SubprogramCall') -> bool:
        """Generate write call to console"""
        if len(call.args) != 1:
            raise ValueError("write takes exactly one argument")

        arg = call.args[0]
        arg_type = arg.type

        # Generate argument value
        self._generate_expr(arg)

        # Call appropriate console function
        if arg_type == Type.int():
            self.emit('call $console_write_int')
        elif arg_type == Type.float():
            self.emit('call $console_write_float')
        elif arg_type == Type.bool():
            self.emit('call $console_write_bool')
        elif arg_type == Type.string():
            # For strings, we need length too (simplified)
            self.emit('i32.const 0')  # Placeholder for length
            self.emit('call $console_write_string')

        # write returns void
        return False

    def _generate_read_call(self, call: 'SubprogramCall') -> bool:
        """Generate read call from console"""
        if len(call.args) != 0:
            raise ValueError("read takes no arguments")

        # Call appropriate console function based on expected return type
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
        """Generate math function call"""
        if len(call.args) != 1:
            raise ValueError(f"{call.name} takes exactly one argument")

        arg = call.args[0]
        if arg.type != Type.float():
            raise ValueError(f"{call.name} requires float argument")

        # Generate argument value
        self._generate_expr(arg)

        # Call math function
        self.emit(f'call $Math_{call.name}')

        return True

    def _generate_cast(self, expr: CastExpr) -> bool:
        """Generate type cast"""
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

        return True