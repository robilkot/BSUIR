# Generated from grammar/MathLang.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,39,255,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,1,0,5,0,54,
        8,0,10,0,12,0,57,9,0,1,0,5,0,60,8,0,10,0,12,0,63,9,0,1,0,1,0,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,3,1,74,8,1,1,2,1,2,1,2,1,2,3,2,80,8,2,1,
        2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,92,8,3,1,4,1,4,1,5,1,5,
        3,5,98,8,5,1,5,1,5,1,5,1,6,1,6,1,6,3,6,106,8,6,1,6,1,6,1,7,1,7,1,
        7,3,7,113,8,7,1,8,1,8,1,8,3,8,118,8,8,1,8,1,8,3,8,122,8,8,1,8,1,
        8,3,8,126,8,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,
        1,10,1,10,1,10,1,11,1,11,5,11,145,8,11,10,11,12,11,148,9,11,1,11,
        1,11,1,12,1,12,5,12,154,8,12,10,12,12,12,157,9,12,1,12,1,12,1,13,
        1,13,1,13,5,13,164,8,13,10,13,12,13,167,9,13,1,13,1,13,1,14,1,14,
        1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,183,8,14,
        1,14,1,14,1,14,1,14,5,14,189,8,14,10,14,12,14,192,9,14,1,15,1,15,
        1,15,1,15,1,15,1,16,1,16,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,
        1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,3,18,219,8,18,
        1,19,1,19,1,20,1,20,1,21,1,21,1,22,3,22,228,8,22,1,22,1,22,1,22,
        1,22,3,22,234,8,22,1,22,3,22,237,8,22,1,22,5,22,240,8,22,10,22,12,
        22,243,9,22,1,23,1,23,1,23,1,23,3,23,249,8,23,1,24,1,24,1,25,1,25,
        1,25,0,1,28,26,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,
        36,38,40,42,44,46,48,50,0,3,1,0,23,25,1,0,33,36,1,0,30,32,271,0,
        55,1,0,0,0,2,73,1,0,0,0,4,75,1,0,0,0,6,84,1,0,0,0,8,93,1,0,0,0,10,
        97,1,0,0,0,12,102,1,0,0,0,14,112,1,0,0,0,16,114,1,0,0,0,18,130,1,
        0,0,0,20,136,1,0,0,0,22,142,1,0,0,0,24,155,1,0,0,0,26,165,1,0,0,
        0,28,182,1,0,0,0,30,193,1,0,0,0,32,198,1,0,0,0,34,200,1,0,0,0,36,
        218,1,0,0,0,38,220,1,0,0,0,40,222,1,0,0,0,42,224,1,0,0,0,44,227,
        1,0,0,0,46,244,1,0,0,0,48,250,1,0,0,0,50,252,1,0,0,0,52,54,3,4,2,
        0,53,52,1,0,0,0,54,57,1,0,0,0,55,53,1,0,0,0,55,56,1,0,0,0,56,61,
        1,0,0,0,57,55,1,0,0,0,58,60,3,2,1,0,59,58,1,0,0,0,60,63,1,0,0,0,
        61,59,1,0,0,0,61,62,1,0,0,0,62,64,1,0,0,0,63,61,1,0,0,0,64,65,5,
        0,0,1,65,1,1,0,0,0,66,74,3,40,20,0,67,74,3,22,11,0,68,74,3,8,4,0,
        69,74,3,6,3,0,70,74,3,14,7,0,71,74,3,10,5,0,72,74,3,12,6,0,73,66,
        1,0,0,0,73,67,1,0,0,0,73,68,1,0,0,0,73,69,1,0,0,0,73,70,1,0,0,0,
        73,71,1,0,0,0,73,72,1,0,0,0,74,3,1,0,0,0,75,76,5,28,0,0,76,77,5,
        37,0,0,77,79,5,10,0,0,78,80,3,44,22,0,79,78,1,0,0,0,79,80,1,0,0,
        0,80,81,1,0,0,0,81,82,5,11,0,0,82,83,3,22,11,0,83,5,1,0,0,0,84,85,
        5,26,0,0,85,86,5,10,0,0,86,87,3,28,14,0,87,88,5,11,0,0,88,91,3,22,
        11,0,89,90,5,27,0,0,90,92,3,22,11,0,91,89,1,0,0,0,91,92,1,0,0,0,
        92,7,1,0,0,0,93,94,3,44,22,0,94,9,1,0,0,0,95,98,3,44,22,0,96,98,
        3,24,12,0,97,95,1,0,0,0,97,96,1,0,0,0,98,99,1,0,0,0,99,100,3,32,
        16,0,100,101,3,26,13,0,101,11,1,0,0,0,102,103,5,37,0,0,103,105,5,
        10,0,0,104,106,3,26,13,0,105,104,1,0,0,0,105,106,1,0,0,0,106,107,
        1,0,0,0,107,108,5,11,0,0,108,13,1,0,0,0,109,113,3,16,8,0,110,113,
        3,18,9,0,111,113,3,20,10,0,112,109,1,0,0,0,112,110,1,0,0,0,112,111,
        1,0,0,0,113,15,1,0,0,0,114,115,5,20,0,0,115,117,5,10,0,0,116,118,
        3,10,5,0,117,116,1,0,0,0,117,118,1,0,0,0,118,119,1,0,0,0,119,121,
        5,8,0,0,120,122,3,28,14,0,121,120,1,0,0,0,121,122,1,0,0,0,122,123,
        1,0,0,0,123,125,5,8,0,0,124,126,3,2,1,0,125,124,1,0,0,0,125,126,
        1,0,0,0,126,127,1,0,0,0,127,128,5,11,0,0,128,129,3,22,11,0,129,17,
        1,0,0,0,130,131,5,21,0,0,131,132,5,10,0,0,132,133,3,28,14,0,133,
        134,5,11,0,0,134,135,3,22,11,0,135,19,1,0,0,0,136,137,5,22,0,0,137,
        138,5,10,0,0,138,139,3,28,14,0,139,140,5,11,0,0,140,141,3,22,11,
        0,141,21,1,0,0,0,142,146,5,12,0,0,143,145,3,2,1,0,144,143,1,0,0,
        0,145,148,1,0,0,0,146,144,1,0,0,0,146,147,1,0,0,0,147,149,1,0,0,
        0,148,146,1,0,0,0,149,150,5,13,0,0,150,23,1,0,0,0,151,152,5,37,0,
        0,152,154,5,7,0,0,153,151,1,0,0,0,154,157,1,0,0,0,155,153,1,0,0,
        0,155,156,1,0,0,0,156,158,1,0,0,0,157,155,1,0,0,0,158,159,5,37,0,
        0,159,25,1,0,0,0,160,161,3,28,14,0,161,162,5,7,0,0,162,164,1,0,0,
        0,163,160,1,0,0,0,164,167,1,0,0,0,165,163,1,0,0,0,165,166,1,0,0,
        0,166,168,1,0,0,0,167,165,1,0,0,0,168,169,3,28,14,0,169,27,1,0,0,
        0,170,171,6,14,-1,0,171,183,5,37,0,0,172,183,3,42,21,0,173,183,3,
        12,6,0,174,183,3,30,15,0,175,176,3,38,19,0,176,177,3,28,14,2,177,
        183,1,0,0,0,178,179,5,10,0,0,179,180,3,28,14,0,180,181,5,11,0,0,
        181,183,1,0,0,0,182,170,1,0,0,0,182,172,1,0,0,0,182,173,1,0,0,0,
        182,174,1,0,0,0,182,175,1,0,0,0,182,178,1,0,0,0,183,190,1,0,0,0,
        184,185,10,3,0,0,185,186,3,36,18,0,186,187,3,28,14,4,187,189,1,0,
        0,0,188,184,1,0,0,0,189,192,1,0,0,0,190,188,1,0,0,0,190,191,1,0,
        0,0,191,29,1,0,0,0,192,190,1,0,0,0,193,194,3,48,24,0,194,195,5,10,
        0,0,195,196,3,28,14,0,196,197,5,11,0,0,197,31,1,0,0,0,198,199,3,
        34,17,0,199,33,1,0,0,0,200,201,5,4,0,0,201,35,1,0,0,0,202,219,5,
        15,0,0,203,219,5,16,0,0,204,219,5,17,0,0,205,219,5,14,0,0,206,219,
        5,18,0,0,207,208,5,4,0,0,208,219,5,4,0,0,209,219,5,2,0,0,210,219,
        5,1,0,0,211,219,5,3,0,0,212,219,5,5,0,0,213,219,5,6,0,0,214,215,
        5,5,0,0,215,219,5,4,0,0,216,217,5,6,0,0,217,219,5,4,0,0,218,202,
        1,0,0,0,218,203,1,0,0,0,218,204,1,0,0,0,218,205,1,0,0,0,218,206,
        1,0,0,0,218,207,1,0,0,0,218,209,1,0,0,0,218,210,1,0,0,0,218,211,
        1,0,0,0,218,212,1,0,0,0,218,213,1,0,0,0,218,214,1,0,0,0,218,216,
        1,0,0,0,219,37,1,0,0,0,220,221,5,16,0,0,221,39,1,0,0,0,222,223,7,
        0,0,0,223,41,1,0,0,0,224,225,7,1,0,0,225,43,1,0,0,0,226,228,3,50,
        25,0,227,226,1,0,0,0,227,228,1,0,0,0,228,229,1,0,0,0,229,230,3,48,
        24,0,230,241,3,46,23,0,231,233,5,7,0,0,232,234,3,50,25,0,233,232,
        1,0,0,0,233,234,1,0,0,0,234,236,1,0,0,0,235,237,3,48,24,0,236,235,
        1,0,0,0,236,237,1,0,0,0,237,238,1,0,0,0,238,240,3,46,23,0,239,231,
        1,0,0,0,240,243,1,0,0,0,241,239,1,0,0,0,241,242,1,0,0,0,242,45,1,
        0,0,0,243,241,1,0,0,0,244,248,5,37,0,0,245,246,3,34,17,0,246,247,
        3,28,14,0,247,249,1,0,0,0,248,245,1,0,0,0,248,249,1,0,0,0,249,47,
        1,0,0,0,250,251,7,2,0,0,251,49,1,0,0,0,252,253,5,19,0,0,253,51,1,
        0,0,0,22,55,61,73,79,91,97,105,112,117,121,125,146,155,165,182,190,
        218,227,233,236,241,248
    ]

class MathLangParser ( Parser ):

    grammarFileName = "MathLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'and'", "'or'", "'not'", "'='", "'>'", 
                     "'<'", "','", "';'", "':'", "'('", "')'", "'{'", "'}'", 
                     "'/'", "'+'", "'-'", "'*'", "'^'", "'global'", "'for'", 
                     "'while'", "'until'", "'break'", "'continue'", "'return'", 
                     "'if'", "'else'", "'sub'", "<INVALID>", "'float'", 
                     "'int'", "'bool'" ]

    symbolicNames = [ "<INVALID>", "AND", "OR", "NOT", "EQ", "GT", "LS", 
                      "COMMA", "SEMI", "COLON", "LPAREN", "RPAREN", "LCURLY", 
                      "RCURLY", "SLASH", "PLUS", "MINUS", "ASTERISK", "CARET", 
                      "GLOBAL", "FOR", "WHILE", "UNTIL", "BREAK", "CONTINUE", 
                      "RETURN", "IF", "ELSE", "SUB", "DSLASH", "FLOAT_T", 
                      "INT_T", "BOOL_T", "INT", "FLOAT", "BOOL", "STRING", 
                      "ID", "LINE_COMMENT", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_subprogram = 2
    RULE_branching = 3
    RULE_declaration = 4
    RULE_assignment = 5
    RULE_call = 6
    RULE_loop = 7
    RULE_for_loop = 8
    RULE_while_loop = 9
    RULE_until_loop = 10
    RULE_block = 11
    RULE_id_list = 12
    RULE_expression_list = 13
    RULE_expression = 14
    RULE_cast_expression = 15
    RULE_assignment_operator = 16
    RULE_simple_assignment_operator = 17
    RULE_binary_operator = 18
    RULE_unary_operator = 19
    RULE_control_flow_operator = 20
    RULE_literal = 21
    RULE_declaration_list = 22
    RULE_variable_declaration = 23
    RULE_type_specifier = 24
    RULE_scope_modifier = 25

    ruleNames =  [ "program", "statement", "subprogram", "branching", "declaration", 
                   "assignment", "call", "loop", "for_loop", "while_loop", 
                   "until_loop", "block", "id_list", "expression_list", 
                   "expression", "cast_expression", "assignment_operator", 
                   "simple_assignment_operator", "binary_operator", "unary_operator", 
                   "control_flow_operator", "literal", "declaration_list", 
                   "variable_declaration", "type_specifier", "scope_modifier" ]

    EOF = Token.EOF
    AND=1
    OR=2
    NOT=3
    EQ=4
    GT=5
    LS=6
    COMMA=7
    SEMI=8
    COLON=9
    LPAREN=10
    RPAREN=11
    LCURLY=12
    RCURLY=13
    SLASH=14
    PLUS=15
    MINUS=16
    ASTERISK=17
    CARET=18
    GLOBAL=19
    FOR=20
    WHILE=21
    UNTIL=22
    BREAK=23
    CONTINUE=24
    RETURN=25
    IF=26
    ELSE=27
    SUB=28
    DSLASH=29
    FLOAT_T=30
    INT_T=31
    BOOL_T=32
    INT=33
    FLOAT=34
    BOOL=35
    STRING=36
    ID=37
    LINE_COMMENT=38
    WS=39

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MathLangParser.EOF, 0)

        def subprogram(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathLangParser.SubprogramContext)
            else:
                return self.getTypedRuleContext(MathLangParser.SubprogramContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(MathLangParser.StatementContext,i)


        def getRuleIndex(self):
            return MathLangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MathLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==28:
                self.state = 52
                self.subprogram()
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 145088843776) != 0):
                self.state = 58
                self.statement()
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 64
            self.match(MathLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def control_flow_operator(self):
            return self.getTypedRuleContext(MathLangParser.Control_flow_operatorContext,0)


        def block(self):
            return self.getTypedRuleContext(MathLangParser.BlockContext,0)


        def declaration(self):
            return self.getTypedRuleContext(MathLangParser.DeclarationContext,0)


        def branching(self):
            return self.getTypedRuleContext(MathLangParser.BranchingContext,0)


        def loop(self):
            return self.getTypedRuleContext(MathLangParser.LoopContext,0)


        def assignment(self):
            return self.getTypedRuleContext(MathLangParser.AssignmentContext,0)


        def call(self):
            return self.getTypedRuleContext(MathLangParser.CallContext,0)


        def getRuleIndex(self):
            return MathLangParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MathLangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 73
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 66
                self.control_flow_operator()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 67
                self.block()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 68
                self.declaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 69
                self.branching()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 70
                self.loop()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 71
                self.assignment()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 72
                self.call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubprogramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB(self):
            return self.getToken(MathLangParser.SUB, 0)

        def ID(self):
            return self.getToken(MathLangParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MathLangParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MathLangParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(MathLangParser.BlockContext,0)


        def declaration_list(self):
            return self.getTypedRuleContext(MathLangParser.Declaration_listContext,0)


        def getRuleIndex(self):
            return MathLangParser.RULE_subprogram

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubprogram" ):
                listener.enterSubprogram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubprogram" ):
                listener.exitSubprogram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubprogram" ):
                return visitor.visitSubprogram(self)
            else:
                return visitor.visitChildren(self)




    def subprogram(self):

        localctx = MathLangParser.SubprogramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_subprogram)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(MathLangParser.SUB)
            self.state = 76
            self.match(MathLangParser.ID)
            self.state = 77
            self.match(MathLangParser.LPAREN)
            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 7516717056) != 0):
                self.state = 78
                self.declaration_list()


            self.state = 81
            self.match(MathLangParser.RPAREN)
            self.state = 82
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BranchingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MathLangParser.IF, 0)

        def LPAREN(self):
            return self.getToken(MathLangParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MathLangParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MathLangParser.RPAREN, 0)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathLangParser.BlockContext)
            else:
                return self.getTypedRuleContext(MathLangParser.BlockContext,i)


        def ELSE(self):
            return self.getToken(MathLangParser.ELSE, 0)

        def getRuleIndex(self):
            return MathLangParser.RULE_branching

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBranching" ):
                listener.enterBranching(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBranching" ):
                listener.exitBranching(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBranching" ):
                return visitor.visitBranching(self)
            else:
                return visitor.visitChildren(self)




    def branching(self):

        localctx = MathLangParser.BranchingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_branching)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(MathLangParser.IF)
            self.state = 85
            self.match(MathLangParser.LPAREN)
            self.state = 86
            self.expression(0)
            self.state = 87
            self.match(MathLangParser.RPAREN)
            self.state = 88
            self.block()
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 89
                self.match(MathLangParser.ELSE)
                self.state = 90
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration_list(self):
            return self.getTypedRuleContext(MathLangParser.Declaration_listContext,0)


        def getRuleIndex(self):
            return MathLangParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = MathLangParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.declaration_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment_operator(self):
            return self.getTypedRuleContext(MathLangParser.Assignment_operatorContext,0)


        def expression_list(self):
            return self.getTypedRuleContext(MathLangParser.Expression_listContext,0)


        def declaration_list(self):
            return self.getTypedRuleContext(MathLangParser.Declaration_listContext,0)


        def id_list(self):
            return self.getTypedRuleContext(MathLangParser.Id_listContext,0)


        def getRuleIndex(self):
            return MathLangParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = MathLangParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19, 30, 31, 32]:
                self.state = 95
                self.declaration_list()
                pass
            elif token in [37]:
                self.state = 96
                self.id_list()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 99
            self.assignment_operator()
            self.state = 100
            self.expression_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MathLangParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MathLangParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MathLangParser.RPAREN, 0)

        def expression_list(self):
            return self.getTypedRuleContext(MathLangParser.Expression_listContext,0)


        def getRuleIndex(self):
            return MathLangParser.RULE_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCall" ):
                listener.enterCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCall" ):
                listener.exitCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall" ):
                return visitor.visitCall(self)
            else:
                return visitor.visitChildren(self)




    def call(self):

        localctx = MathLangParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(MathLangParser.ID)
            self.state = 103
            self.match(MathLangParser.LPAREN)
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 273804231680) != 0):
                self.state = 104
                self.expression_list()


            self.state = 107
            self.match(MathLangParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def for_loop(self):
            return self.getTypedRuleContext(MathLangParser.For_loopContext,0)


        def while_loop(self):
            return self.getTypedRuleContext(MathLangParser.While_loopContext,0)


        def until_loop(self):
            return self.getTypedRuleContext(MathLangParser.Until_loopContext,0)


        def getRuleIndex(self):
            return MathLangParser.RULE_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoop" ):
                listener.enterLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoop" ):
                listener.exitLoop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop" ):
                return visitor.visitLoop(self)
            else:
                return visitor.visitChildren(self)




    def loop(self):

        localctx = MathLangParser.LoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_loop)
        try:
            self.state = 112
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 109
                self.for_loop()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 110
                self.while_loop()
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 3)
                self.state = 111
                self.until_loop()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MathLangParser.FOR, 0)

        def LPAREN(self):
            return self.getToken(MathLangParser.LPAREN, 0)

        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(MathLangParser.SEMI)
            else:
                return self.getToken(MathLangParser.SEMI, i)

        def RPAREN(self):
            return self.getToken(MathLangParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(MathLangParser.BlockContext,0)


        def assignment(self):
            return self.getTypedRuleContext(MathLangParser.AssignmentContext,0)


        def expression(self):
            return self.getTypedRuleContext(MathLangParser.ExpressionContext,0)


        def statement(self):
            return self.getTypedRuleContext(MathLangParser.StatementContext,0)


        def getRuleIndex(self):
            return MathLangParser.RULE_for_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_loop" ):
                listener.enterFor_loop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_loop" ):
                listener.exitFor_loop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_loop" ):
                return visitor.visitFor_loop(self)
            else:
                return visitor.visitChildren(self)




    def for_loop(self):

        localctx = MathLangParser.For_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_for_loop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(MathLangParser.FOR)
            self.state = 115
            self.match(MathLangParser.LPAREN)
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 144955670528) != 0):
                self.state = 116
                self.assignment()


            self.state = 119
            self.match(MathLangParser.SEMI)
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 273804231680) != 0):
                self.state = 120
                self.expression(0)


            self.state = 123
            self.match(MathLangParser.SEMI)
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 145088843776) != 0):
                self.state = 124
                self.statement()


            self.state = 127
            self.match(MathLangParser.RPAREN)
            self.state = 128
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(MathLangParser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(MathLangParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MathLangParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MathLangParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(MathLangParser.BlockContext,0)


        def getRuleIndex(self):
            return MathLangParser.RULE_while_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_loop" ):
                listener.enterWhile_loop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_loop" ):
                listener.exitWhile_loop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_loop" ):
                return visitor.visitWhile_loop(self)
            else:
                return visitor.visitChildren(self)




    def while_loop(self):

        localctx = MathLangParser.While_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_while_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(MathLangParser.WHILE)
            self.state = 131
            self.match(MathLangParser.LPAREN)
            self.state = 132
            self.expression(0)
            self.state = 133
            self.match(MathLangParser.RPAREN)
            self.state = 134
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Until_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UNTIL(self):
            return self.getToken(MathLangParser.UNTIL, 0)

        def LPAREN(self):
            return self.getToken(MathLangParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MathLangParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MathLangParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(MathLangParser.BlockContext,0)


        def getRuleIndex(self):
            return MathLangParser.RULE_until_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUntil_loop" ):
                listener.enterUntil_loop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUntil_loop" ):
                listener.exitUntil_loop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUntil_loop" ):
                return visitor.visitUntil_loop(self)
            else:
                return visitor.visitChildren(self)




    def until_loop(self):

        localctx = MathLangParser.Until_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_until_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(MathLangParser.UNTIL)
            self.state = 137
            self.match(MathLangParser.LPAREN)
            self.state = 138
            self.expression(0)
            self.state = 139
            self.match(MathLangParser.RPAREN)
            self.state = 140
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCURLY(self):
            return self.getToken(MathLangParser.LCURLY, 0)

        def RCURLY(self):
            return self.getToken(MathLangParser.RCURLY, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(MathLangParser.StatementContext,i)


        def getRuleIndex(self):
            return MathLangParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = MathLangParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.match(MathLangParser.LCURLY)
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 145088843776) != 0):
                self.state = 143
                self.statement()
                self.state = 148
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 149
            self.match(MathLangParser.RCURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MathLangParser.ID)
            else:
                return self.getToken(MathLangParser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MathLangParser.COMMA)
            else:
                return self.getToken(MathLangParser.COMMA, i)

        def getRuleIndex(self):
            return MathLangParser.RULE_id_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId_list" ):
                listener.enterId_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId_list" ):
                listener.exitId_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId_list" ):
                return visitor.visitId_list(self)
            else:
                return visitor.visitChildren(self)




    def id_list(self):

        localctx = MathLangParser.Id_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_id_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 151
                    self.match(MathLangParser.ID)
                    self.state = 152
                    self.match(MathLangParser.COMMA) 
                self.state = 157
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

            self.state = 158
            self.match(MathLangParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MathLangParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MathLangParser.COMMA)
            else:
                return self.getToken(MathLangParser.COMMA, i)

        def getRuleIndex(self):
            return MathLangParser.RULE_expression_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression_list" ):
                listener.enterExpression_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression_list" ):
                listener.exitExpression_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_list" ):
                return visitor.visitExpression_list(self)
            else:
                return visitor.visitChildren(self)




    def expression_list(self):

        localctx = MathLangParser.Expression_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_expression_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 160
                    self.expression(0)
                    self.state = 161
                    self.match(MathLangParser.COMMA) 
                self.state = 167
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

            self.state = 168
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MathLangParser.ID, 0)

        def literal(self):
            return self.getTypedRuleContext(MathLangParser.LiteralContext,0)


        def call(self):
            return self.getTypedRuleContext(MathLangParser.CallContext,0)


        def cast_expression(self):
            return self.getTypedRuleContext(MathLangParser.Cast_expressionContext,0)


        def unary_operator(self):
            return self.getTypedRuleContext(MathLangParser.Unary_operatorContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MathLangParser.ExpressionContext,i)


        def LPAREN(self):
            return self.getToken(MathLangParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MathLangParser.RPAREN, 0)

        def binary_operator(self):
            return self.getTypedRuleContext(MathLangParser.Binary_operatorContext,0)


        def getRuleIndex(self):
            return MathLangParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MathLangParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 171
                self.match(MathLangParser.ID)
                pass

            elif la_ == 2:
                self.state = 172
                self.literal()
                pass

            elif la_ == 3:
                self.state = 173
                self.call()
                pass

            elif la_ == 4:
                self.state = 174
                self.cast_expression()
                pass

            elif la_ == 5:
                self.state = 175
                self.unary_operator()
                self.state = 176
                self.expression(2)
                pass

            elif la_ == 6:
                self.state = 178
                self.match(MathLangParser.LPAREN)
                self.state = 179
                self.expression(0)
                self.state = 180
                self.match(MathLangParser.RPAREN)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 190
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MathLangParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 184
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 185
                    self.binary_operator()
                    self.state = 186
                    self.expression(4) 
                self.state = 192
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Cast_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_specifier(self):
            return self.getTypedRuleContext(MathLangParser.Type_specifierContext,0)


        def LPAREN(self):
            return self.getToken(MathLangParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MathLangParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MathLangParser.RPAREN, 0)

        def getRuleIndex(self):
            return MathLangParser.RULE_cast_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCast_expression" ):
                listener.enterCast_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCast_expression" ):
                listener.exitCast_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCast_expression" ):
                return visitor.visitCast_expression(self)
            else:
                return visitor.visitChildren(self)




    def cast_expression(self):

        localctx = MathLangParser.Cast_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_cast_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.type_specifier()
            self.state = 194
            self.match(MathLangParser.LPAREN)
            self.state = 195
            self.expression(0)
            self.state = 196
            self.match(MathLangParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simple_assignment_operator(self):
            return self.getTypedRuleContext(MathLangParser.Simple_assignment_operatorContext,0)


        def getRuleIndex(self):
            return MathLangParser.RULE_assignment_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment_operator" ):
                listener.enterAssignment_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment_operator" ):
                listener.exitAssignment_operator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_operator" ):
                return visitor.visitAssignment_operator(self)
            else:
                return visitor.visitChildren(self)




    def assignment_operator(self):

        localctx = MathLangParser.Assignment_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_assignment_operator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.simple_assignment_operator()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Simple_assignment_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(MathLangParser.EQ, 0)

        def getRuleIndex(self):
            return MathLangParser.RULE_simple_assignment_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimple_assignment_operator" ):
                listener.enterSimple_assignment_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimple_assignment_operator" ):
                listener.exitSimple_assignment_operator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimple_assignment_operator" ):
                return visitor.visitSimple_assignment_operator(self)
            else:
                return visitor.visitChildren(self)




    def simple_assignment_operator(self):

        localctx = MathLangParser.Simple_assignment_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_simple_assignment_operator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.match(MathLangParser.EQ)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Binary_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(MathLangParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(MathLangParser.MINUS, 0)

        def ASTERISK(self):
            return self.getToken(MathLangParser.ASTERISK, 0)

        def SLASH(self):
            return self.getToken(MathLangParser.SLASH, 0)

        def CARET(self):
            return self.getToken(MathLangParser.CARET, 0)

        def EQ(self, i:int=None):
            if i is None:
                return self.getTokens(MathLangParser.EQ)
            else:
                return self.getToken(MathLangParser.EQ, i)

        def OR(self):
            return self.getToken(MathLangParser.OR, 0)

        def AND(self):
            return self.getToken(MathLangParser.AND, 0)

        def NOT(self):
            return self.getToken(MathLangParser.NOT, 0)

        def GT(self):
            return self.getToken(MathLangParser.GT, 0)

        def LS(self):
            return self.getToken(MathLangParser.LS, 0)

        def getRuleIndex(self):
            return MathLangParser.RULE_binary_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinary_operator" ):
                listener.enterBinary_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinary_operator" ):
                listener.exitBinary_operator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinary_operator" ):
                return visitor.visitBinary_operator(self)
            else:
                return visitor.visitChildren(self)




    def binary_operator(self):

        localctx = MathLangParser.Binary_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_binary_operator)
        try:
            self.state = 218
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 202
                self.match(MathLangParser.PLUS)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 203
                self.match(MathLangParser.MINUS)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 204
                self.match(MathLangParser.ASTERISK)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 205
                self.match(MathLangParser.SLASH)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 206
                self.match(MathLangParser.CARET)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 207
                self.match(MathLangParser.EQ)
                self.state = 208
                self.match(MathLangParser.EQ)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 209
                self.match(MathLangParser.OR)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 210
                self.match(MathLangParser.AND)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 211
                self.match(MathLangParser.NOT)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 212
                self.match(MathLangParser.GT)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 213
                self.match(MathLangParser.LS)
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 214
                self.match(MathLangParser.GT)
                self.state = 215
                self.match(MathLangParser.EQ)
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 216
                self.match(MathLangParser.LS)
                self.state = 217
                self.match(MathLangParser.EQ)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Unary_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(MathLangParser.MINUS, 0)

        def getRuleIndex(self):
            return MathLangParser.RULE_unary_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnary_operator" ):
                listener.enterUnary_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnary_operator" ):
                listener.exitUnary_operator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnary_operator" ):
                return visitor.visitUnary_operator(self)
            else:
                return visitor.visitChildren(self)




    def unary_operator(self):

        localctx = MathLangParser.Unary_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_unary_operator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.match(MathLangParser.MINUS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Control_flow_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MathLangParser.RETURN, 0)

        def BREAK(self):
            return self.getToken(MathLangParser.BREAK, 0)

        def CONTINUE(self):
            return self.getToken(MathLangParser.CONTINUE, 0)

        def getRuleIndex(self):
            return MathLangParser.RULE_control_flow_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterControl_flow_operator" ):
                listener.enterControl_flow_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitControl_flow_operator" ):
                listener.exitControl_flow_operator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitControl_flow_operator" ):
                return visitor.visitControl_flow_operator(self)
            else:
                return visitor.visitChildren(self)




    def control_flow_operator(self):

        localctx = MathLangParser.Control_flow_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_control_flow_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 58720256) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MathLangParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MathLangParser.FLOAT, 0)

        def BOOL(self):
            return self.getToken(MathLangParser.BOOL, 0)

        def STRING(self):
            return self.getToken(MathLangParser.STRING, 0)

        def getRuleIndex(self):
            return MathLangParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = MathLangParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 128849018880) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declaration_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_specifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathLangParser.Type_specifierContext)
            else:
                return self.getTypedRuleContext(MathLangParser.Type_specifierContext,i)


        def variable_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathLangParser.Variable_declarationContext)
            else:
                return self.getTypedRuleContext(MathLangParser.Variable_declarationContext,i)


        def scope_modifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathLangParser.Scope_modifierContext)
            else:
                return self.getTypedRuleContext(MathLangParser.Scope_modifierContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MathLangParser.COMMA)
            else:
                return self.getToken(MathLangParser.COMMA, i)

        def getRuleIndex(self):
            return MathLangParser.RULE_declaration_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration_list" ):
                listener.enterDeclaration_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration_list" ):
                listener.exitDeclaration_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration_list" ):
                return visitor.visitDeclaration_list(self)
            else:
                return visitor.visitChildren(self)




    def declaration_list(self):

        localctx = MathLangParser.Declaration_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_declaration_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 226
                self.scope_modifier()


            self.state = 229
            self.type_specifier()
            self.state = 230
            self.variable_declaration()
            self.state = 241
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 231
                self.match(MathLangParser.COMMA)
                self.state = 233
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==19:
                    self.state = 232
                    self.scope_modifier()


                self.state = 236
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 7516192768) != 0):
                    self.state = 235
                    self.type_specifier()


                self.state = 238
                self.variable_declaration()
                self.state = 243
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MathLangParser.ID, 0)

        def simple_assignment_operator(self):
            return self.getTypedRuleContext(MathLangParser.Simple_assignment_operatorContext,0)


        def expression(self):
            return self.getTypedRuleContext(MathLangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MathLangParser.RULE_variable_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable_declaration" ):
                listener.enterVariable_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable_declaration" ):
                listener.exitVariable_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_declaration" ):
                return visitor.visitVariable_declaration(self)
            else:
                return visitor.visitChildren(self)




    def variable_declaration(self):

        localctx = MathLangParser.Variable_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_variable_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.match(MathLangParser.ID)
            self.state = 248
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 245
                self.simple_assignment_operator()
                self.state = 246
                self.expression(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_specifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT_T(self):
            return self.getToken(MathLangParser.FLOAT_T, 0)

        def INT_T(self):
            return self.getToken(MathLangParser.INT_T, 0)

        def BOOL_T(self):
            return self.getToken(MathLangParser.BOOL_T, 0)

        def getRuleIndex(self):
            return MathLangParser.RULE_type_specifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_specifier" ):
                listener.enterType_specifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_specifier" ):
                listener.exitType_specifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_specifier" ):
                return visitor.visitType_specifier(self)
            else:
                return visitor.visitChildren(self)




    def type_specifier(self):

        localctx = MathLangParser.Type_specifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_type_specifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7516192768) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Scope_modifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GLOBAL(self):
            return self.getToken(MathLangParser.GLOBAL, 0)

        def getRuleIndex(self):
            return MathLangParser.RULE_scope_modifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScope_modifier" ):
                listener.enterScope_modifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScope_modifier" ):
                listener.exitScope_modifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScope_modifier" ):
                return visitor.visitScope_modifier(self)
            else:
                return visitor.visitChildren(self)




    def scope_modifier(self):

        localctx = MathLangParser.Scope_modifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_scope_modifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self.match(MathLangParser.GLOBAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[14] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         




