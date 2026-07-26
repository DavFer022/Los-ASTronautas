# -*- coding: utf-8 -*-
"""
main.py
-------
Orquesta el pipeline híbrido Lexer -> Parser para UnegScript y muestra:
  1) Tokens corregidos
  2) AST (árbol de sintaxis abstracta)
  3) Sugerencias generadas por el módulo de IA (léxicas y sintácticas)
"""

import json
import sys

import lexer
import parser as uneg_parser

EJEMPLO_CON_ERRORES = 'pront x = 5;\nif x > 3 prnt(x) else prnt("no")'


def run(code: str, titulo="UnegScript"):
    print("=" * 70)
    print(f"CÓDIGO FUENTE ({titulo}):")
    print("-" * 70)
    print(code)
    print("=" * 70)

    # --- 1) Análisis léxico híbrido ---
    lex_res = lexer.tokenize(code)

    print("\n[1] TOKENS CORREGIDOS")
    print("-" * 70)
    for tok in lex_res.tokens:
        print(f"  {tok}")

    # --- 2) Análisis sintáctico híbrido ---
    parse_res = uneg_parser.parse(lex_res.tokens)

    print("\n[2] AST (Árbol de Sintaxis Abstracta)")
    print("-" * 70)
    print(json.dumps(parse_res.ast.to_dict(), indent=2, ensure_ascii=False))

    print("\n[3] SUGERENCIAS IA")
    print("-" * 70)
    todas = lex_res.suggestions + parse_res.suggestions
    if todas:
        for s in todas:
            print(f"  {s}")
    else:
        print("  (sin sugerencias)")

    if lex_res.errors or parse_res.errors:
        print("\n[!] ERRORES NO RECUPERABLES")
        print("-" * 70)
        for e in lex_res.errors + parse_res.errors:
            print(f"  {e}")

    return lex_res, parse_res


if __name__ == "__main__":
    code = sys.argv[1] if len(sys.argv) > 1 else EJEMPLO_CON_ERRORES
    run(code)
