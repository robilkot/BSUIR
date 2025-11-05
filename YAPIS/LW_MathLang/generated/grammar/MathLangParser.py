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
        4,1,42,259,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,1,0,5,0,48,8,0,10,0,12,0,51,9,0,1,0,5,0,
        54,8,0,10,0,12,0,57,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,3,1,67,8,
        1,1,2,1,2,1,2,1,2,3,2,73,8,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,3,3,85,8,3,1,4,1,4,3,4,89,8,4,1,4,1,4,1,4,1,5,3,5,95,8,5,1,5,
        1,5,1,5,1,5,1,5,1,5,5,5,103,8,5,10,5,12,5,106,9,5,1,6,1,6,1,6,1,
        6,3,6,112,8,6,1,7,1,7,1,7,3,7,117,8,7,1,7,1,7,1,8,1,8,1,8,3,8,124,
        8,8,1,9,1,9,1,9,3,9,129,8,9,1,9,1,9,3,9,133,8,9,1,9,1,9,3,9,137,
        8,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,
        1,11,1,11,1,12,1,12,5,12,156,8,12,10,12,12,12,159,9,12,1,12,1,12,
        1,13,1,13,5,13,165,8,13,10,13,12,13,168,9,13,1,13,1,13,1,14,1,14,
        1,14,5,14,175,8,14,10,14,12,14,178,9,14,1,14,1,14,1,15,1,15,1,15,
        1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,3,15,195,8,15,
        1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,5,15,237,8,15,10,15,12,15,240,9,15,1,16,1,16,1,16,1,16,1,16,
        1,17,1,17,1,18,1,18,1,19,1,19,1,20,1,20,1,21,1,21,1,22,1,22,1,22,
        0,1,30,23,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,
        40,42,44,0,3,1,0,26,28,1,0,36,39,1,0,33,35,276,0,49,1,0,0,0,2,66,
        1,0,0,0,4,68,1,0,0,0,6,77,1,0,0,0,8,88,1,0,0,0,10,94,1,0,0,0,12,
        107,1,0,0,0,14,113,1,0,0,0,16,123,1,0,0,0,18,125,1,0,0,0,20,141,
        1,0,0,0,22,147,1,0,0,0,24,153,1,0,0,0,26,166,1,0,0,0,28,176,1,0,
        0,0,30,194,1,0,0,0,32,241,1,0,0,0,34,246,1,0,0,0,36,248,1,0,0,0,
        38,250,1,0,0,0,40,252,1,0,0,0,42,254,1,0,0,0,44,256,1,0,0,0,46,48,
        3,4,2,0,47,46,1,0,0,0,48,51,1,0,0,0,49,47,1,0,0,0,49,50,1,0,0,0,
        50,55,1,0,0,0,51,49,1,0,0,0,52,54,3,2,1,0,53,52,1,0,0,0,54,57,1,
        0,0,0,55,53,1,0,0,0,55,56,1,0,0,0,56,58,1,0,0,0,57,55,1,0,0,0,58,
        59,5,0,0,1,59,1,1,0,0,0,60,67,3,38,19,0,61,67,3,24,12,0,62,67,3,
        6,3,0,63,67,3,16,8,0,64,67,3,8,4,0,65,67,3,14,7,0,66,60,1,0,0,0,
        66,61,1,0,0,0,66,62,1,0,0,0,66,63,1,0,0,0,66,64,1,0,0,0,66,65,1,
        0,0,0,67,3,1,0,0,0,68,69,5,31,0,0,69,70,5,40,0,0,70,72,5,13,0,0,
        71,73,3,10,5,0,72,71,1,0,0,0,72,73,1,0,0,0,73,74,1,0,0,0,74,75,5,
        14,0,0,75,76,3,24,12,0,76,5,1,0,0,0,77,78,5,29,0,0,78,79,5,13,0,
        0,79,80,3,30,15,0,80,81,5,14,0,0,81,84,3,24,12,0,82,83,5,30,0,0,
        83,85,3,24,12,0,84,82,1,0,0,0,84,85,1,0,0,0,85,7,1,0,0,0,86,89,3,
        10,5,0,87,89,3,26,13,0,88,86,1,0,0,0,88,87,1,0,0,0,89,90,1,0,0,0,
        90,91,3,34,17,0,91,92,3,28,14,0,92,9,1,0,0,0,93,95,3,44,22,0,94,
        93,1,0,0,0,94,95,1,0,0,0,95,96,1,0,0,0,96,97,3,42,21,0,97,104,3,
        12,6,0,98,99,5,10,0,0,99,100,3,42,21,0,100,101,3,12,6,0,101,103,
        1,0,0,0,102,98,1,0,0,0,103,106,1,0,0,0,104,102,1,0,0,0,104,105,1,
        0,0,0,105,11,1,0,0,0,106,104,1,0,0,0,107,111,5,40,0,0,108,109,3,
        36,18,0,109,110,3,30,15,0,110,112,1,0,0,0,111,108,1,0,0,0,111,112,
        1,0,0,0,112,13,1,0,0,0,113,114,5,40,0,0,114,116,5,13,0,0,115,117,
        3,28,14,0,116,115,1,0,0,0,116,117,1,0,0,0,117,118,1,0,0,0,118,119,
        5,14,0,0,119,15,1,0,0,0,120,124,3,18,9,0,121,124,3,20,10,0,122,124,
        3,22,11,0,123,120,1,0,0,0,123,121,1,0,0,0,123,122,1,0,0,0,124,17,
        1,0,0,0,125,126,5,23,0,0,126,128,5,13,0,0,127,129,3,8,4,0,128,127,
        1,0,0,0,128,129,1,0,0,0,129,130,1,0,0,0,130,132,5,11,0,0,131,133,
        3,30,15,0,132,131,1,0,0,0,132,133,1,0,0,0,133,134,1,0,0,0,134,136,
        5,11,0,0,135,137,3,2,1,0,136,135,1,0,0,0,136,137,1,0,0,0,137,138,
        1,0,0,0,138,139,5,14,0,0,139,140,3,24,12,0,140,19,1,0,0,0,141,142,
        5,24,0,0,142,143,5,13,0,0,143,144,3,30,15,0,144,145,5,14,0,0,145,
        146,3,24,12,0,146,21,1,0,0,0,147,148,5,25,0,0,148,149,5,13,0,0,149,
        150,3,30,15,0,150,151,5,14,0,0,151,152,3,24,12,0,152,23,1,0,0,0,
        153,157,5,15,0,0,154,156,3,2,1,0,155,154,1,0,0,0,156,159,1,0,0,0,
        157,155,1,0,0,0,157,158,1,0,0,0,158,160,1,0,0,0,159,157,1,0,0,0,
        160,161,5,16,0,0,161,25,1,0,0,0,162,163,5,40,0,0,163,165,5,10,0,
        0,164,162,1,0,0,0,165,168,1,0,0,0,166,164,1,0,0,0,166,167,1,0,0,
        0,167,169,1,0,0,0,168,166,1,0,0,0,169,170,5,40,0,0,170,27,1,0,0,
        0,171,172,3,30,15,0,172,173,5,10,0,0,173,175,1,0,0,0,174,171,1,0,
        0,0,175,178,1,0,0,0,176,174,1,0,0,0,176,177,1,0,0,0,177,179,1,0,
        0,0,178,176,1,0,0,0,179,180,3,30,15,0,180,29,1,0,0,0,181,182,6,15,
        -1,0,182,195,5,40,0,0,183,195,3,40,20,0,184,195,3,14,7,0,185,195,
        3,32,16,0,186,187,5,13,0,0,187,188,3,30,15,0,188,189,5,14,0,0,189,
        195,1,0,0,0,190,191,5,3,0,0,191,195,3,30,15,15,192,193,5,19,0,0,
        193,195,3,30,15,14,194,181,1,0,0,0,194,183,1,0,0,0,194,184,1,0,0,
        0,194,185,1,0,0,0,194,186,1,0,0,0,194,190,1,0,0,0,194,192,1,0,0,
        0,195,238,1,0,0,0,196,197,10,13,0,0,197,198,5,21,0,0,198,237,3,30,
        15,14,199,200,10,12,0,0,200,201,5,20,0,0,201,237,3,30,15,13,202,
        203,10,11,0,0,203,204,5,17,0,0,204,237,3,30,15,12,205,206,10,10,
        0,0,206,207,5,18,0,0,207,237,3,30,15,11,208,209,10,9,0,0,209,210,
        5,19,0,0,210,237,3,30,15,10,211,212,10,8,0,0,212,213,5,1,0,0,213,
        237,3,30,15,9,214,215,10,7,0,0,215,216,5,2,0,0,216,237,3,30,15,8,
        217,218,10,6,0,0,218,219,5,4,0,0,219,220,5,4,0,0,220,237,3,30,15,
        7,221,222,10,5,0,0,222,223,5,5,0,0,223,237,3,30,15,6,224,225,10,
        4,0,0,225,226,5,6,0,0,226,237,3,30,15,5,227,228,10,3,0,0,228,229,
        5,7,0,0,229,237,3,30,15,4,230,231,10,2,0,0,231,232,5,8,0,0,232,237,
        3,30,15,3,233,234,10,1,0,0,234,235,5,9,0,0,235,237,3,30,15,2,236,
        196,1,0,0,0,236,199,1,0,0,0,236,202,1,0,0,0,236,205,1,0,0,0,236,
        208,1,0,0,0,236,211,1,0,0,0,236,214,1,0,0,0,236,217,1,0,0,0,236,
        221,1,0,0,0,236,224,1,0,0,0,236,227,1,0,0,0,236,230,1,0,0,0,236,
        233,1,0,0,0,237,240,1,0,0,0,238,236,1,0,0,0,238,239,1,0,0,0,239,
        31,1,0,0,0,240,238,1,0,0,0,241,242,3,42,21,0,242,243,5,13,0,0,243,
        244,3,30,15,0,244,245,5,14,0,0,245,33,1,0,0,0,246,247,3,36,18,0,
        247,35,1,0,0,0,248,249,5,4,0,0,249,37,1,0,0,0,250,251,7,0,0,0,251,
        39,1,0,0,0,252,253,7,1,0,0,253,41,1,0,0,0,254,255,7,2,0,0,255,43,
        1,0,0,0,256,257,5,22,0,0,257,45,1,0,0,0,20,49,55,66,72,84,88,94,
        104,111,116,123,128,132,136,157,166,176,194,236,238
    ]

class MathLangParser ( Parser ):

    grammarFileName = "MathLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'and'", "'or'", "'not'", "'='", "'!='", 
                     "'>'", "'<'", "'>='", "'<='", "','", "';'", "':'", 
                     "'('", "')'", "'{'", "'}'", "'/'", "'+'", "'-'", "'*'", 
                     "'^'", "'global'", "'for'", "'while'", "'until'", "'break'", 
                     "'continue'", "'return'", "'if'", "'else'", "'sub'", 
                     "<INVALID>", "'float'", "'int'", "'bool'" ]

    symbolicNames = [ "<INVALID>", "AND", "OR", "NOT", "EQ", "NEQ", "GT", 
                      "LT", "GE", "LE", "COMMA", "SEMI", "COLON", "LPAREN", 
                      "RPAREN", "LCURLY", "RCURLY", "SLASH", "PLUS", "MINUS", 
                      "ASTERISK", "CARET", "GLOBAL", "FOR", "WHILE", "UNTIL", 
                      "BREAK", "CONTINUE", "RETURN", "IF", "ELSE", "SUB", 
                      "DSLASH", "FLOAT_T", "INT_T", "BOOL_T", "INT", "FLOAT", 
                      "BOOL", "STRING", "ID", "LINE_COMMENT", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_subprogram = 2
    RULE_branching = 3
    RULE_assignment = 4
    RULE_declaration_list = 5
    RULE_variable_declaration = 6
    RULE_call = 7
    RULE_loop = 8
    RULE_for_loop = 9
    RULE_while_loop = 10
    RULE_until_loop = 11
    RULE_block = 12
    RULE_id_list = 13
    RULE_expression_list = 14
    RULE_expression = 15
    RULE_cast_expression = 16
    RULE_assignment_operator = 17
    RULE_simple_assignment_operator = 18
    RULE_control_flow_operator = 19
    RULE_literal = 20
    RULE_type_specifier = 21
    RULE_scope_modifier = 22

    ruleNames =  [ "program", "statement", "subprogram", "branching", "assignment", 
                   "declaration_list", "variable_declaration", "call", "loop", 
                   "for_loop", "while_loop", "until_loop", "block", "id_list", 
                   "expression_list", "expression", "cast_expression", "assignment_operator", 
                   "simple_assignment_operator", "control_flow_operator", 
                   "literal", "type_specifier", "scope_modifier" ]

    EOF = Token.EOF
    AND=1
    OR=2
    NOT=3
    EQ=4
    NEQ=5
    GT=6
    LT=7
    GE=8
    LE=9
    COMMA=10
    SEMI=11
    COLON=12
    LPAREN=13
    RPAREN=14
    LCURLY=15
    RCURLY=16
    SLASH=17
    PLUS=18
    MINUS=19
    ASTERISK=20
    CARET=21
    GLOBAL=22
    FOR=23
    WHILE=24
    UNTIL=25
    BREAK=26
    CONTINUE=27
    RETURN=28
    IF=29
    ELSE=30
    SUB=31
    DSLASH=32
    FLOAT_T=33
    INT_T=34
    BOOL_T=35
    INT=36
    FLOAT=37
    BOOL=38
    STRING=39
    ID=40
    LINE_COMMENT=41
    WS=42

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
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==31:
                self.state = 46
                self.subprogram()
                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1160710750208) != 0):
                self.state = 52
                self.statement()
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 58
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
            self.state = 66
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 60
                self.control_flow_operator()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 61
                self.block()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 62
                self.branching()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 63
                self.loop()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 64
                self.assignment()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 65
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
            self.state = 68
            self.match(MathLangParser.SUB)
            self.state = 69
            self.match(MathLangParser.ID)
            self.state = 70
            self.match(MathLangParser.LPAREN)
            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 60133736448) != 0):
                self.state = 71
                self.declaration_list()


            self.state = 74
            self.match(MathLangParser.RPAREN)
            self.state = 75
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
            self.state = 77
            self.match(MathLangParser.IF)
            self.state = 78
            self.match(MathLangParser.LPAREN)
            self.state = 79
            self.expression(0)
            self.state = 80
            self.match(MathLangParser.RPAREN)
            self.state = 81
            self.block()
            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 82
                self.match(MathLangParser.ELSE)
                self.state = 83
                self.block()


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
        self.enterRule(localctx, 8, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22, 33, 34, 35]:
                self.state = 86
                self.declaration_list()
                pass
            elif token in [40]:
                self.state = 87
                self.id_list()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 90
            self.assignment_operator()
            self.state = 91
            self.expression_list()
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


        def scope_modifier(self):
            return self.getTypedRuleContext(MathLangParser.Scope_modifierContext,0)


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
        self.enterRule(localctx, 10, self.RULE_declaration_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22:
                self.state = 93
                self.scope_modifier()


            self.state = 96
            self.type_specifier()
            self.state = 97
            self.variable_declaration()
            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 98
                self.match(MathLangParser.COMMA)
                self.state = 99
                self.type_specifier()
                self.state = 100
                self.variable_declaration()
                self.state = 106
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
        self.enterRule(localctx, 12, self.RULE_variable_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(MathLangParser.ID)
            self.state = 111
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 108
                self.simple_assignment_operator()
                self.state = 109
                self.expression(0)


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
        self.enterRule(localctx, 14, self.RULE_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(MathLangParser.ID)
            self.state = 114
            self.match(MathLangParser.LPAREN)
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2190433853448) != 0):
                self.state = 115
                self.expression_list()


            self.state = 118
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
        self.enterRule(localctx, 16, self.RULE_loop)
        try:
            self.state = 123
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23]:
                self.enterOuterAlt(localctx, 1)
                self.state = 120
                self.for_loop()
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 2)
                self.state = 121
                self.while_loop()
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 3)
                self.state = 122
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
        self.enterRule(localctx, 18, self.RULE_for_loop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.match(MathLangParser.FOR)
            self.state = 126
            self.match(MathLangParser.LPAREN)
            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1159645364224) != 0):
                self.state = 127
                self.assignment()


            self.state = 130
            self.match(MathLangParser.SEMI)
            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2190433853448) != 0):
                self.state = 131
                self.expression(0)


            self.state = 134
            self.match(MathLangParser.SEMI)
            self.state = 136
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1160710750208) != 0):
                self.state = 135
                self.statement()


            self.state = 138
            self.match(MathLangParser.RPAREN)
            self.state = 139
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
        self.enterRule(localctx, 20, self.RULE_while_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(MathLangParser.WHILE)
            self.state = 142
            self.match(MathLangParser.LPAREN)
            self.state = 143
            self.expression(0)
            self.state = 144
            self.match(MathLangParser.RPAREN)
            self.state = 145
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
        self.enterRule(localctx, 22, self.RULE_until_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(MathLangParser.UNTIL)
            self.state = 148
            self.match(MathLangParser.LPAREN)
            self.state = 149
            self.expression(0)
            self.state = 150
            self.match(MathLangParser.RPAREN)
            self.state = 151
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
        self.enterRule(localctx, 24, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(MathLangParser.LCURLY)
            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1160710750208) != 0):
                self.state = 154
                self.statement()
                self.state = 159
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 160
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
        self.enterRule(localctx, 26, self.RULE_id_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 162
                    self.match(MathLangParser.ID)
                    self.state = 163
                    self.match(MathLangParser.COMMA) 
                self.state = 168
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

            self.state = 169
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
        self.enterRule(localctx, 28, self.RULE_expression_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 171
                    self.expression(0)
                    self.state = 172
                    self.match(MathLangParser.COMMA) 
                self.state = 178
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

            self.state = 179
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


        def LPAREN(self):
            return self.getToken(MathLangParser.LPAREN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MathLangParser.ExpressionContext,i)


        def RPAREN(self):
            return self.getToken(MathLangParser.RPAREN, 0)

        def NOT(self):
            return self.getToken(MathLangParser.NOT, 0)

        def MINUS(self):
            return self.getToken(MathLangParser.MINUS, 0)

        def CARET(self):
            return self.getToken(MathLangParser.CARET, 0)

        def ASTERISK(self):
            return self.getToken(MathLangParser.ASTERISK, 0)

        def SLASH(self):
            return self.getToken(MathLangParser.SLASH, 0)

        def PLUS(self):
            return self.getToken(MathLangParser.PLUS, 0)

        def AND(self):
            return self.getToken(MathLangParser.AND, 0)

        def OR(self):
            return self.getToken(MathLangParser.OR, 0)

        def EQ(self, i:int=None):
            if i is None:
                return self.getTokens(MathLangParser.EQ)
            else:
                return self.getToken(MathLangParser.EQ, i)

        def NEQ(self):
            return self.getToken(MathLangParser.NEQ, 0)

        def GT(self):
            return self.getToken(MathLangParser.GT, 0)

        def LT(self):
            return self.getToken(MathLangParser.LT, 0)

        def GE(self):
            return self.getToken(MathLangParser.GE, 0)

        def LE(self):
            return self.getToken(MathLangParser.LE, 0)

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
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 182
                self.match(MathLangParser.ID)
                pass

            elif la_ == 2:
                self.state = 183
                self.literal()
                pass

            elif la_ == 3:
                self.state = 184
                self.call()
                pass

            elif la_ == 4:
                self.state = 185
                self.cast_expression()
                pass

            elif la_ == 5:
                self.state = 186
                self.match(MathLangParser.LPAREN)
                self.state = 187
                self.expression(0)
                self.state = 188
                self.match(MathLangParser.RPAREN)
                pass

            elif la_ == 6:
                self.state = 190
                self.match(MathLangParser.NOT)
                self.state = 191
                self.expression(15)
                pass

            elif la_ == 7:
                self.state = 192
                self.match(MathLangParser.MINUS)
                self.state = 193
                self.expression(14)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 238
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 236
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                    if la_ == 1:
                        localctx = MathLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 196
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 197
                        self.match(MathLangParser.CARET)
                        self.state = 198
                        self.expression(14)
                        pass

                    elif la_ == 2:
                        localctx = MathLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 199
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 200
                        self.match(MathLangParser.ASTERISK)
                        self.state = 201
                        self.expression(13)
                        pass

                    elif la_ == 3:
                        localctx = MathLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 202
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 203
                        self.match(MathLangParser.SLASH)
                        self.state = 204
                        self.expression(12)
                        pass

                    elif la_ == 4:
                        localctx = MathLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 205
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 206
                        self.match(MathLangParser.PLUS)
                        self.state = 207
                        self.expression(11)
                        pass

                    elif la_ == 5:
                        localctx = MathLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 208
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 209
                        self.match(MathLangParser.MINUS)
                        self.state = 210
                        self.expression(10)
                        pass

                    elif la_ == 6:
                        localctx = MathLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 211
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 212
                        self.match(MathLangParser.AND)
                        self.state = 213
                        self.expression(9)
                        pass

                    elif la_ == 7:
                        localctx = MathLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 214
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 215
                        self.match(MathLangParser.OR)
                        self.state = 216
                        self.expression(8)
                        pass

                    elif la_ == 8:
                        localctx = MathLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 217
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 218
                        self.match(MathLangParser.EQ)
                        self.state = 219
                        self.match(MathLangParser.EQ)
                        self.state = 220
                        self.expression(7)
                        pass

                    elif la_ == 9:
                        localctx = MathLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 221
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 222
                        self.match(MathLangParser.NEQ)
                        self.state = 223
                        self.expression(6)
                        pass

                    elif la_ == 10:
                        localctx = MathLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 224
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 225
                        self.match(MathLangParser.GT)
                        self.state = 226
                        self.expression(5)
                        pass

                    elif la_ == 11:
                        localctx = MathLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 227
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 228
                        self.match(MathLangParser.LT)
                        self.state = 229
                        self.expression(4)
                        pass

                    elif la_ == 12:
                        localctx = MathLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 230
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 231
                        self.match(MathLangParser.GE)
                        self.state = 232
                        self.expression(3)
                        pass

                    elif la_ == 13:
                        localctx = MathLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 233
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 234
                        self.match(MathLangParser.LE)
                        self.state = 235
                        self.expression(2)
                        pass

             
                self.state = 240
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

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
        self.enterRule(localctx, 32, self.RULE_cast_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.type_specifier()
            self.state = 242
            self.match(MathLangParser.LPAREN)
            self.state = 243
            self.expression(0)
            self.state = 244
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
        self.enterRule(localctx, 34, self.RULE_assignment_operator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
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
        self.enterRule(localctx, 36, self.RULE_simple_assignment_operator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.match(MathLangParser.EQ)
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
        self.enterRule(localctx, 38, self.RULE_control_flow_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 469762048) != 0)):
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
        self.enterRule(localctx, 40, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1030792151040) != 0)):
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
        self.enterRule(localctx, 42, self.RULE_type_specifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 60129542144) != 0)):
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
        self.enterRule(localctx, 44, self.RULE_scope_modifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
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
        self._predicates[15] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 1)
         




