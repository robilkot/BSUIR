import sys
from itertools import zip_longest

from antlr4 import *

from generated.grammar.MathLangLexer import MathLangLexer
from generated.grammar.MathLangParser import MathLangParser
from generated.grammar.MathLangVisitor import MathLangVisitor
from models.errors import SemanticError
from models.error_formatter import ErrorFormatter
from models.symbol import Symbol, SubprogramSymbol, SymbolTable
from models.types import Type
from models.type_checker import TypeChecker


class SemanticAnalyzer(MathLangVisitor):
    def __init__(self):
        self.global_scope = SymbolTable()
        self.current_scope = self.global_scope
        self.current_subprogram = None
        self.errors = []
        self.warnings = []

        self.__default_subprograms = [
            SubprogramSymbol(name='write', return_type=Type.void(), parameters=[Type('T')], template_args=[Type('T')]),
            SubprogramSymbol(name='cast', return_type=Type('T'), parameters=[Type('K')], template_args=[Type('K'), Type('T')]),
            SubprogramSymbol(name='abs', return_type=Type.float(), parameters=[Type.float()], template_args=[]),
            SubprogramSymbol(name='log', return_type=Type.float(), parameters=[Type.float()], template_args=[]),
            SubprogramSymbol(name='ln', return_type=Type.float(), parameters=[Type.float()], template_args=[]),
            SubprogramSymbol(name='sin', return_type=Type.float(), parameters=[Type.float()], template_args=[]),
            SubprogramSymbol(name='cos', return_type=Type.float(), parameters=[Type.float()], template_args=[]),
            SubprogramSymbol(name='tg', return_type=Type.float(), parameters=[Type.float()], template_args=[]),
            SubprogramSymbol(name='atg', return_type=Type.float(), parameters=[Type.float()], template_args=[]),
            SubprogramSymbol(name='ctg', return_type=Type.float(), parameters=[Type.float()], template_args=[]),
            SubprogramSymbol(name='actg', return_type=Type.float(), parameters=[Type.float()], template_args=[]),
            SubprogramSymbol(name='asin', return_type=Type.float(), parameters=[Type.float()], template_args=[]),
            SubprogramSymbol(name='acos', return_type=Type.float(), parameters=[Type.float()], template_args=[]),
            SubprogramSymbol(name='read', return_type=Type('T'), parameters=[], template_args=[Type('T')])
        ]

        for sub in self.__default_subprograms:
            self.global_scope.add_symbol(sub)

    def add_error(self, message, ctx=None):
        line = ctx.start.line if ctx else None
        column = ctx.start.column if ctx else None
        error = SemanticError(message, line, column)
        self.errors.append(error)
        print(f"❌ {error}")

    def visitSubprogram(self, ctx: MathLangParser.SubprogramContext):
        sub_name = ctx.ID().getText()

        parameters_symbols: list[Symbol] = []
        if ctx.declaration_list():
            param_symbols = self.visitDeclaration_list(ctx.declaration_list(), allow_decl_only=True)
            for param in param_symbols:
                parameters_symbols.append(param)

        # todo templ args
        subprogram_symbol = SubprogramSymbol(name=sub_name, return_type=Type.void(), parameters=[param.type for param in parameters_symbols], template_args=[])

        try:
            self.global_scope.add_symbol(subprogram_symbol)
        except SemanticError as e:
            self.add_error(e.message, ctx)

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
                self.add_error(e.message, ctx)

        self.visitBlock(ctx.block())

        # Восстанавливаем предыдущий контекст
        self.current_scope = previous_scope
        self.current_subprogram = previous_subprogram

    def visitDeclaration_list(self, ctx: MathLangParser.Declaration_listContext, allow_decl_only: bool = False) -> list[Symbol]:
        # NOT float x
        # float x = 0
        # global float x = 0
        # global float x
        local = ctx.scope_modifier() is None

        def get_right_expr_count(decl_ctx) -> int:
            return len([expr for expr in decl_ctx if expr.expression() is not None])

        is_expr_count_valid_func = \
            lambda i: i == 0 or i == 1 or i == len(ctx.type_specifier()) \
                if not local else\
                lambda i: i == 1 or i == len(ctx.type_specifier() or (i == 0 and allow_decl_only))

        expr_count = get_right_expr_count(ctx.variable_declaration())
        if not is_expr_count_valid_func(expr_count):
            # print(ctx.getText(), expr_count)
            self.add_error(ErrorFormatter.unmatched_number_of_expressions_or_not_single_expression(), ctx)

        declarations = []

        left_type = None
        init_type = None
        for type_ctx, decl_ctx in zip_longest(reversed(ctx.type_specifier()), reversed(ctx.variable_declaration()), fillvalue=None):
            if type_ctx is not None:
                left_type = Type.create(type_ctx.getText())

            init_expression = decl_ctx.expression()
            if init_expression is not None:
                init_type = TypeChecker.get_expression_type(init_expression, self)

            var_name = decl_ctx.ID().getText()
            # print('GLOBAL' if not local else '', safe_type_name(left_type), var_name, safe_type_name(init_type), init_expression.getText() if init_expression else None)

            if init_type and not TypeChecker.can_cast(init_type, left_type):
                self.add_error(ErrorFormatter.cant_assign_from_to(from_type=init_type, to_type=left_type), decl_ctx)

            symbol = Symbol(var_name, left_type)
            declarations.insert(0, symbol)  # todo check sometime

        return declarations

    def visitAssignment(self, ctx: MathLangParser.AssignmentContext):
        def add_assignment_error(expected: Type, actual: Type):
            self.add_error(ErrorFormatter.cant_assign_from_to(from_type=actual, to_type=expected), ctx)

        left_side = ctx.declaration_list() or ctx.id_list()
        right_expressions = self.visitExpression_list(ctx.expression_list())

        left_side: MathLangParser.Id_listContext
        if isinstance(left_side, MathLangParser.Id_listContext):
            left_symbols: list[Symbol] | None = self.visitId_list(left_side)

            if left_symbols is None or len(left_symbols) != len(right_expressions):
                self.add_error(ErrorFormatter.unmatched_variables_and_expressions(), ctx)
                return

            for symbol, expression_type in zip(left_symbols, right_expressions):
                if symbol is not None:
                    if not TypeChecker.can_cast(expression_type, symbol.type):
                        add_assignment_error(symbol.type, expression_type)

        elif isinstance(left_side, MathLangParser.Declaration_listContext):
            left_symbols = self.visitDeclaration_list(left_side)

            for symbol in left_symbols:
                try:
                    self.current_scope.add_symbol(symbol)
                except SemanticError as e:
                    self.add_error(e.message, ctx)

            if len(right_expressions) != 1:
                if len(left_symbols) != len(right_expressions):
                    self.add_error(ErrorFormatter.unmatched_variables_and_expressions(), ctx)
                    return

                for symbol, expression_type in zip(left_symbols, right_expressions):
                    if not TypeChecker.can_cast(expression_type, symbol.type):
                        add_assignment_error(symbol.type, expression_type)
            else:
                for symbol in left_symbols:
                    if not TypeChecker.can_cast(right_expressions[0], symbol.type):
                        add_assignment_error(symbol.type, right_expressions[0])
        else:
            raise ValueError("Unknown type")

    def visitId_list(self, ctx: MathLangParser.Id_listContext) -> list[Symbol] | None:
        ids: list[Symbol | None] = []

        for id in ctx.ID():
            symbols = self.current_scope.lookup(id.getText())

            if symbols is None:
                self.add_error(ErrorFormatter.undefined_symbol(id), ctx)
                ids.append(None)
            else:
                ids += symbols

        return ids

    def visitExpression_list(self, ctx: MathLangParser.Expression_listContext) -> list[Type]:
        types = []
        if ctx.expression():
            for expr in ctx.expression():
                expr_type = self.visitExpression(expr)
                types.append(expr_type)
        return types

    def visitExpression(self, ctx: MathLangParser.ExpressionContext) -> Type | None:
        def visit_binary_expression(ctx, operator: str) -> Type | None:
            left_type = self.visitExpression(ctx.expression(0))
            right_type = self.visitExpression(ctx.expression(1))

            if left_type is None or right_type is None:
                return None

            try:
                result_type = TypeChecker.get_binary_operation_type(left_type, right_type, operator)
                return result_type
            except SemanticError as e:
                self.add_error(e.message, ctx)
                return None

        def visit_unary_expression(ctx, operator: str) -> Type | None:
            expr_type = self.visit(ctx.expression(0))

            if operator == '-' and not TypeChecker.is_numeric_type(expr_type) and not TypeChecker.is_boolean_type(expr_type):
                self.add_error(ErrorFormatter.unary_operator_only_valid_on_types(operator, 'числовым и булевым типам', expr_type), ctx)
                return None

            return expr_type

        if ctx.ID():
            var_name = ctx.ID().getText()
            symbol = self.current_scope.lookup(var_name)
            if not symbol:
                self.add_error(ErrorFormatter.undefined_symbol(var_name), ctx)
                return None
            else:
                symbol = symbol[0]

            return symbol.type

        elif ctx.literal():
            return self.visitLiteral(ctx.literal())
        elif ctx.call():
            return self.visitCall(ctx.call())

        elif ctx.getChildCount() == 3 and ctx.getChild(0).getText() == '(':
            # Выражение в скобках
            expr_type = self.visitExpression(ctx.expression(0))
            return expr_type

        elif ctx.NOT():
            return visit_unary_expression(ctx, ctx.NOT().getText())
        elif ctx.MINUS() and ctx.getChildCount() == 2:
            return visit_unary_expression(ctx, ctx.MINUS().getText())
        elif len(ctx.EQ()) == 2:
            return visit_binary_expression(ctx, "==")
        else:
            binary_operator = ctx.getChild(1).getText()
            return visit_binary_expression(ctx, binary_operator)

    def visitCall(self, ctx: MathLangParser.CallContext, expected_type: Type = Type.void) -> Type | None:
        sub_name = ctx.ID().getText()
        sub_parameters = self.visitExpression_list(ctx.expression_list()) if ctx.expression_list() is not None else []

        defined_subprograms = self.global_scope.lookup(sub_name)
        if defined_subprograms is None:
            self.add_error(ErrorFormatter.undefined_subprogram(sub_name), ctx)
            return None

        found_overload = None
        for defined_subprogram in defined_subprograms:
            if not isinstance(defined_subprogram, SubprogramSymbol):
                continue

            if len(defined_subprogram.parameters) != len(sub_parameters):
                continue

            params_ok = True
            for (param_called, param_actual) in zip(defined_subprogram.parameters, sub_parameters):
                if not TypeChecker.can_cast(param_called, param_actual):
                    params_ok = False
                    break

            if not params_ok:
                continue

            found_overload = defined_subprogram
            break

        # todo cast subprogram
        #     target_type = Type.create(ctx.type_specifier().getText())
        #     expr_type = self.visitExpression(ctx.expression())
        #
        #     if not TypeChecker.can_cast(expr_type, target_type):
        #         self.add_error(ErrorFormatter.invalid_cast(from_type=expr_type, to_type=target_type), ctx)
        #         return None
        #
        #     return target_type

        if found_overload is None:
            self.add_error(ErrorFormatter.no_overload_found(sub_name, sub_parameters), ctx)
            return None

        return found_overload.type

    def visitLiteral(self, ctx: MathLangParser.LiteralContext) -> Type:
        if ctx.INT():
            string = 'int'
        elif ctx.FLOAT():
            string = 'float'
        elif ctx.BOOL():
            string = 'bool'
        elif ctx.STRING():
            string = 'string'
        else:
            string = 'unknown'

        return Type.create(string)


    def visitBranching(self, ctx: MathLangParser.BranchingContext):
        condition_type = self.visit(ctx.expression())

        if not TypeChecker.is_boolean_type(condition_type):
            self.add_error(ErrorFormatter.unmatched_condition_type(condition_type), ctx.expression())

        self.visitBlock(ctx.block(0))

        if ctx.ELSE():
            self.visitBlock(ctx.block(1))

    def visitLoop(self, ctx: MathLangParser.LoopContext):
        # Сохраняем текущий контекст и создаем новую область видимости
        previous_scope = self.current_scope

        self.current_scope = self.current_scope.create_child_scope()
        self.current_scope.parent = previous_scope

        if ctx.for_loop():
            self.visitFor_loop(ctx.for_loop())
        elif ctx.while_loop():
            self.visitWhile_loop(ctx.while_loop())
        elif ctx.until_loop():
            self.visitUntil_loop(ctx.until_loop())

        # Восстанавливаем предыдущий контекст
        self.current_scope = previous_scope

    def visitWhile_loop(self, ctx: MathLangParser.While_loopContext):
        condition_type = self.visit(ctx.expression())

        if not TypeChecker.is_boolean_type(condition_type):
            self.add_error(ErrorFormatter.unmatched_condition_type(condition_type), ctx.expression())

        self.visitBlock(ctx.block())

    def visitUntil_loop(self, ctx: MathLangParser.Until_loopContext):
        condition_type = self.visit(ctx.expression())

        if not TypeChecker.is_boolean_type(condition_type):
            self.add_error(ErrorFormatter.unmatched_condition_type(condition_type), ctx.expression())

        self.visitBlock(ctx.block())

    def visitFor_loop(self, ctx: MathLangParser.For_loopContext):
        self.visitAssignment(ctx.assignment())

        condition_type = self.visit(ctx.expression())
        if not TypeChecker.is_boolean_type(condition_type):
            self.add_error(ErrorFormatter.unmatched_condition_type(condition_type), ctx.expression())

        self.visit(ctx.statement())

        self.visitBlock(ctx.block())

    def visitBlock(self, ctx: MathLangParser.BlockContext):
        # Создаем новую область видимости для блока
        previous_scope = self.current_scope
        self.current_scope = self.current_scope.create_child_scope()

        # Обрабатываем statements внутри блока
        if ctx:
            for stmt in ctx.statement():
                self.visit(stmt)

        # Восстанавливаем предыдущую область видимости
        self.current_scope = previous_scope

    def visitControl_flow_operator(self, ctx: MathLangParser.Control_flow_operatorContext):
        if ctx.RETURN() and not self.current_subprogram:
            self.add_error(ErrorFormatter.return_outside_of_subprogram(), ctx)


def main():
    if len(sys.argv) != 2:
        print("No file specified. Using default one.")

    source_file = sys.argv[1] if len(sys.argv) > 1 else 'samples/sample4.ml'

    try:
        input_stream = FileStream(source_file, encoding='utf-8')
        lexer = MathLangLexer(input_stream)
        tokens = CommonTokenStream(lexer)

        parser = MathLangParser(tokens)
        tree = parser.program()

        analyzer = SemanticAnalyzer()
        analyzer.visit(tree)

        if analyzer.errors:
            print(f"\n🔴 Семантический анализ завершен с ошибками: {len(analyzer.errors)}")
            sys.exit(1)
        else:
            print("✅ Программа семантически корректна!")
            sys.exit(0)

    except FileNotFoundError:
        print(f"❌ Файл {source_file} не найден")
        sys.exit(1)


if __name__ == "__main__":
    main()