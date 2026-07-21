# Generated from experimento_parsers/grammars/DockerCompose.g4 by ANTLR 4.9.3
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\25")
        buf.write("\u0086\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\3\2\3\2\3\2\3\2\7\2%\n\2\f\2")
        buf.write("\16\2(\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4\6\4\63")
        buf.write("\n\4\r\4\16\4\64\3\5\3\5\3\5\3\5\3\5\3\5\3\6\6\6>\n\6")
        buf.write("\r\6\16\6?\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\6\7K\n")
        buf.write("\7\r\7\16\7L\5\7O\n\7\3\b\3\b\3\b\5\bT\n\b\3\b\5\bW\n")
        buf.write("\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\6\na\n\n\r\n\16\nb")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\f\6\fl\n\f\r\f\16\fm")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\5\rx\n\r\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20")
        buf.write("\2\2\21\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36\2\2\2\u0083")
        buf.write("\2&\3\2\2\2\4+\3\2\2\2\6/\3\2\2\2\b\66\3\2\2\2\n=\3\2")
        buf.write("\2\2\fN\3\2\2\2\16V\3\2\2\2\20X\3\2\2\2\22]\3\2\2\2\24")
        buf.write("d\3\2\2\2\26k\3\2\2\2\30w\3\2\2\2\32y\3\2\2\2\34~\3\2")
        buf.write("\2\2\36\u0083\3\2\2\2 %\5\4\3\2!%\5\6\4\2\"%\5\22\n\2")
        buf.write("#%\5\36\20\2$ \3\2\2\2$!\3\2\2\2$\"\3\2\2\2$#\3\2\2\2")
        buf.write("%(\3\2\2\2&$\3\2\2\2&\'\3\2\2\2\')\3\2\2\2(&\3\2\2\2)")
        buf.write("*\7\2\2\3*\3\3\2\2\2+,\7\3\2\2,-\7\21\2\2-.\7\24\2\2.")
        buf.write("\5\3\2\2\2/\60\7\4\2\2\60\62\7\24\2\2\61\63\5\b\5\2\62")
        buf.write("\61\3\2\2\2\63\64\3\2\2\2\64\62\3\2\2\2\64\65\3\2\2\2")
        buf.write("\65\7\3\2\2\2\66\67\7\20\2\2\678\7\23\2\289\7\f\2\29:")
        buf.write("\7\24\2\2:;\5\n\6\2;\t\3\2\2\2<>\5\f\7\2=<\3\2\2\2>?\3")
        buf.write("\2\2\2?=\3\2\2\2?@\3\2\2\2@\13\3\2\2\2AB\7\17\2\2BC\7")
        buf.write("\6\2\2CD\5\16\b\2DE\7\24\2\2EO\3\2\2\2FG\7\17\2\2GH\7")
        buf.write("\5\2\2HJ\7\24\2\2IK\5\20\t\2JI\3\2\2\2KL\3\2\2\2LJ\3\2")
        buf.write("\2\2LM\3\2\2\2MO\3\2\2\2NA\3\2\2\2NF\3\2\2\2O\r\3\2\2")
        buf.write("\2PS\7\23\2\2QR\7\f\2\2RT\7\23\2\2SQ\3\2\2\2ST\3\2\2\2")
        buf.write("TW\3\2\2\2UW\7\21\2\2VP\3\2\2\2VU\3\2\2\2W\17\3\2\2\2")
        buf.write("XY\7\16\2\2YZ\7\13\2\2Z[\7\23\2\2[\\\7\24\2\2\\\21\3\2")
        buf.write("\2\2]^\7\5\2\2^`\7\24\2\2_a\5\24\13\2`_\3\2\2\2ab\3\2")
        buf.write("\2\2b`\3\2\2\2bc\3\2\2\2c\23\3\2\2\2de\7\20\2\2ef\7\23")
        buf.write("\2\2fg\7\f\2\2gh\7\24\2\2hi\5\26\f\2i\25\3\2\2\2jl\5\30")
        buf.write("\r\2kj\3\2\2\2lm\3\2\2\2mk\3\2\2\2mn\3\2\2\2n\27\3\2\2")
        buf.write("\2op\7\17\2\2pq\7\7\2\2qr\7\23\2\2rx\7\24\2\2st\7\17\2")
        buf.write("\2tu\7\b\2\2uv\7\24\2\2vx\5\32\16\2wo\3\2\2\2ws\3\2\2")
        buf.write("\2x\31\3\2\2\2yz\7\16\2\2z{\7\t\2\2{|\7\24\2\2|}\5\34")
        buf.write("\17\2}\33\3\2\2\2~\177\7\r\2\2\177\u0080\7\n\2\2\u0080")
        buf.write("\u0081\7\22\2\2\u0081\u0082\7\24\2\2\u0082\35\3\2\2\2")
        buf.write("\u0083\u0084\7\24\2\2\u0084\37\3\2\2\2\r$&\64?LNSVbmw")
        return buf.getvalue()


class DockerComposeParser ( Parser ):

    grammarFileName = "DockerCompose.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'version:'", "'services:'", "'networks:'", 
                     "'image:'", "'driver:'", "'ipam:'", "'config:'", "'subnet:'", 
                     "'-'", "':'", "'        '", "'      '", "'    '", "'  '" ]

    symbolicNames = [ "<INVALID>", "VERSION_KEY", "SERVICES_KEY", "NETWORKS_KEY", 
                      "IMAGE_KEY", "DRIVER_KEY", "IPAM_KEY", "CONFIG_KEY", 
                      "SUBNET_KEY", "DASH", "COLON", "INDENT8", "INDENT6", 
                      "INDENT4", "INDENT2", "QUOTED_STRING", "IP_SUBNET", 
                      "ID", "NEWLINE", "WS" ]

    RULE_dockerComposeFile = 0
    RULE_versionDecl = 1
    RULE_servicesDecl = 2
    RULE_serviceEntry = 3
    RULE_serviceBody = 4
    RULE_serviceAttr = 5
    RULE_imageVal = 6
    RULE_networkRef = 7
    RULE_networksDecl = 8
    RULE_networkEntry = 9
    RULE_networkBody = 10
    RULE_networkAttr = 11
    RULE_ipamBody = 12
    RULE_configBody = 13
    RULE_emptyLine = 14

    ruleNames =  [ "dockerComposeFile", "versionDecl", "servicesDecl", "serviceEntry", 
                   "serviceBody", "serviceAttr", "imageVal", "networkRef", 
                   "networksDecl", "networkEntry", "networkBody", "networkAttr", 
                   "ipamBody", "configBody", "emptyLine" ]

    EOF = Token.EOF
    VERSION_KEY=1
    SERVICES_KEY=2
    NETWORKS_KEY=3
    IMAGE_KEY=4
    DRIVER_KEY=5
    IPAM_KEY=6
    CONFIG_KEY=7
    SUBNET_KEY=8
    DASH=9
    COLON=10
    INDENT8=11
    INDENT6=12
    INDENT4=13
    INDENT2=14
    QUOTED_STRING=15
    IP_SUBNET=16
    ID=17
    NEWLINE=18
    WS=19

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class DockerComposeFileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(DockerComposeParser.EOF, 0)

        def versionDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DockerComposeParser.VersionDeclContext)
            else:
                return self.getTypedRuleContext(DockerComposeParser.VersionDeclContext,i)


        def servicesDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DockerComposeParser.ServicesDeclContext)
            else:
                return self.getTypedRuleContext(DockerComposeParser.ServicesDeclContext,i)


        def networksDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DockerComposeParser.NetworksDeclContext)
            else:
                return self.getTypedRuleContext(DockerComposeParser.NetworksDeclContext,i)


        def emptyLine(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DockerComposeParser.EmptyLineContext)
            else:
                return self.getTypedRuleContext(DockerComposeParser.EmptyLineContext,i)


        def getRuleIndex(self):
            return DockerComposeParser.RULE_dockerComposeFile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDockerComposeFile" ):
                listener.enterDockerComposeFile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDockerComposeFile" ):
                listener.exitDockerComposeFile(self)




    def dockerComposeFile(self):

        localctx = DockerComposeParser.DockerComposeFileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_dockerComposeFile)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << DockerComposeParser.VERSION_KEY) | (1 << DockerComposeParser.SERVICES_KEY) | (1 << DockerComposeParser.NETWORKS_KEY) | (1 << DockerComposeParser.NEWLINE))) != 0):
                self.state = 34
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [DockerComposeParser.VERSION_KEY]:
                    self.state = 30
                    self.versionDecl()
                    pass
                elif token in [DockerComposeParser.SERVICES_KEY]:
                    self.state = 31
                    self.servicesDecl()
                    pass
                elif token in [DockerComposeParser.NETWORKS_KEY]:
                    self.state = 32
                    self.networksDecl()
                    pass
                elif token in [DockerComposeParser.NEWLINE]:
                    self.state = 33
                    self.emptyLine()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 38
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 39
            self.match(DockerComposeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VersionDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VERSION_KEY(self):
            return self.getToken(DockerComposeParser.VERSION_KEY, 0)

        def QUOTED_STRING(self):
            return self.getToken(DockerComposeParser.QUOTED_STRING, 0)

        def NEWLINE(self):
            return self.getToken(DockerComposeParser.NEWLINE, 0)

        def getRuleIndex(self):
            return DockerComposeParser.RULE_versionDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVersionDecl" ):
                listener.enterVersionDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVersionDecl" ):
                listener.exitVersionDecl(self)




    def versionDecl(self):

        localctx = DockerComposeParser.VersionDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_versionDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(DockerComposeParser.VERSION_KEY)
            self.state = 42
            self.match(DockerComposeParser.QUOTED_STRING)
            self.state = 43
            self.match(DockerComposeParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ServicesDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SERVICES_KEY(self):
            return self.getToken(DockerComposeParser.SERVICES_KEY, 0)

        def NEWLINE(self):
            return self.getToken(DockerComposeParser.NEWLINE, 0)

        def serviceEntry(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DockerComposeParser.ServiceEntryContext)
            else:
                return self.getTypedRuleContext(DockerComposeParser.ServiceEntryContext,i)


        def getRuleIndex(self):
            return DockerComposeParser.RULE_servicesDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterServicesDecl" ):
                listener.enterServicesDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitServicesDecl" ):
                listener.exitServicesDecl(self)




    def servicesDecl(self):

        localctx = DockerComposeParser.ServicesDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_servicesDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(DockerComposeParser.SERVICES_KEY)
            self.state = 46
            self.match(DockerComposeParser.NEWLINE)
            self.state = 48 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 47
                self.serviceEntry()
                self.state = 50 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==DockerComposeParser.INDENT2):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ServiceEntryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INDENT2(self):
            return self.getToken(DockerComposeParser.INDENT2, 0)

        def ID(self):
            return self.getToken(DockerComposeParser.ID, 0)

        def COLON(self):
            return self.getToken(DockerComposeParser.COLON, 0)

        def NEWLINE(self):
            return self.getToken(DockerComposeParser.NEWLINE, 0)

        def serviceBody(self):
            return self.getTypedRuleContext(DockerComposeParser.ServiceBodyContext,0)


        def getRuleIndex(self):
            return DockerComposeParser.RULE_serviceEntry

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterServiceEntry" ):
                listener.enterServiceEntry(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitServiceEntry" ):
                listener.exitServiceEntry(self)




    def serviceEntry(self):

        localctx = DockerComposeParser.ServiceEntryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_serviceEntry)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(DockerComposeParser.INDENT2)
            self.state = 53
            self.match(DockerComposeParser.ID)
            self.state = 54
            self.match(DockerComposeParser.COLON)
            self.state = 55
            self.match(DockerComposeParser.NEWLINE)
            self.state = 56
            self.serviceBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ServiceBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def serviceAttr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DockerComposeParser.ServiceAttrContext)
            else:
                return self.getTypedRuleContext(DockerComposeParser.ServiceAttrContext,i)


        def getRuleIndex(self):
            return DockerComposeParser.RULE_serviceBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterServiceBody" ):
                listener.enterServiceBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitServiceBody" ):
                listener.exitServiceBody(self)




    def serviceBody(self):

        localctx = DockerComposeParser.ServiceBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_serviceBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 58
                self.serviceAttr()
                self.state = 61 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==DockerComposeParser.INDENT4):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ServiceAttrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INDENT4(self):
            return self.getToken(DockerComposeParser.INDENT4, 0)

        def IMAGE_KEY(self):
            return self.getToken(DockerComposeParser.IMAGE_KEY, 0)

        def imageVal(self):
            return self.getTypedRuleContext(DockerComposeParser.ImageValContext,0)


        def NEWLINE(self):
            return self.getToken(DockerComposeParser.NEWLINE, 0)

        def NETWORKS_KEY(self):
            return self.getToken(DockerComposeParser.NETWORKS_KEY, 0)

        def networkRef(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DockerComposeParser.NetworkRefContext)
            else:
                return self.getTypedRuleContext(DockerComposeParser.NetworkRefContext,i)


        def getRuleIndex(self):
            return DockerComposeParser.RULE_serviceAttr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterServiceAttr" ):
                listener.enterServiceAttr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitServiceAttr" ):
                listener.exitServiceAttr(self)




    def serviceAttr(self):

        localctx = DockerComposeParser.ServiceAttrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_serviceAttr)
        self._la = 0 # Token type
        try:
            self.state = 76
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self.match(DockerComposeParser.INDENT4)
                self.state = 64
                self.match(DockerComposeParser.IMAGE_KEY)
                self.state = 65
                self.imageVal()
                self.state = 66
                self.match(DockerComposeParser.NEWLINE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 68
                self.match(DockerComposeParser.INDENT4)
                self.state = 69
                self.match(DockerComposeParser.NETWORKS_KEY)
                self.state = 70
                self.match(DockerComposeParser.NEWLINE)
                self.state = 72 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 71
                    self.networkRef()
                    self.state = 74 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==DockerComposeParser.INDENT6):
                        break

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImageValContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(DockerComposeParser.ID)
            else:
                return self.getToken(DockerComposeParser.ID, i)

        def COLON(self):
            return self.getToken(DockerComposeParser.COLON, 0)

        def QUOTED_STRING(self):
            return self.getToken(DockerComposeParser.QUOTED_STRING, 0)

        def getRuleIndex(self):
            return DockerComposeParser.RULE_imageVal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImageVal" ):
                listener.enterImageVal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImageVal" ):
                listener.exitImageVal(self)




    def imageVal(self):

        localctx = DockerComposeParser.ImageValContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_imageVal)
        self._la = 0 # Token type
        try:
            self.state = 84
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [DockerComposeParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 78
                self.match(DockerComposeParser.ID)
                self.state = 81
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==DockerComposeParser.COLON:
                    self.state = 79
                    self.match(DockerComposeParser.COLON)
                    self.state = 80
                    self.match(DockerComposeParser.ID)


                pass
            elif token in [DockerComposeParser.QUOTED_STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 83
                self.match(DockerComposeParser.QUOTED_STRING)
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


    class NetworkRefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INDENT6(self):
            return self.getToken(DockerComposeParser.INDENT6, 0)

        def DASH(self):
            return self.getToken(DockerComposeParser.DASH, 0)

        def ID(self):
            return self.getToken(DockerComposeParser.ID, 0)

        def NEWLINE(self):
            return self.getToken(DockerComposeParser.NEWLINE, 0)

        def getRuleIndex(self):
            return DockerComposeParser.RULE_networkRef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNetworkRef" ):
                listener.enterNetworkRef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNetworkRef" ):
                listener.exitNetworkRef(self)




    def networkRef(self):

        localctx = DockerComposeParser.NetworkRefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_networkRef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(DockerComposeParser.INDENT6)
            self.state = 87
            self.match(DockerComposeParser.DASH)
            self.state = 88
            self.match(DockerComposeParser.ID)
            self.state = 89
            self.match(DockerComposeParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NetworksDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NETWORKS_KEY(self):
            return self.getToken(DockerComposeParser.NETWORKS_KEY, 0)

        def NEWLINE(self):
            return self.getToken(DockerComposeParser.NEWLINE, 0)

        def networkEntry(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DockerComposeParser.NetworkEntryContext)
            else:
                return self.getTypedRuleContext(DockerComposeParser.NetworkEntryContext,i)


        def getRuleIndex(self):
            return DockerComposeParser.RULE_networksDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNetworksDecl" ):
                listener.enterNetworksDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNetworksDecl" ):
                listener.exitNetworksDecl(self)




    def networksDecl(self):

        localctx = DockerComposeParser.NetworksDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_networksDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(DockerComposeParser.NETWORKS_KEY)
            self.state = 92
            self.match(DockerComposeParser.NEWLINE)
            self.state = 94 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 93
                self.networkEntry()
                self.state = 96 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==DockerComposeParser.INDENT2):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NetworkEntryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INDENT2(self):
            return self.getToken(DockerComposeParser.INDENT2, 0)

        def ID(self):
            return self.getToken(DockerComposeParser.ID, 0)

        def COLON(self):
            return self.getToken(DockerComposeParser.COLON, 0)

        def NEWLINE(self):
            return self.getToken(DockerComposeParser.NEWLINE, 0)

        def networkBody(self):
            return self.getTypedRuleContext(DockerComposeParser.NetworkBodyContext,0)


        def getRuleIndex(self):
            return DockerComposeParser.RULE_networkEntry

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNetworkEntry" ):
                listener.enterNetworkEntry(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNetworkEntry" ):
                listener.exitNetworkEntry(self)




    def networkEntry(self):

        localctx = DockerComposeParser.NetworkEntryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_networkEntry)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(DockerComposeParser.INDENT2)
            self.state = 99
            self.match(DockerComposeParser.ID)
            self.state = 100
            self.match(DockerComposeParser.COLON)
            self.state = 101
            self.match(DockerComposeParser.NEWLINE)
            self.state = 102
            self.networkBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NetworkBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def networkAttr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DockerComposeParser.NetworkAttrContext)
            else:
                return self.getTypedRuleContext(DockerComposeParser.NetworkAttrContext,i)


        def getRuleIndex(self):
            return DockerComposeParser.RULE_networkBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNetworkBody" ):
                listener.enterNetworkBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNetworkBody" ):
                listener.exitNetworkBody(self)




    def networkBody(self):

        localctx = DockerComposeParser.NetworkBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_networkBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 104
                self.networkAttr()
                self.state = 107 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==DockerComposeParser.INDENT4):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NetworkAttrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INDENT4(self):
            return self.getToken(DockerComposeParser.INDENT4, 0)

        def DRIVER_KEY(self):
            return self.getToken(DockerComposeParser.DRIVER_KEY, 0)

        def ID(self):
            return self.getToken(DockerComposeParser.ID, 0)

        def NEWLINE(self):
            return self.getToken(DockerComposeParser.NEWLINE, 0)

        def IPAM_KEY(self):
            return self.getToken(DockerComposeParser.IPAM_KEY, 0)

        def ipamBody(self):
            return self.getTypedRuleContext(DockerComposeParser.IpamBodyContext,0)


        def getRuleIndex(self):
            return DockerComposeParser.RULE_networkAttr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNetworkAttr" ):
                listener.enterNetworkAttr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNetworkAttr" ):
                listener.exitNetworkAttr(self)




    def networkAttr(self):

        localctx = DockerComposeParser.NetworkAttrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_networkAttr)
        try:
            self.state = 117
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 109
                self.match(DockerComposeParser.INDENT4)
                self.state = 110
                self.match(DockerComposeParser.DRIVER_KEY)
                self.state = 111
                self.match(DockerComposeParser.ID)
                self.state = 112
                self.match(DockerComposeParser.NEWLINE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 113
                self.match(DockerComposeParser.INDENT4)
                self.state = 114
                self.match(DockerComposeParser.IPAM_KEY)
                self.state = 115
                self.match(DockerComposeParser.NEWLINE)
                self.state = 116
                self.ipamBody()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IpamBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INDENT6(self):
            return self.getToken(DockerComposeParser.INDENT6, 0)

        def CONFIG_KEY(self):
            return self.getToken(DockerComposeParser.CONFIG_KEY, 0)

        def NEWLINE(self):
            return self.getToken(DockerComposeParser.NEWLINE, 0)

        def configBody(self):
            return self.getTypedRuleContext(DockerComposeParser.ConfigBodyContext,0)


        def getRuleIndex(self):
            return DockerComposeParser.RULE_ipamBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIpamBody" ):
                listener.enterIpamBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIpamBody" ):
                listener.exitIpamBody(self)




    def ipamBody(self):

        localctx = DockerComposeParser.IpamBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_ipamBody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(DockerComposeParser.INDENT6)
            self.state = 120
            self.match(DockerComposeParser.CONFIG_KEY)
            self.state = 121
            self.match(DockerComposeParser.NEWLINE)
            self.state = 122
            self.configBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConfigBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INDENT8(self):
            return self.getToken(DockerComposeParser.INDENT8, 0)

        def SUBNET_KEY(self):
            return self.getToken(DockerComposeParser.SUBNET_KEY, 0)

        def IP_SUBNET(self):
            return self.getToken(DockerComposeParser.IP_SUBNET, 0)

        def NEWLINE(self):
            return self.getToken(DockerComposeParser.NEWLINE, 0)

        def getRuleIndex(self):
            return DockerComposeParser.RULE_configBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConfigBody" ):
                listener.enterConfigBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConfigBody" ):
                listener.exitConfigBody(self)




    def configBody(self):

        localctx = DockerComposeParser.ConfigBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_configBody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.match(DockerComposeParser.INDENT8)
            self.state = 125
            self.match(DockerComposeParser.SUBNET_KEY)
            self.state = 126
            self.match(DockerComposeParser.IP_SUBNET)
            self.state = 127
            self.match(DockerComposeParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EmptyLineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(DockerComposeParser.NEWLINE, 0)

        def getRuleIndex(self):
            return DockerComposeParser.RULE_emptyLine

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmptyLine" ):
                listener.enterEmptyLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmptyLine" ):
                listener.exitEmptyLine(self)




    def emptyLine(self):

        localctx = DockerComposeParser.EmptyLineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_emptyLine)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(DockerComposeParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





