"""
generar_imagenes.py
====================

Genera previsualizaciones en formato PNG de las 5 figuras derivadas de
la Gramática Libre de Contexto (GLC) sobre el alfabeto Sigma = {a, c, g, t}.

A diferencia de interprete.py (que usa el módulo `turtle` y requiere
una ventana gráfica), este script usa `matplotlib` y puede ejecutarse
sin interfaz gráfica (headless), por lo que es útil para generar las
imágenes que se incluyen en la carpeta `images/` del repositorio.

Uso:
    python3 generar_imagenes.py
"""

import os
import matplotlib
matplotlib.use("Agg")  # backend sin interfaz gráfica
import matplotlib.pyplot as plt

from core import generar_segmentos, bounding_box, FIGURAS


def dibujar_figura(nombre_archivo, nombre, cadena, params, carpeta_salida):
    segmentos = generar_segmentos(cadena, **params)

    fig, ax = plt.subplots(figsize=(5, 5))
    for x1, y1, x2, y2 in segmentos:
        ax.plot([x1, x2], [y1, y2], color="green", linewidth=2)

    xmin, ymin, xmax, ymax = bounding_box(segmentos)
    margen = max(xmax - xmin, ymax - ymin) * 0.1 + 1
    ax.set_xlim(xmin - margen, xmax + margen)
    ax.set_ylim(ymin - margen, ymax + margen)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title(f"{nombre}\ncadena: {cadena}", fontsize=10)

    ruta = os.path.join(carpeta_salida, f"{nombre_archivo}.png")
    fig.savefig(ruta, dpi=120, bbox_inches="tight")
    plt.close(fig)
    print(f"Generado: {ruta}")


def main():
    carpeta_salida = os.path.join(os.path.dirname(__file__), "..", "images")
    carpeta_salida = os.path.abspath(carpeta_salida)
    os.makedirs(carpeta_salida, exist_ok=True)

    for clave, datos in FIGURAS.items():
        dibujar_figura(
            nombre_archivo=clave,
            nombre=datos["nombre"],
            cadena=datos["cadena"],
            params=datos["params"],
            carpeta_salida=carpeta_salida,
        )


if __name__ == "__main__":
    main()
