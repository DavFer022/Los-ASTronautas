# Algoritmo de Collatz en Python

## Descripción del algoritmo
La **conjetura de Collatz** (también conocida como problema 3n+1) es un problema matemático que establece que, para cualquier número entero positivo, aplicando las siguientes reglas se llega siempre al número 1:

- Si el número es **par**, se divide entre 2.
- Si el número es **impar**, se multiplica por 3 y se suma 1.

Este programa calcula la **cantidad de pasos** que tarda cada número desde 1 hasta N (N = 100,000) en llegar a 1, y acumula el total de pasos de todos los números. Además, mide el **tiempo de ejecución** para evaluar el rendimiento del lenguaje.

## Requisitos previos
| Requisito | Versión mínima | Comando de verificación |
|-----------|---------------|------------------------|
| Python | 3.12 o superior | python --version |

## Instalación (si no tienes Python)
Si no tienes Python instalado, descárgalo desde:
- [python.org/downloads/](https://www.python.org/downloads/)

**Importante:** Durante la instalación, marca la opción **"Add Python to PATH"**.

## Ejecución del programa

### Paso 1: Abrir terminal
- En Windows: Abre **PowerShell** o **Símbolo del sistema**
- En Linux/Mac: Abre **Terminal**

### Paso 2: Navegar a la carpeta del código

cd ruta/donde/guardaste/el/codigo

### Paso 3: Ejecutar el programa
python collatz.py

## Ejemplo completo (asumiendo que el archivo está en el Escritorio)
cd C:\Users\TuUsuario\Desktop
python collatz.py

## Resultado esperado
Lenguaje: Python
Números procesados: 1 hasta 100000
Tiempo de ejecución: 895.14 milisegundos
Total de pasos acumulados: 10753840

## Hardware utilizado para las pruebas
Procesador: AMD Ryzen 5 3600 6-Core (3.60 GHz)
RAM: 16.0 GB
Sistema operativo: Windows 11 Pro (23H2)

## Análisis de rendimiento
Python es un lenguaje interpretado, lo que significa que cada instrucción se traduce y ejecuta línea por línea en tiempo real. Esto lo hace más lento que lenguajes compilados como Rust o Zig, pero su sintaxis clara y su gran ecosistema de bibliotecas lo hacen ideal para ciencia de datos, IA y prototipado rápido.

## Factores que afectan el rendimiento en Python:
Global Interpreter Lock (GIL): Limita la ejecución de hilos en paralelo.
Tipado dinámico: Las variables pueden cambiar de tipo en tiempo de ejecución.
Interpretación vs compilación: No se genera código nativo previamente.

## Cómo reproducir las pruebas empíricas
Asegúrate de tener Python instalado correctamente.
Descarga el archivo collatz.py desde este repositorio.
Ejecuta el programa al menos 3 veces y calcula el promedio de los tiempos.
Registra los resultados en la tabla comparativa del informe.

## Enlaces de interés
Conjetura de Collatz - Wikipedia
Documentación oficial de Python
Descargar Python

## Créditos
Asignatura: Lenguajes y Compiladores (UNEG)
Grupo: Los ASTronautas
Actividad: II - Benchmarking y análisis morfosintáctico
