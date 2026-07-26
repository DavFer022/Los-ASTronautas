# -*- coding: utf-8 -*-
"""
lexer.py
--------
Analizador léxico híbrido para UnegScript.

Componente tradicional:
    Se define un conjunto de expresiones regulares (equivalentes a un
    Autómata Finito Determinista, ya que el motor `re` de Python compila
    cada patrón a un autómata reconocedor) que cubren: palabras reservadas,
    identificadores, números, cadenas, operadores y signos de puntuación.

Componente IA (fallback):
    Cuando un lexema es reconocido como IDENTIFICADOR (el AFD no lo
    reconoce como ninguna palabra reservada exacta), se consulta al
    módulo ai_assist, que calcula la confianza/similitud del lexema
    contra el vocabulario de palabras reservadas. Si esa confianza es
    >= UMBRAL_CONFIANZA (0.8) -- es decir, el autómata tradicional "no
    coincide" con seguridad y la IA detecta una similitud alta con un
    token válido -- se aplica la corrección automáticamente sobre el
    flujo de salida ("tokens corregidos") y se registra la sugerencia.

    Si un carácter no es reconocido por ningún patrón (error léxico puro),
    también se delega en ai_assist para intentar una reparación.
"""

import re
from dataclasses import dataclass, field
from typing import List, Optional

import ai_assist

UMBRAL_CONFIANZA = 0.8

# --- Especificación de tokens (orden importa: se evalúa de arriba hacia abajo) ---
TOKEN_SPEC = [
    ("COMMENT",   r"#[^\n]*"),
    ("NEWLINE",   r"\n"),
    ("SKIP",      r"[ \t]+"),
    ("NUMBER",    r"\d+(\.\d+)?"),
    ("STRING",    r'"([^"\\]|\\.)*"|\'([^\'\\]|\\.)*\''),
    ("ID",        r"[A-Za-z_][A-Za-z0-9_]*"),
    ("OP",        r"==|!=|<=|>=|[+\-*/=<>():;,{}]"),
    ("MISMATCH",  r"."),
]

MASTER_REGEX = re.compile(
    "|".join(f"(?P<{name}>{pattern})" for name, pattern in TOKEN_SPEC)
)


@dataclass
class Token:
    type: str
    value: str
    line: int
    col: int
    corrected: bool = False
    original: Optional[str] = None

    def __repr__(self):
        base = f"<{self.type}:{self.value!r}"
        if self.corrected:
            base += f" (orig:{self.original!r})"
        return base + f" L{self.line}C{self.col}>"


@dataclass
class LexResult:
    tokens: List[Token] = field(default_factory=list)
    suggestions: List[str] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)


def tokenize(code: str) -> LexResult:
    result = LexResult()
    line_num = 1
    line_start = 0

    for match in MASTER_REGEX.finditer(code):
        kind = match.lastgroup
        value = match.group()
        col = match.start() - line_start + 1

        if kind == "NEWLINE":
            line_num += 1
            line_start = match.end()
            continue
        if kind in ("SKIP", "COMMENT"):
            continue

        if kind == "ID":
            token = _process_identifier(value, line_num, col, result)
        elif kind == "MISMATCH":
            token = _process_mismatch(value, line_num, col, result)
        else:
            token = Token(kind, value, line_num, col)

        if token is not None:
            result.tokens.append(token)

    result.tokens.append(Token("EOF", "", line_num, 0))
    return result


def _process_identifier(value: str, line: int, col: int, result: LexResult) -> Token:
    """Clasifica un identificador con el autómata determinista.

    El AFD reconoce con confianza=1.0 una palabra reservada exacta. Para
    cualquier otro lexema, el autómata no puede decidir por sí mismo si se
    trata de un identificador legítimo o de un error de tipeo sobre una
    palabra reservada; por eso delega en el módulo de IA (ai_assist), que
    calcula qué tan "cerca" está el lexema de cada palabra reservada
    (similitud = confianza de la sugerencia, en [0,1]).

    Si esa confianza >= UMBRAL_CONFIANZA (0.8), la IA considera que la
    sugerencia es lo bastante fiable como para aplicarla automáticamente
    sobre el flujo de tokens ("tokens corregidos") y se deja registro de
    la sugerencia. En caso contrario, el lexema se acepta tal cual como
    identificador de usuario.
    """
    if value in ai_assist.KEYWORDS:
        return Token("KEYWORD", value, line, col)

    candidate, confianza = ai_assist.suggest_token(value, ai_assist.KEYWORDS)

    if candidate and confianza >= UMBRAL_CONFIANZA and candidate != value:
        result.suggestions.append(
            f"Sugerencia: '{value}' → '{candidate}' "
            f"(confianza IA={confianza:.2f} >= {UMBRAL_CONFIANZA})"
        )
        return Token("KEYWORD", candidate, line, col, corrected=True, original=value)

    return Token("ID", value, line, col)


def _process_mismatch(value: str, line: int, col: int, result: LexResult):
    """Carácter no reconocido por ningún patrón: se intenta reparación IA
    comparándolo contra el vocabulario de operadores; si no hay una
    coincidencia razonable, se reporta como error léxico."""
    candidate, confianza = ai_assist.suggest_token(value, ai_assist.OPERATORS)
    if candidate and confianza >= 0.5:
        result.suggestions.append(
            f"Sugerencia: '{value}' → '{candidate}' "
            f"(confianza IA={confianza:.2f}, símbolo no reconocido por el AFD)"
        )
        return Token("OP", candidate, line, col, corrected=True, original=value)

    result.errors.append(
        f"Error léxico L{line}C{col}: carácter no reconocido '{value}'"
    )
    return None


if __name__ == "__main__":
    demo = 'pront x = 5;\nif x > 3 prnt(x) else prnt("no")'
    res = tokenize(demo)
    for t in res.tokens:
        print(t)
    print("\n".join(res.suggestions))
