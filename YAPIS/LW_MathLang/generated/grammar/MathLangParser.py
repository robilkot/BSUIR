# Generated from grammar/MathLang.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3*")
        buf.write("\u0112\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\3\2\7\2\64\n\2\f\2\16\2\67\13\2\3\2\7\2:\n\2\f\2")
        buf.write("\16\2=\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3H\n")
        buf.write("\3\3\4\3\4\3\4\5\4M\n\4\3\4\3\4\5\4Q\n\4\3\4\3\4\3\4\3")
        buf.write("\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6a\n\6\3")
        buf.write("\7\3\7\5\7e\n\7\3\7\3\7\3\7\3\b\5\bk\n\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\7\bs\n\b\f\b\16\bv\13\b\3\t\3\t\3\t\3\t\3\n")
        buf.write("\3\n\5\n~\n\n\3\n\3\n\5\n\u0082\n\n\3\n\3\n\3\13\3\13")
        buf.write("\3\13\5\13\u0089\n\13\3\f\3\f\3\f\5\f\u008e\n\f\3\f\3")
        buf.write("\f\5\f\u0092\n\f\3\f\3\f\5\f\u0096\n\f\3\f\3\f\3\f\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17")
        buf.write("\3\17\7\17\u00a9\n\17\f\17\16\17\u00ac\13\17\3\17\3\17")
        buf.write("\3\20\3\20\7\20\u00b2\n\20\f\20\16\20\u00b5\13\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\7\21\u00bc\n\21\f\21\16\21\u00bf")
        buf.write("\13\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3")
        buf.write("\22\3\22\3\22\3\22\3\22\5\22\u00cf\n\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\7\22\u00f9\n\22\f\22\16\22\u00fc")
        buf.write("\13\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3")
        buf.write("\27\3\30\3\30\3\30\7\30\u010b\n\30\f\30\16\30\u010e\13")
        buf.write("\30\3\31\3\31\3\31\2\3\"\32\2\4\6\b\n\f\16\20\22\24\26")
        buf.write("\30\32\34\36 \"$&(*,.\60\2\4\3\2\35\37\3\2$\'\2\u0124")
        buf.write("\2\65\3\2\2\2\4G\3\2\2\2\6I\3\2\2\2\bU\3\2\2\2\nY\3\2")
        buf.write("\2\2\fd\3\2\2\2\16j\3\2\2\2\20w\3\2\2\2\22{\3\2\2\2\24")
        buf.write("\u0088\3\2\2\2\26\u008a\3\2\2\2\30\u009a\3\2\2\2\32\u00a0")
        buf.write("\3\2\2\2\34\u00a6\3\2\2\2\36\u00b3\3\2\2\2 \u00bd\3\2")
        buf.write("\2\2\"\u00ce\3\2\2\2$\u00fd\3\2\2\2&\u00ff\3\2\2\2(\u0101")
        buf.write("\3\2\2\2*\u0103\3\2\2\2,\u0105\3\2\2\2.\u0107\3\2\2\2")
        buf.write("\60\u010f\3\2\2\2\62\64\5\6\4\2\63\62\3\2\2\2\64\67\3")
        buf.write("\2\2\2\65\63\3\2\2\2\65\66\3\2\2\2\66;\3\2\2\2\67\65\3")
        buf.write("\2\2\28:\5\4\3\298\3\2\2\2:=\3\2\2\2;9\3\2\2\2;<\3\2\2")
        buf.write("\2<>\3\2\2\2=;\3\2\2\2>?\7\2\2\3?\3\3\2\2\2@H\5(\25\2")
        buf.write("AH\5\34\17\2BH\5\n\6\2CH\5\24\13\2DH\5\f\7\2EH\5\20\t")
        buf.write("\2FH\5\22\n\2G@\3\2\2\2GA\3\2\2\2GB\3\2\2\2GC\3\2\2\2")
        buf.write("GD\3\2\2\2GE\3\2\2\2GF\3\2\2\2H\5\3\2\2\2IJ\7\"\2\2JL")
        buf.write("\7(\2\2KM\5\b\5\2LK\3\2\2\2LM\3\2\2\2MN\3\2\2\2NP\7\20")
        buf.write("\2\2OQ\5\16\b\2PO\3\2\2\2PQ\3\2\2\2QR\3\2\2\2RS\7\21\2")
        buf.write("\2ST\5\34\17\2T\7\3\2\2\2UV\7\3\2\2VW\5.\30\2WX\7\21\2")
        buf.write("\2X\t\3\2\2\2YZ\7 \2\2Z[\7\20\2\2[\\\5\"\22\2\\]\7\21")
        buf.write("\2\2]`\5\34\17\2^_\7!\2\2_a\5\34\17\2`^\3\2\2\2`a\3\2")
        buf.write("\2\2a\13\3\2\2\2be\5\16\b\2ce\5\36\20\2db\3\2\2\2dc\3")
        buf.write("\2\2\2ef\3\2\2\2fg\5$\23\2gh\5 \21\2h\r\3\2\2\2ik\5\60")
        buf.write("\31\2ji\3\2\2\2jk\3\2\2\2kl\3\2\2\2lm\5,\27\2mt\7(\2\2")
        buf.write("no\7\r\2\2op\5,\27\2pq\7(\2\2qs\3\2\2\2rn\3\2\2\2sv\3")
        buf.write("\2\2\2tr\3\2\2\2tu\3\2\2\2u\17\3\2\2\2vt\3\2\2\2wx\5\60")
        buf.write("\31\2xy\5,\27\2yz\7(\2\2z\21\3\2\2\2{}\7(\2\2|~\5\b\5")
        buf.write("\2}|\3\2\2\2}~\3\2\2\2~\177\3\2\2\2\177\u0081\7\20\2\2")
        buf.write("\u0080\u0082\5 \21\2\u0081\u0080\3\2\2\2\u0081\u0082\3")
        buf.write("\2\2\2\u0082\u0083\3\2\2\2\u0083\u0084\7\21\2\2\u0084")
        buf.write("\23\3\2\2\2\u0085\u0089\5\26\f\2\u0086\u0089\5\30\r\2")
        buf.write("\u0087\u0089\5\32\16\2\u0088\u0085\3\2\2\2\u0088\u0086")
        buf.write("\3\2\2\2\u0088\u0087\3\2\2\2\u0089\25\3\2\2\2\u008a\u008b")
        buf.write("\7\32\2\2\u008b\u008d\7\20\2\2\u008c\u008e\5\f\7\2\u008d")
        buf.write("\u008c\3\2\2\2\u008d\u008e\3\2\2\2\u008e\u008f\3\2\2\2")
        buf.write("\u008f\u0091\7\16\2\2\u0090\u0092\5\"\22\2\u0091\u0090")
        buf.write("\3\2\2\2\u0091\u0092\3\2\2\2\u0092\u0093\3\2\2\2\u0093")
        buf.write("\u0095\7\16\2\2\u0094\u0096\5\4\3\2\u0095\u0094\3\2\2")
        buf.write("\2\u0095\u0096\3\2\2\2\u0096\u0097\3\2\2\2\u0097\u0098")
        buf.write("\7\21\2\2\u0098\u0099\5\34\17\2\u0099\27\3\2\2\2\u009a")
        buf.write("\u009b\7\33\2\2\u009b\u009c\7\20\2\2\u009c\u009d\5\"\22")
        buf.write("\2\u009d\u009e\7\21\2\2\u009e\u009f\5\34\17\2\u009f\31")
        buf.write("\3\2\2\2\u00a0\u00a1\7\34\2\2\u00a1\u00a2\7\20\2\2\u00a2")
        buf.write("\u00a3\5\"\22\2\u00a3\u00a4\7\21\2\2\u00a4\u00a5\5\34")
        buf.write("\17\2\u00a5\33\3\2\2\2\u00a6\u00aa\7\22\2\2\u00a7\u00a9")
        buf.write("\5\4\3\2\u00a8\u00a7\3\2\2\2\u00a9\u00ac\3\2\2\2\u00aa")
        buf.write("\u00a8\3\2\2\2\u00aa\u00ab\3\2\2\2\u00ab\u00ad\3\2\2\2")
        buf.write("\u00ac\u00aa\3\2\2\2\u00ad\u00ae\7\23\2\2\u00ae\35\3\2")
        buf.write("\2\2\u00af\u00b0\7(\2\2\u00b0\u00b2\7\r\2\2\u00b1\u00af")
        buf.write("\3\2\2\2\u00b2\u00b5\3\2\2\2\u00b3\u00b1\3\2\2\2\u00b3")
        buf.write("\u00b4\3\2\2\2\u00b4\u00b6\3\2\2\2\u00b5\u00b3\3\2\2\2")
        buf.write("\u00b6\u00b7\7(\2\2\u00b7\37\3\2\2\2\u00b8\u00b9\5\"\22")
        buf.write("\2\u00b9\u00ba\7\r\2\2\u00ba\u00bc\3\2\2\2\u00bb\u00b8")
        buf.write("\3\2\2\2\u00bc\u00bf\3\2\2\2\u00bd\u00bb\3\2\2\2\u00bd")
        buf.write("\u00be\3\2\2\2\u00be\u00c0\3\2\2\2\u00bf\u00bd\3\2\2\2")
        buf.write("\u00c0\u00c1\5\"\22\2\u00c1!\3\2\2\2\u00c2\u00c3\b\22")
        buf.write("\1\2\u00c3\u00cf\5\22\n\2\u00c4\u00cf\7(\2\2\u00c5\u00cf")
        buf.write("\5*\26\2\u00c6\u00c7\7\20\2\2\u00c7\u00c8\5\"\22\2\u00c8")
        buf.write("\u00c9\7\21\2\2\u00c9\u00cf\3\2\2\2\u00ca\u00cb\7\6\2")
        buf.write("\2\u00cb\u00cf\5\"\22\21\u00cc\u00cd\7\26\2\2\u00cd\u00cf")
        buf.write("\5\"\22\20\u00ce\u00c2\3\2\2\2\u00ce\u00c4\3\2\2\2\u00ce")
        buf.write("\u00c5\3\2\2\2\u00ce\u00c6\3\2\2\2\u00ce\u00ca\3\2\2\2")
        buf.write("\u00ce\u00cc\3\2\2\2\u00cf\u00fa\3\2\2\2\u00d0\u00d1\f")
        buf.write("\17\2\2\u00d1\u00d2\7\30\2\2\u00d2\u00f9\5\"\22\20\u00d3")
        buf.write("\u00d4\f\16\2\2\u00d4\u00d5\7\27\2\2\u00d5\u00f9\5\"\22")
        buf.write("\17\u00d6\u00d7\f\r\2\2\u00d7\u00d8\7\24\2\2\u00d8\u00f9")
        buf.write("\5\"\22\16\u00d9\u00da\f\f\2\2\u00da\u00db\7\25\2\2\u00db")
        buf.write("\u00f9\5\"\22\r\u00dc\u00dd\f\13\2\2\u00dd\u00de\7\26")
        buf.write("\2\2\u00de\u00f9\5\"\22\f\u00df\u00e0\f\n\2\2\u00e0\u00e1")
        buf.write("\7\4\2\2\u00e1\u00f9\5\"\22\13\u00e2\u00e3\f\t\2\2\u00e3")
        buf.write("\u00e4\7\5\2\2\u00e4\u00f9\5\"\22\n\u00e5\u00e6\f\b\2")
        buf.write("\2\u00e6\u00e7\7\7\2\2\u00e7\u00e8\7\7\2\2\u00e8\u00f9")
        buf.write("\5\"\22\t\u00e9\u00ea\f\7\2\2\u00ea\u00eb\7\b\2\2\u00eb")
        buf.write("\u00f9\5\"\22\b\u00ec\u00ed\f\6\2\2\u00ed\u00ee\7\t\2")
        buf.write("\2\u00ee\u00f9\5\"\22\7\u00ef\u00f0\f\5\2\2\u00f0\u00f1")
        buf.write("\7\n\2\2\u00f1\u00f9\5\"\22\6\u00f2\u00f3\f\4\2\2\u00f3")
        buf.write("\u00f4\7\13\2\2\u00f4\u00f9\5\"\22\5\u00f5\u00f6\f\3\2")
        buf.write("\2\u00f6\u00f7\7\f\2\2\u00f7\u00f9\5\"\22\4\u00f8\u00d0")
        buf.write("\3\2\2\2\u00f8\u00d3\3\2\2\2\u00f8\u00d6\3\2\2\2\u00f8")
        buf.write("\u00d9\3\2\2\2\u00f8\u00dc\3\2\2\2\u00f8\u00df\3\2\2\2")
        buf.write("\u00f8\u00e2\3\2\2\2\u00f8\u00e5\3\2\2\2\u00f8\u00e9\3")
        buf.write("\2\2\2\u00f8\u00ec\3\2\2\2\u00f8\u00ef\3\2\2\2\u00f8\u00f2")
        buf.write("\3\2\2\2\u00f8\u00f5\3\2\2\2\u00f9\u00fc\3\2\2\2\u00fa")
        buf.write("\u00f8\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fb#\3\2\2\2\u00fc")
        buf.write("\u00fa\3\2\2\2\u00fd\u00fe\5&\24\2\u00fe%\3\2\2\2\u00ff")
        buf.write("\u0100\7\7\2\2\u0100\'\3\2\2\2\u0101\u0102\t\2\2\2\u0102")
        buf.write(")\3\2\2\2\u0103\u0104\t\3\2\2\u0104+\3\2\2\2\u0105\u0106")
        buf.write("\7(\2\2\u0106-\3\2\2\2\u0107\u010c\5,\27\2\u0108\u0109")
        buf.write("\7\r\2\2\u0109\u010b\5,\27\2\u010a\u0108\3\2\2\2\u010b")
        buf.write("\u010e\3\2\2\2\u010c\u010a\3\2\2\2\u010c\u010d\3\2\2\2")
        buf.write("\u010d/\3\2\2\2\u010e\u010c\3\2\2\2\u010f\u0110\7\31\2")
        buf.write("\2\u0110\61\3\2\2\2\30\65;GLP`djt}\u0081\u0088\u008d\u0091")
        buf.write("\u0095\u00aa\u00b3\u00bd\u00ce\u00f8\u00fa\u010c")
        return buf.getvalue()


class MathLangParser ( Parser ):

    grammarFileName = "MathLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':('", "'and'", "'or'", "'not'", "'='", 
                     "'!='", "'>'", "'<'", "'>='", "'<='", "','", "';'", 
                     "':'", "'('", "')'", "'{'", "'}'", "'/'", "'+'", "'-'", 
                     "'*'", "'^'", "'global'", "'for'", "'while'", "'until'", 
                     "'break'", "'continue'", "'return'", "'if'", "'else'", 
                     "'sub'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "AND", "OR", "NOT", "EQ", 
                      "NEQ", "GT", "LT", "GE", "LE", "COMMA", "SEMI", "COLON", 
                      "LPAREN", "RPAREN", "LCURLY", "RCURLY", "SLASH", "PLUS", 
                      "MINUS", "ASTERISK", "CARET", "GLOBAL", "FOR", "WHILE", 
                      "UNTIL", "BREAK", "CONTINUE", "RETURN", "IF", "ELSE", 
                      "SUB", "DSLASH", "INT", "FLOAT", "BOOL", "STRING", 
                      "ID", "LINE_COMMENT", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_subprogram = 2
    RULE_template = 3
    RULE_branching = 4
    RULE_assignment = 5
    RULE_declaration_list = 6
    RULE_global_variable_declaration = 7
    RULE_call = 8
    RULE_loop = 9
    RULE_for_loop = 10
    RULE_while_loop = 11
    RULE_until_loop = 12
    RULE_block = 13
    RULE_id_list = 14
    RULE_expression_list = 15
    RULE_expression = 16
    RULE_assignment_operator = 17
    RULE_simple_assignment_operator = 18
    RULE_control_flow_operator = 19
    RULE_literal = 20
    RULE_type_specifier = 21
    RULE_type_specifier_list = 22
    RULE_scope_modifier = 23

    ruleNames =  [ "program", "statement", "subprogram", "template", "branching", 
                   "assignment", "declaration_list", "global_variable_declaration", 
                   "call", "loop", "for_loop", "while_loop", "until_loop", 
                   "block", "id_list", "expression_list", "expression", 
                   "assignment_operator", "simple_assignment_operator", 
                   "control_flow_operator", "literal", "type_specifier", 
                   "type_specifier_list", "scope_modifier" ]

    EOF = Token.EOF
    T__0=1
    AND=2
    OR=3
    NOT=4
    EQ=5
    NEQ=6
    GT=7
    LT=8
    GE=9
    LE=10
    COMMA=11
    SEMI=12
    COLON=13
    LPAREN=14
    RPAREN=15
    LCURLY=16
    RCURLY=17
    SLASH=18
    PLUS=19
    MINUS=20
    ASTERISK=21
    CARET=22
    GLOBAL=23
    FOR=24
    WHILE=25
    UNTIL=26
    BREAK=27
    CONTINUE=28
    RETURN=29
    IF=30
    ELSE=31
    SUB=32
    DSLASH=33
    INT=34
    FLOAT=35
    BOOL=36
    STRING=37
    ID=38
    LINE_COMMENT=39
    WS=40

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
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
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MathLangParser.SUB:
                self.state = 48
                self.subprogram()
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MathLangParser.LCURLY) | (1 << MathLangParser.GLOBAL) | (1 << MathLangParser.FOR) | (1 << MathLangParser.WHILE) | (1 << MathLangParser.UNTIL) | (1 << MathLangParser.BREAK) | (1 << MathLangParser.CONTINUE) | (1 << MathLangParser.RETURN) | (1 << MathLangParser.IF) | (1 << MathLangParser.ID))) != 0):
                self.state = 54
                self.statement()
                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 60
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


        def global_variable_declaration(self):
            return self.getTypedRuleContext(MathLangParser.Global_variable_declarationContext,0)


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
            self.state = 69
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 62
                self.control_flow_operator()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 63
                self.block()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 64
                self.branching()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 65
                self.loop()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 66
                self.assignment()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 67
                self.global_variable_declaration()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 68
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
            self.state = 71
            self.match(MathLangParser.SUB)
            self.state = 72
            self.match(MathLangParser.ID)
            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MathLangParser.T__0:
                self.state = 73
                self.template()


            self.state = 76
            self.match(MathLangParser.LPAREN)
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MathLangParser.GLOBAL or _la==MathLangParser.ID:
                self.state = 77
                self.declaration_list()


            self.state = 80
            self.match(MathLangParser.RPAREN)
            self.state = 81
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

        def type_specifier_list(self):
            return self.getTypedRuleContext(MathLangParser.Type_specifier_listContext,0)


        def RPAREN(self):
            return self.getToken(MathLangParser.RPAREN, 0)

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
            self.state = 83
            self.match(MathLangParser.T__0)
            self.state = 84
            self.type_specifier_list()
            self.state = 85
            self.match(MathLangParser.RPAREN)
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
            self.state = 87
            self.match(MathLangParser.IF)
            self.state = 88
            self.match(MathLangParser.LPAREN)
            self.state = 89
            self.expression(0)
            self.state = 90
            self.match(MathLangParser.RPAREN)
            self.state = 91
            self.block()
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MathLangParser.ELSE:
                self.state = 92
                self.match(MathLangParser.ELSE)
                self.state = 93
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
            self.state = 98
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 96
                self.declaration_list()
                pass

            elif la_ == 2:
                self.state = 97
                self.id_list()
                pass


            self.state = 100
            self.assignment_operator()
            self.state = 101
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


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MathLangParser.ID)
            else:
                return self.getToken(MathLangParser.ID, i)

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
            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MathLangParser.GLOBAL:
                self.state = 103
                self.scope_modifier()


            self.state = 106
            self.type_specifier()
            self.state = 107
            self.match(MathLangParser.ID)
            self.state = 114
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MathLangParser.COMMA:
                self.state = 108
                self.match(MathLangParser.COMMA)
                self.state = 109
                self.type_specifier()
                self.state = 110
                self.match(MathLangParser.ID)
                self.state = 116
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Global_variable_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scope_modifier(self):
            return self.getTypedRuleContext(MathLangParser.Scope_modifierContext,0)


        def type_specifier(self):
            return self.getTypedRuleContext(MathLangParser.Type_specifierContext,0)


        def ID(self):
            return self.getToken(MathLangParser.ID, 0)

        def getRuleIndex(self):
            return MathLangParser.RULE_global_variable_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGlobal_variable_declaration" ):
                listener.enterGlobal_variable_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGlobal_variable_declaration" ):
                listener.exitGlobal_variable_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGlobal_variable_declaration" ):
                return visitor.visitGlobal_variable_declaration(self)
            else:
                return visitor.visitChildren(self)




    def global_variable_declaration(self):

        localctx = MathLangParser.Global_variable_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_global_variable_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.scope_modifier()
            self.state = 118
            self.type_specifier()
            self.state = 119
            self.match(MathLangParser.ID)
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
            self.state = 121
            self.match(MathLangParser.ID)
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MathLangParser.T__0:
                self.state = 122
                self.template()


            self.state = 125
            self.match(MathLangParser.LPAREN)
            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MathLangParser.NOT) | (1 << MathLangParser.LPAREN) | (1 << MathLangParser.MINUS) | (1 << MathLangParser.INT) | (1 << MathLangParser.FLOAT) | (1 << MathLangParser.BOOL) | (1 << MathLangParser.STRING) | (1 << MathLangParser.ID))) != 0):
                self.state = 126
                self.expression_list()


            self.state = 129
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
            self.state = 134
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MathLangParser.FOR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 131
                self.for_loop()
                pass
            elif token in [MathLangParser.WHILE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 132
                self.while_loop()
                pass
            elif token in [MathLangParser.UNTIL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 133
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
            self.state = 136
            self.match(MathLangParser.FOR)
            self.state = 137
            self.match(MathLangParser.LPAREN)
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MathLangParser.GLOBAL or _la==MathLangParser.ID:
                self.state = 138
                self.assignment()


            self.state = 141
            self.match(MathLangParser.SEMI)
            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MathLangParser.NOT) | (1 << MathLangParser.LPAREN) | (1 << MathLangParser.MINUS) | (1 << MathLangParser.INT) | (1 << MathLangParser.FLOAT) | (1 << MathLangParser.BOOL) | (1 << MathLangParser.STRING) | (1 << MathLangParser.ID))) != 0):
                self.state = 142
                self.expression(0)


            self.state = 145
            self.match(MathLangParser.SEMI)
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MathLangParser.LCURLY) | (1 << MathLangParser.GLOBAL) | (1 << MathLangParser.FOR) | (1 << MathLangParser.WHILE) | (1 << MathLangParser.UNTIL) | (1 << MathLangParser.BREAK) | (1 << MathLangParser.CONTINUE) | (1 << MathLangParser.RETURN) | (1 << MathLangParser.IF) | (1 << MathLangParser.ID))) != 0):
                self.state = 146
                self.statement()


            self.state = 149
            self.match(MathLangParser.RPAREN)
            self.state = 150
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
            self.state = 152
            self.match(MathLangParser.WHILE)
            self.state = 153
            self.match(MathLangParser.LPAREN)
            self.state = 154
            self.expression(0)
            self.state = 155
            self.match(MathLangParser.RPAREN)
            self.state = 156
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
            self.state = 158
            self.match(MathLangParser.UNTIL)
            self.state = 159
            self.match(MathLangParser.LPAREN)
            self.state = 160
            self.expression(0)
            self.state = 161
            self.match(MathLangParser.RPAREN)
            self.state = 162
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
            self.state = 164
            self.match(MathLangParser.LCURLY)
            self.state = 168
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MathLangParser.LCURLY) | (1 << MathLangParser.GLOBAL) | (1 << MathLangParser.FOR) | (1 << MathLangParser.WHILE) | (1 << MathLangParser.UNTIL) | (1 << MathLangParser.BREAK) | (1 << MathLangParser.CONTINUE) | (1 << MathLangParser.RETURN) | (1 << MathLangParser.IF) | (1 << MathLangParser.ID))) != 0):
                self.state = 165
                self.statement()
                self.state = 170
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 171
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
            self.state = 177
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 173
                    self.match(MathLangParser.ID)
                    self.state = 174
                    self.match(MathLangParser.COMMA) 
                self.state = 179
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

            self.state = 180
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
            self.state = 187
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 182
                    self.expression(0)
                    self.state = 183
                    self.match(MathLangParser.COMMA) 
                self.state = 189
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

            self.state = 190
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

        def call(self):
            return self.getTypedRuleContext(MathLangParser.CallContext,0)


        def ID(self):
            return self.getToken(MathLangParser.ID, 0)

        def literal(self):
            return self.getTypedRuleContext(MathLangParser.LiteralContext,0)


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
            self.state = 204
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 193
                self.call()
                pass

            elif la_ == 2:
                self.state = 194
                self.match(MathLangParser.ID)
                pass

            elif la_ == 3:
                self.state = 195
                self.literal()
                pass

            elif la_ == 4:
                self.state = 196
                self.match(MathLangParser.LPAREN)
                self.state = 197
                self.expression(0)
                self.state = 198
                self.match(MathLangParser.RPAREN)
                pass

            elif la_ == 5:
                self.state = 200
                self.match(MathLangParser.NOT)
                self.state = 201
                self.expression(15)
                pass

            elif la_ == 6:
                self.state = 202
                self.match(MathLangParser.MINUS)
                self.state = 203
                self.expression(14)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 248
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 246
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                    if la_ == 1:
                        localctx = MathLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 206
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 207
                        self.match(MathLangParser.CARET)
                        self.state = 208
                        self.expression(14)
                        pass

                    elif la_ == 2:
                        localctx = MathLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 209
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 210
                        self.match(MathLangParser.ASTERISK)
                        self.state = 211
                        self.expression(13)
                        pass

                    elif la_ == 3:
                        localctx = MathLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 212
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 213
                        self.match(MathLangParser.SLASH)
                        self.state = 214
                        self.expression(12)
                        pass

                    elif la_ == 4:
                        localctx = MathLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 215
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 216
                        self.match(MathLangParser.PLUS)
                        self.state = 217
                        self.expression(11)
                        pass

                    elif la_ == 5:
                        localctx = MathLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 218
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 219
                        self.match(MathLangParser.MINUS)
                        self.state = 220
                        self.expression(10)
                        pass

                    elif la_ == 6:
                        localctx = MathLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 221
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 222
                        self.match(MathLangParser.AND)
                        self.state = 223
                        self.expression(9)
                        pass

                    elif la_ == 7:
                        localctx = MathLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 224
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 225
                        self.match(MathLangParser.OR)
                        self.state = 226
                        self.expression(8)
                        pass

                    elif la_ == 8:
                        localctx = MathLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 227
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 228
                        self.match(MathLangParser.EQ)
                        self.state = 229
                        self.match(MathLangParser.EQ)
                        self.state = 230
                        self.expression(7)
                        pass

                    elif la_ == 9:
                        localctx = MathLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 231
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 232
                        self.match(MathLangParser.NEQ)
                        self.state = 233
                        self.expression(6)
                        pass

                    elif la_ == 10:
                        localctx = MathLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 234
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 235
                        self.match(MathLangParser.GT)
                        self.state = 236
                        self.expression(5)
                        pass

                    elif la_ == 11:
                        localctx = MathLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 237
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 238
                        self.match(MathLangParser.LT)
                        self.state = 239
                        self.expression(4)
                        pass

                    elif la_ == 12:
                        localctx = MathLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 240
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 241
                        self.match(MathLangParser.GE)
                        self.state = 242
                        self.expression(3)
                        pass

                    elif la_ == 13:
                        localctx = MathLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 243
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 244
                        self.match(MathLangParser.LE)
                        self.state = 245
                        self.expression(2)
                        pass

             
                self.state = 250
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
            self.state = 251
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
            self.state = 253
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
            self.state = 255
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MathLangParser.BREAK) | (1 << MathLangParser.CONTINUE) | (1 << MathLangParser.RETURN))) != 0)):
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
            self.state = 257
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MathLangParser.INT) | (1 << MathLangParser.FLOAT) | (1 << MathLangParser.BOOL) | (1 << MathLangParser.STRING))) != 0)):
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
        self.enterRule(localctx, 42, self.RULE_type_specifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.match(MathLangParser.ID)
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
        self.enterRule(localctx, 44, self.RULE_type_specifier_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.type_specifier()
            self.state = 266
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MathLangParser.COMMA:
                self.state = 262
                self.match(MathLangParser.COMMA)
                self.state = 263
                self.type_specifier()
                self.state = 268
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
        self.enterRule(localctx, 46, self.RULE_scope_modifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
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
         




