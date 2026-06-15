"""
core.py
=======

Núcleo de interpretación de la Gramática Libre de Contexto (GLC) basada
en el alfabeto del genoma  Σ = {a, c, g, t}.

Este módulo NO depende de ninguna librería gráfica concreta: toma una
cadena derivada de la gramática y la traduce a una lista de SEGMENTOS
DE LÍNEA (x1, y1, x2, y2) que luego puede ser dibujada con cualquier
backend (turtle, matplotlib, SVG, etc.).

Tabla de equivalencias (acción de la "tortuga"):

    Símbolo | Acción de dibujo                | Equivalente turtle
    --------|----------------------------------|--------------------
       a    | Avanzar dibujando un segmento    |  F
       c    | Girar (sentido horario)          |  +
       g    | Abrir rama (push posición/ángulo)|  [
       t    | Cerrar rama (pop posición/ángulo)|  ]

Esta correspondencia es la misma usada en los Sistemas-L (L-Systems)
para modelar estructuras ramificadas (plantas, fractales), aplicada
aquí sobre cadenas de ADN {a, c, g, t}.
"""

import math


# Alfabeto válido de la gramática
ALFABETO = {"a", "c", "g", "t"}


def generar_segmentos(cadena, step=30.0, angle_turn=90.0, angle_branch=45.0,
                       heading_inicial=90.0, origen=(0.0, 0.0)):
    """
    Recorre una cadena generada por la GLC y devuelve la lista de
    segmentos de línea que la "tortuga" dibujaría.

    Parámetros
    ----------
    cadena : str
        Cadena formada solo por símbolos del alfabeto {a, c, g, t}.
    step : float
        Longitud de cada segmento dibujado por el símbolo 'a'.
    angle_turn : float
        Ángulo (en grados) que gira la tortuga con el símbolo 'c'.
        Gira en sentido horario.
    angle_branch : float
        Ángulo (en grados) que se añade a la orientación al abrir una
        rama con el símbolo 'g' (sentido antihorario).
    heading_inicial : float
        Orientación inicial de la tortuga en grados (90 = hacia arriba).
    origen : tuple(float, float)
        Punto inicial (x, y) de la tortuga.

    Devuelve
    --------
    list[tuple[float, float, float, float]]
        Lista de segmentos (x1, y1, x2, y2) en el orden en que se dibujan.

    Excepciones
    -----------
    ValueError
        Si la cadena contiene un símbolo fuera del alfabeto {a, c, g, t}.
    """
    x, y = origen
    heading = heading_inicial
    pila = []          # pila de estados (x, y, heading) para 'g' / 't'
    segmentos = []
    g_count = 0        # número de aperturas de rama 'g' encontradas

    for simbolo in cadena:
        if simbolo not in ALFABETO:
            raise ValueError(
                f"Símbolo '{simbolo}' no pertenece al alfabeto "
                f"Sigma = {{a, c, g, t}} de la gramática."
            )

        if simbolo == "a":
            # Avanzar dibujando un segmento
            rad = math.radians(heading)
            nx = x + step * math.cos(rad)
            ny = y + step * math.sin(rad)
            segmentos.append((x, y, nx, ny))
            x, y = nx, ny

        elif simbolo == "c":
            # Girar en sentido horario
            heading -= angle_turn

        elif simbolo == "g":
            # Abrir rama: guardar estado y desviar el trazo.
            # Convención del intérprete: las aperturas de rama
            # sucesivas alternan el sentido del giro (+/-) para que
            # ramas "hermanas" se distingan visualmente, ya que el
            # alfabeto Sigma = {a, c, g, t} no dispone de un símbolo
            # exclusivo para "girar a la izquierda" / "a la derecha".
            pila.append((x, y, heading))
            g_count += 1
            signo = 1 if g_count % 2 == 1 else -1
            heading += signo * angle_branch

        elif simbolo == "t":
            # Cerrar rama: recuperar el estado guardado
            if not pila:
                raise ValueError(
                    "Símbolo 't' sin un 'g' previo (pila vacía)."
                )
            x, y, heading = pila.pop()

    return segmentos


def bounding_box(segmentos):
    """Devuelve (xmin, ymin, xmax, ymax) para una lista de segmentos."""
    xs = []
    ys = []
    for x1, y1, x2, y2 in segmentos:
        xs += [x1, x2]
        ys += [y1, y2]
    return min(xs), min(ys), max(xs), max(ys)


# ---------------------------------------------------------------------
# Cadenas obtenidas en las 5 derivaciones (docs/derivaciones.md)
# junto con parámetros sugeridos de dibujo
# ---------------------------------------------------------------------
FIGURAS = {
    "cuadrado": {
        "nombre": "Cuadrado",
        "cadena": "acacacac",
        "params": {"step": 60, "angle_turn": 90, "angle_branch": 0},
    },
    "arbol_simple": {
        "nombre": "Arbol con una rama y hojas",
        "cadena": "agaatcaa",
        "params": {"step": 35, "angle_turn": 90, "angle_branch": 40},
    },
    "arbol_ramificado": {
        "nombre": "Arbol con ramificacion anidada",
        "cadena": "agagaatcaatcaa",
        "params": {"step": 35, "angle_turn": 90, "angle_branch": 35},
    },
    "arbol_simetrico": {
        "nombre": "Arbol con doble ramificacion simetrica",
        "cadena": "agaatgaatcaa",
        "params": {"step": 35, "angle_turn": 90, "angle_branch": 40},
    },
    "cubo": {
        "nombre": "Cubo (proyeccion isometrica simplificada)",
        "cadena": "acacacacgacacacactaaaa",
        "params": {"step": 45, "angle_turn": 90, "angle_branch": -45},
    },
}
