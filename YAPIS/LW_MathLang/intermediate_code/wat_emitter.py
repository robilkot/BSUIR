from intermediate_code.ast_nodes import *
from models.types import Type


# WAT Generator Class
class WATGenerator:
    def __init__(self):
        self.module_parts = []
        self.func_defs = []
        self.main_func_body = []
        self.variable_counter = 0
        self.label_counter = 0
        self.local_vars = {}
        self.current_function = None
        self.return_type = None
        self.param_types = {}
        self.loop_break_labels = []
        self.loop_continue_labels = []

    def generate_wat(self, program: ProgramNode) -> str:
        """Generate WAT code from the AST"""
        self.module_parts = []

        # Start module
        self.module_parts.append("(module")

        # Memory for strings (if needed)
        self.module_parts.append("  (memory 1)")

        # Data section for string literals
        string_literals = self._collect_string_literals(program)
        if string_literals:
            self.module_parts.append("  (data (i32.const 0)")
            for s in string_literals:
                escaped = s.replace('"', '\\"')
                self.module_parts.append(f'    "{escaped}"')
            self.module_parts.append("  )")

        # Process subprograms (functions)
        for subprogram in program.subprograms:
            self._generate_subprogram(subprogram)

        # Generate main function from top-level statements
        self._generate_main_function(program.statements)

        self.module_parts.append(")")
        return "\n".join(self.module_parts)

    def _collect_string_literals(self, program: ProgramNode) -> List[str]:
        """Collect all string literals for the data section"""
        strings = []

        def collect_from_expr(expr):
            if isinstance(expr, StringLiteral):
                strings.append(expr.value)
            elif isinstance(expr, BinaryOp):
                collect_from_expr(expr.left)
                collect_from_expr(expr.right)
            elif isinstance(expr, UnaryOp):
                collect_from_expr(expr.expr)
            elif isinstance(expr, SubprogramCall):
                for arg in expr.args:
                    collect_from_expr(arg)
            elif isinstance(expr, CastExpr):
                collect_from_expr(expr.expr)
            elif isinstance(expr, AssignNode):
                collect_from_expr(expr.value)

        def collect_from_stmt(stmt: StatementNode):
            if isinstance(stmt, VarDecl) and stmt.init:
                collect_from_expr(stmt.init)
            elif isinstance(stmt, BlockNode):
                for s in stmt.body:
                    collect_from_stmt(s)
            elif isinstance(stmt, IfStmt):
                collect_from_expr(stmt.cond)
                collect_from_stmt(stmt.then_body)
                if stmt.else_body:
                    collect_from_stmt(stmt.else_body)
            elif isinstance(stmt, (WhileStmt, UntilStmt)):
                collect_from_expr(stmt.cond)
                collect_from_stmt(stmt.body)
            elif isinstance(stmt, ForStmt):
                if stmt.init:
                    collect_from_stmt(stmt.init)
                if stmt.cond:
                    collect_from_expr(stmt.cond)
                if stmt.step:
                    collect_from_expr(stmt.step)
                collect_from_stmt(stmt.body)
            elif isinstance(stmt, Expr):
                collect_from_expr(stmt)

        for subprogram in program.subprograms:
            collect_from_stmt(subprogram.body)

        for program_stmt in program.statements:
            collect_from_stmt(program_stmt)

        return list(set(strings))  # Remove duplicates

    def _collect_local_vars(self, block: BlockNode) -> dict[str, str]:
        """Collect all local variables declared in a block"""
        local_vars = {}

        def collect_from_stmt(stmt):
            if isinstance(stmt, VarDecl):
                wasm_type = self._type_to_wasm(stmt.type)
                local_vars[stmt.name] = wasm_type
            elif isinstance(stmt, BlockNode):
                for s in stmt.body:
                    collect_from_stmt(s)
            elif isinstance(stmt, IfStmt):
                collect_from_stmt(stmt.then_body)
                if stmt.else_body:
                    collect_from_stmt(stmt.else_body)
            elif isinstance(stmt, (WhileStmt, UntilStmt)):
                collect_from_stmt(stmt.body)
            elif isinstance(stmt, ForStmt):
                if stmt.init:
                    collect_from_stmt(stmt.init)
                collect_from_stmt(stmt.body)

        for stmt in block.body:
            collect_from_stmt(stmt)

        return local_vars

    def _generate_subprogram(self, subprogram: SubprogramNode):
        """Generate a function definition"""
        func_name = f"${subprogram.name}"
        param_strs = []
        self.param_types = {}

        # Build parameter strings and track types
        for i, (name, type_) in enumerate(zip(subprogram.param_names, subprogram.param_types)):
            wasm_type = self._type_to_wasm(type_)
            param_strs.append(f"(param ${name} {wasm_type})")
            self.param_types[name] = wasm_type

        # Return type
        result_str = ""
        if subprogram.type and subprogram.type != Type.void():
            result_str = f"(result {self._type_to_wasm(subprogram.type)})"

        # Save current context
        old_function = self.current_function
        old_return_type = self.return_type
        old_locals = self.local_vars.copy()

        # Set new context
        self.current_function = subprogram.name
        self.return_type = subprogram.type
        self.local_vars = {name: self.param_types[name]
                           for name in subprogram.param_names}

        # Collect all local variables first by analyzing the function body
        local_vars_to_declare = self._collect_local_vars(subprogram.body)

        # Build function definition
        func_def = [f"  (func {func_name}"]
        func_def.append(f"    {' '.join(param_strs)}")
        if result_str:
            func_def.append(f"    {result_str}")

        # Declare all local variables at function start
        for var_name, var_type in local_vars_to_declare.items():
            func_def.append(f"    (local ${var_name} {var_type})")

        # Add to local_vars map
        self.local_vars.update(local_vars_to_declare)

        # Generate function body
        body_code = self._generate_block(subprogram.body.body, is_function_body=True)
        func_def.extend(f"    {line}" for line in body_code)

        # Ensure function returns if needed
        if subprogram.type != Type.void() and not self._has_return(subprogram.body):
            func_def.append("    unreachable  ;; default return if missing")

        func_def.append("  )")

        # Restore context
        self.current_function = old_function
        self.return_type = old_return_type
        self.local_vars = old_locals

        self.module_parts.extend(func_def)

    def _has_return(self, block: BlockNode) -> bool:
        """Check if a block contains a return statement"""

        def check_stmt(stmt):
            if isinstance(stmt, Return) or isinstance(stmt, ReturnNode):
                return True
            elif isinstance(stmt, BlockNode):
                for s in stmt.body:
                    if check_stmt(s):
                        return True
            elif isinstance(stmt, IfStmt):
                if check_stmt(stmt.then_body):
                    return True
                if stmt.else_body and check_stmt(stmt.else_body):
                    return True
            elif isinstance(stmt, (WhileStmt, UntilStmt, ForStmt)):
                # Don't check loops for returns that might not execute
                pass
            return False

        return check_stmt(block)

    def _collect_local_vars_from_statements(self, statements: List[StatementNode]) -> dict[str, str]:
        """Collect all local variables from a list of statements"""
        local_vars = {}

        def collect_from_stmt(stmt):
            if isinstance(stmt, VarDecl):
                wasm_type = self._type_to_wasm(stmt.type)
                local_vars[stmt.name] = wasm_type
            elif isinstance(stmt, BlockNode):
                for s in stmt.body:
                    collect_from_stmt(s)
            elif isinstance(stmt, IfStmt):
                collect_from_stmt(stmt.then_body)
                if stmt.else_body:
                    collect_from_stmt(stmt.else_body)
            elif isinstance(stmt, (WhileStmt, UntilStmt)):
                collect_from_stmt(stmt.body)
            elif isinstance(stmt, ForStmt):
                if stmt.init:
                    collect_from_stmt(stmt.init)
                collect_from_stmt(stmt.body)

        for stmt in statements:
            collect_from_stmt(stmt)

        return local_vars

    def _generate_main_function(self, statements: List[StatementNode]):
        """Generate the main function"""
        # Collect all local variables first
        local_vars = self._collect_local_vars_from_statements(statements)

        self.module_parts.append('  (func $main (export "main") (result i32)')

        # Declare all local variables
        for var_name, var_type in local_vars.items():
            self.module_parts.append(f'    (local ${var_name} {var_type})')

        # Add to local_vars map
        self.local_vars.update(local_vars)

        # Generate statements
        main_body = self._generate_block(statements)
        for line in main_body:
            self.module_parts.append(f'    {line}')

        # Return 0 by default
        self.module_parts.append('    i32.const 0')
        self.module_parts.append('  )')

    def _generate_block(self, statements: List[StatementNode], is_function_body=False) -> List[str]:
        """Generate code for a block of statements"""
        result = []
        for stmt in statements:
            result.extend(self._generate_statement(stmt))
        return result

    def _generate_statement(self, stmt: StatementNode) -> List[str]:
        """Generate code for a statement"""
        if isinstance(stmt, VarDecl):
            return self._generate_var_decl(stmt)
        elif isinstance(stmt, Return):
            return self._generate_return(stmt)
        elif isinstance(stmt, BreakNode):
            return self._generate_break()
        elif isinstance(stmt, ContinueNode):
            return self._generate_continue()
        elif isinstance(stmt, BlockNode):
            return self._generate_block(stmt.body)
        elif isinstance(stmt, IfStmt):
            return self._generate_if(stmt)
        elif isinstance(stmt, WhileStmt):
            return self._generate_while(stmt)
        elif isinstance(stmt, UntilStmt):
            return self._generate_until(stmt)
        elif isinstance(stmt, ForStmt):
            return self._generate_for(stmt)
        elif isinstance(stmt, Expr):
            # Expression statement - evaluate and drop result
            expr_code = self._generate_expression(stmt)
            if stmt.type != Type.void():  # Don't drop void expressions
                expr_code.append("drop")
            return expr_code
        else:
            return [f";; Unknown statement: {type(stmt).__name__}"]

    def _generate_var_decl(self, var_decl: VarDecl) -> List[str]:
        """Generate variable declaration"""
        result = []

        # Variable was already declared at function start, just initialize if needed
        var_name = f"${var_decl.name}"

        # Generate initialization if present
        if var_decl.init:
            init_code = self._generate_expression(var_decl.init)
            result.extend(init_code)
            result.append(f"local.set {var_name}")
        else:
            # Default initialization based on type
            if var_decl.type == Type.int():
                result.append("i32.const 0")
            elif var_decl.type == Type.float():
                result.append("f32.const 0.0")
            elif var_decl.type == Type.bool():
                result.append("i32.const 0")
            elif var_decl.type == Type.string():
                result.append("i32.const 0")  # null pointer
            result.append(f"local.set {var_name}")

        return result

    def _generate_return(self, ret: Return) -> List[str]:
        """Generate return statement"""
        result = []

        # For void returns or no expression
        if isinstance(ret, ReturnNode) or self.return_type == Type.void():
            result.append("return")
        # For return with expression (if Return had an expression field)
        elif hasattr(ret, 'expr') and ret.expr:
            expr_code = self._generate_expression(ret.expr)
            result.extend(expr_code)
            result.append("return")
        else:
            result.append("return")

        return result

    def _generate_break(self) -> List[str]:
        """Generate break statement"""
        if self.loop_break_labels:
            return [f"br {self.loop_break_labels[-1]}"]
        return [";; Error: break outside loop"]

    def _generate_continue(self) -> List[str]:
        """Generate continue statement"""
        if self.loop_continue_labels:
            return [f"br {self.loop_continue_labels[-1]}"]
        return [";; Error: continue outside loop"]

    def _generate_if(self, if_stmt: IfStmt) -> List[str]:
        """Generate if statement"""
        result = []

        # Generate condition
        cond_code = self._generate_expression(if_stmt.cond)
        result.extend(cond_code)

        # For boolean conditions, ensure i32
        if if_stmt.cond.type == Type.bool():
            result.append("i32.const 0")
            result.append("i32.ne")

        # Generate then block
        then_code = self._generate_block(if_stmt.then_body.body)

        if if_stmt.else_body:
            # Generate else block
            else_code = self._generate_block(if_stmt.else_body.body)

            result.append("if")
            result.extend(f"  {line}" for line in then_code)
            result.append("else")
            result.extend(f"  {line}" for line in else_code)
            result.append("end")
        else:
            result.append("if")
            result.extend(f"  {line}" for line in then_code)
            result.append("end")

        return result

    def _generate_while(self, while_stmt: WhileStmt) -> List[str]:
        """Generate while loop"""
        result = []

        # Create labels for break/continue
        loop_label = f"$loop_{self.label_counter}"
        end_label = f"$end_{self.label_counter}"
        self.label_counter += 1

        # Push labels for break/continue
        self.loop_break_labels.append(end_label)
        self.loop_continue_labels.append(loop_label)

        result.append(f"block {end_label}")
        result.append(f"  loop {loop_label}")

        # Generate condition
        cond_code = self._generate_expression(while_stmt.cond)
        result.extend(f"    {line}" for line in cond_code)

        # For boolean conditions
        if while_stmt.cond.type == Type.bool():
            result.append("    i32.const 0")
            result.append("    i32.ne")

        # Branch to end if condition is false
        result.append("    i32.eqz")
        result.append(f"    br_if {end_label}")

        # Generate loop body
        body_code = self._generate_block(while_stmt.body.body)
        result.extend(f"    {line}" for line in body_code)

        # Jump back to loop start
        result.append(f"    br {loop_label}")
        result.append("  end")
        result.append("end")

        # Pop labels
        self.loop_break_labels.pop()
        self.loop_continue_labels.pop()

        return result

    def _generate_until(self, until_stmt: UntilStmt) -> List[str]:
        """Generate until loop (runs until condition is true)"""
        result = []

        # Create labels for break/continue
        loop_label = f"$loop_{self.label_counter}"
        end_label = f"$end_{self.label_counter}"
        self.label_counter += 1

        # Push labels for break/continue
        self.loop_break_labels.append(end_label)
        self.loop_continue_labels.append(loop_label)

        result.append(f"block {end_label}")
        result.append(f"  loop {loop_label}")

        # Generate loop body
        body_code = self._generate_block(until_stmt.body.body)
        result.extend(f"    {line}" for line in body_code)

        # Generate condition
        cond_code = self._generate_expression(until_stmt.cond)
        result.extend(f"    {line}" for line in cond_code)

        # For boolean conditions
        if until_stmt.cond.type == Type.bool():
            result.append("    i32.const 0")
            result.append("    i32.ne")

        # Branch to end if condition is true
        result.append(f"    br_if {end_label}")

        # Jump back to loop start
        result.append(f"    br {loop_label}")
        result.append("  end")
        result.append("end")

        # Pop labels
        self.loop_break_labels.pop()
        self.loop_continue_labels.pop()

        return result

    def _generate_for(self, for_stmt: ForStmt) -> List[str]:
        """Generate for loop"""
        result = []

        # Create labels for break/continue
        loop_label = f"$loop_{self.label_counter}"
        end_label = f"$end_{self.label_counter}"
        step_label = f"$step_{self.label_counter}"
        self.label_counter += 1

        # Push labels for break/continue
        self.loop_break_labels.append(end_label)
        self.loop_continue_labels.append(step_label)

        # Initialization
        if for_stmt.init:
            init_code = self._generate_statement(for_stmt.init)
            result.extend(init_code)

        result.append(f"block {end_label}")
        result.append(f"  loop {loop_label}")

        # Condition (if present)
        if for_stmt.cond:
            cond_code = self._generate_expression(for_stmt.cond)
            result.extend(f"    {line}" for line in cond_code)

            # For boolean conditions
            if for_stmt.cond.type == Type.bool():
                result.append("    i32.const 0")
                result.append("    i32.ne")

            # Branch to end if condition is false
            result.append("    i32.eqz")
            result.append(f"    br_if {end_label}")

        # Loop body
        body_code = self._generate_block(for_stmt.body.body)
        result.extend(f"    {line}" for line in body_code)

        # Step label for continue
        result.append(f"  {step_label}:")

        # Step expression (if present)
        if for_stmt.step:
            step_code = self._generate_expression(for_stmt.step)
            result.extend(f"    {line}" for line in step_code)
            result.append("    drop")  # Drop step result

        # Jump back to loop start
        result.append(f"    br {loop_label}")
        result.append("  end")
        result.append("end")

        # Pop labels
        self.loop_break_labels.pop()
        self.loop_continue_labels.pop()

        return result

    def _generate_expression(self, expr: Expr) -> List[str]:
        """Generate code for an expression"""
        if isinstance(expr, IntLiteral):
            return [f"i32.const {expr.value}"]
        elif isinstance(expr, FloatLiteral):
            return [f"f32.const {expr.value}"]
        elif isinstance(expr, StringLiteral):
            # String literals are stored in memory, return pointer
            # For simplicity, we'll return a placeholder
            return ["i32.const 0 ;; TODO: string literal address"]
        elif isinstance(expr, BoolLiteral):
            return [f"i32.const {1 if expr.value else 0}"]
        elif isinstance(expr, VarRef):
            var_name = f"${expr.name}"
            if expr.name in self.local_vars:
                return [f"local.get {var_name}"]
            else:
                return [f"global.get {var_name}"]
        elif isinstance(expr, AssignNode):
            # Generate value first
            result = self._generate_expression(expr.value)
            var_name = f"${expr.name}"
            result.append(f"local.set {var_name}")
            result.append(f"local.get {var_name}")  # Return assigned value
            return result
        elif isinstance(expr, BinaryOp):
            return self._generate_binary_op(expr)
        elif isinstance(expr, UnaryOp):
            return self._generate_unary_op(expr)
        elif isinstance(expr, SubprogramCall):
            return self._generate_function_call(expr)
        elif isinstance(expr, CastExpr):
            return self._generate_cast(expr)
        else:
            return [f";; Unknown expression: {type(expr).__name__}"]

    def _generate_binary_op(self, op: BinaryOp) -> List[str]:
        """Generate binary operation"""
        result = []

        # Generate left and right operands
        left_code = self._generate_expression(op.left)
        right_code = self._generate_expression(op.right)

        result.extend(left_code)
        result.extend(right_code)

        # Determine operation based on type and operator
        if op.left.type == Type.int() and op.right.type == Type.int():
            if op.op == '+':
                result.append("i32.add")
            elif op.op == '-':
                result.append("i32.sub")
            elif op.op == '*':
                result.append("i32.mul")
            elif op.op == '/':
                result.append("i32.div_s")
            elif op.op == '%':
                result.append("i32.rem_s")
            elif op.op == '==':
                result.append("i32.eq")
            elif op.op == '!=':
                result.append("i32.ne")
            elif op.op == '<':
                result.append("i32.lt_s")
            elif op.op == '<=':
                result.append("i32.le_s")
            elif op.op == '>':
                result.append("i32.gt_s")
            elif op.op == '>=':
                result.append("i32.ge_s")
            elif op.op == '&&' or op.op == 'and':
                result.append("i32.and")
            elif op.op == '||' or op.op == 'or':
                result.append("i32.or")
            elif op.op == '&':
                result.append("i32.and")
            elif op.op == '|':
                result.append("i32.or")
            elif op.op == '^':
                result.append("i32.xor")
            elif op.op == '<<':
                result.append("i32.shl")
            elif op.op == '>>':
                result.append("i32.shr_s")
            else:
                result.append(f";; Unknown integer operator: {op.op}")

        elif op.left.type == Type.float() and op.right.type == Type.float():
            if op.op == '+':
                result.append("f32.add")
            elif op.op == '-':
                result.append("f32.sub")
            elif op.op == '*':
                result.append("f32.mul")
            elif op.op == '/':
                result.append("f32.div")
            elif op.op == '==':
                result.append("f32.eq")
            elif op.op == '!=':
                result.append("f32.ne")
            elif op.op == '<':
                result.append("f32.lt")
            elif op.op == '<=':
                result.append("f32.le")
            elif op.op == '>':
                result.append("f32.gt")
            elif op.op == '>=':
                result.append("f32.ge")
            else:
                result.append(f";; Unknown float operator: {op.op}")

        elif op.left.type == Type.bool() and op.right.type == Type.bool():
            if op.op == '&&' or op.op == 'and':
                result.append("i32.and")
            elif op.op == '||' or op.op == 'or':
                result.append("i32.or")
            elif op.op == '==':
                result.append("i32.eq")
            elif op.op == '!=':
                result.append("i32.ne")
            else:
                result.append(f";; Unknown boolean operator: {op.op}")

        else:
            # Type mismatch - need cast
            result.append(f";; Type mismatch in binary op: {op.left.type} {op.op} {op.right.type}")

        return result

    def _generate_unary_op(self, op: UnaryOp) -> List[str]:
        """Generate unary operation"""
        result = self._generate_expression(op.expr)

        if op.expr.type == Type.int():
            if op.op == '-':
                result.append("i32.const 0")
                result.append("i32.sub")
            elif op.op == '~':
                result.append("i32.const -1")
                result.append("i32.xor")
            elif op.op == '!' or op.op == 'not':
                result.append("i32.eqz")
            else:
                result.append(f";; Unknown integer unary operator: {op.op}")

        elif op.expr.type == Type.float():
            if op.op == '-':
                result.append("f32.neg")
            else:
                result.append(f";; Unknown float unary operator: {op.op}")

        elif op.expr.type == Type.bool():
            if op.op == '!' or op.op == 'not':
                result.append("i32.eqz")
            else:
                result.append(f";; Unknown boolean unary operator: {op.op}")

        else:
            result.append(f";; Unknown type for unary op: {op.expr.type}")

        return result

    def _generate_function_call(self, call: SubprogramCall) -> List[str]:
        """Generate function call"""
        result = []

        # Generate arguments
        for arg in call.args:
            arg_code = self._generate_expression(arg)
            result.extend(arg_code)

        # Call function
        result.append(f"call ${call.name}")

        return result

    def _generate_cast(self, cast: CastExpr) -> List[str]:
        """Generate type cast"""
        result = self._generate_expression(cast.expr)

        src_type = cast.expr.type
        dst_type = cast.target_type

        if src_type == dst_type:
            return result  # No cast needed

        # Integer to Float
        if src_type == Type.int() and dst_type == Type.float():
            result.append("f32.convert_i32_s")

        # Float to Integer
        elif src_type == Type.float() and dst_type == Type.int():
            result.append("i32.trunc_f32_s")

        # Boolean to Integer
        elif src_type == Type.bool() and dst_type == Type.int():
            # Boolean is already i32, no conversion needed
            pass

        # Integer to Boolean
        elif src_type == Type.int() and dst_type == Type.bool():
            result.append("i32.const 0")
            result.append("i32.ne")

        # Float to Boolean
        elif src_type == Type.float() and dst_type == Type.bool():
            result.append("f32.const 0.0")
            result.append("f32.ne")

        else:
            result.append(f";; Unsupported cast: {src_type} -> {dst_type}")

        return result

    def _type_to_wasm(self, type_: Type) -> str:
        """Convert Type enum to WAT type string"""
        if type_ == Type.int():
            return "i32"
        elif type_ == Type.float():
            return "f32"
        elif type_ == Type.bool():
            return "i32"
        elif type_ == Type.string():
            return "i32"  # Strings as pointers
        elif type_ == Type.void():
            return ""
        else:
            return "i32"  # Default


def ast_to_wat(program: ProgramNode) -> str:
    generator = WATGenerator()
    return generator.generate_wat(program)


if __name__ == "__main__":
    sample_program = ProgramNode(
        subprograms=[
            SubprogramNode(
                name="factorial",
                param_names=["n"],
                param_types=[Type.int()],
                body=BlockNode(body=[
                    VarDecl(type=Type.int(), name="result", init=IntLiteral(value=1)),
                    VarDecl(type=Type.int(), name="i", init=IntLiteral(value=1)),
                    WhileStmt(
                        cond=BinaryOp(op="<=",
                                      left=VarRef(name="i", type=Type.int()),
                                      right=VarRef(name="n", type=Type.int()),
                                      type=Type.bool()),
                        body=BlockNode(body=[
                            AssignNode(
                                name="result",
                                value=BinaryOp(op="*",
                                               left=VarRef(name="result", type=Type.int()),
                                               right=VarRef(name="i", type=Type.int()),
                                               type=Type.int()),
                                type=Type.int()
                            ),
                            AssignNode(
                                name="i",
                                value=BinaryOp(op="+",
                                               left=VarRef(name="i", type=Type.int()),
                                               right=IntLiteral(value=1),
                                               type=Type.int()),
                                type=Type.int()
                            )
                        ])
                    ),
                    Return()
                ]),
                type=Type.int()
            )
        ],
        statements=[
            VarDecl(type=Type.int(), name="x", init=IntLiteral(value=5)),
            VarDecl(type=Type.int(), name="result", init=None),
            AssignNode(
                name="result",
                value=SubprogramCall(
                    name="factorial",
                    args=[VarRef(name="x", type=Type.int())],
                    type=Type.int()
                ),
                type=Type.int()
            ),
            Return()
        ]
    )

    wat_code = ast_to_wat(sample_program)
    print(wat_code)