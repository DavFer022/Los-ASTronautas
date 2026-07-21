# Generated from experimento_parsers/grammars/DockerCompose.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .DockerComposeParser import DockerComposeParser
else:
    from DockerComposeParser import DockerComposeParser

# This class defines a complete listener for a parse tree produced by DockerComposeParser.
class DockerComposeListener(ParseTreeListener):

    # Enter a parse tree produced by DockerComposeParser#dockerComposeFile.
    def enterDockerComposeFile(self, ctx:DockerComposeParser.DockerComposeFileContext):
        pass

    # Exit a parse tree produced by DockerComposeParser#dockerComposeFile.
    def exitDockerComposeFile(self, ctx:DockerComposeParser.DockerComposeFileContext):
        pass


    # Enter a parse tree produced by DockerComposeParser#versionDecl.
    def enterVersionDecl(self, ctx:DockerComposeParser.VersionDeclContext):
        pass

    # Exit a parse tree produced by DockerComposeParser#versionDecl.
    def exitVersionDecl(self, ctx:DockerComposeParser.VersionDeclContext):
        pass


    # Enter a parse tree produced by DockerComposeParser#servicesDecl.
    def enterServicesDecl(self, ctx:DockerComposeParser.ServicesDeclContext):
        pass

    # Exit a parse tree produced by DockerComposeParser#servicesDecl.
    def exitServicesDecl(self, ctx:DockerComposeParser.ServicesDeclContext):
        pass


    # Enter a parse tree produced by DockerComposeParser#serviceEntry.
    def enterServiceEntry(self, ctx:DockerComposeParser.ServiceEntryContext):
        pass

    # Exit a parse tree produced by DockerComposeParser#serviceEntry.
    def exitServiceEntry(self, ctx:DockerComposeParser.ServiceEntryContext):
        pass


    # Enter a parse tree produced by DockerComposeParser#serviceBody.
    def enterServiceBody(self, ctx:DockerComposeParser.ServiceBodyContext):
        pass

    # Exit a parse tree produced by DockerComposeParser#serviceBody.
    def exitServiceBody(self, ctx:DockerComposeParser.ServiceBodyContext):
        pass


    # Enter a parse tree produced by DockerComposeParser#serviceAttr.
    def enterServiceAttr(self, ctx:DockerComposeParser.ServiceAttrContext):
        pass

    # Exit a parse tree produced by DockerComposeParser#serviceAttr.
    def exitServiceAttr(self, ctx:DockerComposeParser.ServiceAttrContext):
        pass


    # Enter a parse tree produced by DockerComposeParser#imageVal.
    def enterImageVal(self, ctx:DockerComposeParser.ImageValContext):
        pass

    # Exit a parse tree produced by DockerComposeParser#imageVal.
    def exitImageVal(self, ctx:DockerComposeParser.ImageValContext):
        pass


    # Enter a parse tree produced by DockerComposeParser#networkRef.
    def enterNetworkRef(self, ctx:DockerComposeParser.NetworkRefContext):
        pass

    # Exit a parse tree produced by DockerComposeParser#networkRef.
    def exitNetworkRef(self, ctx:DockerComposeParser.NetworkRefContext):
        pass


    # Enter a parse tree produced by DockerComposeParser#networksDecl.
    def enterNetworksDecl(self, ctx:DockerComposeParser.NetworksDeclContext):
        pass

    # Exit a parse tree produced by DockerComposeParser#networksDecl.
    def exitNetworksDecl(self, ctx:DockerComposeParser.NetworksDeclContext):
        pass


    # Enter a parse tree produced by DockerComposeParser#networkEntry.
    def enterNetworkEntry(self, ctx:DockerComposeParser.NetworkEntryContext):
        pass

    # Exit a parse tree produced by DockerComposeParser#networkEntry.
    def exitNetworkEntry(self, ctx:DockerComposeParser.NetworkEntryContext):
        pass


    # Enter a parse tree produced by DockerComposeParser#networkBody.
    def enterNetworkBody(self, ctx:DockerComposeParser.NetworkBodyContext):
        pass

    # Exit a parse tree produced by DockerComposeParser#networkBody.
    def exitNetworkBody(self, ctx:DockerComposeParser.NetworkBodyContext):
        pass


    # Enter a parse tree produced by DockerComposeParser#networkAttr.
    def enterNetworkAttr(self, ctx:DockerComposeParser.NetworkAttrContext):
        pass

    # Exit a parse tree produced by DockerComposeParser#networkAttr.
    def exitNetworkAttr(self, ctx:DockerComposeParser.NetworkAttrContext):
        pass


    # Enter a parse tree produced by DockerComposeParser#ipamBody.
    def enterIpamBody(self, ctx:DockerComposeParser.IpamBodyContext):
        pass

    # Exit a parse tree produced by DockerComposeParser#ipamBody.
    def exitIpamBody(self, ctx:DockerComposeParser.IpamBodyContext):
        pass


    # Enter a parse tree produced by DockerComposeParser#configBody.
    def enterConfigBody(self, ctx:DockerComposeParser.ConfigBodyContext):
        pass

    # Exit a parse tree produced by DockerComposeParser#configBody.
    def exitConfigBody(self, ctx:DockerComposeParser.ConfigBodyContext):
        pass


    # Enter a parse tree produced by DockerComposeParser#emptyLine.
    def enterEmptyLine(self, ctx:DockerComposeParser.EmptyLineContext):
        pass

    # Exit a parse tree produced by DockerComposeParser#emptyLine.
    def exitEmptyLine(self, ctx:DockerComposeParser.EmptyLineContext):
        pass



del DockerComposeParser