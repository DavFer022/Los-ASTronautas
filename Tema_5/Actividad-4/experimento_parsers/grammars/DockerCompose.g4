grammar DockerCompose;

// Parser Rules
dockerComposeFile
    : (versionDecl | servicesDecl | networksDecl | emptyLine)* EOF
    ;

versionDecl
    : VERSION_KEY QUOTED_STRING NEWLINE
    ;

servicesDecl
    : SERVICES_KEY NEWLINE serviceEntry+
    ;

serviceEntry
    : INDENT2 ID COLON NEWLINE serviceBody
    ;

serviceBody
    : serviceAttr+
    ;

serviceAttr
    : INDENT4 IMAGE_KEY imageVal NEWLINE
    | INDENT4 NETWORKS_KEY NEWLINE networkRef+
    ;

imageVal
    : ID (COLON ID)?
    | QUOTED_STRING
    ;

networkRef
    : INDENT6 DASH ID NEWLINE
    ;

networksDecl
    : NETWORKS_KEY NEWLINE networkEntry+
    ;

networkEntry
    : INDENT2 ID COLON NEWLINE networkBody
    ;

networkBody
    : networkAttr+
    ;

networkAttr
    : INDENT4 DRIVER_KEY ID NEWLINE
    | INDENT4 IPAM_KEY NEWLINE ipamBody
    ;

ipamBody
    : INDENT6 CONFIG_KEY NEWLINE configBody
    ;

configBody
    : INDENT8 SUBNET_KEY IP_SUBNET NEWLINE
    ;

emptyLine
    : NEWLINE
    ;

// Lexer Rules
VERSION_KEY  : 'version:' ;
SERVICES_KEY : 'services:' ;
NETWORKS_KEY : 'networks:' ;
IMAGE_KEY    : 'image:' ;
DRIVER_KEY   : 'driver:' ;
IPAM_KEY     : 'ipam:' ;
CONFIG_KEY   : 'config:' ;
SUBNET_KEY   : 'subnet:' ;

DASH  : '-' ;
COLON : ':' ;

INDENT8 : '        ' ;
INDENT6 : '      ' ;
INDENT4 : '    ' ;
INDENT2 : '  ' ;

QUOTED_STRING : '\'' ~[\r\n']+ '\'' ;

IP_SUBNET : [0-9]+ '.' [0-9]+ '.' [0-9]+ '.' [0-9]+ '/' [0-9]+ ;

ID : [a-zA-Z0-9_-]+ ;

NEWLINE : '\r'? '\n' ;

WS : [ \t]+ -> skip ;
