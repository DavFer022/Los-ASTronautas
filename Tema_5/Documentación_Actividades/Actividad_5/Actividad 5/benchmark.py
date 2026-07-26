# -*- coding: utf-8 -*-
"""
benchmark.py
------------
Ejecuta n pruebas de tiempo de ejecución sobre el pipeline Lexer -> Parser,
variando el tamaño del programa de entrada (número de sentencias), y genera:
  - benchmark_resultados.csv
  - benchmark_tiempos.png   (tiempo lexer/parser vs. tamaño del programa)
  - benchmark_desglose.png  (proporción tiempo lexer vs parser)

Se generan programas sintéticos que combinan sentencias válidas y sentencias
con errores típicos (typos 'pront'/'prnt', ':' faltante) en proporción fija,
para que el camino de fallback a IA se ejerza en todas las pruebas, tal como
ocurriría con código real escrito por estudiantes.
"""

import csv
import random
import statistics
import time

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

import lexer
import parser as uneg_parser

random.seed(42)

PLANTILLAS_OK = [
    "x{i} = {n};",
    "print(x{i});",
    "if x{i} > {n}: print(x{i}) else: print(\"no\")",
    "while x{i} > 0: x{i} = x{i} - 1;",
]

PLANTILLAS_ERROR = [
    "pront x{i} = {n};",          # typo léxico -> IA lexer
    "prnt(x{i});",                 # typo léxico -> IA lexer
    "if x{i} > {n} print(x{i}) else print(\"no\")",  # ':' faltante -> IA parser
]


def generar_programa(n_statements: int, prop_error=0.4) -> str:
    """Genera un programa UnegScript sintético de n_statements sentencias,
    mezclando sentencias correctas y con errores típicos."""
    lineas = []
    for i in range(n_statements):
        plantilla = random.choice(PLANTILLAS_ERROR if random.random() < prop_error else PLANTILLAS_OK)
        lineas.append(plantilla.format(i=i, n=random.randint(1, 100)))
    return "\n".join(lineas)


def medir(codigo: str, repeticiones=5):
    """Retorna (tiempo_lexer_ms, tiempo_parser_ms) promedio sobre varias
    repeticiones para reducir ruido de medición."""
    t_lex, t_par = [], []
    for _ in range(repeticiones):
        t0 = time.perf_counter()
        lex_res = lexer.tokenize(codigo)
        t1 = time.perf_counter()
        uneg_parser.parse(lex_res.tokens)
        t2 = time.perf_counter()
        t_lex.append((t1 - t0) * 1000)
        t_par.append((t2 - t1) * 1000)
    return statistics.median(t_lex), statistics.median(t_par)


def run_benchmark(tamanos, out_dir="."):
    filas = []
    for n in tamanos:
        codigo = generar_programa(n)
        t_lex, t_par = medir(codigo)
        filas.append({
            "n_statements": n,
            "n_tokens_aprox": len(lexer.tokenize(codigo).tokens),
            "tiempo_lexer_ms": round(t_lex, 4),
            "tiempo_parser_ms": round(t_par, 4),
            "tiempo_total_ms": round(t_lex + t_par, 4),
        })
        print(f"n={n:>5}  lexer={t_lex:8.4f} ms  parser={t_par:8.4f} ms  total={t_lex+t_par:8.4f} ms")

    # CSV
    csv_path = f"{out_dir}/benchmark_resultados.csv"
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(filas[0].keys()))
        writer.writeheader()
        writer.writerows(filas)

    # Gráfica 1: tiempo vs tamaño
    xs = [f["n_statements"] for f in filas]
    ys_lex = [f["tiempo_lexer_ms"] for f in filas]
    ys_par = [f["tiempo_parser_ms"] for f in filas]
    ys_tot = [f["tiempo_total_ms"] for f in filas]

    plt.figure(figsize=(8, 5))
    plt.plot(xs, ys_lex, marker="o", label="Lexer (léxico)")
    plt.plot(xs, ys_par, marker="s", label="Parser (sintáctico)")
    plt.plot(xs, ys_tot, marker="^", linestyle="--", label="Total (lexer+parser)")
    plt.xlabel("Tamaño del programa (n° de sentencias)")
    plt.ylabel("Tiempo de ejecución (ms, mediana de 5 repeticiones)")
    plt.title("Tiempo de ejecución del análisis Lexer→Parser vs. tamaño de entrada")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{out_dir}/benchmark_tiempos.png", dpi=150)
    plt.close()

    # Gráfica 2: proporción lexer vs parser (barras apiladas)
    plt.figure(figsize=(8, 5))
    plt.bar([str(x) for x in xs], ys_lex, label="Lexer")
    plt.bar([str(x) for x in xs], ys_par, bottom=ys_lex, label="Parser")
    plt.xlabel("Tamaño del programa (n° de sentencias)")
    plt.ylabel("Tiempo de ejecución (ms)")
    plt.title("Desglose del tiempo total: Lexer vs. Parser")
    plt.legend()
    plt.grid(True, axis="y", alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{out_dir}/benchmark_desglose.png", dpi=150)
    plt.close()

    return filas, csv_path


if __name__ == "__main__":
    tamanos = [10, 25, 50, 100, 200, 400, 800, 1600]
    run_benchmark(tamanos, out_dir=".")
