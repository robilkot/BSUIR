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
        self.local_var_counter = 0
        self.label_counter = 0


    def new_local_var(self):
        self.local_var_counter += 1
        return self.local_var_counter - 1

    def new_label(self):
        self.label_counter += 1
        return f"L{self.label_counter}"


    def visitAssignment(self, ctx):
        left_side = ctx.declaration_list() or ctx.id_list()
        right_expressions = self.visitExpression_list(ctx.expression_list())

        if isinstance(left_side, MathLangParser.Id_listContext):
            left_symbols = self.visitId_list(left_side)

            for i, (symbol, expr_type) in enumerate(zip(left_symbols, right_expressions)):
                if symbol and symbol.type == expr_type:
                    if symbol.is_global:
                        self.add_wat(f"    (global.set ${symbol.name} (local.get ${expr_type}))")
                    else:
                        self.add_wat(f"    (local.set ${symbol.name} (local.get ${expr_type}))")

        elif isinstance(left_side, MathLangParser.Declaration_listContext):
            left_symbols = self.visitDeclaration_list(left_side)

            for symbol in left_symbols:
                try:
                    self.current_scope.add_symbol(symbol)
                    var_idx = self.new_local_var()
                    self.add_wat(f"    (local ${symbol.name} {self.type_to_wat(symbol.type)})")
                except SemanticError as e:
                    self.add_error(e.message, ctx)

            if len(right_expressions) == 1 and len(left_symbols) > 1:
                pass
            else:
                for i, (symbol, expr_type) in enumerate(zip(left_symbols, right_expressions)):
                    if symbol and symbol.type == expr_type:
                        self.add_wat(f"    (local.set ${symbol.name} (local.get ${expr_type}))")

    def visitLiteral(self, ctx):
        if ctx.INT():
            val = int(ctx.INT().getText())
            var_idx = self.new_local_var()
            self.add_wat(f"    (local.set ${var_idx} (i32.const {val}))")
            return Type.int()
        elif ctx.FLOAT():
            val = float(ctx.FLOAT().getText())
            var_idx = self.new_local_var()
            self.add_wat(f"    (local.set ${var_idx} (f32.const {val}))")
            return Type.float()
        elif ctx.BOOL():
            val = 1 if ctx.BOOL().getText() == "true" else 0
            var_idx = self.new_local_var()
            self.add_wat(f"    (local.set ${var_idx} (i32.const {val}))")
            return Type.bool()
        elif ctx.STRING():
            text = ctx.STRING().getText()[1:-1]
            var_idx = self.new_local_var()
            self.add_wat(f"    (local.set ${var_idx} (call $store_string \"{text}\"))")
            return Type.string()

    def visitExpression(self, ctx):
        if ctx.ID():
            var_name = ctx.ID().getText()
            symbol = self.current_scope.lookup(var_name)
            if symbol:
                var_idx = self.new_local_var()
                symbol = symbol[0]
                if symbol.is_global:
                    self.add_wat(f"    (local.set ${var_idx} (global.get ${symbol.name}))")
                else:
                    self.add_wat(f"    (local.set ${var_idx} (local.get ${symbol.name}))")
                return symbol.type
            return None

        elif ctx.literal():
            return self.visitLiteral(ctx.literal())
        elif ctx.call():
            return self.visitCall(ctx.call())

        elif ctx.getChildCount() == 3 and ctx.getChild(0).getText() == '(':
            return self.visitExpression(ctx.expression(0))

        elif ctx.NOT():
            expr_type = self.visitExpression(ctx.expression(0))
            var_idx = self.new_local_var()
            self.add_wat(f"    (local.set ${var_idx} (i32.eqz (local.get ${expr_type})))")
            return Type.bool()

        elif ctx.MINUS() and ctx.getChildCount() == 2:
            expr_type = self.visitExpression(ctx.expression(0))
            var_idx = self.new_local_var()
            if expr_type == Type.int():
                self.add_wat(f"    (local.set ${var_idx} (i32.sub (i32.const 0) (local.get ${expr_type})))")
            elif expr_type == Type.float():
                self.add_wat(f"    (local.set ${var_idx} (f32.neg (local.get ${expr_type})))")
            return expr_type

        elif len(ctx.EQ()) == 2:
            left_type = self.visitExpression(ctx.expression(0))
            right_type = self.visitExpression(ctx.expression(1))
            var_idx = self.new_local_var()
            if left_type == Type.int() and right_type == Type.int():
                self.add_wat(f"    (local.set ${var_idx} (i32.eq (local.get ${left_type}) (local.get ${right_type})))")
            elif left_type == Type.float() and right_type == Type.float():
                self.add_wat(f"    (local.set ${var_idx} (f32.eq (local.get ${left_type}) (local.get ${right_type})))")
            return Type.bool()

        else:
            left_type = self.visitExpression(ctx.expression(0))
            right_type = self.visitExpression(ctx.expression(1))
            op = ctx.getChild(1).getText()

            var_idx = self.new_local_var()
            result_type = TypeChecker.get_binary_operation_type(left_type, right_type, op)

            if result_type == Type.int():
                if op == '+':
                    self.add_wat(
                        f"    (local.set ${var_idx} (i32.add (local.get ${left_type}) (local.get ${right_type})))")
                elif op == '-':
                    self.add_wat(
                        f"    (local.set ${var_idx} (i32.sub (local.get ${left_type}) (local.get ${right_type})))")
                elif op == '*':
                    self.add_wat(
                        f"    (local.set ${var_idx} (i32.mul (local.get ${left_type}) (local.get ${right_type})))")
                elif op == '/':
                    self.add_wat(
                        f"    (local.set ${var_idx} (i32.div_s (local.get ${left_type}) (local.get ${right_type})))")
                elif op == '%':
                    self.add_wat(
                        f"    (local.set ${var_idx} (i32.rem_s (local.get ${left_type}) (local.get ${right_type})))")
                elif op == '<':
                    self.add_wat(
                        f"    (local.set ${var_idx} (i32.lt_s (local.get ${left_type}) (local.get ${right_type})))")
                elif op == '>':
                    self.add_wat(
                        f"    (local.set ${var_idx} (i32.gt_s (local.get ${left_type}) (local.get ${right_type})))")
                elif op == '<=':
                    self.add_wat(
                        f"    (local.set ${var_idx} (i32.le_s (local.get ${left_type}) (local.get ${right_type})))")
                elif op == '>=':
                    self.add_wat(
                        f"    (local.set ${var_idx} (i32.ge_s (local.get ${left_type}) (local.get ${right_type})))")
                elif op == '!=':
                    self.add_wat(
                        f"    (local.set ${var_idx} (i32.ne (local.get ${left_type}) (local.get ${right_type})))")
                elif op == 'and':
                    self.add_wat(
                        f"    (local.set ${var_idx} (i32.and (local.get ${left_type}) (local.get ${right_type})))")
                elif op == 'or':
                    self.add_wat(
                        f"    (local.set ${var_idx} (i32.or (local.get ${left_type}) (local.get ${right_type})))")
            elif result_type == Type.float():
                if op == '+':
                    self.add_wat(
                        f"    (local.set ${var_idx} (f32.add (local.get ${left_type}) (local.get ${right_type})))")
                elif op == '-':
                    self.add_wat(
                        f"    (local.set ${var_idx} (f32.sub (local.get ${left_type}) (local.get ${right_type})))")
                elif op == '*':
                    self.add_wat(
                        f"    (local.set ${var_idx} (f32.mul (local.get ${left_type}) (local.get ${right_type})))")
                elif op == '/':
                    self.add_wat(
                        f"    (local.set ${var_idx} (f32.div (local.get ${left_type}) (local.get ${right_type})))")

            return result_type

    def visitBranching(self, ctx):
        self.visit(ctx.expression())
        else_label = self.new_label()
        end_label = self.new_label()

        self.add_wat(f"    (local.get ${ctx.expression()})")
        self.add_wat(f"    (i32.eqz)")
        self.add_wat(f"    (br_if ${else_label})")

        self.visitBlock(ctx.block(0))
        self.add_wat(f"    (br ${end_label})")
        self.add_wat(f"    (label ${else_label})")

        if ctx.ELSE():
            self.visitBlock(ctx.block(1))

        self.add_wat(f"    (label ${end_label})")

    def visitWhile_loop(self, ctx):
        start_label = self.new_label()
        end_label = self.new_label()

        self.add_wat(f"    (label ${start_label})")
        self.visit(ctx.expression())
        self.add_wat(f"    (local.get ${ctx.expression()})")
        self.add_wat(f"    (i32.eqz)")
        self.add_wat(f"    (br_if ${end_label})")

        self.in_loop = True
        self.visitBlock(ctx.block())
        self.in_loop = False

        self.add_wat(f"    (br ${start_label})")
        self.add_wat(f"    (label ${end_label})")

    def visitBlock(self, ctx):
        previous_scope = self.current_scope
        self.current_scope = self.current_scope.create_child_scope()

        if ctx:
            for stmt in ctx.statement():
                self.visit(stmt)

        self.current_scope = previous_scope

    def visitControl_flow_operator(self, ctx):
        if ctx.RETURN():
            if ctx.expression():
                expr_type = self.visit(ctx.expression())
                self.add_wat(f"    (local.get ${ctx.expression()})")
                self.add_wat(f"    (return)")
            else:
                self.add_wat(f"    (return)")
        elif ctx.BREAK():
            self.add_wat(f"    (br 1)")
        elif ctx.CONTINUE():
            self.add_wat(f"    (br 0)")


