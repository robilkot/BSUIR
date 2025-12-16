import sys

from antlr4 import *

from generated.grammar.MathLangLexer import MathLangLexer
from generated.grammar.MathLangParser import MathLangParser
from generated.grammar.MathLangVisitor import MathLangVisitor
from intermediate_code.ast_nodes import ProgramNode, SubprogramNode, BlockNode, VarDecl, StatementNode, ReturnNode, \
    BreakNode, ContinueNode, IfStmt, Expr, UnaryOp, AssignNode, VarRef, IntLiteral, FloatLiteral, BoolLiteral, \
    StringLiteral, BinaryOp, ForStmt, WhileStmt, UntilStmt, SubprogramCall
from intermediate_code.wat_emitter import WATEmitter
from models.error_formatter import ErrorFormatter
from models.errors import SemanticError
from models.symbol import Symbol, SubprogramSymbol, SymbolTable
from models.type_checker import TypeChecker
from models.types import Type
from syntax_analyzer import CustomErrorListener


# todo check for unused template arguments
# todo check for templated sub before using explicit implementation
class SemanticAnalyzer(MathLangVisitor):
    def __init__(self):
        self.global_scope = SymbolTable()
        self.current_scope = self.global_scope
        self.current_subprogram: SubprogramSymbol | None = None
        self.in_loop = False
        self.type_mapping: dict[Type, Type] | None = None
        self.subprogram_ctx: dict[SubprogramSymbol, MathLangParser.SubprogramContext] = {}
        self.defining_subprogram = True
        self.errors = []
        self.wat_code = []

        self.program_node: ProgramNode = ProgramNode(subprograms=[], statements=[])
        self.__subprograms_blocks: dict[SubprogramSymbol, BlockNode] = {}

        self.binding_cache = set()

        self.__default_subprograms = [
            SubprogramSymbol(name='cast', return_type=Type('T'), parameters=[Symbol(type=Type('K'), name='from')], template_args=[Type('K'), Type('T')]),
            SubprogramSymbol(name='write', return_type=Type.void(), parameters=[Symbol(type=Type('T'), name='msg')], template_args=[Type('T')]),
            SubprogramSymbol(name='read', return_type=Type('T'), parameters=[], template_args=[Type('T')]),
        ]

        self.__math_subprograms = [
            SubprogramSymbol(name='abs', return_type=Type.float(), parameters=[Symbol(type=Type.float(), name='x')], template_args=[]),
            SubprogramSymbol(name='log', return_type=Type.float(), parameters=[Symbol(type=Type.float(), name='x')], template_args=[]),
            SubprogramSymbol(name='ln', return_type=Type.float(), parameters=[Symbol(type=Type.float(), name='x')], template_args=[]),
            SubprogramSymbol(name='sin', return_type=Type.float(), parameters=[Symbol(type=Type.float(), name='x')], template_args=[]),
            SubprogramSymbol(name='cos', return_type=Type.float(), parameters=[Symbol(type=Type.float(), name='x')], template_args=[]),
            SubprogramSymbol(name='tg', return_type=Type.float(), parameters=[Symbol(type=Type.float(), name='x')], template_args=[]),
            SubprogramSymbol(name='atg', return_type=Type.float(), parameters=[Symbol(type=Type.float(), name='x')], template_args=[]),
            SubprogramSymbol(name='ctg', return_type=Type.float(), parameters=[Symbol(type=Type.float(), name='x')], template_args=[]),
            SubprogramSymbol(name='actg', return_type=Type.float(), parameters=[Symbol(type=Type.float(), name='x')], template_args=[]),
            SubprogramSymbol(name='asin', return_type=Type.float(), parameters=[Symbol(type=Type.float(), name='x')], template_args=[]),
            SubprogramSymbol(name='acos', return_type=Type.float(), parameters=[Symbol(type=Type.float(), name='x')], template_args=[]),
        ]

        for sub in self.__default_subprograms:
            self.global_scope.add_symbol(sub)
        for sub in self.__math_subprograms:
            self.global_scope.add_symbol(sub)

    @property
    def is_binding(self) -> bool:
        return self.type_mapping is not None

    def add_error(self, message, ctx=None):
        line = ctx.start.line if ctx else None
        column = ctx.start.column if ctx else None
        error = SemanticError(message, line, column)
        self.errors.append(error)


    def visitProgram(self, ctx:MathLangParser.ProgramContext):
        for sub in ctx.subprogram():
            self.visitSubprogram(sub)

        self.defining_subprogram = False

        for statement in ctx.statement():
            node = self.visit(statement)
            if isinstance(node, list):
                for subnode in node:
                    self.program_node.statements.append(subnode)
            else:
                self.program_node.statements.append(node)

        # AST
        for symbol in self.global_scope.symbols:
            if isinstance(symbol, SubprogramSymbol):
                sub_node = SubprogramNode(
                    name=symbol.name,
                    type=symbol.type,
                    param_types=[param.type for param in symbol.parameters],
                    param_names=[param.name for param in symbol.parameters],
                    # body=self.__subprograms_blocks[symbol]
                    body=BlockNode(body=[])
                )
                self.program_node.subprograms.append(sub_node)

    def visitSubprogram(self, ctx: MathLangParser.SubprogramContext) -> SubprogramNode | None:
        sub_name = ctx.ID().getText()

        parameters_symbols: list[Symbol] = []
        if ctx.declaration_list():
            params_symbols = self.visitDeclaration_list(ctx.declaration_list())

            # map params types
            if self.is_binding:
                for symbol in params_symbols:
                    parameters_symbols.append(Symbol(name=symbol.name, type=self.type_mapping.get(symbol.type, symbol.type), is_global=symbol.is_global))
            else:
                parameters_symbols += params_symbols

        template_args: list[Type] | None = None
        if ctx.template():
            template_args = self.visitTemplate(ctx.template())

        # map template args
        if template_args is not None:
            template_args = [self.type_mapping.get(type, type) for type in template_args] if self.is_binding else template_args

        if template_args:
            for symbol in parameters_symbols:
                if TypeChecker.is_templated_argument(symbol.type) and symbol.type not in template_args:
                    self.add_error(ErrorFormatter.undefined_templated_argument(symbol.type), ctx)
        else:
            for symbol in parameters_symbols:
                if TypeChecker.is_templated_argument(symbol.type):
                    self.add_error(ErrorFormatter.undefined_templated_argument(symbol.type), ctx)

        if self.is_binding:
            if template_args:
                mangled_name = "_".join([sub_name] + [type.name for type in template_args])
            else:
                mangled_name = sub_name
            subprogram_symbol = SubprogramSymbol(name=mangled_name, return_type=Type.void(), parameters=parameters_symbols,template_args=template_args)
        else:
            subprogram_symbol = SubprogramSymbol(name=sub_name, return_type=Type.void(), parameters=parameters_symbols, template_args=template_args)

        try:
            self.global_scope.add_symbol(subprogram_symbol)
            self.subprogram_ctx[subprogram_symbol] = ctx
        except SemanticError as e:
            if not self.is_binding:
                self.add_error(e.message, ctx)

        if self.is_binding:
            if self.binding_cache.__contains__(subprogram_symbol):
                print("Warning: templated recursion detected")
                return None
            self.binding_cache.add(subprogram_symbol)

        # Сохраняем текущий контекст и создаем новую область видимости
        previous_scope = self.current_scope
        previous_subprogram = self.current_subprogram

        self.current_subprogram = subprogram_symbol
        self.current_scope = subprogram_symbol.local_scope

        # Добавляем параметры в локальную область видимости подпрограммы
        for param_symbol in parameters_symbols:
            try:
                self.current_scope.add_symbol(param_symbol)
            except SemanticError as e:
                if not self.is_binding:
                    self.add_error(e.message, ctx)


        block_node = self.visitBlock(ctx.block())
        subprogram_node = SubprogramNode(
            name=subprogram_symbol.name,
            type=subprogram_symbol.type,
            param_types=[param.type for param in subprogram_symbol.parameters],
            param_names=[param.name for param in subprogram_symbol.parameters],
            body=block_node
        )

        # Восстанавливаем предыдущий контекст
        self.current_scope = previous_scope
        self.current_subprogram = previous_subprogram

        if self.is_binding:
            self.binding_cache.remove(subprogram_symbol)

        return subprogram_node

    # todo return expr
    def visitCall(self, ctx: MathLangParser.CallContext) -> Expr | None:
        sub_name = ctx.ID().getText()
        sub_parameters = self.visitExpression_list(ctx.expression_list()) if ctx.expression_list() is not None else []
        sub_templated_arguments = self.visitTemplate(ctx.template()) if ctx.template() is not None else []

        # Special case: cast subprogram
        if sub_name == 'cast':
            if len(sub_templated_arguments) != 2:
                self.add_error(ErrorFormatter.cast_with_not_two_arguments(len(sub_templated_arguments)), ctx)
                return None

        if sub_name == 'read':
            if len(sub_templated_arguments) != 1:
                self.add_error(ErrorFormatter.read_with_not_one_template_argument(len(sub_templated_arguments)), ctx)
                return None

        if self.is_binding and not self.current_subprogram:
            for param in sub_parameters:
                param.type = self.type_mapping.get(param.type, param.type)

                if TypeChecker.is_templated_argument(param.type):
                    # todo error message
                    self.add_error(f"fuck {param}", ctx)

            sub_templated_arguments = [self.type_mapping.get(type, type) for type in sub_templated_arguments]

        defined_subprograms = self.global_scope.lookup(sub_name)
        if defined_subprograms is None:
            self.add_error(ErrorFormatter.undefined_subprogram(sub_name), ctx)
            return None

        overload_candidate_subprograms: list[tuple[SubprogramSymbol, dict[Type, Type]]] = []

        for defined_subprogram in defined_subprograms:
            if not isinstance(defined_subprogram, SubprogramSymbol):
                continue

            if len(defined_subprogram.parameters) != len(sub_parameters):
                continue

            templated_types_mapping: dict[Type, Type] = {}
            params_ok = True
            for (param_expected, actual_node) in zip(defined_subprogram.parameters, sub_parameters):
                if actual_node is None:
                    continue

                node_type = actual_node.type
                if TypeChecker.is_templated_argument(param_expected.type):
                    if templated_types_mapping.get(param_expected.type, None) is None:
                        templated_types_mapping[param_expected.type] = node_type
                else:
                    if param_expected.type != node_type:
                        params_ok = False
                        break

            if params_ok:
                # = Is templated subprogram
                if len(templated_types_mapping) > 0:
                    overload_candidate_subprograms.append((defined_subprogram, templated_types_mapping))
                else:
                    overload_candidate_subprograms.insert(0, (defined_subprogram, templated_types_mapping))

        # Try to find suitable with higher priority for non-templated subs
        can_bind = False
        type_mapping: dict[Type, Type] | None = None
        subprogram: SubprogramSymbol | None = None

        previous_mapping = self.type_mapping

        for subprogram, type_mapping in overload_candidate_subprograms:
            if subprogram.template_args:
                for declared, provided in zip(subprogram.template_args, sub_templated_arguments):
                    if type_mapping.get(declared, None) is None:
                        type_mapping[declared] = provided

            self.type_mapping = type_mapping

            subprogram_ctx = self.subprogram_ctx.get(subprogram, None)
            if subprogram_ctx is None:
                # print("No ctx found for", subprogram)
                can_bind = True
            else:
                can_bind = self.visitSubprogram(subprogram_ctx)

            if can_bind:
                # if self.is_binding:
                #     print("call to", ctx.getText(), "= bind", subprogram , "with", type_mapping)

                # Special case: cast subprogram
                if subprogram.name == 'cast':
                    from_type = self.type_mapping.get(subprogram.template_args[0], None)
                    to_type = self.type_mapping.get(subprogram.template_args[1], None)
                    if (not TypeChecker.is_templated_argument(from_type)
                            and not TypeChecker.is_templated_argument(to_type)
                            and not TypeChecker.can_cast(from_type, to_type)):
                        self.add_error(ErrorFormatter.invalid_cast(from_type, to_type, self.type_mapping), ctx)

            self.type_mapping = previous_mapping

            if can_bind:
                break

        if not can_bind and not self.defining_subprogram:
            self.add_error(ErrorFormatter.no_overload_found(sub_name, sub_parameters), ctx)
            return None

        if subprogram is None:
            return None

        return_type = subprogram.type
        if type_mapping:
            return_type = type_mapping.get(return_type, return_type)

        call_node = SubprogramCall(
            name=subprogram.name,
            args=sub_parameters,
            type=return_type,
        )
        print(call_node)
        return call_node


    def visitTemplate(self, ctx:MathLangParser.TemplateContext) -> list[Type]:
        return self.visitType_specifier_list(ctx.type_specifier_list())

    def visitType_specifier_list(self, ctx:MathLangParser.Type_specifier_listContext) -> list[Type]:
        result = []
        for type_specifier in ctx.type_specifier():
            result.append(Type.create(type_specifier.getText()))
        return result

    # todo review
    def visitGlobal_variable_declaration(self, ctx:MathLangParser.Global_variable_declarationContext) -> VarDecl:
        if self.current_subprogram is None:
            self.add_error(ErrorFormatter.uninitialized_global_symbol(ctx.ID().getText()), ctx)

        return VarDecl(
            name=ctx.ID().getText(),
            type=ctx.type_specifier().getText(),
            init=None
        )

    def visitDeclaration_list(self, ctx: MathLangParser.Declaration_listContext) -> list[Symbol]:
        local = ctx.scope_modifier() is None

        declarations = []
        for type_ctx, id_ctx in zip(ctx.type_specifier(), ctx.ID()):
            var_type = Type.create(type_ctx.getText())
            var_name = id_ctx.getText()

            if self.is_binding:
                var_type = self.type_mapping.get(var_type, var_type)

            # print('GLOBAL' if not local else '', var_type, var_name)

            symbol = Symbol(var_name, var_type, is_global=(not local))
            declarations.append(symbol)

        return declarations

    def visitAssignment(self, ctx: MathLangParser.AssignmentContext) -> list[AssignNode]:
        result: list[AssignNode] = []

        def add_assignment_error(expected: Type, actual: Type):
            self.add_error(ErrorFormatter.cant_assign_from_to(from_type=actual, to_type=expected), ctx)

        left_side = ctx.declaration_list() if ctx.declaration_list() else ctx.id_list()
        right_expressions: list[Expr] = self.visitExpression_list(ctx.expression_list())

        left_side: MathLangParser.Id_listContext
        if isinstance(left_side, MathLangParser.Id_listContext):
            left_symbols: list[Symbol] | None = self.visitId_list(left_side)

            if left_symbols is None or len(left_symbols) != len(right_expressions):
                self.add_error(ErrorFormatter.unmatched_number_of_expressions_or_not_single_expression(), ctx)
                return []

            for symbol, expression_node in zip(left_symbols, right_expressions):
                if expression_node is None:
                    continue

                if symbol is not None:
                    result.append(AssignNode(name=symbol.name, value=expression_node, type=symbol.type))

                    expr_type = expression_node.type
                    if expr_type != symbol.type:
                        can_ignore_error_while_templating = (self.current_subprogram
                                                             and (TypeChecker.is_templated_argument(expr_type)
                                                                  or TypeChecker.is_templated_argument(symbol.type)))
                        if not can_ignore_error_while_templating:
                            add_assignment_error(symbol.type, expr_type)

        elif isinstance(left_side, MathLangParser.Declaration_listContext):
            left_symbols = self.visitDeclaration_list(left_side)

            for symbol in left_symbols:
                try:
                    self.current_scope.add_symbol(symbol)
                except SemanticError as e:
                    self.add_error(e.message, ctx)

            for symbol in left_symbols:
                if not self.is_binding and not self.current_subprogram:
                    if TypeChecker.is_templated_argument(symbol.type):
                        self.add_error(ErrorFormatter.undefined_type(symbol.type), ctx)

            if len(right_expressions) != 1:
                if len(left_symbols) != len(right_expressions):
                    self.add_error(ErrorFormatter.unmatched_number_of_expressions_or_not_single_expression(), ctx)
                    return []

                for symbol, expression_node in zip(left_symbols, right_expressions):
                    expr_type = expression_node.type

                    result.append(AssignNode(name=symbol.name, value=expression_node, type=symbol.type))
                    if expr_type != symbol.type:
                        add_assignment_error(symbol.type, expr_type)
            else:
                for symbol in left_symbols:
                    right_expr = right_expressions[0]
                    if right_expr is None:
                        continue
                        
                    expr_type = right_expr.type

                    result.append(AssignNode(name=symbol.name, value=right_expr, type=symbol.type))
                    if expr_type != symbol.type:
                        add_assignment_error(symbol.type, expr_type)

        return result

    def visitId_list(self, ctx: MathLangParser.Id_listContext) -> list[Symbol] | None:
        ids: list[Symbol | None] = []

        for id in ctx.ID():
            symbols = self.current_scope.lookup(id.getText())

            if symbols is None:
                self.add_error(ErrorFormatter.undefined_symbol(id), ctx)
                ids.append(None)
            else:
                for symbol in symbols:
                    if self.is_binding:
                        symbol.type = self.type_mapping.get(symbol.type, symbol.type)

                    ids.append(symbol)

        return ids

    def visitExpression_list(self, ctx: MathLangParser.Expression_listContext) -> list[Expr]:
        expr_list: list[Expr] = []
        if ctx.expression():
            for expr in ctx.expression():
                expr_node = self.visitExpression(expr)
                expr_list.append(expr_node)
        return expr_list

    def visitExpression(self, ctx: MathLangParser.ExpressionContext) -> Expr | None:
        result: Expr | None = None

        def visit_binary_expression(ctx, operator: str) -> Expr | None:
            left_expr_node = self.visitExpression(ctx.expression(0))
            right_expr_node = self.visitExpression(ctx.expression(1))

            if left_expr_node is None or right_expr_node is None:
                return None

            try:
                result_node_type = TypeChecker.get_binary_operation_type(
                    left_expr_node.type,
                    right_expr_node.type,
                    operator, self.type_mapping)

                return BinaryOp(type=result_node_type, op=operator, left=left_expr_node, right=right_expr_node)
            except SemanticError as e:
                self.add_error(e, ctx)
                return BinaryOp(type=left_expr_node.type, op=operator, left=left_expr_node, right=right_expr_node)

        def visit_unary_expression(ctx, operator: str) -> Expr | None:
            expr_node = self.visitExpression(ctx.expression(0))

            def valid_type(type: Type | None) -> bool:
                return TypeChecker.is_numeric_type(type) or TypeChecker.is_boolean_type(type)

            expr_type = expr_node.type
            if operator == '-' and not valid_type(expr_type):
                self.add_error(ErrorFormatter.unary_operator_only_valid_on_types(operator, 'числовым и булевым типам', expr_type, self.type_mapping), ctx)
                return None

            return UnaryOp(type=expr_node.type, expr=expr_node, op=operator)

        if ctx.ID():
            var_name = ctx.ID().getText()
            symbol = self.current_scope.lookup(var_name)
            if not symbol:
                self.add_error(ErrorFormatter.undefined_symbol(var_name), ctx)
            else:
                result = VarRef(name=var_name, type=symbol[0].type)

        elif ctx.literal():
            result = self.visitLiteral(ctx.literal())
        elif ctx.call():
            result = self.visitCall(ctx.call())

        elif ctx.getChildCount() == 3 and ctx.getChild(0).getText() == '(':
            # Выражение в скобках
            result = self.visitExpression(ctx.expression(0))


        elif ctx.NOT():
            result = visit_unary_expression(ctx, ctx.NOT().getText())
        elif ctx.MINUS() and ctx.getChildCount() == 2:
            result = visit_unary_expression(ctx, ctx.MINUS().getText())
        elif len(ctx.EQ()) == 2:
            result = visit_binary_expression(ctx, "==")
        else:
            binary_operator = ctx.getChild(1).getText()
            result = visit_binary_expression(ctx, binary_operator)

        if self.is_binding:
            if result is not None:
                result.type = self.type_mapping.get(result.type, result.type)

        return result

    def visitLiteral(self, ctx: MathLangParser.LiteralContext) -> Expr:
        if ctx.INT():
            return IntLiteral(value=int(ctx.getText()), type=Type.int())
        elif ctx.FLOAT():
            return FloatLiteral(value=float(ctx.getText()), type=Type.float())
        elif ctx.BOOL():
            return BoolLiteral(value=bool(ctx.getText()), type=Type.bool())
        elif ctx.STRING():
            return StringLiteral(value=ctx.getText(), type=Type.string())
        else:
            raise ValueError('Unknown literal type')

    def visitBranching(self, ctx: MathLangParser.BranchingContext) -> StatementNode:
        condition_expr_node = self.visitExpression(ctx.expression())
        condition_type = condition_expr_node.type
        if not TypeChecker.is_boolean_type(condition_type):
            self.add_error(ErrorFormatter.unmatched_condition_type(condition_type), ctx.expression())

        then_block = self.visitBlock(ctx.block(0))

        else_block = None
        if ctx.ELSE():
            else_block = self.visitBlock(ctx.block(1))

        return IfStmt(
            cond=condition_expr_node,
            then_body=then_block,
            else_body=else_block,
        )

    def visitLoop(self, ctx: MathLangParser.LoopContext) -> WhileStmt | ForStmt | UntilStmt:
        # Сохраняем текущий контекст и создаем новую область видимости
        previous_scope = self.current_scope

        self.current_scope = self.current_scope.create_child_scope()
        self.current_scope.parent = previous_scope

        result = None
        if ctx.for_loop():
            result = self.visitFor_loop(ctx.for_loop())
        elif ctx.while_loop():
            result = self.visitWhile_loop(ctx.while_loop())
        elif ctx.until_loop():
            result = self.visitUntil_loop(ctx.until_loop())

        # Восстанавливаем предыдущий контекст
        self.current_scope = previous_scope
        return result

    def visitWhile_loop(self, ctx: MathLangParser.While_loopContext):
        condition_node = self.visitExpression(ctx.expression())
        if condition_node is None:
            condition_node = Expr(type=Type.bool())

        condition_type = condition_node.type
        if not TypeChecker.is_boolean_type(condition_type):
            self.add_error(ErrorFormatter.unmatched_condition_type(condition_type), ctx.expression())

        self.in_loop = True
        block_node = self.visitBlock(ctx.block())
        self.in_loop = False

        return WhileStmt(cond=condition_node, body=block_node)

    def visitUntil_loop(self, ctx: MathLangParser.Until_loopContext):
        condition_node = self.visitExpression(ctx.expression())
        if condition_node is None:
            condition_node = Expr(type=Type.bool())

        condition_type = condition_node.type
        if not TypeChecker.is_boolean_type(condition_type):
            self.add_error(ErrorFormatter.unmatched_condition_type(condition_type), ctx.expression())

        self.in_loop = True
        block_node = self.visitBlock(ctx.block())
        self.in_loop = False

        return UntilStmt(cond=condition_node, body=block_node)

    def visitFor_loop(self, ctx: MathLangParser.For_loopContext) -> ForStmt:
        init_expr_node = self.visitAssignment(ctx.assignment())
        if len(init_expr_node) == 0:
            init_expr_node = Expr(type=Type.create('Unknown'))
        else:
            init_expr_node = init_expr_node[0]

        condition_node = self.visitExpression(ctx.expression())
        if condition_node is None:
            condition_node = Expr(type=Type.bool())

        condition_type = condition_node.type
        if not TypeChecker.is_boolean_type(condition_type):
            self.add_error(ErrorFormatter.unmatched_condition_type(condition_type), ctx.expression())

        step_node = self.visit(ctx.statement())

        self.in_loop = True
        block_node = self.visitBlock(ctx.block())
        self.in_loop = False

        return ForStmt(init=init_expr_node, cond=condition_node, step=step_node, body=block_node)

    def visitBlock(self, ctx: MathLangParser.BlockContext) -> BlockNode:
        previous_scope = self.current_scope
        self.current_scope = self.current_scope.create_child_scope()

        block_node = BlockNode(body=[])
        if ctx:
            for stmt in ctx.statement():
                node = self.visit(stmt)
                if isinstance(node, list):
                    for subnode in node:
                        block_node.body.append(subnode)
                else:
                    block_node.body.append(node)

        self.current_scope = previous_scope
        return block_node

    def visitControl_flow_operator(self, ctx: MathLangParser.Control_flow_operatorContext) -> StatementNode:
        if ctx.RETURN() and not self.current_subprogram:
            self.add_error(ErrorFormatter.return_outside_of_subprogram(), ctx)
        elif ctx.BREAK() and not self.in_loop:
            self.add_error(ErrorFormatter.flow_control_operator_outside_of_loop(), ctx)
        elif ctx.CONTINUE() and not self.in_loop:
            self.add_error(ErrorFormatter.flow_control_operator_outside_of_loop(), ctx)

        if ctx.RETURN():
            return ReturnNode()
        elif ctx.BREAK():
            return BreakNode()
        else: # ctx.CONTINUE():
            return ContinueNode()


def main():
    default_file = 'samples/sample4.ml'
    # default_file = 'samples/samples_templates.ml'

    if len(sys.argv) != 2:
        print(f"No file specified. Using {default_file}.")

    source_file = sys.argv[1] if len(sys.argv) > 1 else default_file
    # source_file = sys.argv[1] if len(sys.argv) > 1 else 'samples/samples_templates.ml'

    try:
        input_stream = FileStream(source_file, encoding='utf-8')
        lexer = MathLangLexer(input_stream)
        tokens = CommonTokenStream(lexer)

        parser = MathLangParser(tokens)

        syntax_error_listener = CustomErrorListener()
        parser.addErrorListener(syntax_error_listener)
        lexer.addErrorListener(syntax_error_listener)

        tree = parser.program()

        if syntax_error_listener.has_errors:
            print(f"\n🔴 Семантический анализ не выполнен, потому что программа синтаксически некорректна")
            sys.exit(1)

        analyzer = SemanticAnalyzer()
        analyzer.visit(tree)

        if analyzer.errors:
            print(f"\n🔴 Семантический анализ завершен с ошибками: {len(analyzer.errors)}")

            for error in analyzer.errors:
                print(f"❌ {error}")
            sys.exit(1)
        else:
            print("✅ Программа семантически корректна!")
            print("\nGenerated WAT code:")

            emitter = WATEmitter()
            print(analyzer.program_node)

            # code = emitter.emit(analyzer.program_node)
            # print(code)

            sys.exit(0)

    except FileNotFoundError:
        print(f"❌ Файл {source_file} не найден")
        sys.exit(1)


if __name__ == "__main__":
    main()