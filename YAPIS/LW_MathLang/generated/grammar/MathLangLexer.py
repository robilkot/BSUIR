# Generated from grammar/MathLang.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2*")
        buf.write("\u0104\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\3\2\3\2\3\2\3\3\3\3\3\3\3\3")
        buf.write("\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3\b\3")
        buf.write("\b\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\r\3\r")
        buf.write("\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23")
        buf.write("\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\37")
        buf.write("\3\37\3\37\3 \3 \3 \3 \3 \3!\3!\3!\3!\3\"\3\"\3\"\3#\5")
        buf.write("#\u00c6\n#\3#\6#\u00c9\n#\r#\16#\u00ca\3$\3$\3$\5$\u00d0")
        buf.write("\n$\3$\3$\3$\3$\5$\u00d6\n$\3%\3%\3%\3%\3%\3%\3%\3%\3")
        buf.write("%\5%\u00e1\n%\3&\3&\7&\u00e5\n&\f&\16&\u00e8\13&\3&\3")
        buf.write("&\3\'\3\'\7\'\u00ee\n\'\f\'\16\'\u00f1\13\'\3(\3(\3(\3")
        buf.write("(\7(\u00f7\n(\f(\16(\u00fa\13(\3(\3(\3)\6)\u00ff\n)\r")
        buf.write(")\16)\u0100\3)\3)\2\2*\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24")
        buf.write("\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37")
        buf.write("= ?!A\"C#E$G%I&K\'M(O)Q*\3\2\b\3\2\62;\3\2$$\5\2C\\aa")
        buf.write("c|\6\2\62;C\\aac|\4\2\f\f\17\17\5\2\13\f\16\17\"\"\2\u010c")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\3S\3\2\2")
        buf.write("\2\5V\3\2\2\2\7Z\3\2\2\2\t]\3\2\2\2\13a\3\2\2\2\rc\3\2")
        buf.write("\2\2\17f\3\2\2\2\21h\3\2\2\2\23j\3\2\2\2\25m\3\2\2\2\27")
        buf.write("p\3\2\2\2\31r\3\2\2\2\33t\3\2\2\2\35v\3\2\2\2\37x\3\2")
        buf.write("\2\2!z\3\2\2\2#|\3\2\2\2%~\3\2\2\2\'\u0080\3\2\2\2)\u0082")
        buf.write("\3\2\2\2+\u0084\3\2\2\2-\u0086\3\2\2\2/\u0088\3\2\2\2")
        buf.write("\61\u008f\3\2\2\2\63\u0093\3\2\2\2\65\u0099\3\2\2\2\67")
        buf.write("\u009f\3\2\2\29\u00a5\3\2\2\2;\u00ae\3\2\2\2=\u00b5\3")
        buf.write("\2\2\2?\u00b8\3\2\2\2A\u00bd\3\2\2\2C\u00c1\3\2\2\2E\u00c5")
        buf.write("\3\2\2\2G\u00d5\3\2\2\2I\u00e0\3\2\2\2K\u00e2\3\2\2\2")
        buf.write("M\u00eb\3\2\2\2O\u00f2\3\2\2\2Q\u00fe\3\2\2\2ST\7<\2\2")
        buf.write("TU\7*\2\2U\4\3\2\2\2VW\7c\2\2WX\7p\2\2XY\7f\2\2Y\6\3\2")
        buf.write("\2\2Z[\7q\2\2[\\\7t\2\2\\\b\3\2\2\2]^\7p\2\2^_\7q\2\2")
        buf.write("_`\7v\2\2`\n\3\2\2\2ab\7?\2\2b\f\3\2\2\2cd\7#\2\2de\7")
        buf.write("?\2\2e\16\3\2\2\2fg\7@\2\2g\20\3\2\2\2hi\7>\2\2i\22\3")
        buf.write("\2\2\2jk\7@\2\2kl\7?\2\2l\24\3\2\2\2mn\7>\2\2no\7?\2\2")
        buf.write("o\26\3\2\2\2pq\7.\2\2q\30\3\2\2\2rs\7=\2\2s\32\3\2\2\2")
        buf.write("tu\7<\2\2u\34\3\2\2\2vw\7*\2\2w\36\3\2\2\2xy\7+\2\2y ")
        buf.write("\3\2\2\2z{\7}\2\2{\"\3\2\2\2|}\7\177\2\2}$\3\2\2\2~\177")
        buf.write("\7\61\2\2\177&\3\2\2\2\u0080\u0081\7-\2\2\u0081(\3\2\2")
        buf.write("\2\u0082\u0083\7/\2\2\u0083*\3\2\2\2\u0084\u0085\7,\2")
        buf.write("\2\u0085,\3\2\2\2\u0086\u0087\7`\2\2\u0087.\3\2\2\2\u0088")
        buf.write("\u0089\7i\2\2\u0089\u008a\7n\2\2\u008a\u008b\7q\2\2\u008b")
        buf.write("\u008c\7d\2\2\u008c\u008d\7c\2\2\u008d\u008e\7n\2\2\u008e")
        buf.write("\60\3\2\2\2\u008f\u0090\7h\2\2\u0090\u0091\7q\2\2\u0091")
        buf.write("\u0092\7t\2\2\u0092\62\3\2\2\2\u0093\u0094\7y\2\2\u0094")
        buf.write("\u0095\7j\2\2\u0095\u0096\7k\2\2\u0096\u0097\7n\2\2\u0097")
        buf.write("\u0098\7g\2\2\u0098\64\3\2\2\2\u0099\u009a\7w\2\2\u009a")
        buf.write("\u009b\7p\2\2\u009b\u009c\7v\2\2\u009c\u009d\7k\2\2\u009d")
        buf.write("\u009e\7n\2\2\u009e\66\3\2\2\2\u009f\u00a0\7d\2\2\u00a0")
        buf.write("\u00a1\7t\2\2\u00a1\u00a2\7g\2\2\u00a2\u00a3\7c\2\2\u00a3")
        buf.write("\u00a4\7m\2\2\u00a48\3\2\2\2\u00a5\u00a6\7e\2\2\u00a6")
        buf.write("\u00a7\7q\2\2\u00a7\u00a8\7p\2\2\u00a8\u00a9\7v\2\2\u00a9")
        buf.write("\u00aa\7k\2\2\u00aa\u00ab\7p\2\2\u00ab\u00ac\7w\2\2\u00ac")
        buf.write("\u00ad\7g\2\2\u00ad:\3\2\2\2\u00ae\u00af\7t\2\2\u00af")
        buf.write("\u00b0\7g\2\2\u00b0\u00b1\7v\2\2\u00b1\u00b2\7w\2\2\u00b2")
        buf.write("\u00b3\7t\2\2\u00b3\u00b4\7p\2\2\u00b4<\3\2\2\2\u00b5")
        buf.write("\u00b6\7k\2\2\u00b6\u00b7\7h\2\2\u00b7>\3\2\2\2\u00b8")
        buf.write("\u00b9\7g\2\2\u00b9\u00ba\7n\2\2\u00ba\u00bb\7u\2\2\u00bb")
        buf.write("\u00bc\7g\2\2\u00bc@\3\2\2\2\u00bd\u00be\7u\2\2\u00be")
        buf.write("\u00bf\7w\2\2\u00bf\u00c0\7d\2\2\u00c0B\3\2\2\2\u00c1")
        buf.write("\u00c2\5%\23\2\u00c2\u00c3\5%\23\2\u00c3D\3\2\2\2\u00c4")
        buf.write("\u00c6\7/\2\2\u00c5\u00c4\3\2\2\2\u00c5\u00c6\3\2\2\2")
        buf.write("\u00c6\u00c8\3\2\2\2\u00c7\u00c9\t\2\2\2\u00c8\u00c7\3")
        buf.write("\2\2\2\u00c9\u00ca\3\2\2\2\u00ca\u00c8\3\2\2\2\u00ca\u00cb")
        buf.write("\3\2\2\2\u00cbF\3\2\2\2\u00cc\u00cd\5E#\2\u00cd\u00cf")
        buf.write("\7\60\2\2\u00ce\u00d0\5E#\2\u00cf\u00ce\3\2\2\2\u00cf")
        buf.write("\u00d0\3\2\2\2\u00d0\u00d6\3\2\2\2\u00d1\u00d2\5E#\2\u00d2")
        buf.write("\u00d3\7g\2\2\u00d3\u00d4\5E#\2\u00d4\u00d6\3\2\2\2\u00d5")
        buf.write("\u00cc\3\2\2\2\u00d5\u00d1\3\2\2\2\u00d6H\3\2\2\2\u00d7")
        buf.write("\u00d8\7v\2\2\u00d8\u00d9\7t\2\2\u00d9\u00da\7w\2\2\u00da")
        buf.write("\u00e1\7g\2\2\u00db\u00dc\7h\2\2\u00dc\u00dd\7c\2\2\u00dd")
        buf.write("\u00de\7n\2\2\u00de\u00df\7u\2\2\u00df\u00e1\7g\2\2\u00e0")
        buf.write("\u00d7\3\2\2\2\u00e0\u00db\3\2\2\2\u00e1J\3\2\2\2\u00e2")
        buf.write("\u00e6\7$\2\2\u00e3\u00e5\n\3\2\2\u00e4\u00e3\3\2\2\2")
        buf.write("\u00e5\u00e8\3\2\2\2\u00e6\u00e4\3\2\2\2\u00e6\u00e7\3")
        buf.write("\2\2\2\u00e7\u00e9\3\2\2\2\u00e8\u00e6\3\2\2\2\u00e9\u00ea")
        buf.write("\7$\2\2\u00eaL\3\2\2\2\u00eb\u00ef\t\4\2\2\u00ec\u00ee")
        buf.write("\t\5\2\2\u00ed\u00ec\3\2\2\2\u00ee\u00f1\3\2\2\2\u00ef")
        buf.write("\u00ed\3\2\2\2\u00ef\u00f0\3\2\2\2\u00f0N\3\2\2\2\u00f1")
        buf.write("\u00ef\3\2\2\2\u00f2\u00f3\7\61\2\2\u00f3\u00f4\7\61\2")
        buf.write("\2\u00f4\u00f8\3\2\2\2\u00f5\u00f7\n\6\2\2\u00f6\u00f5")
        buf.write("\3\2\2\2\u00f7\u00fa\3\2\2\2\u00f8\u00f6\3\2\2\2\u00f8")
        buf.write("\u00f9\3\2\2\2\u00f9\u00fb\3\2\2\2\u00fa\u00f8\3\2\2\2")
        buf.write("\u00fb\u00fc\b(\2\2\u00fcP\3\2\2\2\u00fd\u00ff\t\7\2\2")
        buf.write("\u00fe\u00fd\3\2\2\2\u00ff\u0100\3\2\2\2\u0100\u00fe\3")
        buf.write("\2\2\2\u0100\u0101\3\2\2\2\u0101\u0102\3\2\2\2\u0102\u0103")
        buf.write("\b)\3\2\u0103R\3\2\2\2\f\2\u00c5\u00ca\u00cf\u00d5\u00e0")
        buf.write("\u00e6\u00ef\u00f8\u0100\4\2\3\2\b\2\2")
        return buf.getvalue()


class MathLangLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    AND = 2
    OR = 3
    NOT = 4
    EQ = 5
    NEQ = 6
    GT = 7
    LT = 8
    GE = 9
    LE = 10
    COMMA = 11
    SEMI = 12
    COLON = 13
    LPAREN = 14
    RPAREN = 15
    LCURLY = 16
    RCURLY = 17
    SLASH = 18
    PLUS = 19
    MINUS = 20
    ASTERISK = 21
    CARET = 22
    GLOBAL = 23
    FOR = 24
    WHILE = 25
    UNTIL = 26
    BREAK = 27
    CONTINUE = 28
    RETURN = 29
    IF = 30
    ELSE = 31
    SUB = 32
    DSLASH = 33
    INT = 34
    FLOAT = 35
    BOOL = 36
    STRING = 37
    ID = 38
    LINE_COMMENT = 39
    WS = 40

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':('", "'and'", "'or'", "'not'", "'='", "'!='", "'>'", "'<'", 
            "'>='", "'<='", "','", "';'", "':'", "'('", "')'", "'{'", "'}'", 
            "'/'", "'+'", "'-'", "'*'", "'^'", "'global'", "'for'", "'while'", 
            "'until'", "'break'", "'continue'", "'return'", "'if'", "'else'", 
            "'sub'" ]

    symbolicNames = [ "<INVALID>",
            "AND", "OR", "NOT", "EQ", "NEQ", "GT", "LT", "GE", "LE", "COMMA", 
            "SEMI", "COLON", "LPAREN", "RPAREN", "LCURLY", "RCURLY", "SLASH", 
            "PLUS", "MINUS", "ASTERISK", "CARET", "GLOBAL", "FOR", "WHILE", 
            "UNTIL", "BREAK", "CONTINUE", "RETURN", "IF", "ELSE", "SUB", 
            "DSLASH", "INT", "FLOAT", "BOOL", "STRING", "ID", "LINE_COMMENT", 
            "WS" ]

    ruleNames = [ "T__0", "AND", "OR", "NOT", "EQ", "NEQ", "GT", "LT", "GE", 
                  "LE", "COMMA", "SEMI", "COLON", "LPAREN", "RPAREN", "LCURLY", 
                  "RCURLY", "SLASH", "PLUS", "MINUS", "ASTERISK", "CARET", 
                  "GLOBAL", "FOR", "WHILE", "UNTIL", "BREAK", "CONTINUE", 
                  "RETURN", "IF", "ELSE", "SUB", "DSLASH", "INT", "FLOAT", 
                  "BOOL", "STRING", "ID", "LINE_COMMENT", "WS" ]

    grammarFileName = "MathLang.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


