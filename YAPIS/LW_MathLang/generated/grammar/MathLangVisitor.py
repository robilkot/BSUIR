# Generated from grammar/MathLang.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MathLangParser import MathLangParser
else:
    from MathLangParser import MathLangParser

# This class defines a complete generic visitor for a parse tree produced by MathLangParser.

class MathLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MathLangParser#program.
    def visitProgram(self, ctx:MathLangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathLangParser#statement.
    def visitStatement(self, ctx:MathLangParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathLangParser#subprogram.
    def visitSubprogram(self, ctx:MathLangParser.SubprogramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathLangParser#template.
    def visitTemplate(self, ctx:MathLangParser.TemplateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathLangParser#branching.
    def visitBranching(self, ctx:MathLangParser.BranchingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathLangParser#assignment.
    def visitAssignment(self, ctx:MathLangParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathLangParser#declaration_list.
    def visitDeclaration_list(self, ctx:MathLangParser.Declaration_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathLangParser#global_variable_declaration.
    def visitGlobal_variable_declaration(self, ctx:MathLangParser.Global_variable_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathLangParser#call.
    def visitCall(self, ctx:MathLangParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathLangParser#loop.
    def visitLoop(self, ctx:MathLangParser.LoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathLangParser#for_loop.
    def visitFor_loop(self, ctx:MathLangParser.For_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathLangParser#while_loop.
    def visitWhile_loop(self, ctx:MathLangParser.While_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathLangParser#until_loop.
    def visitUntil_loop(self, ctx:MathLangParser.Until_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathLangParser#block.
    def visitBlock(self, ctx:MathLangParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathLangParser#id_list.
    def visitId_list(self, ctx:MathLangParser.Id_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathLangParser#expression_list.
    def visitExpression_list(self, ctx:MathLangParser.Expression_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathLangParser#expression.
    def visitExpression(self, ctx:MathLangParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathLangParser#assignment_operator.
    def visitAssignment_operator(self, ctx:MathLangParser.Assignment_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathLangParser#simple_assignment_operator.
    def visitSimple_assignment_operator(self, ctx:MathLangParser.Simple_assignment_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathLangParser#control_flow_operator.
    def visitControl_flow_operator(self, ctx:MathLangParser.Control_flow_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathLangParser#literal.
    def visitLiteral(self, ctx:MathLangParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathLangParser#type_specifier.
    def visitType_specifier(self, ctx:MathLangParser.Type_specifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathLangParser#type_specifier_list.
    def visitType_specifier_list(self, ctx:MathLangParser.Type_specifier_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathLangParser#scope_modifier.
    def visitScope_modifier(self, ctx:MathLangParser.Scope_modifierContext):
        return self.visitChildren(ctx)



del MathLangParser