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
        4,1,42,281,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,1,0,5,0,52,8,0,10,0,
        12,0,55,9,0,1,0,5,0,58,8,0,10,0,12,0,61,9,0,1,0,1,0,1,1,1,1,1,1,
        1,1,1,1,1,1,3,1,71,8,1,1,2,1,2,1,2,3,2,76,8,2,1,2,1,2,3,2,80,8,2,
        1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,96,8,
        4,1,5,1,5,3,5,100,8,5,1,5,1,5,1,5,1,6,3,6,106,8,6,1,6,1,6,1,6,1,
        6,1,6,1,6,5,6,114,8,6,10,6,12,6,117,9,6,1,7,1,7,1,7,1,7,3,7,123,
        8,7,1,8,1,8,3,8,127,8,8,1,8,1,8,3,8,131,8,8,1,8,1,8,1,9,1,9,1,9,
        3,9,138,8,9,1,10,1,10,1,10,3,10,143,8,10,1,10,1,10,3,10,147,8,10,
        1,10,1,10,3,10,151,8,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,
        1,11,1,12,1,12,1,12,1,12,1,12,1,12,1,13,1,13,5,13,170,8,13,10,13,
        12,13,173,9,13,1,13,1,13,1,14,1,14,5,14,179,8,14,10,14,12,14,182,
        9,14,1,14,1,14,1,15,1,15,1,15,5,15,189,8,15,10,15,12,15,192,9,15,
        1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,3,16,209,8,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,5,16,251,8,16,10,16,12,16,254,9,16,
        1,17,1,17,1,17,1,17,1,17,1,18,1,18,1,19,1,19,1,20,1,20,1,21,1,21,
        1,22,1,22,1,23,1,23,1,23,5,23,274,8,23,10,23,12,23,277,9,23,1,24,
        1,24,1,24,0,1,32,25,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,
        34,36,38,40,42,44,46,48,0,3,1,0,26,28,1,0,36,39,2,0,33,35,40,40,
        299,0,53,1,0,0,0,2,70,1,0,0,0,4,72,1,0,0,0,6,84,1,0,0,0,8,88,1,0,
        0,0,10,99,1,0,0,0,12,105,1,0,0,0,14,118,1,0,0,0,16,124,1,0,0,0,18,
        137,1,0,0,0,20,139,1,0,0,0,22,155,1,0,0,0,24,161,1,0,0,0,26,167,
        1,0,0,0,28,180,1,0,0,0,30,190,1,0,0,0,32,208,1,0,0,0,34,255,1,0,
        0,0,36,260,1,0,0,0,38,262,1,0,0,0,40,264,1,0,0,0,42,266,1,0,0,0,
        44,268,1,0,0,0,46,270,1,0,0,0,48,278,1,0,0,0,50,52,3,4,2,0,51,50,
        1,0,0,0,52,55,1,0,0,0,53,51,1,0,0,0,53,54,1,0,0,0,54,59,1,0,0,0,
        55,53,1,0,0,0,56,58,3,2,1,0,57,56,1,0,0,0,58,61,1,0,0,0,59,57,1,
        0,0,0,59,60,1,0,0,0,60,62,1,0,0,0,61,59,1,0,0,0,62,63,5,0,0,1,63,
        1,1,0,0,0,64,71,3,40,20,0,65,71,3,26,13,0,66,71,3,8,4,0,67,71,3,
        18,9,0,68,71,3,10,5,0,69,71,3,16,8,0,70,64,1,0,0,0,70,65,1,0,0,0,
        70,66,1,0,0,0,70,67,1,0,0,0,70,68,1,0,0,0,70,69,1,0,0,0,71,3,1,0,
        0,0,72,73,5,31,0,0,73,75,5,40,0,0,74,76,3,6,3,0,75,74,1,0,0,0,75,
        76,1,0,0,0,76,77,1,0,0,0,77,79,5,13,0,0,78,80,3,12,6,0,79,78,1,0,
        0,0,79,80,1,0,0,0,80,81,1,0,0,0,81,82,5,14,0,0,82,83,3,26,13,0,83,
        5,1,0,0,0,84,85,5,7,0,0,85,86,3,46,23,0,86,87,5,6,0,0,87,7,1,0,0,
        0,88,89,5,29,0,0,89,90,5,13,0,0,90,91,3,32,16,0,91,92,5,14,0,0,92,
        95,3,26,13,0,93,94,5,30,0,0,94,96,3,26,13,0,95,93,1,0,0,0,95,96,
        1,0,0,0,96,9,1,0,0,0,97,100,3,12,6,0,98,100,3,28,14,0,99,97,1,0,
        0,0,99,98,1,0,0,0,100,101,1,0,0,0,101,102,3,36,18,0,102,103,3,30,
        15,0,103,11,1,0,0,0,104,106,3,48,24,0,105,104,1,0,0,0,105,106,1,
        0,0,0,106,107,1,0,0,0,107,108,3,44,22,0,108,115,3,14,7,0,109,110,
        5,10,0,0,110,111,3,44,22,0,111,112,3,14,7,0,112,114,1,0,0,0,113,
        109,1,0,0,0,114,117,1,0,0,0,115,113,1,0,0,0,115,116,1,0,0,0,116,
        13,1,0,0,0,117,115,1,0,0,0,118,122,5,40,0,0,119,120,3,38,19,0,120,
        121,3,32,16,0,121,123,1,0,0,0,122,119,1,0,0,0,122,123,1,0,0,0,123,
        15,1,0,0,0,124,126,5,40,0,0,125,127,3,6,3,0,126,125,1,0,0,0,126,
        127,1,0,0,0,127,128,1,0,0,0,128,130,5,13,0,0,129,131,3,30,15,0,130,
        129,1,0,0,0,130,131,1,0,0,0,131,132,1,0,0,0,132,133,5,14,0,0,133,
        17,1,0,0,0,134,138,3,20,10,0,135,138,3,22,11,0,136,138,3,24,12,0,
        137,134,1,0,0,0,137,135,1,0,0,0,137,136,1,0,0,0,138,19,1,0,0,0,139,
        140,5,23,0,0,140,142,5,13,0,0,141,143,3,10,5,0,142,141,1,0,0,0,142,
        143,1,0,0,0,143,144,1,0,0,0,144,146,5,11,0,0,145,147,3,32,16,0,146,
        145,1,0,0,0,146,147,1,0,0,0,147,148,1,0,0,0,148,150,5,11,0,0,149,
        151,3,2,1,0,150,149,1,0,0,0,150,151,1,0,0,0,151,152,1,0,0,0,152,
        153,5,14,0,0,153,154,3,26,13,0,154,21,1,0,0,0,155,156,5,24,0,0,156,
        157,5,13,0,0,157,158,3,32,16,0,158,159,5,14,0,0,159,160,3,26,13,
        0,160,23,1,0,0,0,161,162,5,25,0,0,162,163,5,13,0,0,163,164,3,32,
        16,0,164,165,5,14,0,0,165,166,3,26,13,0,166,25,1,0,0,0,167,171,5,
        15,0,0,168,170,3,2,1,0,169,168,1,0,0,0,170,173,1,0,0,0,171,169,1,
        0,0,0,171,172,1,0,0,0,172,174,1,0,0,0,173,171,1,0,0,0,174,175,5,
        16,0,0,175,27,1,0,0,0,176,177,5,40,0,0,177,179,5,10,0,0,178,176,
        1,0,0,0,179,182,1,0,0,0,180,178,1,0,0,0,180,181,1,0,0,0,181,183,
        1,0,0,0,182,180,1,0,0,0,183,184,5,40,0,0,184,29,1,0,0,0,185,186,
        3,32,16,0,186,187,5,10,0,0,187,189,1,0,0,0,188,185,1,0,0,0,189,192,
        1,0,0,0,190,188,1,0,0,0,190,191,1,0,0,0,191,193,1,0,0,0,192,190,
        1,0,0,0,193,194,3,32,16,0,194,31,1,0,0,0,195,196,6,16,-1,0,196,209,
        5,40,0,0,197,209,3,42,21,0,198,209,3,16,8,0,199,209,3,34,17,0,200,
        201,5,13,0,0,201,202,3,32,16,0,202,203,5,14,0,0,203,209,1,0,0,0,
        204,205,5,3,0,0,205,209,3,32,16,15,206,207,5,19,0,0,207,209,3,32,
        16,14,208,195,1,0,0,0,208,197,1,0,0,0,208,198,1,0,0,0,208,199,1,
        0,0,0,208,200,1,0,0,0,208,204,1,0,0,0,208,206,1,0,0,0,209,252,1,
        0,0,0,210,211,10,13,0,0,211,212,5,21,0,0,212,251,3,32,16,14,213,
        214,10,12,0,0,214,215,5,20,0,0,215,251,3,32,16,13,216,217,10,11,
        0,0,217,218,5,17,0,0,218,251,3,32,16,12,219,220,10,10,0,0,220,221,
        5,18,0,0,221,251,3,32,16,11,222,223,10,9,0,0,223,224,5,19,0,0,224,
        251,3,32,16,10,225,226,10,8,0,0,226,227,5,1,0,0,227,251,3,32,16,
        9,228,229,10,7,0,0,229,230,5,2,0,0,230,251,3,32,16,8,231,232,10,
        6,0,0,232,233,5,4,0,0,233,234,5,4,0,0,234,251,3,32,16,7,235,236,
        10,5,0,0,236,237,5,5,0,0,237,251,3,32,16,6,238,239,10,4,0,0,239,
        240,5,6,0,0,240,251,3,32,16,5,241,242,10,3,0,0,242,243,5,7,0,0,243,
        251,3,32,16,4,244,245,10,2,0,0,245,246,5,8,0,0,246,251,3,32,16,3,
        247,248,10,1,0,0,248,249,5,9,0,0,249,251,3,32,16,2,250,210,1,0,0,
        0,250,213,1,0,0,0,250,216,1,0,0,0,250,219,1,0,0,0,250,222,1,0,0,
        0,250,225,1,0,0,0,250,228,1,0,0,0,250,231,1,0,0,0,250,235,1,0,0,
        0,250,238,1,0,0,0,250,241,1,0,0,0,250,244,1,0,0,0,250,247,1,0,0,
        0,251,254,1,0,0,0,252,250,1,0,0,0,252,253,1,0,0,0,253,33,1,0,0,0,
        254,252,1,0,0,0,255,256,3,44,22,0,256,257,5,13,0,0,257,258,3,32,
        16,0,258,259,5,14,0,0,259,35,1,0,0,0,260,261,3,38,19,0,261,37,1,
        0,0,0,262,263,5,4,0,0,263,39,1,0,0,0,264,265,7,0,0,0,265,41,1,0,
        0,0,266,267,7,1,0,0,267,43,1,0,0,0,268,269,7,2,0,0,269,45,1,0,0,
        0,270,275,3,44,22,0,271,272,5,10,0,0,272,274,3,44,22,0,273,271,1,
        0,0,0,274,277,1,0,0,0,275,273,1,0,0,0,275,276,1,0,0,0,276,47,1,0,
        0,0,277,275,1,0,0,0,278,279,5,22,0,0,279,49,1,0,0,0,23,53,59,70,
        75,79,95,99,105,115,122,126,130,137,142,146,150,171,180,190,208,
        250,252,275
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
    RULE_template = 3
    RULE_branching = 4
    RULE_assignment = 5
    RULE_declaration_list = 6
    RULE_variable_declaration = 7
    RULE_call = 8
    RULE_loop = 9
    RULE_for_loop = 10
    RULE_while_loop = 11
    RULE_until_loop = 12
    RULE_block = 13
    RULE_id_list = 14
    RULE_expression_list = 15
    RULE_expression = 16
    RULE_cast_expression = 17
    RULE_assignment_operator = 18
    RULE_simple_assignment_operator = 19
    RULE_control_flow_operator = 20
    RULE_literal = 21
    RULE_type_specifier = 22
    RULE_type_specifier_list = 23
    RULE_scope_modifier = 24

    ruleNames =  [ "program", "statement", "subprogram", "template", "branching", 
                   "assignment", "declaration_list", "variable_declaration", 
                   "call", "loop", "for_loop", "while_loop", "until_loop", 
                   "block", "id_list", "expression_list", "expression", 
                   "cast_expression", "assignment_operator", "simple_assignment_operator", 
                   "control_flow_operator", "literal", "type_specifier", 
                   "type_specifier_list", "scope_modifier" ]

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
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==31:
                self.state = 50
                self.subprogram()
                self.state = 55
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1160710750208) != 0):
                self.state = 56
                self.statement()
                self.state = 61
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 62
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
            self.state = 70
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 64
                self.control_flow_operator()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 65
                self.block()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 66
                self.branching()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 67
                self.loop()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 68
                self.assignment()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 69
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


        def template(self):
            return self.getTypedRuleContext(MathLangParser.TemplateContext,0)


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
            self.state = 72
            self.match(MathLangParser.SUB)
            self.state = 73
            self.match(MathLangParser.ID)
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 74
                self.template()


            self.state = 77
            self.match(MathLangParser.LPAREN)
            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1159645364224) != 0):
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


    class TemplateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LT(self):
            return self.getToken(MathLangParser.LT, 0)

        def type_specifier_list(self):
            return self.getTypedRuleContext(MathLangParser.Type_specifier_listContext,0)


        def GT(self):
            return self.getToken(MathLangParser.GT, 0)

        def getRuleIndex(self):
            return MathLangParser.RULE_template

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTemplate" ):
                listener.enterTemplate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTemplate" ):
                listener.exitTemplate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTemplate" ):
                return visitor.visitTemplate(self)
            else:
                return visitor.visitChildren(self)




    def template(self):

        localctx = MathLangParser.TemplateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_template)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(MathLangParser.LT)
            self.state = 85
            self.type_specifier_list()
            self.state = 86
            self.match(MathLangParser.GT)
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
        self.enterRule(localctx, 8, self.RULE_branching)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(MathLangParser.IF)
            self.state = 89
            self.match(MathLangParser.LPAREN)
            self.state = 90
            self.expression(0)
            self.state = 91
            self.match(MathLangParser.RPAREN)
            self.state = 92
            self.block()
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 93
                self.match(MathLangParser.ELSE)
                self.state = 94
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
        self.enterRule(localctx, 10, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 97
                self.declaration_list()
                pass

            elif la_ == 2:
                self.state = 98
                self.id_list()
                pass


            self.state = 101
            self.assignment_operator()
            self.state = 102
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
        self.enterRule(localctx, 12, self.RULE_declaration_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22:
                self.state = 104
                self.scope_modifier()


            self.state = 107
            self.type_specifier()
            self.state = 108
            self.variable_declaration()
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 109
                self.match(MathLangParser.COMMA)
                self.state = 110
                self.type_specifier()
                self.state = 111
                self.variable_declaration()
                self.state = 117
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
        self.enterRule(localctx, 14, self.RULE_variable_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(MathLangParser.ID)
            self.state = 122
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 119
                self.simple_assignment_operator()
                self.state = 120
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

        def template(self):
            return self.getTypedRuleContext(MathLangParser.TemplateContext,0)


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
        self.enterRule(localctx, 16, self.RULE_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.match(MathLangParser.ID)
            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 125
                self.template()


            self.state = 128
            self.match(MathLangParser.LPAREN)
            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2190433853448) != 0):
                self.state = 129
                self.expression_list()


            self.state = 132
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
        self.enterRule(localctx, 18, self.RULE_loop)
        try:
            self.state = 137
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23]:
                self.enterOuterAlt(localctx, 1)
                self.state = 134
                self.for_loop()
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 2)
                self.state = 135
                self.while_loop()
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 3)
                self.state = 136
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
        self.enterRule(localctx, 20, self.RULE_for_loop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(MathLangParser.FOR)
            self.state = 140
            self.match(MathLangParser.LPAREN)
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1159645364224) != 0):
                self.state = 141
                self.assignment()


            self.state = 144
            self.match(MathLangParser.SEMI)
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2190433853448) != 0):
                self.state = 145
                self.expression(0)


            self.state = 148
            self.match(MathLangParser.SEMI)
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1160710750208) != 0):
                self.state = 149
                self.statement()


            self.state = 152
            self.match(MathLangParser.RPAREN)
            self.state = 153
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
        self.enterRule(localctx, 22, self.RULE_while_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(MathLangParser.WHILE)
            self.state = 156
            self.match(MathLangParser.LPAREN)
            self.state = 157
            self.expression(0)
            self.state = 158
            self.match(MathLangParser.RPAREN)
            self.state = 159
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
        self.enterRule(localctx, 24, self.RULE_until_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(MathLangParser.UNTIL)
            self.state = 162
            self.match(MathLangParser.LPAREN)
            self.state = 163
            self.expression(0)
            self.state = 164
            self.match(MathLangParser.RPAREN)
            self.state = 165
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
        self.enterRule(localctx, 26, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(MathLangParser.LCURLY)
            self.state = 171
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1160710750208) != 0):
                self.state = 168
                self.statement()
                self.state = 173
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 174
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
        self.enterRule(localctx, 28, self.RULE_id_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 176
                    self.match(MathLangParser.ID)
                    self.state = 177
                    self.match(MathLangParser.COMMA) 
                self.state = 182
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

            self.state = 183
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
        self.enterRule(localctx, 30, self.RULE_expression_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 185
                    self.expression(0)
                    self.state = 186
                    self.match(MathLangParser.COMMA) 
                self.state = 192
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

            self.state = 193
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
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 196
                self.match(MathLangParser.ID)
                pass

            elif la_ == 2:
                self.state = 197
                self.literal()
                pass

            elif la_ == 3:
                self.state = 198
                self.call()
                pass

            elif la_ == 4:
                self.state = 199
                self.cast_expression()
                pass

            elif la_ == 5:
                self.state = 200
                self.match(MathLangParser.LPAREN)
                self.state = 201
                self.expression(0)
                self.state = 202
                self.match(MathLangParser.RPAREN)
                pass

            elif la_ == 6:
                self.state = 204
                self.match(MathLangParser.NOT)
                self.state = 205
                self.expression(15)
                pass

            elif la_ == 7:
                self.state = 206
                self.match(MathLangParser.MINUS)
                self.state = 207
                self.expression(14)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 252
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 250
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                    if la_ == 1:
                        localctx = MathLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 210
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 211
                        self.match(MathLangParser.CARET)
                        self.state = 212
                        self.expression(14)
                        pass

                    elif la_ == 2:
                        localctx = MathLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 213
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 214
                        self.match(MathLangParser.ASTERISK)
                        self.state = 215
                        self.expression(13)
                        pass

                    elif la_ == 3:
                        localctx = MathLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 216
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 217
                        self.match(MathLangParser.SLASH)
                        self.state = 218
                        self.expression(12)
                        pass

                    elif la_ == 4:
                        localctx = MathLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 219
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 220
                        self.match(MathLangParser.PLUS)
                        self.state = 221
                        self.expression(11)
                        pass

                    elif la_ == 5:
                        localctx = MathLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 222
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 223
                        self.match(MathLangParser.MINUS)
                        self.state = 224
                        self.expression(10)
                        pass

                    elif la_ == 6:
                        localctx = MathLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 225
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 226
                        self.match(MathLangParser.AND)
                        self.state = 227
                        self.expression(9)
                        pass

                    elif la_ == 7:
                        localctx = MathLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 228
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 229
                        self.match(MathLangParser.OR)
                        self.state = 230
                        self.expression(8)
                        pass

                    elif la_ == 8:
                        localctx = MathLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 231
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 232
                        self.match(MathLangParser.EQ)
                        self.state = 233
                        self.match(MathLangParser.EQ)
                        self.state = 234
                        self.expression(7)
                        pass

                    elif la_ == 9:
                        localctx = MathLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 235
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 236
                        self.match(MathLangParser.NEQ)
                        self.state = 237
                        self.expression(6)
                        pass

                    elif la_ == 10:
                        localctx = MathLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 238
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 239
                        self.match(MathLangParser.GT)
                        self.state = 240
                        self.expression(5)
                        pass

                    elif la_ == 11:
                        localctx = MathLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 241
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 242
                        self.match(MathLangParser.LT)
                        self.state = 243
                        self.expression(4)
                        pass

                    elif la_ == 12:
                        localctx = MathLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 244
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 245
                        self.match(MathLangParser.GE)
                        self.state = 246
                        self.expression(3)
                        pass

                    elif la_ == 13:
                        localctx = MathLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 247
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 248
                        self.match(MathLangParser.LE)
                        self.state = 249
                        self.expression(2)
                        pass

             
                self.state = 254
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

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
        self.enterRule(localctx, 34, self.RULE_cast_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.type_specifier()
            self.state = 256
            self.match(MathLangParser.LPAREN)
            self.state = 257
            self.expression(0)
            self.state = 258
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
        self.enterRule(localctx, 36, self.RULE_assignment_operator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
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
        self.enterRule(localctx, 38, self.RULE_simple_assignment_operator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
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
        self.enterRule(localctx, 40, self.RULE_control_flow_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
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
        self.enterRule(localctx, 42, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
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

        def ID(self):
            return self.getToken(MathLangParser.ID, 0)

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
        self.enterRule(localctx, 44, self.RULE_type_specifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1159641169920) != 0)):
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


    class Type_specifier_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_specifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathLangParser.Type_specifierContext)
            else:
                return self.getTypedRuleContext(MathLangParser.Type_specifierContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MathLangParser.COMMA)
            else:
                return self.getToken(MathLangParser.COMMA, i)

        def getRuleIndex(self):
            return MathLangParser.RULE_type_specifier_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_specifier_list" ):
                listener.enterType_specifier_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_specifier_list" ):
                listener.exitType_specifier_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_specifier_list" ):
                return visitor.visitType_specifier_list(self)
            else:
                return visitor.visitChildren(self)




    def type_specifier_list(self):

        localctx = MathLangParser.Type_specifier_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_type_specifier_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.type_specifier()
            self.state = 275
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 271
                self.match(MathLangParser.COMMA)
                self.state = 272
                self.type_specifier()
                self.state = 277
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 48, self.RULE_scope_modifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
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
        self._predicates[16] = self.expression_sempred
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
         




