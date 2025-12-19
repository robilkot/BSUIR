import logging
import sys

from antlr4 import *

from generated.grammar.MathLangLexer import MathLangLexer
from generated.grammar.MathLangParser import MathLangParser
from generated.grammar.MathLangVisitor import MathLangVisitor
from intermediate_code.wat_emitter import *
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
        self.current_subprogram: SubprogramSymbol | None = None
        self.defining_subprogram: bool = True
        self.in_loop = False
        self.__subprogram_templates: dict[str, MathLangParser.SubprogramContext] = {}
        self.errors = []
        self.program_node: ProgramNode = ProgramNode(subprograms=[], statements=[])

        self.__subprograms_nodes = set()


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

        for sub_node in self.__subprograms_nodes:
            self.program_node.subprograms.append(sub_node)


    def visitSubprogram(self, ctx: MathLangParser.SubprogramContext, type_mapping: dict[Type, Type] | None = None) -> SubprogramNode | None:
        sub_name = ctx.ID().getText()

        parameters_symbols: list[Symbol] = []
        if ctx.declaration_list():
            parameters_symbols += self.visitDeclaration_list(ctx.declaration_list())

        template_args: list[Type] | None = None
        if ctx.template():
            template_args = self.visitTemplate(ctx.template())

        if template_args:
            for symbol in parameters_symbols:
                if TypeChecker.is_templated_argument(symbol.type) and symbol.type not in template_args:
                    self.add_error(ErrorFormatter.undefined_templated_argument(symbol.type), ctx)
        else:
            for symbol in parameters_symbols:
                if TypeChecker.is_templated_argument(symbol.type):
                    self.add_error(ErrorFormatter.undefined_templated_argument(symbol.type), ctx)


        # Templated sub branch
        if template_args is not None and type_mapping is None:
            is_explicit_implementation = False
            for arg in template_args:
                if not TypeChecker.is_templated_argument(arg):
                    is_explicit_implementation = True
                    break

            if self.__subprogram_templates.__contains__(sub_name):
                subprogram_template = self.__subprogram_templates[sub_name]
                subprogram_template_args = self.visitTemplate(subprogram_template.template())

                explicit_implementation_type_mapping: dict[Type, Type] = {}
                for template_arg, explicit_arg in zip(subprogram_template_args, template_args):
                    explicit_implementation_type_mapping[template_arg] = explicit_arg
                    if TypeChecker.is_templated_argument(explicit_arg):
                        self.add_error(ErrorFormatter.explicit_impl_argument_not_specified(explicit_arg), ctx)
                        is_explicit_implementation = False

                if is_explicit_implementation:
                    return self.visitSubprogram(ctx, explicit_implementation_type_mapping)

                self.add_error(ErrorFormatter.redefined_symbol(sub_name), ctx)
                return None

            if is_explicit_implementation:
                self.add_error(ErrorFormatter.explicit_impl_now_allowed_without_templated_decl(sub_name), ctx)
                return None

            self.__subprogram_templates[sub_name] = ctx
            # print("TEMPLATED_SUB", sub_name)
            return None

        # Not templated sub branch (calling and trying to bind)

        # Map types
        subprogram_symbol = SubprogramSymbol(
            name=sub_name,
            return_type=Type.void(),
            parameters=[Symbol(name=symb.name, type=type_mapping.get(symb.type, symb.type)) for symb in parameters_symbols] if type_mapping is not None else parameters_symbols,
            template_args=[type_mapping.get(typ, typ) for typ in template_args] if type_mapping else template_args
        )
        previous_sub = self.current_subprogram
        self.current_subprogram = subprogram_symbol

        try:
            self.global_scope.add_symbol(subprogram_symbol)
        except SemanticError as e:
            self.add_error(e.message, ctx)


        # Сохраняем текущий контекст и создаем новую область видимости
        previous_scope = self.current_scope
        self.current_scope = subprogram_symbol.local_scope

        # Добавляем параметры в локальную область видимости подпрограммы
        for param_symbol in subprogram_symbol.parameters:
            try:
                self.current_scope.add_symbol(param_symbol)
            except SemanticError as e:
                if type_mapping is None:
                    self.add_error(e.message, ctx)

        block_node = self.visitBlock(ctx.block(), type_mapping)

        # Check for unused template arguments
        if subprogram_symbol.template_args:
            used_template_args: dict[Type, bool] = {type: False for type in subprogram_symbol.template_args}
            for symbol in self.current_scope.symbols:
                if symbol.type in subprogram_symbol.template_args:
                    used_template_args[symbol.type] = True

            for type, used in used_template_args.items():
                if not used:
                    self.add_error(ErrorFormatter.unused_template_argument(type, type_mapping), ctx)

        # Восстанавливаем предыдущий контекст
        self.current_scope = previous_scope

        subprogram_node = SubprogramNode(
            name=subprogram_symbol.get_mangled_name(),
            type=subprogram_symbol.type,
            param_types=[param.type for param in subprogram_symbol.parameters],
            param_names=[param.name for param in subprogram_symbol.parameters],
            body=block_node
        )

        self.__subprograms_nodes.add(subprogram_node)

        # print("SPECIFIC_SUB", subprogram_node.name)

        self.current_subprogram = previous_sub
        return subprogram_node


    def visitCall(self, ctx: MathLangParser.CallContext, type_mapping: dict[Type, Type] | None = None) -> Expr | None:
        sub_name = ctx.ID().getText()
        sub_arguments = self.visitExpression_list(ctx.expression_list(), type_mapping) if ctx.expression_list() is not None else []
        sub_templated_arguments = self.visitTemplate(ctx.template()) if ctx.template() is not None else []

        # Map types if mapping provided
        if type_mapping is not None:
            for param in sub_arguments:
                param.type = type_mapping.get(param.type, param.type)
            sub_templated_arguments = [type_mapping.get(typ, typ) for typ in sub_templated_arguments]


        # Special case: cast subprogram
        if sub_name == 'cast':
            if len(sub_templated_arguments) != 2:
                self.add_error(ErrorFormatter.unmatched_arguments_count(actual=len(sub_templated_arguments), expected=2), ctx)
                return None

            if len(sub_arguments) != 1:
                self.add_error(ErrorFormatter.unmatched_arguments_count(actual=len(sub_arguments), expected=1), ctx)
                return None

            from_type = sub_templated_arguments[0]
            to_type = sub_templated_arguments[1]
            if sub_arguments[0].type != from_type:
                self.add_error(ErrorFormatter.unmatched_argument_type(expected=from_type, actual=sub_arguments[0].type), ctx)
                return None

            if not TypeChecker.can_cast(from_type, to_type):
                self.add_error(ErrorFormatter.invalid_cast(from_type, to_type, type_mapping), ctx)

            node = CastExpr(type=to_type, expr=sub_arguments[0])
            return node

        # Special case: read subprogram
        if sub_name == 'read':
            if len(sub_templated_arguments) != 1:
                self.add_error(ErrorFormatter.unmatched_arguments_count(actual=len(sub_templated_arguments), expected=1), ctx)
                return None

            if sub_templated_arguments[0] not in [Type.int(), Type.float(), Type.bool()]:
                self.add_error(ErrorFormatter.no_overload_found(sub_name, sub_templated_arguments), ctx)
                return None

            node = SubprogramCall(name=sub_name, type=sub_templated_arguments[0], args=[])
            return node

        # Special case: write subprogram
        if sub_name == 'write':
            if len(sub_arguments) == 1:
                if len(sub_templated_arguments) > 1:
                    self.add_error(ErrorFormatter.unmatched_arguments_count(actual=len(sub_templated_arguments), expected=1), ctx)
                    return None
                if len(sub_templated_arguments) > 0 and sub_arguments[0].type != sub_templated_arguments[0]:
                    self.add_error(ErrorFormatter.unmatched_argument_type(actual=sub_arguments[0].type, expected=sub_templated_arguments[0]), ctx)

                node = SubprogramCall(name=sub_name, type=sub_arguments[0].type, args=sub_arguments)
                return node

        # Special case: math functions
        if sub_name in [sub.name for sub in self.__math_subprograms]:
            if len(sub_arguments) != 1:
                self.add_error(
                    ErrorFormatter.unmatched_arguments_count(actual=len(sub_arguments), expected=1), ctx)
                return None
            if len(sub_templated_arguments) > 1:
                self.add_error(
                    ErrorFormatter.unmatched_arguments_count(actual=len(sub_templated_arguments), expected=1), ctx)
                return None
            if len(sub_templated_arguments) > 0 and sub_templated_arguments[0] != Type.float():
                self.add_error(ErrorFormatter.unmatched_argument_type(actual=sub_templated_arguments[0],
                                                                      expected=Type.float()), ctx)
            if len(sub_arguments) > 0 and sub_arguments[0].type != Type.float():
                self.add_error(ErrorFormatter.unmatched_argument_type(actual=sub_arguments[0].type,
                                                                      expected=Type.float()), ctx)

            typ = sub_arguments[0].type if len(sub_arguments) > 0 else Type.float()  # fallback to float for math
            node = SubprogramCall(name=sub_name, type=typ, args=sub_arguments)
            return node

        # Try to find non-templated function
        candidates = self.global_scope.lookup(sub_name)

        if candidates is not None:
            found_candidate: SubprogramSymbol | None = None
            for candidate in candidates:
                if not isinstance(candidate, SubprogramSymbol):
                    continue

                if len(candidate.parameters) != len(sub_arguments):
                    continue

                candidate_ok = True
                for candidate_param, actual_param in zip(candidate.parameters, sub_arguments):
                    if candidate_param.type != actual_param.type:
                        candidate_ok = False
                        break

                if not candidate_ok:
                    continue

                if found_candidate is not None:
                    self.add_error(f"Ambiguous call to {sub_name}", ctx)

                found_candidate = candidate

            if found_candidate is not None:
                node = SubprogramCall(
                    name=found_candidate.get_mangled_name(),
                    args=sub_arguments,
                    type=found_candidate.type,
                )
                return node

        # Try to bind to templated function
        templ_ctx = self.__subprogram_templates.get(sub_name, None)
        if templ_ctx is None:
            self.add_error(ErrorFormatter.undefined_subprogram(sub_name), ctx)
            return None

        # Map types to bind
        callee_type_mapping: dict[Type, Type] = {}

        # Bind using templated args if provided
        callee_templated_arguments = self.visitTemplate(templ_ctx.template())
        if len(sub_templated_arguments) != 0:
            if len(callee_templated_arguments) != len(sub_templated_arguments):
                self.add_error(ErrorFormatter.no_overload_found(sub_name, [param.type for param in sub_arguments]), ctx)
                return None

            for caller_type, callee_type in zip(sub_templated_arguments, callee_templated_arguments):
                callee_type_mapping[callee_type] = caller_type

        # Or infer using arguments
        callee_arguments = self.visitDeclaration_list(templ_ctx.declaration_list()) if templ_ctx.declaration_list() is not None else []
        if len(sub_arguments) != len(callee_arguments):
            self.add_error(ErrorFormatter.no_overload_found(sub_name, [param.type for param in sub_arguments]), ctx)

        for caller_arg_expr, callee_arg_symbol in zip(sub_arguments, callee_arguments):
            if callee_type_mapping.__contains__(callee_arg_symbol.type):
                self.add_error(ErrorFormatter.provided_argument_does_not_match_templated_argument_type(actual=caller_arg_expr.type, expected=callee_type_mapping[callee_arg_symbol.type]), ctx)
                continue
            callee_type_mapping[callee_arg_symbol.type] = caller_arg_expr.type

        # Visit subprogram template to generate specific implementation
        subprogram_node = self.visitSubprogram(templ_ctx, callee_type_mapping)

        if subprogram_node is None:
            self.add_error(ErrorFormatter.no_overload_found(sub_name, [param.type for param in sub_arguments]), ctx)

        # Return
        node = SubprogramCall(
            name=subprogram_node.name,
            args=sub_arguments,
            type=subprogram_node.type,
        )
        # print("CALL", node.name)
        return node


    def visitTemplate(self, ctx:MathLangParser.TemplateContext) -> list[Type]:
        return self.visitType_specifier_list(ctx.type_specifier_list())

    def visitType_specifier_list(self, ctx:MathLangParser.Type_specifier_listContext) -> list[Type]:
        result = []
        for type_specifier in ctx.type_specifier():
            result.append(Type.create(type_specifier.getText()))
        return result

    def visitGlobal_variable_declaration(self, ctx:MathLangParser.Global_variable_declarationContext, type_mapping: dict[Type, Type] | None = None) -> GlobalVarDeclaration:
        if self.current_subprogram is None:
            self.add_error(ErrorFormatter.uninitialized_global_symbol(ctx.ID().getText()), ctx)

        typ = Type.create(ctx.type_specifier().getText())
        if type_mapping is not None:
            typ = type_mapping.get(typ, typ)

        return GlobalVarDeclaration(
            name=ctx.ID().getText(),
            type=typ,
        )

    def visitDeclaration_list(self, ctx: MathLangParser.Declaration_listContext, type_mapping: dict[Type, Type] | None = None) -> list[Symbol]:
        local = ctx.scope_modifier() is None

        declarations = []
        for type_ctx, id_ctx in zip(ctx.type_specifier(), ctx.ID()):
            var_type = Type.create(type_ctx.getText())
            var_name = id_ctx.getText()

            if type_mapping is not None:
                var_type = type_mapping.get(var_type, var_type)

            # print('GLOBAL' if not local else '', var_type, var_name)

            symbol = Symbol(var_name, var_type, is_global=(not local))
            declarations.append(symbol)

        return declarations

    def visitAssignment(self, ctx: MathLangParser.AssignmentContext, type_mapping: dict[Type, Type] | None = None) -> list[AssignNode]:
        result: list[AssignNode] = []

        def add_assignment_error(expected: Type, actual: Type):
            self.add_error(ErrorFormatter.cant_assign_from_to(from_type=actual, to_type=expected), ctx)

        left_side = ctx.declaration_list() if ctx.declaration_list() else ctx.id_list()
        right_expressions: list[Expr] = self.visitExpression_list(ctx.expression_list(), type_mapping)

        left_side: MathLangParser.Id_listContext
        if isinstance(left_side, MathLangParser.Id_listContext):
            left_symbols: list[Symbol] | None = self.visitId_list(left_side, type_mapping)

            if left_symbols is None or len(left_symbols) != len(right_expressions):
                self.add_error(ErrorFormatter.unmatched_number_of_expressions_or_not_single_expression(), ctx)
                return []

            for symbol, expression_node in zip(left_symbols, right_expressions):
                if expression_node is None:
                    continue

                if symbol is not None:
                    result.append(AssignNode(name=symbol.name, value=expression_node))

                    expr_type = expression_node.type
                    if expr_type != symbol.type:
                        can_ignore_error_while_templating = (self.current_subprogram
                                                             and (TypeChecker.is_templated_argument(expr_type)
                                                                  or TypeChecker.is_templated_argument(symbol.type)))
                        if not can_ignore_error_while_templating:
                            add_assignment_error(symbol.type, expr_type)

        elif isinstance(left_side, MathLangParser.Declaration_listContext):
            left_symbols = self.visitDeclaration_list(left_side, type_mapping)

            for symbol in left_symbols:
                try:
                    self.current_scope.add_symbol(symbol)
                except SemanticError as e:
                    self.add_error(e.message, ctx)

            for symbol in left_symbols:
                if type_mapping is None and not self.current_subprogram:
                    if TypeChecker.is_templated_argument(symbol.type):
                        self.add_error(ErrorFormatter.undefined_type(symbol.type), ctx)

            if len(right_expressions) != 1:
                if len(left_symbols) != len(right_expressions):
                    self.add_error(ErrorFormatter.unmatched_number_of_expressions_or_not_single_expression(), ctx)
                    return []

                for symbol, expression_node in zip(left_symbols, right_expressions):
                    expr_type = expression_node.type

                    result.append(AssignNode(name=symbol.name, value=expression_node))
                    if expr_type != symbol.type:
                        add_assignment_error(symbol.type, expr_type)
            else:
                for symbol in left_symbols:
                    right_expr = right_expressions[0]
                    if right_expr is None:
                        continue
                        
                    expr_type = right_expr.type

                    result.append(AssignNode(name=symbol.name, value=right_expr))
                    if expr_type != symbol.type:
                        add_assignment_error(symbol.type, expr_type)

        for node in result:
            if node.value.type == Type.string():
                self.add_error(ErrorFormatter.string_operations_are_not_supported(type_mapping), ctx)
        return result

    def visitId_list(self, ctx: MathLangParser.Id_listContext, type_mapping: dict[Type, Type] | None = None) -> list[Symbol] | None:
        ids: list[Symbol | None] = []

        for id in ctx.ID():
            symbols = self.current_scope.lookup(id.getText())

            if symbols is None:
                self.add_error(ErrorFormatter.undefined_symbol(id), ctx)
                ids.append(None)
            else:
                for symbol in symbols:
                    if type_mapping is not None:
                        symbol.type = type_mapping.get(symbol.type, symbol.type)

                    ids.append(symbol)

        return ids

    def visitExpression_list(self, ctx: MathLangParser.Expression_listContext, type_mapping: dict[Type, Type] | None = None) -> list[Expr]:
        expr_list: list[Expr] = []
        if ctx.expression():
            for expr in ctx.expression():
                expr_node = self.visitExpression(expr, type_mapping)
                expr_list.append(expr_node)
        return expr_list

    def visitExpression(self, ctx: MathLangParser.ExpressionContext, type_mapping: dict[Type, Type] | None = None) -> Expr | None:
        result: Expr | None = None

        def visit_binary_expression(ctx, operator: str) -> Expr | None:
            left_expr_node = self.visitExpression(ctx.expression(0), type_mapping)
            right_expr_node = self.visitExpression(ctx.expression(1), type_mapping)

            if left_expr_node is None or right_expr_node is None:
                return None

            try:
                result_node_type = TypeChecker.get_binary_operation_type(
                    left_expr_node.type,
                    right_expr_node.type,
                    operator,
                    type_mapping)

                # Special case since there is no operator for ** in WAT
                if operator == '^':
                    return SubprogramCall(type=result_node_type, name='pow', args=[left_expr_node, right_expr_node])

                return BinaryOp(type=result_node_type, op=operator, left=left_expr_node, right=right_expr_node)
            except SemanticError as e:
                self.add_error(e, ctx)
                return BinaryOp(type=left_expr_node.type, op=operator, left=left_expr_node, right=right_expr_node)

        def visit_unary_expression(ctx, operator: str) -> Expr | None:
            expr_node = self.visitExpression(ctx.expression(0), type_mapping)

            def valid_type(type: Type | None) -> bool:
                return TypeChecker.is_numeric_type(type) or TypeChecker.is_boolean_type(type)

            expr_type = expr_node.type
            if operator == '-' and not valid_type(expr_type):
                self.add_error(ErrorFormatter.unary_operator_only_valid_on_types(operator, 'числовым и булевым типам', expr_type, type_mapping), ctx)
                return None

            return UnaryOp(type=expr_node.type, expr=expr_node, op=operator)

        if ctx.ID():
            var_name = ctx.ID().getText()
            symbol = self.current_scope.lookup(var_name)

            if symbol is None:
                self.add_error(ErrorFormatter.undefined_symbol(var_name), ctx)
                result = Expr(type=Type.create('Unknown'))
            else:
                symbol = symbol[0]
                if type_mapping is not None:
                    symbol = Symbol(name=symbol.name, type=type_mapping.get(symbol.type, symbol.type))
                result = VarRef(name=var_name, type=symbol.type)

        elif ctx.literal():
            result = self.visitLiteral(ctx.literal())
        elif ctx.call():
            result = self.visitCall(ctx.call(), type_mapping)

        elif ctx.getChildCount() == 3 and ctx.getChild(0).getText() == '(':
            # Выражение в скобках
            result = self.visitExpression(ctx.expression(0), type_mapping)


        elif ctx.NOT():
            result = visit_unary_expression(ctx, ctx.NOT().getText())
        elif ctx.MINUS() and ctx.getChildCount() == 2:
            result = visit_unary_expression(ctx, ctx.MINUS().getText())
        elif len(ctx.EQ()) == 2:
            result = visit_binary_expression(ctx, "==")
        else:
            binary_operator = ctx.getChild(1).getText()
            result = visit_binary_expression(ctx, binary_operator)

        if type_mapping is not None:
            if result is not None:
                result.type = type_mapping.get(result.type, result.type)

        return result

    def visitLiteral(self, ctx: MathLangParser.LiteralContext) -> Expr:
        if ctx.INT():
            return IntLiteral(value=int(ctx.getText()))
        elif ctx.FLOAT():
            return FloatLiteral(value=float(ctx.getText()))
        elif ctx.BOOL():
            if ctx.BOOL().getText() == 'true':
                return BoolLiteral(value=True)
            else:
                return BoolLiteral(value=False)
        elif ctx.STRING():
            return StringLiteral(value=ctx.getText())
        else:
            raise ValueError('Unknown literal type')

    def visitBranching(self, ctx: MathLangParser.BranchingContext, type_mapping: dict[Type, Type] | None = None) -> StatementNode:
        condition_expr_node = self.visitExpression(ctx.expression(), type_mapping)
        condition_type = condition_expr_node.type
        if not TypeChecker.is_boolean_type(condition_type):
            self.add_error(ErrorFormatter.unmatched_condition_type(condition_type), ctx.expression())

        then_block = self.visitBlock(ctx.block(0), type_mapping)

        else_block = None
        if ctx.ELSE():
            else_block = self.visitBlock(ctx.block(1), type_mapping)

        return IfStmt(
            cond=condition_expr_node,
            then_body=then_block,
            else_body=else_block,
        )

    def visitLoop(self, ctx: MathLangParser.LoopContext, type_mapping: dict[Type, Type] | None = None) -> WhileStmt | ForStmt | UntilStmt:
        previous_scope = self.current_scope

        self.current_scope = self.current_scope.create_child_scope()
        self.current_scope.parent = previous_scope

        result = None
        if ctx.for_loop():
            result = self.visitFor_loop(ctx.for_loop(), type_mapping)
        elif ctx.while_loop():
            result = self.visitWhile_loop(ctx.while_loop(), type_mapping)
        elif ctx.until_loop():
            result = self.visitUntil_loop(ctx.until_loop(), type_mapping)

        # Восстанавливаем предыдущий контекст
        self.current_scope = previous_scope
        return result

    def visitWhile_loop(self, ctx: MathLangParser.While_loopContext, type_mapping: dict[Type, Type] | None = None):
        condition_node = self.visitExpression(ctx.expression(), type_mapping)
        if condition_node is None:
            condition_node = Expr(type=Type.bool())

        condition_type = condition_node.type
        if not TypeChecker.is_boolean_type(condition_type):
            self.add_error(ErrorFormatter.unmatched_condition_type(condition_type), ctx.expression())

        self.in_loop = True
        block_node = self.visitBlock(ctx.block(), type_mapping)
        self.in_loop = False

        return WhileStmt(cond=condition_node, body=block_node)

    def visitUntil_loop(self, ctx: MathLangParser.Until_loopContext, type_mapping: dict[Type, Type] | None = None):
        condition_node = self.visitExpression(ctx.expression(), type_mapping)
        if condition_node is None:
            condition_node = Expr(type=Type.bool())

        condition_type = condition_node.type
        if not TypeChecker.is_boolean_type(condition_type):
            self.add_error(ErrorFormatter.unmatched_condition_type(condition_type), ctx.expression())

        self.in_loop = True
        block_node = self.visitBlock(ctx.block(), type_mapping)
        self.in_loop = False

        return UntilStmt(cond=condition_node, body=block_node)

    def visitFor_loop(self, ctx: MathLangParser.For_loopContext, type_mapping: dict[Type, Type] | None = None) -> ForStmt:
        init_expr_node = self.visitAssignment(ctx.assignment(), type_mapping)
        if len(init_expr_node) == 0:
            init_expr_node = Expr(type=Type.create('Unknown'))
        else:
            init_expr_node = init_expr_node[0]

        condition_node = self.visitExpression(ctx.expression(), type_mapping)
        if condition_node is None:
            condition_node = Expr(type=Type.bool())

        condition_type = condition_node.type
        if not TypeChecker.is_boolean_type(condition_type):
            self.add_error(ErrorFormatter.unmatched_condition_type(condition_type), ctx.expression())

        step_node = self.visitStatement(ctx.statement(), type_mapping)
        if isinstance(step_node, list):
            step_node = step_node[0]
            # todo could have been multiple statements there

        self.in_loop = True
        block_node = self.visitBlock(ctx.block(), type_mapping)
        self.in_loop = False

        return ForStmt(init=init_expr_node, cond=condition_node, step=step_node, body=block_node)

    def visitBlock(self, ctx: MathLangParser.BlockContext, type_mapping: dict[Type, Type] | None = None) -> BlockNode:
        previous_scope = self.current_scope
        self.current_scope = self.current_scope.create_child_scope()

        block_node = BlockNode(body=[])
        if ctx:
            for stmt in ctx.statement():
                node = self.visitStatement(stmt, type_mapping)
                if isinstance(node, list):
                    for subnode in node:
                        block_node.body.append(subnode)
                else:
                    block_node.body.append(node)

        self.current_scope = previous_scope
        return block_node

    def visitStatement(self, ctx:MathLangParser.StatementContext, type_mapping: dict[Type, Type] | None = None):
        if ctx.block():
            return self.visitBlock(ctx.block(), type_mapping)
        elif ctx.control_flow_operator():
            return self.visitControl_flow_operator(ctx.control_flow_operator())
        elif ctx.branching():
            return self.visitBranching(ctx.branching(), type_mapping)
        elif ctx.loop():
            return self.visitLoop(ctx.loop(), type_mapping)
        elif ctx.assignment():
            return self.visitAssignment(ctx.assignment(), type_mapping)
        elif ctx.global_variable_declaration():
            return self.visitGlobal_variable_declaration(ctx.global_variable_declaration(), type_mapping)
        elif ctx.call():
            return self.visitCall(ctx.call(), type_mapping)
        else:
            raise NotImplementedError()

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
    if len(sys.argv) != 2:
        logging.error(f"Usage: python {sys.argv[0]} <source_file.ml>\nExample: python {sys.argv[0]} samples/sample7.ml")
        sys.exit(1)

    source_file = sys.argv[1]

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
            logging.error(f"Семантический анализ не выполнен, потому что программа синтаксически некорректна")
            sys.exit(1)

        analyzer = SemanticAnalyzer()
        analyzer.visit(tree)

        if analyzer.errors:
            logging.error(f"Семантический анализ завершен с ошибками: {len(analyzer.errors)}")

            for error in analyzer.errors:
                logging.error(f"❌ {error}")

            sys.exit(1)
        else:
            logging.info("✅ Программа семантически корректна!")
            generator = WatGenerator()

            code = generator.generate(analyzer.program_node)
            with open(source_file.replace('.ml', '.wat'), 'w', encoding='utf-8') as f:
                f.write(code)

        # print("\nGenerated AST:")
        # print(analyzer.program_node)

        sys.exit(0)

    except FileNotFoundError:
        print(f"❌ Файл {source_file} не найден")
        sys.exit(1)


if __name__ == "__main__":
    main()