%{
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <dirent.h>  


/* Función auxiliar para imprimir en formato tabla */
void imprimir_token(const char *tipo, const char *lexema) {
    printf("%-20s %s\n", tipo, lexema);
}

%}


%option noyywrap
%option yylineno

%%

 /* Palabras clave (cada una en su línea) */
fn          { imprimir_token("KEYWORD", yytext); }
let         { imprimir_token("KEYWORD", yytext); }
mut         { imprimir_token("KEYWORD", yytext); }
if          { imprimir_token("KEYWORD", yytext); }
else        { imprimir_token("KEYWORD", yytext); }
loop        { imprimir_token("KEYWORD", yytext); }
while       { imprimir_token("KEYWORD", yytext); }
for         { imprimir_token("KEYWORD", yytext); }
return      { imprimir_token("KEYWORD", yytext); }
match       { imprimir_token("KEYWORD", yytext); }
struct      { imprimir_token("KEYWORD", yytext); }
enum        { imprimir_token("KEYWORD", yytext); }
impl        { imprimir_token("KEYWORD", yytext); }
trait       { imprimir_token("KEYWORD", yytext); }
pub         { imprimir_token("KEYWORD", yytext); }
use         { imprimir_token("KEYWORD", yytext); }
mod         { imprimir_token("KEYWORD", yytext); }
type        { imprimir_token("KEYWORD", yytext); }
const       { imprimir_token("KEYWORD", yytext); }
static      { imprimir_token("KEYWORD", yytext); }
break       { imprimir_token("KEYWORD", yytext); }
continue    { imprimir_token("KEYWORD", yytext); }
unsafe      { imprimir_token("KEYWORD", yytext); }
extern      { imprimir_token("KEYWORD", yytext); }
crate       { imprimir_token("KEYWORD", yytext); }
super       { imprimir_token("KEYWORD", yytext); }
self        { imprimir_token("KEYWORD", yytext); }
Self        { imprimir_token("KEYWORD", yytext); }
async       { imprimir_token("KEYWORD", yytext); }
await       { imprimir_token("KEYWORD", yytext); }
move        { imprimir_token("KEYWORD", yytext); }
ref         { imprimir_token("KEYWORD", yytext); }
dyn         { imprimir_token("KEYWORD", yytext); }
where       { imprimir_token("KEYWORD", yytext); }
in          { imprimir_token("KEYWORD", yytext); }

 /* Tipos primitivos */
i8          { imprimir_token("TYPE", yytext); }
i16         { imprimir_token("TYPE", yytext); }
i32         { imprimir_token("TYPE", yytext); }
i64         { imprimir_token("TYPE", yytext); }
i128        { imprimir_token("TYPE", yytext); }
u8          { imprimir_token("TYPE", yytext); }
u16         { imprimir_token("TYPE", yytext); }
u32         { imprimir_token("TYPE", yytext); }
u64         { imprimir_token("TYPE", yytext); }
u128        { imprimir_token("TYPE", yytext); }
f32         { imprimir_token("TYPE", yytext); }
f64         { imprimir_token("TYPE", yytext); }
bool        { imprimir_token("TYPE", yytext); }
char        { imprimir_token("TYPE", yytext); }
str         { imprimir_token("TYPE", yytext); }
String      { imprimir_token("TYPE", yytext); }
Vec         { imprimir_token("TYPE", yytext); }
Option      { imprimir_token("TYPE", yytext); }
Result      { imprimir_token("TYPE", yytext); }

 /* Literales booleanos */
true        { imprimir_token("BOOL", yytext); }
false       { imprimir_token("BOOL", yytext); }

 /* Literales con sufijo de tipo */
[0-9]+i8    { imprimir_token("INT_SUFFIX", yytext); }
[0-9]+i16   { imprimir_token("INT_SUFFIX", yytext); }
[0-9]+i32   { imprimir_token("INT_SUFFIX", yytext); }
[0-9]+i64   { imprimir_token("INT_SUFFIX", yytext); }
[0-9]+i128  { imprimir_token("INT_SUFFIX", yytext); }
[0-9]+u8    { imprimir_token("INT_SUFFIX", yytext); }
[0-9]+u16   { imprimir_token("INT_SUFFIX", yytext); }
[0-9]+u32   { imprimir_token("INT_SUFFIX", yytext); }
[0-9]+u64   { imprimir_token("INT_SUFFIX", yytext); }
[0-9]+u128  { imprimir_token("INT_SUFFIX", yytext); }

 /* Números flotantes */
[0-9]+\.[0-9]+ { imprimir_token("FLOAT", yytext); }

 /* Enteros simples */
[0-9]+      { imprimir_token("INT", yytext); }

 /* Caracteres */
'([^'\\\n]|\\.)' { imprimir_token("CHAR", yytext); }

 /* Cadenas */
\"([^\"\\\n]|\\.)*\" { imprimir_token("STRING", yytext); }

 /* Operadores de varios caracteres */
"<<="       { imprimir_token("OP", yytext); }
">>="       { imprimir_token("OP", yytext); }
"&&"        { imprimir_token("OP", yytext); }
"||"        { imprimir_token("OP", yytext); }
"=="        { imprimir_token("OP", yytext); }
"!="        { imprimir_token("OP", yytext); }
"<="        { imprimir_token("OP", yytext); }
">="        { imprimir_token("OP", yytext); }
"+="        { imprimir_token("OP", yytext); }
"-="        { imprimir_token("OP", yytext); }
"*="        { imprimir_token("OP", yytext); }
"/="        { imprimir_token("OP", yytext); }
"%="        { imprimir_token("OP", yytext); }
"&="        { imprimir_token("OP", yytext); }
"|="        { imprimir_token("OP", yytext); }
"^="        { imprimir_token("OP", yytext); }
"<<"        { imprimir_token("OP", yytext); }
">>"        { imprimir_token("OP", yytext); }
".."        { imprimir_token("OP", yytext); }
"..."       { imprimir_token("OP", yytext); }
"=>"        { imprimir_token("OP", yytext); }
"->"        { imprimir_token("OP", yytext); }
"::"        { imprimir_token("OP", yytext); }

 /* Operadores de un solo carácter y símbolos */
"+"         { imprimir_token("OP", yytext); }
"-"         { imprimir_token("OP", yytext); }
"*"         { imprimir_token("OP", yytext); }
"/"         { imprimir_token("OP", yytext); }
"%"         { imprimir_token("OP", yytext); }
"="         { imprimir_token("OP", yytext); }
"<"         { imprimir_token("OP", yytext); }
">"         { imprimir_token("OP", yytext); }
"!"         { imprimir_token("OP", yytext); }
"&"         { imprimir_token("OP", yytext); }
"|"         { imprimir_token("OP", yytext); }
"^"         { imprimir_token("OP", yytext); }
"@"         { imprimir_token("OP", yytext); }
"#"         { imprimir_token("OP", yytext); }
"$"         { imprimir_token("OP", yytext); }
"?"         { imprimir_token("OP", yytext); }
"."         { imprimir_token("DOT", yytext); }
","         { imprimir_token("COMMA", yytext); }
";"         { imprimir_token("SEMICOLON", yytext); }
":"         { imprimir_token("COLON", yytext); }
"("         { imprimir_token("LPAREN", yytext); }
")"         { imprimir_token("RPAREN", yytext); }
"{"         { imprimir_token("LBRACE", yytext); }
"}"         { imprimir_token("RBRACE", yytext); }
"["         { imprimir_token("LBRACKET", yytext); }
"]"         { imprimir_token("RBRACKET", yytext); }

 /* Identificadores */
[a-zA-Z_][a-zA-Z0-9_]* { imprimir_token("IDENTIFIER", yytext); }

 /* Comentarios (ignorar) */
"/*"([^*]|\*+[^*/])*\*+"/" { /* ignorar */ }
"//".*      { /* ignorar */ }

 /* Espacios en blanco */
[ \t\r\n]+  { /* ignorar */ }

 /* Error */
.           { printf("ERROR LEXICO: caracter inesperado '%s' en línea %d\n", yytext, yylineno); }

%%

/* Función para procesar un archivo */
void procesar_archivo(const char *ruta) {
    FILE *file = fopen(ruta, "r");
    if (!file) {
        perror("Error al abrir archivo");
        return;
    }
    yyin = file;
    printf("\n--- Procesando: %s ---\n", ruta);
    printf("%-20s %s\n", "TOKEN", "LEXEMA");
    printf("----------------------------------------\n");
    yylex();
    fclose(file);
    printf("----------------------------------------\n\n");
}

/* Listar archivos en carpeta Pruebas/ (usando dirent.h) */
int listar_archivos(const char *carpeta, char *archivos[], int max) {
    DIR *dir;
    struct dirent *entry;
    int count = 0;
    dir = opendir(carpeta);
    if (!dir) {
        printf("No se pudo abrir la carpeta '%s'\n", carpeta);
        return 0;
    }
    while ((entry = readdir(dir)) != NULL) {
        if (entry->d_type == DT_REG) {  /* solo archivos regulares */
            if (count < max) {
                archivos[count] = strdup(entry->d_name);
                count++;
            }
        }
    }
    closedir(dir);
    return count;
}

int main(int argc, char **argv) {
    if (argc > 1) {
        /* Si se pasa argumento, procesar ese archivo directamente */
        procesar_archivo(argv[1]);
        return 0;
    }

    /* Modo interactivo: mostrar menú con archivos en Pruebas/ */
    const char *carpeta = "Pruebas";
    char *archivos[50];  /* máximo 50 archivos */
    int n = listar_archivos(carpeta, archivos, 50);

    if (n == 0) {
        printf("No se encontraron archivos en la carpeta '%s'\n", carpeta);
        return 1;
    }

    while (1) {
        printf("\n=== MENU DE PRUEBAS ===\n");
        for (int i = 0; i < n; i++) {
            printf("%d. %s\n", i+1, archivos[i]);
        }
        printf("0. Salir\n");
        printf("Seleccione una opcion: ");

        int opcion;
        scanf("%d", &opcion);
        if (opcion == 0) break;
        if (opcion < 1 || opcion > n) {
            printf("Opcion invalida.\n");
            continue;
        }

        /* Construir ruta completa */
        char ruta[256];
        snprintf(ruta, sizeof(ruta), "%s/%s", carpeta, archivos[opcion-1]);
        procesar_archivo(ruta);
    }

    /* Liberar memoria de los nombres */
    for (int i = 0; i < n; i++) free(archivos[i]);

    return 0;
}