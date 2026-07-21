# Generated from experimento_parsers/grammars/DockerCompose.g4 by ANTLR 4.9.3
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\25")
        buf.write("\u00bd\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\17\3\17\3\17\3\20\3\20\6\20\u008a\n\20\r")
        buf.write("\20\16\20\u008b\3\20\3\20\3\21\6\21\u0091\n\21\r\21\16")
        buf.write("\21\u0092\3\21\3\21\6\21\u0097\n\21\r\21\16\21\u0098\3")
        buf.write("\21\3\21\6\21\u009d\n\21\r\21\16\21\u009e\3\21\3\21\6")
        buf.write("\21\u00a3\n\21\r\21\16\21\u00a4\3\21\3\21\6\21\u00a9\n")
        buf.write("\21\r\21\16\21\u00aa\3\22\6\22\u00ae\n\22\r\22\16\22\u00af")
        buf.write("\3\23\5\23\u00b3\n\23\3\23\3\23\3\24\6\24\u00b8\n\24\r")
        buf.write("\24\16\24\u00b9\3\24\3\24\2\2\25\3\3\5\4\7\5\t\6\13\7")
        buf.write("\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21")
        buf.write("!\22#\23%\24\'\25\3\2\6\5\2\f\f\17\17))\3\2\62;\7\2//")
        buf.write("\62;C\\aac|\4\2\13\13\"\"\2\u00c5\2\3\3\2\2\2\2\5\3\2")
        buf.write("\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2")
        buf.write("\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2")
        buf.write("\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37")
        buf.write("\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2")
        buf.write("\3)\3\2\2\2\5\62\3\2\2\2\7<\3\2\2\2\tF\3\2\2\2\13M\3\2")
        buf.write("\2\2\rU\3\2\2\2\17[\3\2\2\2\21c\3\2\2\2\23k\3\2\2\2\25")
        buf.write("m\3\2\2\2\27o\3\2\2\2\31x\3\2\2\2\33\177\3\2\2\2\35\u0084")
        buf.write("\3\2\2\2\37\u0087\3\2\2\2!\u0090\3\2\2\2#\u00ad\3\2\2")
        buf.write("\2%\u00b2\3\2\2\2\'\u00b7\3\2\2\2)*\7x\2\2*+\7g\2\2+,")
        buf.write("\7t\2\2,-\7u\2\2-.\7k\2\2./\7q\2\2/\60\7p\2\2\60\61\7")
        buf.write("<\2\2\61\4\3\2\2\2\62\63\7u\2\2\63\64\7g\2\2\64\65\7t")
        buf.write("\2\2\65\66\7x\2\2\66\67\7k\2\2\678\7e\2\289\7g\2\29:\7")
        buf.write("u\2\2:;\7<\2\2;\6\3\2\2\2<=\7p\2\2=>\7g\2\2>?\7v\2\2?")
        buf.write("@\7y\2\2@A\7q\2\2AB\7t\2\2BC\7m\2\2CD\7u\2\2DE\7<\2\2")
        buf.write("E\b\3\2\2\2FG\7k\2\2GH\7o\2\2HI\7c\2\2IJ\7i\2\2JK\7g\2")
        buf.write("\2KL\7<\2\2L\n\3\2\2\2MN\7f\2\2NO\7t\2\2OP\7k\2\2PQ\7")
        buf.write("x\2\2QR\7g\2\2RS\7t\2\2ST\7<\2\2T\f\3\2\2\2UV\7k\2\2V")
        buf.write("W\7r\2\2WX\7c\2\2XY\7o\2\2YZ\7<\2\2Z\16\3\2\2\2[\\\7e")
        buf.write("\2\2\\]\7q\2\2]^\7p\2\2^_\7h\2\2_`\7k\2\2`a\7i\2\2ab\7")
        buf.write("<\2\2b\20\3\2\2\2cd\7u\2\2de\7w\2\2ef\7d\2\2fg\7p\2\2")
        buf.write("gh\7g\2\2hi\7v\2\2ij\7<\2\2j\22\3\2\2\2kl\7/\2\2l\24\3")
        buf.write("\2\2\2mn\7<\2\2n\26\3\2\2\2op\7\"\2\2pq\7\"\2\2qr\7\"")
        buf.write("\2\2rs\7\"\2\2st\7\"\2\2tu\7\"\2\2uv\7\"\2\2vw\7\"\2\2")
        buf.write("w\30\3\2\2\2xy\7\"\2\2yz\7\"\2\2z{\7\"\2\2{|\7\"\2\2|")
        buf.write("}\7\"\2\2}~\7\"\2\2~\32\3\2\2\2\177\u0080\7\"\2\2\u0080")
        buf.write("\u0081\7\"\2\2\u0081\u0082\7\"\2\2\u0082\u0083\7\"\2\2")
        buf.write("\u0083\34\3\2\2\2\u0084\u0085\7\"\2\2\u0085\u0086\7\"")
        buf.write("\2\2\u0086\36\3\2\2\2\u0087\u0089\7)\2\2\u0088\u008a\n")
        buf.write("\2\2\2\u0089\u0088\3\2\2\2\u008a\u008b\3\2\2\2\u008b\u0089")
        buf.write("\3\2\2\2\u008b\u008c\3\2\2\2\u008c\u008d\3\2\2\2\u008d")
        buf.write("\u008e\7)\2\2\u008e \3\2\2\2\u008f\u0091\t\3\2\2\u0090")
        buf.write("\u008f\3\2\2\2\u0091\u0092\3\2\2\2\u0092\u0090\3\2\2\2")
        buf.write("\u0092\u0093\3\2\2\2\u0093\u0094\3\2\2\2\u0094\u0096\7")
        buf.write("\60\2\2\u0095\u0097\t\3\2\2\u0096\u0095\3\2\2\2\u0097")
        buf.write("\u0098\3\2\2\2\u0098\u0096\3\2\2\2\u0098\u0099\3\2\2\2")
        buf.write("\u0099\u009a\3\2\2\2\u009a\u009c\7\60\2\2\u009b\u009d")
        buf.write("\t\3\2\2\u009c\u009b\3\2\2\2\u009d\u009e\3\2\2\2\u009e")
        buf.write("\u009c\3\2\2\2\u009e\u009f\3\2\2\2\u009f\u00a0\3\2\2\2")
        buf.write("\u00a0\u00a2\7\60\2\2\u00a1\u00a3\t\3\2\2\u00a2\u00a1")
        buf.write("\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4\u00a2\3\2\2\2\u00a4")
        buf.write("\u00a5\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a6\u00a8\7\61\2")
        buf.write("\2\u00a7\u00a9\t\3\2\2\u00a8\u00a7\3\2\2\2\u00a9\u00aa")
        buf.write("\3\2\2\2\u00aa\u00a8\3\2\2\2\u00aa\u00ab\3\2\2\2\u00ab")
        buf.write("\"\3\2\2\2\u00ac\u00ae\t\4\2\2\u00ad\u00ac\3\2\2\2\u00ae")
        buf.write("\u00af\3\2\2\2\u00af\u00ad\3\2\2\2\u00af\u00b0\3\2\2\2")
        buf.write("\u00b0$\3\2\2\2\u00b1\u00b3\7\17\2\2\u00b2\u00b1\3\2\2")
        buf.write("\2\u00b2\u00b3\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4\u00b5")
        buf.write("\7\f\2\2\u00b5&\3\2\2\2\u00b6\u00b8\t\5\2\2\u00b7\u00b6")
        buf.write("\3\2\2\2\u00b8\u00b9\3\2\2\2\u00b9\u00b7\3\2\2\2\u00b9")
        buf.write("\u00ba\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb\u00bc\b\24\2")
        buf.write("\2\u00bc(\3\2\2\2\f\2\u008b\u0092\u0098\u009e\u00a4\u00aa")
        buf.write("\u00af\u00b2\u00b9\3\b\2\2")
        return buf.getvalue()


class DockerComposeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    VERSION_KEY = 1
    SERVICES_KEY = 2
    NETWORKS_KEY = 3
    IMAGE_KEY = 4
    DRIVER_KEY = 5
    IPAM_KEY = 6
    CONFIG_KEY = 7
    SUBNET_KEY = 8
    DASH = 9
    COLON = 10
    INDENT8 = 11
    INDENT6 = 12
    INDENT4 = 13
    INDENT2 = 14
    QUOTED_STRING = 15
    IP_SUBNET = 16
    ID = 17
    NEWLINE = 18
    WS = 19

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'version:'", "'services:'", "'networks:'", "'image:'", "'driver:'", 
            "'ipam:'", "'config:'", "'subnet:'", "'-'", "':'", "'        '", 
            "'      '", "'    '", "'  '" ]

    symbolicNames = [ "<INVALID>",
            "VERSION_KEY", "SERVICES_KEY", "NETWORKS_KEY", "IMAGE_KEY", 
            "DRIVER_KEY", "IPAM_KEY", "CONFIG_KEY", "SUBNET_KEY", "DASH", 
            "COLON", "INDENT8", "INDENT6", "INDENT4", "INDENT2", "QUOTED_STRING", 
            "IP_SUBNET", "ID", "NEWLINE", "WS" ]

    ruleNames = [ "VERSION_KEY", "SERVICES_KEY", "NETWORKS_KEY", "IMAGE_KEY", 
                  "DRIVER_KEY", "IPAM_KEY", "CONFIG_KEY", "SUBNET_KEY", 
                  "DASH", "COLON", "INDENT8", "INDENT6", "INDENT4", "INDENT2", 
                  "QUOTED_STRING", "IP_SUBNET", "ID", "NEWLINE", "WS" ]

    grammarFileName = "DockerCompose.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


