#!/usr/bin/env python3
"""
Семантический анализатор для математического языка программирования
"""

import sys
from enum import IntEnum, auto
from itertools import zip_longest
from symtable import SymbolTable

from antlr4 import *

from generated.grammar.MathLangLexer import MathLangLexer
from generated.grammar.MathLangParser import MathLangParser
from generated.grammar.MathLangVisitor import MathLangVisitor


class Type(IntEnum):
    ANY = auto()
    FLOAT = auto()
    INT = auto()
    BOOL = auto()
    STRING = auto()
    VOID = auto()

    @staticmethod
    def create(typename: str):
        if isinstance(typename, Type):
            raise ValueError(f'typename уже типа ({typename.name})')

        if typename == "float":
            return Type.FLOAT
        elif typename == "int":
            return Type.INT
        elif typename == "bool":
            return Type.BOOL
        elif typename == "string":
            return Type.STRING
        elif typename == "void":
            return Type.VOID
        else:
            raise SemanticError(f'Неизвестный тип {typename}')


def safe_type_name(type: Type | None) -> str:
    return type.name if type is not None else 'unknown'



class SemanticError(Exception):
    """Класс для семантических ошибок"""

    def __init__(self, message, line=None, column=None):
        self.message = message
        self.line = line
        self.column = column
        super().__init__(self.format_message())

    def format_message(self):
        if self.line is not None and self.column is not None:
            return f"[{self.line}:{self.column}]: {self.message}"
        return self.message


class SemanticWarning(SemanticError):
    pass


class Symbol:
    """Класс для представления символа в таблице символов"""

    def __init__(self, name, type: Type):
        self.name = name
        self.type: Type = type

    def __str__(self):
        return f"{self.type.name} {self.name}"

    def __repr__(self):
        return self.__str__()

    def __key(self):
        return (self.name, self.type)

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        if isinstance(other, Symbol):
            return self.__key() == other.__key()
        return NotImplemented


class SubprogramSymbol(Symbol):
    def __init__(self, name, parameters: list[Type], return_type: Type):
        super().__init__(name, return_type)
        self.parameters: list[Type] = parameters
        self.local_scope = SymbolTable()

    def __str__(self):
        return f"sub {self.name}({self.__params_str()})"

    def __repr__(self):
        return self.__str__()

    def __params_str(self):
        return ", ".join([type.name for type in self.parameters])

    def __key(self):
        return (self.name, self.type, self.__params_str())

    def __hash__(self):
        return hash(self.__key())


class SymbolTable:
    """Таблица символов с поддержкой вложенных областей видимости"""

    def __init__(self, parent=None):
        self.symbols = set()
        self.symbols_dict: dict[str, list[Symbol]] = {}

        self.parent = parent
        self.children = []

    def __str__(self):
        return self.symbols.__str__()

    def __repr__(self):
        return self.__str__()

    def add_symbol(self, symbol: Symbol):
        # todo варнинг если объявлен в паренте но не локально
        if symbol in self.symbols:
            raise SemanticError(f"'{symbol}' уже объявлен в этой области видимости")

        if self.parent is not None:
            if self.parent.has_defined(symbol):
                msg = f"'{symbol}' уже объявлен в верхней области видимости"
                print(msg)
                raise SemanticWarning(msg)

        self.symbols.add(symbol)
        existing_symbols = self.symbols_dict.get(symbol.name, [])
        existing_symbols.append(symbol)
        self.symbols_dict[symbol.name] = existing_symbols

    def has_defined(self, symbol: Symbol) -> bool:
        return self.lookup(symbol.name) is not None

    def lookup(self, name: str) -> None | list[Symbol]:
        if name in self.symbols_dict:
            return self.symbols_dict[name]
        if self.parent:
            return self.parent.lookup(name)
        return None

    def create_child_scope(self) -> "SymbolTable":
        child = SymbolTable(self)
        self.children.append(child)
        return child


class TypeChecker:
    @staticmethod
    def is_numeric_type(type: Type) -> bool:
        return type in [Type.FLOAT, Type.INT]

    @staticmethod
    def is_boolean_type(type: Type) -> bool:
        return type in [Type.BOOL]

    @staticmethod
    def get_expression_type(expression_ctx, visitor) -> Type:
        if hasattr(expression_ctx, 'type'):
            return Type.create(expression_ctx.type)
        return visitor.visit(expression_ctx)

    @staticmethod
    def can_cast(from_type: Type, to_type: Type) -> bool:
        if from_type is None or to_type is None:
            return False

        if to_type == Type.ANY:
            return True

        can_cast = {
            Type.BOOL: [],
            Type.STRING: [],
            Type.VOID: [],
            Type.INT: [Type.FLOAT],
            Type.FLOAT: [Type.INT],
            Type.ANY: [Type.INT, Type.FLOAT, Type.BOOL],
        }

        if from_type == to_type:
            return True

        return to_type in can_cast[from_type]

    @staticmethod
    def get_binary_operation_type(left_type: Type, right_type: Type, operator: str) -> Type:
        """Определяет тип результата бинарной операции"""
        numeric_ops = ['+', '-', '*', '/', '%', '^']
        comparison_ops = ['==', '!=', '<', '>', '<=', '>=']
        logical_ops = ['and', 'or']

        if operator in numeric_ops:
            if not (TypeChecker.is_numeric_type(left_type) and TypeChecker.is_numeric_type(right_type)):
                raise SemanticError(f"Операция '{operator}' применима только к числовым типам. Получены типы {left_type.name}, {right_type.name}")
            # Если хотя бы один операнд float - результат float
            if Type.FLOAT in [left_type, right_type]:
                return Type.FLOAT
            return Type.INT

        elif operator in comparison_ops:
            if left_type != right_type and not TypeChecker.can_cast(left_type, right_type):
                raise SemanticError(f"Несовместимые типы для сравнения: {left_type} и {right_type}")
            return Type.BOOL

        elif operator in logical_ops:
            if not (TypeChecker.is_boolean_type(left_type) and TypeChecker.is_boolean_type(right_type)):
                raise SemanticError(f"Логические операции применимы только к boolean типам. Получены типы {left_type}, {right_type}")
            return Type.BOOL

        raise SemanticError(f"Неизвестный оператор: {operator}")


class SemanticAnalyzer(MathLangVisitor):
    def __init__(self):
        self.global_scope = SymbolTable()
        self.current_scope = self.global_scope
        self.current_subprogram = None
        self.errors = []
        self.warnings = []

        self.__write_subprogram = SubprogramSymbol(name='write', return_type=Type.VOID, parameters=[Type.ANY])

        self.__default_subprograms = [
            #tan, asin, acos, atan
            SubprogramSymbol(name='abs', return_type=Type.FLOAT, parameters=[Type.FLOAT]),
            SubprogramSymbol(name='log', return_type=Type.FLOAT, parameters=[Type.FLOAT]),
            SubprogramSymbol(name='ln', return_type=Type.FLOAT, parameters=[Type.FLOAT]),
            SubprogramSymbol(name='sin', return_type=Type.FLOAT, parameters=[Type.FLOAT]),
            SubprogramSymbol(name='cos', return_type=Type.FLOAT, parameters=[Type.FLOAT]),
            SubprogramSymbol(name='tg', return_type=Type.FLOAT, parameters=[Type.FLOAT]),
            SubprogramSymbol(name='atg', return_type=Type.FLOAT, parameters=[Type.FLOAT]),
            SubprogramSymbol(name='ctg', return_type=Type.FLOAT, parameters=[Type.FLOAT]),
            SubprogramSymbol(name='actg', return_type=Type.FLOAT, parameters=[Type.FLOAT]),
            SubprogramSymbol(name='asin', return_type=Type.FLOAT, parameters=[Type.FLOAT]),
            SubprogramSymbol(name='acos', return_type=Type.FLOAT, parameters=[Type.FLOAT]),
            SubprogramSymbol(name='read', return_type=Type.ANY, parameters=[]),
            self.__write_subprogram
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

        subprogram_symbol = SubprogramSymbol(name=sub_name, return_type=Type.VOID, parameters=[param.type for param in parameters_symbols])

        try:
            self.global_scope.add_symbol(subprogram_symbol)
        except (SemanticError, SemanticWarning) as e:
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
            except (SemanticError, SemanticWarning) as e:
                self.add_error(e.message, ctx)

        # Обрабатываем тело подпрограммы
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
        if (not is_expr_count_valid_func(expr_count)):
            # print(ctx.getText(), expr_count)
            self.add_error('Количество выражений должно совпадать с количеством переменных или быть равным 1', ctx)

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
                self.add_error(f"Нельзя присвоить {safe_type_name(init_type)} переменной типа {safe_type_name(left_type)}", decl_ctx)

            symbol = Symbol(var_name, left_type)
            declarations.append(symbol)

        return declarations

    # todo
    def visitAssignment(self, ctx: MathLangParser.AssignmentContext):
        def add_assignment_error(expected: Type, actual: Type):
            self.add_error(f'Невозможно присвоить значение типа {safe_type_name(actual)} к переменной типа {safe_type_name(expected)}', ctx)

        left_side = ctx.declaration_list() or ctx.id_list()
        right_expressions = self.visitExpression_list(ctx.expression_list())

        left_side: MathLangParser.Id_listContext
        if isinstance(left_side, MathLangParser.Id_listContext):
            left_symbols: list[Symbol] | None = self.visitId_list(left_side)

            if left_symbols is None or len(left_symbols) != len(right_expressions):
                self.add_error("Количество переменных и выражений в присваивании не совпадает", ctx)
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
                except (SemanticError, SemanticWarning) as e:
                    self.add_error(e.message, ctx)

            if len(right_expressions) != 1:
                if len(left_symbols) != len(right_expressions):
                    self.add_error("Количество переменных и выражений в присваивании не совпадает", ctx)
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
                self.add_error(f"Символ '{id}' не определен", ctx)
                ids.append(None)
            else:
                ids += symbols

        return ids

    def visitExpression_list(self, ctx: MathLangParser.Expression_listContext) -> list[Type]:
        """Обработка списка выражений"""
        types = []
        if ctx.expression():
            for expr in ctx.expression():
                expr_type = self.visit(expr)
                types.append(expr_type)
        return types

    def visitExpression(self, ctx: MathLangParser.ExpressionContext) -> Type | None:
        def visit_binary_expression(ctx, operator: str) -> Type | None:
            left_type = self.visit(ctx.expression(0))
            right_type = self.visit(ctx.expression(1))

            if left_type is None or right_type is None:
                print(left_type, right_type, ctx.getText())
                # raise ValueError('None found') # todo
                return None

            try:
                result_type = TypeChecker.get_binary_operation_type(left_type, right_type, operator)
                return result_type
            except (SemanticError, SemanticWarning) as e:
                self.add_error(e.message, ctx)
                return None

        def visit_unary_expression(ctx, operator: str) -> Type | None:
            expr_type = self.visit(ctx.expression(0))

            if operator == '-' and not TypeChecker.is_numeric_type(expr_type) and not TypeChecker.is_boolean_type(expr_type):
                self.add_error(f"Унарная операция применима только к числовым и булевым типам. Получен тип {safe_type_name(expr_type)}", ctx)
                return None

            return expr_type

        if ctx.ID():
            var_name = ctx.ID().getText()
            symbol = self.current_scope.lookup(var_name) # todo
            if not symbol:
                self.add_error(f"Переменная '{var_name}' не объявлена", ctx)
                return None
            else:
                symbol = symbol[0]

            return symbol.type

        elif ctx.literal():
            return self.visitLiteral(ctx.literal())
        elif ctx.call():
            return self.visitCall(ctx.call())
        elif ctx.cast_expression():
            return self.visitCast_expression(ctx.cast_expression())

        elif ctx.getChildCount() == 3 and ctx.getChild(0).getText() == '(':
            # Выражение в скобках
            expr_type = self.visit(ctx.expression(0))
            return expr_type

        elif ctx.NOT():
            return visit_unary_expression(ctx, ctx.NOT().getText())
        elif ctx.MINUS() and ctx.getChildCount() == 2:
            return visit_unary_expression(ctx, ctx.MINUS().getText())

        elif ctx.CARET():
            return visit_binary_expression(ctx, ctx.CARET().getText())
        elif ctx.ASTERISK():
            return visit_binary_expression(ctx, ctx.ASTERISK().getText())
        elif ctx.SLASH():
            return visit_binary_expression(ctx, ctx.SLASH().getText())
        elif ctx.PLUS():
            return visit_binary_expression(ctx, ctx.PLUS().getText())
        elif ctx.MINUS():
            return visit_binary_expression(ctx, ctx.MINUS().getText())
        elif ctx.AND():
            return visit_binary_expression(ctx, ctx.AND().getText())
        elif ctx.OR():
            return visit_binary_expression(ctx, ctx.OR().getText())
        elif len(ctx.EQ()) == 2:
            return visit_binary_expression(ctx, "==")
        elif ctx.NEQ():
            return visit_binary_expression(ctx, ctx.NEQ().getText())
        elif ctx.GT():
            return visit_binary_expression(ctx, ctx.GT().getText())
        elif ctx.LT():
            return visit_binary_expression(ctx, ctx.LT().getText())
        elif ctx.GE():
            return visit_binary_expression(ctx, ctx.GE().getText())
        elif ctx.LE():
            return visit_binary_expression(ctx, ctx.LE().getText())

        print(ctx.getText())
        self.add_error("Неизвестный тип выражения", ctx)
        return None

    def visitCast_expression(self, ctx: MathLangParser.Cast_expressionContext) -> Type | None:
        """Обработка преобразования типов"""
        target_type = Type.create(ctx.type_specifier().getText())
        expr_type = self.visitExpression(ctx.expression())

        if not TypeChecker.can_cast(expr_type, target_type):
            self.add_error(f"Невозможно преобразовать {safe_type_name(expr_type)} в {safe_type_name(target_type)}", ctx)
            return None

        return target_type

    def visitCall(self, ctx: MathLangParser.CallContext, expected_type: Type = Type.VOID) -> Type | None:
        sub_name = ctx.ID().getText()
        sub_parameters = self.visitExpression_list(ctx.expression_list()) if ctx.expression_list() is not None else []

        defined_subprograms = self.global_scope.lookup(sub_name)
        if defined_subprograms is None:
            self.add_error(f"Неизвестная подпрограмма '{sub_name}'", ctx)
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
            # todo not beautiful fallback to write
            if sub_name == self.__write_subprogram.name:
                return self.__write_subprogram.type

            params_string = ', '.join([safe_type_name(type) for type in sub_parameters])
            self.add_error(f"Не найдено подходящей перегрузки {sub_name} с параметрами {params_string}", ctx)
            return None

        return found_overload.type

    def visitLiteral(self, ctx: MathLangParser.LiteralContext):
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
        """Обработка условного оператора"""
        condition_type = self.visit(ctx.expression())

        if not TypeChecker.is_boolean_type(condition_type):
            self.add_error(f"Ожидался тип {Type.BOOL.name} в if. Получен {safe_type_name(condition_type)}", ctx.expression())

        # Проверяем then блок
        self.visitBlock(ctx.block(0))

        # Проверяем else блок если есть
        if ctx.ELSE():
            self.visitBlock(ctx.block(1))

    def visitLoop(self, ctx: MathLangParser.LoopContext):
        """Обработка циклов"""
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
        """Обработка цикла while"""
        condition_type = self.visit(ctx.expression())

        if not TypeChecker.is_boolean_type(condition_type):
            self.add_error(f"Ожидался тип {Type.BOOL.name} в while. Получен {safe_type_name(condition_type)}", ctx.expression())

        self.visitBlock(ctx.block())

    def visitUntil_loop(self, ctx: MathLangParser.Until_loopContext):
        """Обработка цикла until"""
        condition_type = self.visit(ctx.expression())

        if not TypeChecker.is_boolean_type(condition_type):
            self.add_error(f"Ожидался тип {Type.BOOL.name} в until. Получен {safe_type_name(condition_type)}", ctx.expression())

        self.visitBlock(ctx.block())

    def visitFor_loop(self, ctx: MathLangParser.For_loopContext):
        """Обработка цикла for"""
        self.visitAssignment(ctx.assignment())

        condition_type = self.visit(ctx.expression())
        if not TypeChecker.is_boolean_type(condition_type):
            self.add_error(f"Ожидался тип {Type.BOOL.name} в for. Получен {safe_type_name(condition_type)}", ctx.expression())

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
        """Обработка операторов управления потоком"""
        if ctx.RETURN() and not self.current_subprogram:
            self.add_error("Оператор return может использоваться только внутри подпрограмм", ctx)


def main():
    """Основная функция"""
    if len(sys.argv) != 2:
        print("No file specified. Using default one.")

    source_file = sys.argv[1] if len(sys.argv) > 1 else 'samples/sample6.ml'

    try:
        # Чтение и лексический анализ
        input_stream = FileStream(source_file, encoding='utf-8')
        lexer = MathLangLexer(input_stream)
        tokens = CommonTokenStream(lexer)

        # Синтаксический анализ
        parser = MathLangParser(tokens)
        tree = parser.program()

        # Семантический анализ
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