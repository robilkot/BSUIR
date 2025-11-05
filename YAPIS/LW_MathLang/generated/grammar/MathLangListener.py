# Generated from grammar/MathLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MathLangParser import MathLangParser
else:
    from MathLangParser import MathLangParser

# This class defines a complete listener for a parse tree produced by MathLangParser.
class MathLangListener(ParseTreeListener):

    # Enter a parse tree produced by MathLangParser#program.
    def enterProgram(self, ctx:MathLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by MathLangParser#program.
    def exitProgram(self, ctx:MathLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by MathLangParser#statement.
    def enterStatement(self, ctx:MathLangParser.StatementContext):
        pass

    # Exit a parse tree produced by MathLangParser#statement.
    def exitStatement(self, ctx:MathLangParser.StatementContext):
        pass


    # Enter a parse tree produced by MathLangParser#subprogram.
    def enterSubprogram(self, ctx:MathLangParser.SubprogramContext):
        pass

    # Exit a parse tree produced by MathLangParser#subprogram.
    def exitSubprogram(self, ctx:MathLangParser.SubprogramContext):
        pass


    # Enter a parse tree produced by MathLangParser#branching.
    def enterBranching(self, ctx:MathLangParser.BranchingContext):
        pass

    # Exit a parse tree produced by MathLangParser#branching.
    def exitBranching(self, ctx:MathLangParser.BranchingContext):
        pass


    # Enter a parse tree produced by MathLangParser#declaration.
    def enterDeclaration(self, ctx:MathLangParser.DeclarationContext):
        pass

    # Exit a parse tree produced by MathLangParser#declaration.
    def exitDeclaration(self, ctx:MathLangParser.DeclarationContext):
        pass


    # Enter a parse tree produced by MathLangParser#assignment.
    def enterAssignment(self, ctx:MathLangParser.AssignmentContext):
        pass

    # Exit a parse tree produced by MathLangParser#assignment.
    def exitAssignment(self, ctx:MathLangParser.AssignmentContext):
        pass


    # Enter a parse tree produced by MathLangParser#call.
    def enterCall(self, ctx:MathLangParser.CallContext):
        pass

    # Exit a parse tree produced by MathLangParser#call.
    def exitCall(self, ctx:MathLangParser.CallContext):
        pass


    # Enter a parse tree produced by MathLangParser#loop.
    def enterLoop(self, ctx:MathLangParser.LoopContext):
        pass

    # Exit a parse tree produced by MathLangParser#loop.
    def exitLoop(self, ctx:MathLangParser.LoopContext):
        pass


    # Enter a parse tree produced by MathLangParser#for_loop.
    def enterFor_loop(self, ctx:MathLangParser.For_loopContext):
        pass

    # Exit a parse tree produced by MathLangParser#for_loop.
    def exitFor_loop(self, ctx:MathLangParser.For_loopContext):
        pass


    # Enter a parse tree produced by MathLangParser#while_loop.
    def enterWhile_loop(self, ctx:MathLangParser.While_loopContext):
        pass

    # Exit a parse tree produced by MathLangParser#while_loop.
    def exitWhile_loop(self, ctx:MathLangParser.While_loopContext):
        pass


    # Enter a parse tree produced by MathLangParser#until_loop.
    def enterUntil_loop(self, ctx:MathLangParser.Until_loopContext):
        pass

    # Exit a parse tree produced by MathLangParser#until_loop.
    def exitUntil_loop(self, ctx:MathLangParser.Until_loopContext):
        pass


    # Enter a parse tree produced by MathLangParser#block.
    def enterBlock(self, ctx:MathLangParser.BlockContext):
        pass

    # Exit a parse tree produced by MathLangParser#block.
    def exitBlock(self, ctx:MathLangParser.BlockContext):
        pass


    # Enter a parse tree produced by MathLangParser#id_list.
    def enterId_list(self, ctx:MathLangParser.Id_listContext):
        pass

    # Exit a parse tree produced by MathLangParser#id_list.
    def exitId_list(self, ctx:MathLangParser.Id_listContext):
        pass


    # Enter a parse tree produced by MathLangParser#expression_list.
    def enterExpression_list(self, ctx:MathLangParser.Expression_listContext):
        pass

    # Exit a parse tree produced by MathLangParser#expression_list.
    def exitExpression_list(self, ctx:MathLangParser.Expression_listContext):
        pass


    # Enter a parse tree produced by MathLangParser#expression.
    def enterExpression(self, ctx:MathLangParser.ExpressionContext):
        pass

    # Exit a parse tree produced by MathLangParser#expression.
    def exitExpression(self, ctx:MathLangParser.ExpressionContext):
        pass


    # Enter a parse tree produced by MathLangParser#cast_expression.
    def enterCast_expression(self, ctx:MathLangParser.Cast_expressionContext):
        pass

    # Exit a parse tree produced by MathLangParser#cast_expression.
    def exitCast_expression(self, ctx:MathLangParser.Cast_expressionContext):
        pass


    # Enter a parse tree produced by MathLangParser#assignment_operator.
    def enterAssignment_operator(self, ctx:MathLangParser.Assignment_operatorContext):
        pass

    # Exit a parse tree produced by MathLangParser#assignment_operator.
    def exitAssignment_operator(self, ctx:MathLangParser.Assignment_operatorContext):
        pass


    # Enter a parse tree produced by MathLangParser#simple_assignment_operator.
    def enterSimple_assignment_operator(self, ctx:MathLangParser.Simple_assignment_operatorContext):
        pass

    # Exit a parse tree produced by MathLangParser#simple_assignment_operator.
    def exitSimple_assignment_operator(self, ctx:MathLangParser.Simple_assignment_operatorContext):
        pass


    # Enter a parse tree produced by MathLangParser#binary_operator.
    def enterBinary_operator(self, ctx:MathLangParser.Binary_operatorContext):
        pass

    # Exit a parse tree produced by MathLangParser#binary_operator.
    def exitBinary_operator(self, ctx:MathLangParser.Binary_operatorContext):
        pass


    # Enter a parse tree produced by MathLangParser#unary_operator.
    def enterUnary_operator(self, ctx:MathLangParser.Unary_operatorContext):
        pass

    # Exit a parse tree produced by MathLangParser#unary_operator.
    def exitUnary_operator(self, ctx:MathLangParser.Unary_operatorContext):
        pass


    # Enter a parse tree produced by MathLangParser#control_flow_operator.
    def enterControl_flow_operator(self, ctx:MathLangParser.Control_flow_operatorContext):
        pass

    # Exit a parse tree produced by MathLangParser#control_flow_operator.
    def exitControl_flow_operator(self, ctx:MathLangParser.Control_flow_operatorContext):
        pass


    # Enter a parse tree produced by MathLangParser#literal.
    def enterLiteral(self, ctx:MathLangParser.LiteralContext):
        pass

    # Exit a parse tree produced by MathLangParser#literal.
    def exitLiteral(self, ctx:MathLangParser.LiteralContext):
        pass


    # Enter a parse tree produced by MathLangParser#declaration_list.
    def enterDeclaration_list(self, ctx:MathLangParser.Declaration_listContext):
        pass

    # Exit a parse tree produced by MathLangParser#declaration_list.
    def exitDeclaration_list(self, ctx:MathLangParser.Declaration_listContext):
        pass


    # Enter a parse tree produced by MathLangParser#variable_declaration.
    def enterVariable_declaration(self, ctx:MathLangParser.Variable_declarationContext):
        pass

    # Exit a parse tree produced by MathLangParser#variable_declaration.
    def exitVariable_declaration(self, ctx:MathLangParser.Variable_declarationContext):
        pass


    # Enter a parse tree produced by MathLangParser#type_specifier.
    def enterType_specifier(self, ctx:MathLangParser.Type_specifierContext):
        pass

    # Exit a parse tree produced by MathLangParser#type_specifier.
    def exitType_specifier(self, ctx:MathLangParser.Type_specifierContext):
        pass


    # Enter a parse tree produced by MathLangParser#scope_modifier.
    def enterScope_modifier(self, ctx:MathLangParser.Scope_modifierContext):
        pass

    # Exit a parse tree produced by MathLangParser#scope_modifier.
    def exitScope_modifier(self, ctx:MathLangParser.Scope_modifierContext):
        pass



del MathLangParser