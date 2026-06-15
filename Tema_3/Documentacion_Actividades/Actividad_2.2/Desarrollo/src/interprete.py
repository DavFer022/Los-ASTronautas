"""
interprete.py
==============

Intérprete gráfico interactivo, basado en el módulo estándar `turtle`,
para la Gramática Libre de Contexto (GLC) sobre el alfabeto del genoma
Sigma = {a, c, g, t}.

Requiere una interfaz gráfica (usa Tkinter a través de `turtle`), por
lo que debe ejecutarse en un entorno de escritorio local, no en un
servidor sin pantalla. Para generar imágenes sin interfaz gráfica
usar `generar_imagenes.py`.

Uso:
    python3 interprete.py

Se mostrará un menú con las 5 figuras derivadas de la gramática
(docs/derivaciones.md) y la opción de introducir una cadena propia
formada solo por los símbolos {a, c, g, t}.

NOTA DE IMPLEMENTACIÓN
-----------------------
A diferencia de una versión anterior, este script crea la `Screen` y
el `Turtle` UNA SOLA VEZ y reutiliza esa misma ventana para cada
figura (usando `screen.clearscreen()` entre dibujos). Crear una
`Screen`/`Turtle` nueva en cada iteración y cerrarla con
`exitonclick()` provoca, en varias versiones de Python/Tk
(especialmente Python 3.14), un error como:

    File ".../turtle.py", line 2744, in _update
        self._update_data()
    ...

al volver a llamar a `turtle.Turtle()` después de que la ventana
anterior fue destruida. Reutilizar la misma ventana evita ese problema.
"""

import turtle

from core import generar_segmentos, FIGURAS


def dibujar_en_pantalla(screen, cadena, params, color="green", grosor=2):
    """
    Limpia la pantalla actual y dibuja 'cadena' interpretada según
    'params'. Crea un nuevo Turtle (necesario tras clearscreen, que
    elimina los turtles existentes) y lo devuelve.
    """
    segmentos = generar_segmentos(cadena, **params)

    screen.clearscreen()
    screen.title(f"GLC genoma -> dibujo | cadena: {cadena}")

    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.pensize(grosor)
    t.color(color)

    for x1, y1, x2, y2 in segmentos:
        t.penup()
        t.goto(x1, y1)
        t.pendown()
        t.goto(x2, y2)

    screen.update()
    return t


def mostrar_menu():
    print("=" * 50)
    print("Interprete de la GLC genoma -> dibujo")
    print("Alfabeto Sigma = {a, c, g, t}")
    print("=" * 50)

    opciones = list(FIGURAS.items())
    for i, (clave, datos) in enumerate(opciones, start=1):
        print(f"{i}. {datos['nombre']}  (cadena: {datos['cadena']})")
    print(f"{len(opciones) + 1}. Introducir una cadena personalizada")
    print("0. Salir")

    return opciones


def main():
    screen = turtle.Screen()
    screen.setup(width=700, height=700)

    while True:
        opciones = mostrar_menu()
        eleccion = input("Elige una opcion: ").strip()

        if eleccion == "0":
            break

        if eleccion == str(len(opciones) + 1):
            cadena = input(
                "Introduce una cadena formada solo por {a,c,g,t}: "
            ).strip().lower()
            params = {"step": 35, "angle_turn": 90, "angle_branch": 40}
            try:
                dibujar_en_pantalla(screen, cadena, params)
            except ValueError as error:
                # Cadena vacía o con símbolos fuera de {a, c, g, t}
                print(f"\nError: {error}\n")
            continue

        try:
            idx = int(eleccion) - 1
            clave, datos = opciones[idx]
        except (ValueError, IndexError):
            print("\nOpcion no valida.\n")
            continue

        dibujar_en_pantalla(screen, datos["cadena"], datos["params"])

    # Cierra la ventana una sola vez, al terminar el programa
    screen.bye()


if __name__ == "__main__":
    main()