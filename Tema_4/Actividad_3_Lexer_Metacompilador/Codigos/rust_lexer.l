%{
#include <stdio.h>
// Aquí va el código C puro que necesites, como variables o librerías[cite: 223].
%}

%option noyywrap

%%
"fn"        { printf("TOKEN: RESERVADA, Lexema: %s\n", yytext); }
"let"       { printf("TOKEN: RESERVADA, Lexema: %s\n", yytext); }
"mut"       { printf("TOKEN: RESERVADA, Lexema: %s\n", yytext); }
"i32"       { printf("TOKEN: TIPO_DATO, Lexema: %s\n", yytext); }

[0-9]+      { printf("TOKEN: ENTERO, Lexema: %s\n", yytext); }
[a-zA-Z_][a-zA-Z0-9_]* { printf("TOKEN: IDENTIFICADOR, Lexema: %s\n", yytext); }

"+"|"-"|"*"|"/"|"=" { printf("TOKEN: OPERADOR, Lexema: %s\n", yytext); }
"{"|"}"|"("|")"|";"|":" { printf("TOKEN: SIMBOLO, Lexema: %s\n", yytext); }

[ \t\n]+    { /* Ignorar espacios, tabulaciones y saltos de línea */ }
.           { printf("ERROR LEXICO: Caracter no reconocido: %s\n", yytext); }
%%

int main(int argc, char **argv) {
    if (argc > 1) {
        FILE *file = fopen(argv[1], "r");
        if (!file) {
            perror("Error al abrir el archivo");
            return 1;
        }
        yyin = file;
    }
    yylex();
    return 0;
}
