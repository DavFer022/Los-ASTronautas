%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <windows.h>

extern int yylex(void);
extern int yyparse(void);
extern FILE *yyin;

void yyerror(const char *s);

int syntax_errors = 0;
%}

%union {
    char *sval;
}

%token VERSION_KEY SERVICES_KEY NETWORKS_KEY IMAGE_KEY DRIVER_KEY IPAM_KEY CONFIG_KEY SUBNET_KEY
%token INDENT8 INDENT6 INDENT4 INDENT2 DASH COLON NEWLINE
%token <sval> QUOTED_STRING IP_SUBNET ID

%%

docker_compose_file:
    file_elements
    ;

file_elements:
    /* empty */
    | file_elements element
    ;

element:
    version_decl
    | services_decl
    | networks_decl
    | NEWLINE
    ;

version_decl:
    VERSION_KEY QUOTED_STRING NEWLINE
    ;

services_decl:
    SERVICES_KEY NEWLINE service_entries
    ;

service_entries:
    service_entry
    | service_entries service_entry
    ;

service_entry:
    INDENT2 ID COLON NEWLINE service_body
    ;

service_body:
    service_attrs
    ;

service_attrs:
    service_attr
    | service_attrs service_attr
    ;

service_attr:
    INDENT4 IMAGE_KEY image_val NEWLINE
    | INDENT4 NETWORKS_KEY NEWLINE network_refs
    ;

image_val:
    ID
    | ID COLON ID
    | QUOTED_STRING
    ;

network_refs:
    network_ref
    | network_refs network_ref
    ;

network_ref:
    INDENT6 DASH ID NEWLINE
    ;

networks_decl:
    NETWORKS_KEY NEWLINE network_entries
    ;

network_entries:
    network_entry
    | network_entries network_entry
    ;

network_entry:
    INDENT2 ID COLON NEWLINE network_body
    ;

network_body:
    network_attrs
    ;

network_attrs:
    network_attr
    | network_attrs network_attr
    ;

network_attr:
    INDENT4 DRIVER_KEY ID NEWLINE
    | INDENT4 IPAM_KEY NEWLINE ipam_body
    ;

ipam_body:
    INDENT6 CONFIG_KEY NEWLINE config_body
    ;

config_body:
    INDENT8 SUBNET_KEY IP_SUBNET NEWLINE
    ;

%%

void yyerror(const char *s) {
    syntax_errors++;
    fprintf(stderr, "Error sintáctico: %s\n", s);
}

int main(int argc, char **argv) {
    if (argc < 2) {
        printf("Uso: %s <archivo.yml>\n", argv[0]);
        return 1;
    }

    FILE *f = fopen(argv[1], "r");
    if (!f) {
        printf("Error al abrir archivo %s\n", argv[1]);
        return 1;
    }

    yyin = f;

    LARGE_INTEGER frequency;
    LARGE_INTEGER t1, t2;
    QueryPerformanceFrequency(&frequency);
    QueryPerformanceCounter(&t1);

    int res = yyparse();

    QueryPerformanceCounter(&t2);
    fclose(f);

    double parse_time_ms = (double)(t2.QuadPart - t1.QuadPart) * 1000.0 / (double)frequency.QuadPart;

    printf("PARSE_TIME: %.4f\n", parse_time_ms);

    if (res != 0 || syntax_errors > 0) {
        return 1;
    }
    return 0;
}
