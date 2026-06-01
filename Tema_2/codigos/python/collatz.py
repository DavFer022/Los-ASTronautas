"""
ALGORITMO DE COLLATZ - BENCHMARKING
Grupo: Los ASTronautas

Enunciado:
Demostrar la conjetura de Collatz para todos los números menores que N.
Para cada número n, se aplica:
- si n es par: n = n / 2
- si n es impar: n = 3 * n + 1
El proceso termina cuando n = 1.

Este programa mide el tiempo de ejecución para N = 100,000
y calcula el total de pasos realizados.
"""

import time  # Para medir el tiempo de ejecución

def pasos_collatz(numero):
    """
    Calcula la cantidad de pasos que tarda un número en llegar a 1
    siguiendo la conjetura de Collatz.
    
    Parámetros:
        numero: El número entero positivo a evaluar
        
    Retorna:
        La cantidad de pasos realizados
    """
    pasos = 0
    while numero > 1:
        if numero % 2 == 0:  # Si es par
            numero = numero // 2
        else:                # Si es impar
            numero = 3 * numero + 1
        pasos += 1
    return pasos

def main():
    # Cantidad de números a probar (desde 1 hasta N)
    N = 100000
    
    # Medimos el tiempo de inicio
    inicio = time.time()
    
    # Variable para acumular todos los pasos
    total_pasos = 0
    
    # Recorremos todos los números desde 1 hasta N
    for i in range(1, N + 1):
        total_pasos = total_pasos + pasos_collatz(i)
    
    # Medimos el tiempo de finalización
    fin = time.time()
    
    # Calculamos el tiempo transcurrido en milisegundos
    tiempo_ms = (fin - inicio) * 1000
    
    # Mostramos los resultados
    print(f"Lenguaje: Python")
    print(f"Números procesados: 1 hasta {N}")
    print(f"Tiempo de ejecución: {tiempo_ms:.2f} milisegundos")
    print(f"Total de pasos acumulados: {total_pasos}")

# Punto de entrada del programa
if __name__ == "__main__":
    main()
