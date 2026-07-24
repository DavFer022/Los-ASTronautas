%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "parser.tab.h"
%}

%option noyywrap

%%

"version:"      { return VERSION_KEY; }
"services:"     { return SERVICES_KEY; }
"networks:"     { return NETWORKS_KEY; }
"image:"        { return IMAGE_KEY; }
"driver:"       { return DRIVER_KEY; }
"ipam:"         { return IPAM_KEY; }
"config:"       { return CONFIG_KEY; }
"subnet:"       { return SUBNET_KEY; }

"        "      { return INDENT8; }
"      "        { return INDENT6; }
"    "          { return INDENT4; }
"  "            { return INDENT2; }

"-"             { return DASH; }
":"             { return COLON; }

"'"[^'\r\n]+"'" { yylval.sval = strdup(yytext); return QUOTED_STRING; }

[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+\/[0-9]+ { yylval.sval = strdup(yytext); return IP_SUBNET; }

[a-zA-Z0-9_-]+  { yylval.sval = strdup(yytext); return ID; }

\r?\n           { return NEWLINE; }

[ \t]+          { /* Ignorar espacios y tabs internos */ }

.               { return yytext[0]; }

%%
