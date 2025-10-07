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
        4,1,39,244,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,1,0,5,0,54,
        8,0,10,0,12,0,57,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,
        69,8,1,1,2,1,2,1,2,1,2,3,2,75,8,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,3,3,87,8,3,1,4,1,4,1,5,1,5,3,5,93,8,5,1,5,1,5,1,5,1,6,
        1,6,1,6,3,6,101,8,6,1,6,1,6,1,7,1,7,1,7,3,7,108,8,7,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,
        10,1,10,1,10,1,10,1,11,1,11,5,11,134,8,11,10,11,12,11,137,9,11,1,
        11,1,11,1,12,1,12,5,12,143,8,12,10,12,12,12,146,9,12,1,12,1,12,1,
        13,1,13,1,13,5,13,153,8,13,10,13,12,13,156,9,13,1,13,1,13,1,14,1,
        14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,172,8,
        14,1,14,1,14,1,14,1,14,5,14,178,8,14,10,14,12,14,181,9,14,1,15,1,
        15,1,15,1,15,1,15,1,16,1,16,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,
        18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,3,18,208,8,
        18,1,19,1,19,1,20,1,20,1,21,1,21,1,22,3,22,217,8,22,1,22,1,22,1,
        22,1,22,3,22,223,8,22,1,22,3,22,226,8,22,1,22,5,22,229,8,22,10,22,
        12,22,232,9,22,1,23,1,23,1,23,1,23,3,23,238,8,23,1,24,1,24,1,25,
        1,25,1,25,0,1,28,26,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,
        34,36,38,40,42,44,46,48,50,0,3,1,0,23,25,1,0,33,36,1,0,30,32,257,
        0,55,1,0,0,0,2,68,1,0,0,0,4,70,1,0,0,0,6,79,1,0,0,0,8,88,1,0,0,0,
        10,92,1,0,0,0,12,97,1,0,0,0,14,107,1,0,0,0,16,109,1,0,0,0,18,119,
        1,0,0,0,20,125,1,0,0,0,22,131,1,0,0,0,24,144,1,0,0,0,26,154,1,0,
        0,0,28,171,1,0,0,0,30,182,1,0,0,0,32,187,1,0,0,0,34,189,1,0,0,0,
        36,207,1,0,0,0,38,209,1,0,0,0,40,211,1,0,0,0,42,213,1,0,0,0,44,216,
        1,0,0,0,46,233,1,0,0,0,48,239,1,0,0,0,50,241,1,0,0,0,52,54,3,2,1,
        0,53,52,1,0,0,0,54,57,1,0,0,0,55,53,1,0,0,0,55,56,1,0,0,0,56,58,
        1,0,0,0,57,55,1,0,0,0,58,59,5,0,0,1,59,1,1,0,0,0,60,69,3,40,20,0,
        61,69,3,22,11,0,62,69,3,8,4,0,63,69,3,4,2,0,64,69,3,6,3,0,65,69,
        3,14,7,0,66,69,3,10,5,0,67,69,3,12,6,0,68,60,1,0,0,0,68,61,1,0,0,
        0,68,62,1,0,0,0,68,63,1,0,0,0,68,64,1,0,0,0,68,65,1,0,0,0,68,66,
        1,0,0,0,68,67,1,0,0,0,69,3,1,0,0,0,70,71,5,28,0,0,71,72,5,37,0,0,
        72,74,5,10,0,0,73,75,3,44,22,0,74,73,1,0,0,0,74,75,1,0,0,0,75,76,
        1,0,0,0,76,77,5,11,0,0,77,78,3,22,11,0,78,5,1,0,0,0,79,80,5,26,0,
        0,80,81,5,10,0,0,81,82,3,28,14,0,82,83,5,11,0,0,83,86,3,22,11,0,
        84,85,5,27,0,0,85,87,3,22,11,0,86,84,1,0,0,0,86,87,1,0,0,0,87,7,
        1,0,0,0,88,89,3,44,22,0,89,9,1,0,0,0,90,93,3,44,22,0,91,93,3,24,
        12,0,92,90,1,0,0,0,92,91,1,0,0,0,93,94,1,0,0,0,94,95,3,32,16,0,95,
        96,3,26,13,0,96,11,1,0,0,0,97,98,5,37,0,0,98,100,5,10,0,0,99,101,
        3,26,13,0,100,99,1,0,0,0,100,101,1,0,0,0,101,102,1,0,0,0,102,103,
        5,11,0,0,103,13,1,0,0,0,104,108,3,16,8,0,105,108,3,18,9,0,106,108,
        3,20,10,0,107,104,1,0,0,0,107,105,1,0,0,0,107,106,1,0,0,0,108,15,
        1,0,0,0,109,110,5,20,0,0,110,111,5,10,0,0,111,112,3,10,5,0,112,113,
        5,8,0,0,113,114,3,28,14,0,114,115,5,8,0,0,115,116,3,2,1,0,116,117,
        5,11,0,0,117,118,3,22,11,0,118,17,1,0,0,0,119,120,5,21,0,0,120,121,
        5,10,0,0,121,122,3,28,14,0,122,123,5,11,0,0,123,124,3,22,11,0,124,
        19,1,0,0,0,125,126,5,22,0,0,126,127,5,10,0,0,127,128,3,28,14,0,128,
        129,5,11,0,0,129,130,3,22,11,0,130,21,1,0,0,0,131,135,5,12,0,0,132,
        134,3,2,1,0,133,132,1,0,0,0,134,137,1,0,0,0,135,133,1,0,0,0,135,
        136,1,0,0,0,136,138,1,0,0,0,137,135,1,0,0,0,138,139,5,13,0,0,139,
        23,1,0,0,0,140,141,5,37,0,0,141,143,5,7,0,0,142,140,1,0,0,0,143,
        146,1,0,0,0,144,142,1,0,0,0,144,145,1,0,0,0,145,147,1,0,0,0,146,
        144,1,0,0,0,147,148,5,37,0,0,148,25,1,0,0,0,149,150,3,28,14,0,150,
        151,5,7,0,0,151,153,1,0,0,0,152,149,1,0,0,0,153,156,1,0,0,0,154,
        152,1,0,0,0,154,155,1,0,0,0,155,157,1,0,0,0,156,154,1,0,0,0,157,
        158,3,28,14,0,158,27,1,0,0,0,159,160,6,14,-1,0,160,172,5,37,0,0,
        161,172,3,42,21,0,162,172,3,12,6,0,163,172,3,30,15,0,164,165,3,38,
        19,0,165,166,3,28,14,2,166,172,1,0,0,0,167,168,5,10,0,0,168,169,
        3,28,14,0,169,170,5,11,0,0,170,172,1,0,0,0,171,159,1,0,0,0,171,161,
        1,0,0,0,171,162,1,0,0,0,171,163,1,0,0,0,171,164,1,0,0,0,171,167,
        1,0,0,0,172,179,1,0,0,0,173,174,10,3,0,0,174,175,3,36,18,0,175,176,
        3,28,14,4,176,178,1,0,0,0,177,173,1,0,0,0,178,181,1,0,0,0,179,177,
        1,0,0,0,179,180,1,0,0,0,180,29,1,0,0,0,181,179,1,0,0,0,182,183,3,
        48,24,0,183,184,5,10,0,0,184,185,3,28,14,0,185,186,5,11,0,0,186,
        31,1,0,0,0,187,188,3,34,17,0,188,33,1,0,0,0,189,190,5,4,0,0,190,
        35,1,0,0,0,191,208,5,15,0,0,192,208,5,16,0,0,193,208,5,17,0,0,194,
        208,5,14,0,0,195,208,5,18,0,0,196,197,5,4,0,0,197,208,5,4,0,0,198,
        208,5,2,0,0,199,208,5,1,0,0,200,208,5,3,0,0,201,208,5,5,0,0,202,
        208,5,6,0,0,203,204,5,5,0,0,204,208,5,4,0,0,205,206,5,6,0,0,206,
        208,5,4,0,0,207,191,1,0,0,0,207,192,1,0,0,0,207,193,1,0,0,0,207,
        194,1,0,0,0,207,195,1,0,0,0,207,196,1,0,0,0,207,198,1,0,0,0,207,
        199,1,0,0,0,207,200,1,0,0,0,207,201,1,0,0,0,207,202,1,0,0,0,207,
        203,1,0,0,0,207,205,1,0,0,0,208,37,1,0,0,0,209,210,5,16,0,0,210,
        39,1,0,0,0,211,212,7,0,0,0,212,41,1,0,0,0,213,214,7,1,0,0,214,43,
        1,0,0,0,215,217,3,50,25,0,216,215,1,0,0,0,216,217,1,0,0,0,217,218,
        1,0,0,0,218,219,3,48,24,0,219,230,3,46,23,0,220,222,5,7,0,0,221,
        223,3,50,25,0,222,221,1,0,0,0,222,223,1,0,0,0,223,225,1,0,0,0,224,
        226,3,48,24,0,225,224,1,0,0,0,225,226,1,0,0,0,226,227,1,0,0,0,227,
        229,3,46,23,0,228,220,1,0,0,0,229,232,1,0,0,0,230,228,1,0,0,0,230,
        231,1,0,0,0,231,45,1,0,0,0,232,230,1,0,0,0,233,237,5,37,0,0,234,
        235,3,34,17,0,235,236,3,28,14,0,236,238,1,0,0,0,237,234,1,0,0,0,
        237,238,1,0,0,0,238,47,1,0,0,0,239,240,7,2,0,0,240,49,1,0,0,0,241,
        242,5,19,0,0,242,51,1,0,0,0,18,55,68,74,86,92,100,107,135,144,154,
        171,179,207,216,222,225,230,237
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




    def program(self):

        localctx = MathLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 145357279232) != 0):
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


        def declaration(self):
            return self.getTypedRuleContext(MathLangParser.DeclarationContext,0)


        def subprogram(self):
            return self.getTypedRuleContext(MathLangParser.SubprogramContext,0)


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




    def statement(self):

        localctx = MathLangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 68
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
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
                self.declaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 63
                self.subprogram()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 64
                self.branching()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 65
                self.loop()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 66
                self.assignment()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 67
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




    def subprogram(self):

        localctx = MathLangParser.SubprogramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_subprogram)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(MathLangParser.SUB)
            self.state = 71
            self.match(MathLangParser.ID)
            self.state = 72
            self.match(MathLangParser.LPAREN)
            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 7516717056) != 0):
                self.state = 73
                self.declaration_list()


            self.state = 76
            self.match(MathLangParser.RPAREN)
            self.state = 77
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




    def branching(self):

        localctx = MathLangParser.BranchingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_branching)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(MathLangParser.IF)
            self.state = 80
            self.match(MathLangParser.LPAREN)
            self.state = 81
            self.expression(0)
            self.state = 82
            self.match(MathLangParser.RPAREN)
            self.state = 83
            self.block()
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 84
                self.match(MathLangParser.ELSE)
                self.state = 85
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




    def declaration(self):

        localctx = MathLangParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
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




    def assignment(self):

        localctx = MathLangParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19, 30, 31, 32]:
                self.state = 90
                self.declaration_list()
                pass
            elif token in [37]:
                self.state = 91
                self.id_list()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 94
            self.assignment_operator()
            self.state = 95
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




    def call(self):

        localctx = MathLangParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(MathLangParser.ID)
            self.state = 98
            self.match(MathLangParser.LPAREN)
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 273804231680) != 0):
                self.state = 99
                self.expression_list()


            self.state = 102
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




    def loop(self):

        localctx = MathLangParser.LoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_loop)
        try:
            self.state = 107
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 104
                self.for_loop()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 105
                self.while_loop()
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 3)
                self.state = 106
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

        def assignment(self):
            return self.getTypedRuleContext(MathLangParser.AssignmentContext,0)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(MathLangParser.SEMI)
            else:
                return self.getToken(MathLangParser.SEMI, i)

        def expression(self):
            return self.getTypedRuleContext(MathLangParser.ExpressionContext,0)


        def statement(self):
            return self.getTypedRuleContext(MathLangParser.StatementContext,0)


        def RPAREN(self):
            return self.getToken(MathLangParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(MathLangParser.BlockContext,0)


        def getRuleIndex(self):
            return MathLangParser.RULE_for_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_loop" ):
                listener.enterFor_loop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_loop" ):
                listener.exitFor_loop(self)




    def for_loop(self):

        localctx = MathLangParser.For_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_for_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(MathLangParser.FOR)
            self.state = 110
            self.match(MathLangParser.LPAREN)
            self.state = 111
            self.assignment()
            self.state = 112
            self.match(MathLangParser.SEMI)
            self.state = 113
            self.expression(0)
            self.state = 114
            self.match(MathLangParser.SEMI)
            self.state = 115
            self.statement()
            self.state = 116
            self.match(MathLangParser.RPAREN)
            self.state = 117
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




    def while_loop(self):

        localctx = MathLangParser.While_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_while_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(MathLangParser.WHILE)
            self.state = 120
            self.match(MathLangParser.LPAREN)
            self.state = 121
            self.expression(0)
            self.state = 122
            self.match(MathLangParser.RPAREN)
            self.state = 123
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




    def until_loop(self):

        localctx = MathLangParser.Until_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_until_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.match(MathLangParser.UNTIL)
            self.state = 126
            self.match(MathLangParser.LPAREN)
            self.state = 127
            self.expression(0)
            self.state = 128
            self.match(MathLangParser.RPAREN)
            self.state = 129
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




    def block(self):

        localctx = MathLangParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(MathLangParser.LCURLY)
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 145357279232) != 0):
                self.state = 132
                self.statement()
                self.state = 137
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 138
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




    def id_list(self):

        localctx = MathLangParser.Id_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_id_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 140
                    self.match(MathLangParser.ID)
                    self.state = 141
                    self.match(MathLangParser.COMMA) 
                self.state = 146
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

            self.state = 147
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




    def expression_list(self):

        localctx = MathLangParser.Expression_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_expression_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 149
                    self.expression(0)
                    self.state = 150
                    self.match(MathLangParser.COMMA) 
                self.state = 156
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

            self.state = 157
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



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MathLangParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 160
                self.match(MathLangParser.ID)
                pass

            elif la_ == 2:
                self.state = 161
                self.literal()
                pass

            elif la_ == 3:
                self.state = 162
                self.call()
                pass

            elif la_ == 4:
                self.state = 163
                self.cast_expression()
                pass

            elif la_ == 5:
                self.state = 164
                self.unary_operator()
                self.state = 165
                self.expression(2)
                pass

            elif la_ == 6:
                self.state = 167
                self.match(MathLangParser.LPAREN)
                self.state = 168
                self.expression(0)
                self.state = 169
                self.match(MathLangParser.RPAREN)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 179
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MathLangParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 173
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 174
                    self.binary_operator()
                    self.state = 175
                    self.expression(4) 
                self.state = 181
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

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




    def cast_expression(self):

        localctx = MathLangParser.Cast_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_cast_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.type_specifier()
            self.state = 183
            self.match(MathLangParser.LPAREN)
            self.state = 184
            self.expression(0)
            self.state = 185
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




    def assignment_operator(self):

        localctx = MathLangParser.Assignment_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_assignment_operator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
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




    def simple_assignment_operator(self):

        localctx = MathLangParser.Simple_assignment_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_simple_assignment_operator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
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




    def binary_operator(self):

        localctx = MathLangParser.Binary_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_binary_operator)
        try:
            self.state = 207
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 191
                self.match(MathLangParser.PLUS)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 192
                self.match(MathLangParser.MINUS)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 193
                self.match(MathLangParser.ASTERISK)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 194
                self.match(MathLangParser.SLASH)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 195
                self.match(MathLangParser.CARET)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 196
                self.match(MathLangParser.EQ)
                self.state = 197
                self.match(MathLangParser.EQ)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 198
                self.match(MathLangParser.OR)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 199
                self.match(MathLangParser.AND)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 200
                self.match(MathLangParser.NOT)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 201
                self.match(MathLangParser.GT)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 202
                self.match(MathLangParser.LS)
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 203
                self.match(MathLangParser.GT)
                self.state = 204
                self.match(MathLangParser.EQ)
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 205
                self.match(MathLangParser.LS)
                self.state = 206
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




    def unary_operator(self):

        localctx = MathLangParser.Unary_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_unary_operator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
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




    def control_flow_operator(self):

        localctx = MathLangParser.Control_flow_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_control_flow_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
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




    def literal(self):

        localctx = MathLangParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
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




    def declaration_list(self):

        localctx = MathLangParser.Declaration_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_declaration_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 215
                self.scope_modifier()


            self.state = 218
            self.type_specifier()
            self.state = 219
            self.variable_declaration()
            self.state = 230
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 220
                self.match(MathLangParser.COMMA)
                self.state = 222
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==19:
                    self.state = 221
                    self.scope_modifier()


                self.state = 225
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 7516192768) != 0):
                    self.state = 224
                    self.type_specifier()


                self.state = 227
                self.variable_declaration()
                self.state = 232
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




    def variable_declaration(self):

        localctx = MathLangParser.Variable_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_variable_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.match(MathLangParser.ID)
            self.state = 237
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 234
                self.simple_assignment_operator()
                self.state = 235
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




    def type_specifier(self):

        localctx = MathLangParser.Type_specifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_type_specifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
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




    def scope_modifier(self):

        localctx = MathLangParser.Scope_modifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_scope_modifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
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
         




