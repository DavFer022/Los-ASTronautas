@echo off
set TOOL_DIR=..\..\tools\winflexbison

echo Compilando Bison...
%TOOL_DIR%\win_bison.exe -d -o parser.tab.c parser.y
if %errorlevel% neq 0 exit /b %errorlevel%

echo Compilando Flex...
%TOOL_DIR%\win_flex.exe -o lex.yy.c lexer.l
if %errorlevel% neq 0 exit /b %errorlevel%

echo Compilando con GCC...
gcc -O2 -o parser_c.exe parser.tab.c lex.yy.c
if %errorlevel% neq 0 exit /b %errorlevel%

echo Parser C compilado con exito! (parser_c.exe)
