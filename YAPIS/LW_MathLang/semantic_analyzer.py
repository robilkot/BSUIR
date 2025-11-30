import sys

from antlr4 import *

from generated.grammar.MathLangLexer import MathLangLexer
from generated.grammar.MathLangParser import MathLangParser
from generated.grammar.MathLangVisitor import MathLangVisitor
from models.error_formatter import ErrorFormatter
from models.errors import SemanticError
from models.symbol import Symbol, SubprogramSymbol, SymbolTable
from models.type_checker import TypeChecker
from models.types import Type
from syntax_analyzer import CustomErrorListener


class SemanticAnalyzer(MathLangVisitor):
    def __init__(self):
        self.global_scope = SymbolTable()
        self.current_scope = self.global_scope
        self.current_subprogram = None
        self.in_loop = False
        self.errors = []

        self.__cast_subprogram = SubprogramSymbol(name='cast', return_type=Type('Tto'), parameters=[Type('Tfrom')], template_args=[Type('Tfrom'), Type('Tto')])

        self.__default_subprograms = [
            self.__cast_subprogram,
            SubprogramSymbol(name='write', return_type=Type.void(), parameters=[Type('T')], template_args=[Type('T')]),
            SubprogramSymbol(name='read', return_type=Type('T'), parameters=[], template_args=[Type('T')]),
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
            SubprogramSymbol(name='acos', return_type=Type.float(), parameters=[Type.float()], template_args=[])
        ]

        for sub in self.__default_subprograms:
            self.global_scope.add_symbol(sub)

    def add_error(self, message, ctx=None):
        line = ctx.start.line if ctx else None
        column = ctx.start.column if ctx else None
        error = SemanticError(message, line, column)
        self.errors.append(error)

    def visitSubprogram(self, ctx: MathLangParser.SubprogramContext):
        sub_name = ctx.ID().getText()

        parameters_symbols: list[Symbol] = []
        if ctx.declaration_list():
            parameters_symbols += self.visitDeclaration_list(ctx.declaration_list())

        template_args: list[Type] = []
        if ctx.template():
            template_args += self.visitTemplate(ctx.template())

        subprogram_symbol = SubprogramSymbol(name=sub_name, return_type=Type.void(), parameters=[param.type for param in parameters_symbols], template_args=template_args)
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

    def visitCall(self, ctx: MathLangParser.CallContext, expected_type: Type | None = None) -> Type | None:
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

        if found_overload is None:
            self.add_error(ErrorFormatter.no_overload_found(sub_name, sub_parameters), ctx)
            return None


        if found_overload == self.__cast_subprogram:
            expr_type = self.visitExpression_list(ctx.expression_list())[0]

            if not TypeChecker.can_cast(expr_type, expected_type):
                self.add_error(ErrorFormatter.invalid_cast(from_type=expr_type, to_type=expected_type), ctx)
                return None

        return found_overload.type


    def visitTemplate(self, ctx:MathLangParser.TemplateContext) -> list[Type]:
        return self.visitType_specifier_list(ctx.type_specifier_list())

    def visitType_specifier_list(self, ctx:MathLangParser.Type_specifier_listContext) -> list[Type]:
        result = []
        for type_specifier in ctx.type_specifier():
            result.append(Type.create(type_specifier.getText()))
        return result

    # todo review
    def visitGlobal_variable_declaration(self, ctx:MathLangParser.Global_variable_declarationContext):
        if self.current_subprogram is None:
            self.add_error(ErrorFormatter.uninitialized_global_symbol(ctx.ID().getText()), ctx)

    def visitDeclaration_list(self, ctx: MathLangParser.Declaration_listContext) -> list[Symbol]:
        local = ctx.scope_modifier() is None

        declarations = []
        for type_ctx, id_ctx in zip(ctx.type_specifier(), ctx.ID()):
            var_type = Type.create(type_ctx.getText())
            var_name = id_ctx.getText()

            # print('GLOBAL' if not local else '', var_type, var_name)

            symbol = Symbol(var_name, var_type, is_global=(not local))
            declarations.append(symbol)

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
                self.add_error(ErrorFormatter.unmatched_number_of_expressions_or_not_single_expression(), ctx)
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
                    self.add_error(ErrorFormatter.unmatched_number_of_expressions_or_not_single_expression(), ctx)
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


    def visitLiteral(self, ctx: MathLangParser.LiteralContext) -> Type:
        if ctx.INT():
            return Type.int()
        elif ctx.FLOAT():
            return Type.float()
        elif ctx.BOOL():
            return Type.bool()
        elif ctx.STRING():
            return Type.string()
        else:
            raise ValueError('Unknown literal type')

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

        self.in_loop = True
        self.visitBlock(ctx.block())
        self.in_loop = False

    def visitUntil_loop(self, ctx: MathLangParser.Until_loopContext):
        condition_type = self.visit(ctx.expression())

        if not TypeChecker.is_boolean_type(condition_type):
            self.add_error(ErrorFormatter.unmatched_condition_type(condition_type), ctx.expression())

        self.in_loop = True
        self.visitBlock(ctx.block())
        self.in_loop = False

    def visitFor_loop(self, ctx: MathLangParser.For_loopContext):
        self.visitAssignment(ctx.assignment())

        condition_type = self.visit(ctx.expression())
        if not TypeChecker.is_boolean_type(condition_type):
            self.add_error(ErrorFormatter.unmatched_condition_type(condition_type), ctx.expression())

        self.visit(ctx.statement())

        self.in_loop = True
        self.visitBlock(ctx.block())
        self.in_loop = False

    def visitBlock(self, ctx: MathLangParser.BlockContext):
        previous_scope = self.current_scope
        self.current_scope = self.current_scope.create_child_scope()

        if ctx:
            for stmt in ctx.statement():
                self.visit(stmt)

        self.current_scope = previous_scope

    def visitControl_flow_operator(self, ctx: MathLangParser.Control_flow_operatorContext):
        if ctx.RETURN() and not self.current_subprogram:
            self.add_error(ErrorFormatter.return_outside_of_subprogram(), ctx)
        elif ctx.BREAK() and not self.in_loop:
            self.add_error(ErrorFormatter.flow_control_operator_outside_of_loop(), ctx)
        elif ctx.CONTINUE() and not self.in_loop:
            self.add_error(ErrorFormatter.flow_control_operator_outside_of_loop(), ctx)


def main():
    if len(sys.argv) != 2:
        print("No file specified. Using default one.")

    source_file = sys.argv[1] if len(sys.argv) > 1 else 'samples/samples_templates.ml'

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
            sys.exit(0)

    except FileNotFoundError:
        print(f"❌ Файл {source_file} не найден")
        sys.exit(1)


if __name__ == "__main__":
    main()