# -*- coding: utf-8 -*-
"""
parser.py
---------
Parser descendente recursivo (recursive descent) con 1 token de lookahead
para el subconjunto de Python "UnegScript".

Gramática (EBNF simplificada):

    program    := statement* EOF
    statement  := assign_stmt | if_stmt | while_stmt | print_stmt
    assign_stmt:= ID '=' expr ';'
    if_stmt    := 'if' expr ':' statement ('else' ':' statement)?
    while_stmt := 'while' expr ':' statement
    print_stmt := 'print' '(' expr ')' ';'?
    expr       := comparison
    comparison := arith (('=='|'!='|'<'|'>'|'<='|'>=') arith)?
    arith      := term (('+'|'-') term)*
    term       := factor (('*'|'/') factor)*
    factor     := NUMBER | STRING | ID | '(' expr ')'

Componente IA:
    Cuando `expect()` no encuentra el token esperado, en vez de abortar,
    el parser:
      1) consulta ai_assist.suggest_syntax_fix() para generar una sugerencia
         en lenguaje natural,
      2) aplica una estrategia de "recuperación de pánico asistida":
         si el token faltante es sintácticamente insertable de forma segura
         (p. ej. ':' o ';'), continúa el análisis como si estuviera presente,
         y si no, descarta tokens hasta un punto de sincronización.
    Esto permite seguir construyendo el AST incluso frente a errores.
"""

from dataclasses import dataclass, field
from typing import Any, List, Optional

import ai_assist


@dataclass
class ASTNode:
    kind: str
    value: Any = None
    children: List["ASTNode"] = field(default_factory=list)

    def to_dict(self):
        d = {"kind": self.kind}
        if self.value is not None:
            d["value"] = self.value
        if self.children:
            d["children"] = [c.to_dict() for c in self.children]
        return d


class ParseResult:
    def __init__(self):
        self.ast: Optional[ASTNode] = None
        self.suggestions: List[str] = []
        self.errors: List[str] = []


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.result = ParseResult()

    # ---------- utilidades de lookahead ----------
    def peek(self, offset=0):
        idx = min(self.pos + offset, len(self.tokens) - 1)
        return self.tokens[idx]

    def advance(self):
        tok = self.tokens[self.pos]
        if tok.type != "EOF":
            self.pos += 1
        return tok

    def check(self, type_=None, value=None):
        tok = self.peek()
        if type_ and tok.type != type_:
            return False
        if value and tok.value != value:
            return False
        return True

    def expect(self, type_=None, value=None, context=""):
        """Consume el token esperado o, si falla, consulta a la IA para
        sugerir/recuperar el error sin detener el análisis."""
        if self.check(type_, value):
            return self.advance()

        found_tok = self.peek()
        expected_repr = value if value else type_
        suggestion = ai_assist.suggest_syntax_fix(
            context, expected_repr, found_tok.value or "EOF"
        )
        self.result.suggestions.append(suggestion)
        self.result.errors.append(
            f"Error sintáctico L{found_tok.line}: se esperaba '{expected_repr}' "
            f"en '{context}', se encontró '{found_tok.value or 'EOF'}'"
        )

        # Recuperación asistida: los delimitadores estructurales (':' ';')
        # se consideran "insertables" -> el parser continúa como si
        # estuvieran presentes, sin consumir el token real.
        if expected_repr in (":", ";"):
            return None  # token "virtual" insertado

        # Si no es insertable, se sincroniza avanzando hasta el próximo
        # delimitador conocido (';' ':' ')') o hasta el inicio de un nuevo
        # statement, para evitar una cascada de errores en cadena.
        while not self.check("EOF") and not self.check(value=";") \
                and not self.check(value=":") and not self.check(value=")") \
                and not self._is_stmt_start():
            self.advance()
        return None

    def _is_stmt_start(self) -> bool:
        tok = self.peek()
        if tok.type == "KEYWORD" and tok.value in ("if", "while", "print", "else"):
            return True
        if tok.type == "ID" and self.peek(1).value == "=":
            return True
        return False

    # ---------- gramática ----------
    def parse_program(self) -> ParseResult:
        root = ASTNode("Program")
        while not self.check("EOF"):
            stmt = self.parse_statement()
            if stmt:
                root.children.append(stmt)
        self.result.ast = root
        return self.result

    def parse_statement(self) -> Optional[ASTNode]:
        tok = self.peek()

        if tok.type == "ID" and self.peek(1).value == "=":
            return self.parse_assign()
        if tok.type == "KEYWORD" and tok.value == "if":
            return self.parse_if()
        if tok.type == "KEYWORD" and tok.value == "while":
            return self.parse_while()
        if tok.type == "KEYWORD" and tok.value == "print":
            return self.parse_print()

        # Token inesperado a nivel de statement: reportar y sincronizar
        suggestion = ai_assist.suggest_syntax_fix(
            "statement", ["ID '='", "if", "while", "print"], tok.value or "EOF"
        )
        self.result.suggestions.append(suggestion)
        self.result.errors.append(f"Error sintáctico L{tok.line}: statement inválido '{tok.value}'")
        self.advance()
        return None

    def parse_assign(self) -> ASTNode:
        name_tok = self.expect("ID", context="asignación")
        self.expect(value="=", context="asignación")
        expr = self.parse_expr()
        self.expect(value=";", context="fin de asignación")
        node = ASTNode("Assign", value=name_tok.value if name_tok else "?")
        node.children.append(expr)
        return node

    def parse_if(self) -> ASTNode:
        self.expect(value="if", context="if")
        cond = self.parse_expr()
        self.expect(value=":", context="if")          # recuperación asistida si falta
        then_branch = self.parse_statement()

        node = ASTNode("If")
        node.children.append(ASTNode("Cond", children=[cond]))
        node.children.append(ASTNode("Then", children=[then_branch] if then_branch else []))

        if self.check("KEYWORD", "else"):
            self.advance()
            self.expect(value=":", context="else")
            else_branch = self.parse_statement()
            node.children.append(ASTNode("Else", children=[else_branch] if else_branch else []))
        return node

    def parse_while(self) -> ASTNode:
        self.expect(value="while", context="while")
        cond = self.parse_expr()
        self.expect(value=":", context="while")
        body = self.parse_statement()
        node = ASTNode("While")
        node.children.append(ASTNode("Cond", children=[cond]))
        node.children.append(ASTNode("Body", children=[body] if body else []))
        return node

    def parse_print(self) -> ASTNode:
        self.expect(value="print", context="print")
        self.expect(value="(", context="print")
        expr = self.parse_expr()
        self.expect(value=")", context="print")
        if self.check(value=";"):
            self.advance()
        node = ASTNode("Print")
        node.children.append(expr)
        return node

    def parse_expr(self) -> ASTNode:
        return self.parse_comparison()

    def parse_comparison(self) -> ASTNode:
        left = self.parse_arith()
        if self.peek().value in ("==", "!=", "<", ">", "<=", ">="):
            op = self.advance().value
            right = self.parse_arith()
            node = ASTNode("BinOp", value=op)
            node.children = [left, right]
            return node
        return left

    def parse_arith(self) -> ASTNode:
        node = self.parse_term()
        while self.peek().value in ("+", "-"):
            op = self.advance().value
            right = self.parse_term()
            new_node = ASTNode("BinOp", value=op)
            new_node.children = [node, right]
            node = new_node
        return node

    def parse_term(self) -> ASTNode:
        node = self.parse_factor()
        while self.peek().value in ("*", "/"):
            op = self.advance().value
            right = self.parse_factor()
            new_node = ASTNode("BinOp", value=op)
            new_node.children = [node, right]
            node = new_node
        return node

    def parse_factor(self) -> ASTNode:
        tok = self.peek()
        if tok.type == "NUMBER":
            self.advance()
            return ASTNode("Number", value=tok.value)
        if tok.type == "STRING":
            self.advance()
            return ASTNode("String", value=tok.value)
        if tok.type == "ID":
            self.advance()
            return ASTNode("Var", value=tok.value)
        if tok.value == "(":
            self.advance()
            expr = self.parse_expr()
            self.expect(value=")", context="expresión entre paréntesis")
            return expr

        suggestion = ai_assist.suggest_syntax_fix(
            "expresión", ["NUMBER", "STRING", "ID", "("], tok.value or "EOF"
        )
        self.result.suggestions.append(suggestion)
        self.result.errors.append(f"Error sintáctico L{tok.line}: expresión inválida cerca de '{tok.value}'")
        self.advance()
        return ASTNode("Error", value=tok.value)


def parse(tokens) -> ParseResult:
    return Parser(tokens).parse_program()
