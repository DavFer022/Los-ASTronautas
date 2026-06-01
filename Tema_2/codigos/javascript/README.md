# Algoritmo de Collatz en JavaScript (Node.js)

## Descripción del algoritmo
La **conjetura de Collatz** (también conocida como problema 3n+1) es un problema matemático que establece que, para cualquier número entero positivo, aplicando las siguientes reglas se llega siempre al número 1:

- Si el número es **par**, se divide entre 2.
- Si el número es **impar**, se multiplica por 3 y se suma 1.

Este programa calcula la **cantidad de pasos** que tarda cada número desde 1 hasta N (N = 100,000) en llegar a 1, y acumula el total de pasos de todos los números. Además, mide el **tiempo de ejecución** para evaluar el rendimiento del lenguaje.

## Requisitos previos
| Requisito | Versión mínima | Comando de verificación |
|-----------|---------------|------------------------|
| Node.js | 18.x o superior | `node --version` |

## Instalación (si no tienes Node.js)
Si no tienes Node.js instalado, descárgalo desde:
- [nodejs.org](https://nodejs.org/)

**Recomendación:** Descarga la versión **LTS** (Long Term Support).

## Ejecución del programa

### Paso 1: Abrir terminal
- En Windows: Abre **PowerShell** o **Símbolo del sistema**
- En Linux/Mac: Abre **Terminal**

### Paso 2: Navegar a la carpeta del código
cd ruta/donde/guardaste/el/codigo

### Paso 3: Ejecutar el programa
node collatz.js

## Ejemplo completo (asumiendo que el archivo está en el Escritorio)
cd C:\Users\TuUsuario\Desktop
node collatz.js

## Resultado esperado
Lenguaje: JavaScript (Node.js)
Números procesados: 1 hasta 100000
Tiempo de ejecución: 22 milisegundos
Total de pasos acumulados: 10753840

## Hardware utilizado para las pruebas
Procesador: AMD Ryzen 5 3600 6-Core (3.60 GHz)
RAM: 16.0 GB
Sistema operativo: Windows 11 Pro (23H2)

## Análisis de rendimiento
JavaScript es un lenguaje dinámico e interpretado, pero su motor V8 (utilizado por Node.js) implementa compilación JIT (Just-In-Time). Esto significa que el código se compila a nativo mientras se ejecuta, lo que le permite alcanzar un rendimiento muy superior al de lenguajes interpretados tradicionales como Python.

En las pruebas realizadas, JavaScript fue el más rápido de los cuatro lenguajes (~22 ms), superando incluso a Rust y Zig en este caso particular. Esto se debe a la madurez del motor V8 y sus optimizaciones.

## Factores que afectan el rendimiento en JavaScript:
Compilación JIT: El código se compila a nativo en tiempo de ejecución, no antes.
Tipado dinámico: Las variables pueden cambiar de tipo, lo que añade cierta sobrecarga.
Event Loop: Modelo asíncrono no bloqueante para entrada/salida.
Recolector de basura: Gestiona automáticamente la memoria, pero puede introducir pausas.

## Cómo reproducir las pruebas empíricas
Asegúrate de tener Node.js instalado correctamente.
Descarga el archivo collatz.js desde este repositorio.
Ejecuta el programa al menos 3 veces y calcula el promedio de los tiempos.
Registra los resultados en la tabla comparativa del informe.

## Enlaces de interés
Conjetura de Collatz - Wikipedia
Documentación oficial de Node.js
Motor V8 de Google

## Créditos
Asignatura: Lenguajes y Compiladores (UNEG)
Grupo: Los ASTronautas
Actividad: II - Benchmarking y análisis morfosintáctico
