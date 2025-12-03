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


# todo read requires template arg when called
# todo check for unused template arguments
# todo check for templated sub before using explicit implementation
class SemanticAnalyzer(MathLangVisitor):
    def __init__(self):
        self.global_scope = SymbolTable()
        self.current_scope = self.global_scope
        self.current_subprogram: SubprogramSymbol | None = None
        self.in_loop = False
        self.type_mapping: dict[Type, Type] | None = None
        self.binding_result = True
        self.subprogram_ctx: dict[SubprogramSymbol, MathLangParser.SubprogramContext] = {}
        self.defining_subprogram = True
        self.errors = []
        self.wat_code = []

        self.__default_subprograms = [
            SubprogramSymbol(name='cast', return_type=Type('Tto'), parameters=[Type('Tfrom')], template_args=[Type('Tfrom'), Type('Tto')]),
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

    @property
    def is_binding(self) -> bool:
        return self.type_mapping is not None

    def add_error(self, message, ctx=None):
        line = ctx.start.line if ctx else None
        column = ctx.start.column if ctx else None
        error = SemanticError(message, line, column)
        self.errors.append(error)


    def get_wat_code(self):
        return '\n'.join(self.wat_code)

    def add_wat(self, code):
        self.wat_code.append(code)


    def visitProgram(self, ctx:MathLangParser.ProgramContext):
        self.add_wat("(module")
        self.add_wat("  (import \"console\" \"log\" (func $log (param i32)))")
        self.add_wat("  (import \"js\" \"mem\" (memory 1))")
        self.add_wat("  (global $str_ptr (mut i32) (i32.const 1000))")

        self.add_wat("  (func $write_string (param $ptr i32)")
        self.add_wat("    (local $i i32)")
        self.add_wat("    (local.set $i (i32.const 0))")
        self.add_wat("    (loop $write_loop")
        self.add_wat("      (local.get $ptr)")
        self.add_wat("      (local.get $i)")
        self.add_wat("      (i32.add)")
        self.add_wat("      (i32.load8_u)")
        self.add_wat("      (i32.eqz)")
        self.add_wat("      (br_if $write_loop_end)")
        self.add_wat("      (local.get $ptr)")
        self.add_wat("      (local.get $i)")
        self.add_wat("      (i32.add)")
        self.add_wat("      (i32.load8_u)")
        self.add_wat("      (call $log)")
        self.add_wat("      (local.set $i (i32.add (local.get $i) (i32.const 1)))")
        self.add_wat("      (br $write_loop))")
        self.add_wat("    (end))")

        for sub in ctx.subprogram():
            self.visitSubprogram(sub)

        self.defining_subprogram = False

        for statement in ctx.statement():
            self.visit(statement)

        self.add_wat("  (func $main")
        self.add_wat("    (call $program_start))")
        self.add_wat("  (export \"main\" (func $main))")
        self.add_wat(")")


    def visitSubprogram(self, ctx: MathLangParser.SubprogramContext) -> bool | None:
        self.binding_result = True

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

        template_args: list[Type] = []
        if ctx.template():
            template_args += self.visitTemplate(ctx.template())

        # map template args
        template_args = [self.type_mapping[type] for type in template_args] if self.is_binding else template_args

        for symbol in parameters_symbols:
            if symbol.type not in template_args:
                self.add_error(ErrorFormatter.undefined_templated_argument(symbol.type), ctx)

        subprogram_symbol = SubprogramSymbol(name=sub_name, return_type=Type.void(), parameters=[param.type for param in parameters_symbols], template_args=template_args)

        if not self.is_binding:
            try:
                self.global_scope.add_symbol(subprogram_symbol)
                self.subprogram_ctx[subprogram_symbol] = ctx
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
                self.binding_result = False
                if not self.is_binding:
                    self.add_error(e.message, ctx)

        self.visitBlock(ctx.block())

        # Восстанавливаем предыдущий контекст
        self.current_scope = previous_scope
        self.current_subprogram = previous_subprogram

        if self.is_binding:
            return self.binding_result

    def visitCall(self, ctx: MathLangParser.CallContext) -> Type | None:
        sub_name = ctx.ID().getText()
        sub_parameters = self.visitExpression_list(ctx.expression_list()) if ctx.expression_list() is not None else []
        sub_templated_arguments = self.visitTemplate(ctx.template()) if ctx.template() is not None else []

        if self.is_binding:
            sub_templated_arguments = [self.type_mapping.get(type, type) for type in sub_templated_arguments]

        defined_subprograms = self.global_scope.lookup(sub_name)
        if defined_subprograms is None:
            self.add_error(ErrorFormatter.undefined_subprogram(sub_name), ctx)
            return None

        overload_candidate_subprograms: list[(SubprogramSymbol, dict[Type, Type])] = []

        for defined_subprogram in defined_subprograms:
            if not isinstance(defined_subprogram, SubprogramSymbol):
                continue

            if len(defined_subprogram.parameters) != len(sub_parameters):
                continue

            templated_types_mapping: dict[Type, Type] = {}
            params_ok = True
            for (param_expected, param_actual) in zip(defined_subprogram.parameters, sub_parameters):
                if TypeChecker.is_templated_argument(param_expected):
                    templated_types_mapping[param_expected] = param_actual
                else:
                    if param_expected != param_actual:
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

            self.type_mapping = previous_mapping

            if can_bind:
                # if self.is_binding:
                #     print("call to", ctx.getText(), "= bind", subprogram , "with", type_mapping)
                break

        if not can_bind and not self.defining_subprogram:
            self.add_error(ErrorFormatter.no_overload_found(sub_name, sub_parameters), ctx)
            return None

        if type_mapping:
            return type_mapping.get(subprogram.type, subprogram.type)
        else:
            return subprogram.type


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

            if self.is_binding:
                var_type = self.type_mapping.get(var_type, var_type)

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
                    if expression_type != symbol.type:
                        can_ignore_error_while_templating = self.current_subprogram and (TypeChecker.is_templated_argument(expression_type) or TypeChecker.is_templated_argument(symbol.type))
                        if not can_ignore_error_while_templating:
                            add_assignment_error(symbol.type, expression_type)

                    if symbol.is_global:
                        self.add_wat(f"    (global.set ${symbol.name} (local.get ${expression_type}))")
                    else:
                        self.add_wat(f"    (local.set ${symbol.name} (local.get ${expression_type}))")

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
                    if expression_type != symbol.type:
                        add_assignment_error(symbol.type, expression_type)
            else:
                for symbol in left_symbols:
                    if right_expressions[0] != symbol.type:
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
                for symbol in symbols:
                    if self.is_binding:
                        symbol.type = self.type_mapping.get(symbol.type, symbol.type)

                    ids.append(symbol)

        return ids

    def visitExpression_list(self, ctx: MathLangParser.Expression_listContext) -> list[Type]:
        types = []
        if ctx.expression():
            for expr in ctx.expression():
                expr_type = self.visitExpression(expr)
                types.append(expr_type)
        return types

    def visitExpression(self, ctx: MathLangParser.ExpressionContext) -> Type | None:
        result_type: Type | None = None

        def visit_binary_expression(ctx, operator: str) -> Type | None:
            left_type = self.visitExpression(ctx.expression(0))
            right_type = self.visitExpression(ctx.expression(1))

            if left_type is None or right_type is None:
                return None

            try:
                return TypeChecker.get_binary_operation_type(left_type, right_type, operator)
            except SemanticError as e:
                self.add_error(e.message, ctx)
                return None

        def visit_unary_expression(ctx, operator: str) -> Type | None:
            expr_type = self.visit(ctx.expression(0))

            def valid_type(type: Type | None) -> bool:
                return TypeChecker.is_numeric_type(type) or TypeChecker.is_boolean_type(type)

            if operator == '-' and not valid_type(expr_type):
                self.add_error(ErrorFormatter.unary_operator_only_valid_on_types(operator, 'числовым и булевым типам', expr_type), ctx)
                return None

            return expr_type

        if ctx.ID():
            var_name = ctx.ID().getText()
            symbol = self.current_scope.lookup(var_name)
            if not symbol:
                self.add_error(ErrorFormatter.undefined_symbol(var_name), ctx)
                result_type = None
            else:
                result_type = symbol[0].type

        elif ctx.literal():
            result_type = self.visitLiteral(ctx.literal())
        elif ctx.call():
            result_type = self.visitCall(ctx.call())

        elif ctx.getChildCount() == 3 and ctx.getChild(0).getText() == '(':
            # Выражение в скобках
            result_type = self.visitExpression(ctx.expression(0))


        elif ctx.NOT():
            result_type = visit_unary_expression(ctx, ctx.NOT().getText())
        elif ctx.MINUS() and ctx.getChildCount() == 2:
            result_type = visit_unary_expression(ctx, ctx.MINUS().getText())
        elif len(ctx.EQ()) == 2:
            result_type = visit_binary_expression(ctx, "==")
        else:
            binary_operator = ctx.getChild(1).getText()
            result_type = visit_binary_expression(ctx, binary_operator)

        if self.is_binding:
            result_type = self.type_mapping.get(result_type, result_type)

        return result_type


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
    default_file = 'samples/samples_templates.ml'

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
            # print(analyzer.get_wat_code())
            sys.exit(0)

    except FileNotFoundError:
        print(f"❌ Файл {source_file} не найден")
        sys.exit(1)


if __name__ == "__main__":
    main()