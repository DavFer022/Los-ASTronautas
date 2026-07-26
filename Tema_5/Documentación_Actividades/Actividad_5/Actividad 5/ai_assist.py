# -*- coding: utf-8 -*-
"""
ai_assist.py
------------
Módulo "IA" ligero para UnegScript.

No se dispone de acceso a un LLM externo dentro del entorno de ejecución,
por lo que el componente de Inteligencia Artificial se implementa mediante
una técnica clásica de NLP/ML: un clasificador de vecino más cercano (1-NN)
sobre una métrica de similitud de cadenas (razón de Levenshtein/SequenceMatcher),
equivalente conceptualmente a comparar un token contra "embeddings" de un
vocabulario conocido y devolver la clase (token válido) más cercana junto
con un puntaje de confianza en [0, 1].

Esta capa es la que el Lexer y el Parser consultan cuando su componente
determinista (autómata / gramática) no logra reconocer una entrada con
confianza suficiente.
"""

from difflib import SequenceMatcher

# Vocabulario de palabras reservadas / tokens válidos de UnegScript
KEYWORDS = ["print", "if", "else", "while", "for", "def", "return",
            "True", "False", "and", "or", "not", "in", "elif"]

OPERATORS = ["==", "!=", "<=", ">=", "=", "+", "-", "*", "/", "<", ">",
             "(", ")", ":", ";", ",", "{", "}"]


def _similarity(a: str, b: str) -> float:
    """Razón de similitud [0,1] entre dos cadenas (SequenceMatcher)."""
    return SequenceMatcher(None, a, b).ratio()


def suggest_token(token_text: str, vocabulary=None, threshold=0.8):
    """
    Dado un token 'sospechoso', busca en el vocabulario la palabra más
    parecida y retorna (mejor_candidato, confianza).

    confianza = similitud de cadenas normalizada [0,1]
    Si confianza < threshold, se considera que el lexer debe generar
    una sugerencia de corrección (posible typo).
    """
    vocab = vocabulary if vocabulary is not None else KEYWORDS
    best_word, best_score = None, 0.0
    for word in vocab:
        score = _similarity(token_text.lower(), word.lower())
        if score > best_score:
            best_word, best_score = word, score
    return best_word, best_score


def suggest_syntax_fix(context: str, expected, found):
    """
    'IA' de nivel sintáctico: dado el contexto de un error de parseo
    (token esperado vs. token encontrado), genera una sugerencia en
    lenguaje natural. Se apoya en reglas heurísticas + similitud léxica,
    simulando la consulta a un modelo de lenguaje para reparación de
    errores sintácticos (panic-mode recovery asistido).
    """
    expected_list = expected if isinstance(expected, (list, tuple)) else [expected]
    exp_str = " o ".join(f"'{e}'" for e in expected_list)

    if found is None or found == "EOF":
        return (f"Sugerencia: se esperaba {exp_str} pero el código terminó "
                f"inesperadamente. Verifique que no falte cerrar el bloque "
                f"'{context}'.")

    return (f"Sugerencia: en '{context}' se esperaba {exp_str} pero se "
            f"encontró '{found}'. ¿Olvidó agregar {exp_str}?")
