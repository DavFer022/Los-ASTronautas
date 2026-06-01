# Algoritmo de Collatz en Zig

## Descripción del algoritmo
La **conjetura de Collatz** (también conocida como problema 3n+1) es un problema matemático que establece que, para cualquier número entero positivo, aplicando las siguientes reglas se llega siempre al número 1:

- Si el número es **par**, se divide entre 2.
- Si el número es **impar**, se multiplica por 3 y se suma 1.

Este programa calcula la **cantidad de pasos** que tarda cada número desde 1 hasta N (N = 100,000) en llegar a 1, y acumula el total de pasos de todos los números. Además, mide el **tiempo de ejecución** para evaluar el rendimiento del lenguaje.

## Requisitos previos
| Requisito | Versión mínima | Comando de verificación |
|-----------|---------------|------------------------|
| Zig | 0.13.0 o superior | zig version |

## Instalación (si no tienes Zig)
Zig no requiere un instalador tradicional. Solo debes descargar el archivo ZIP y añadirlo al PATH.

### Paso 1: Descargar Zig
Ve a la página oficial: [ziglang.org/download/](https://ziglang.org/download/)

Descarga la versión para Windows: `zig-windows-x86_64-0.13.0.zip` (o la versión más reciente estable).

### Paso 2: Extraer y mover
- Extrae el contenido del ZIP en una carpeta permanente (ej: `C:\zig`)
- La carpeta debe contener el archivo `zig.exe`

### Paso 3: Añadir al PATH
1. Abre **Configuración** → **Sistema** → **Información**
2. Haz clic en **"Configuración avanzada del sistema"**
3. Ve a **"Variables de entorno"**
4. En **"Variables del sistema"**, busca y edita la variable `Path`
5. Agrega la ruta de la carpeta donde está `zig.exe` (ej: `C:\zig`)
6. Haz clic en **Aceptar** en todas las ventanas

### Paso 4: Verificar la instalación
Abre una nueva terminal y ejecuta:
zig version

Deberías ver la versión instalada (ej: 0.13.0).

## Ejecución del programa
### Paso 1: Abrir terminal
En Windows: Abre PowerShell o Símbolo del sistema

También puedes usar el Developer Command Prompt si tienes problemas

### Paso 2: Navegar a la carpeta del código
cd ruta/donde/guardaste/el/codigo

### Paso 3: Ejecutar el programa
zig run collatz.zig

## Ejemplo completo (asumiendo que el archivo está en el Escritorio)
cd C:\Users\TuUsuario\Desktop
zig run collatz.zig

## Resultado esperado
Lenguaje: Zig
Números procesados: 1 hasta 100000
Tiempo de ejecución: 46.87 milisegundos
Total de pasos acumulados: 10753840

## Hardware utilizado para las pruebas
Procesador: AMD Ryzen 5 3600 6-Core (3.60 GHz)
RAM: 16.0 GB
Sistema operativo: Windows 11 Pro (23H2)

## Análisis de rendimiento
Zig es un lenguaje compilado a nativo mediante LLVM, diseñado como un sucesor moderno de C. Se caracteriza por:
Control explícito de memoria: No tiene recolector de basura.
Ausencia de variables ocultas: Todo es explícito, no hay sobrecarga de funciones ocultas.
Metaprogramación en tiempo de compilación (comptime): Permite ejecutar código en tiempo de compilación.

En las pruebas realizadas, Zig obtuvo tiempos de ~47 ms, ubicándose en el rango medio-alto. Su rendimiento es bueno, aunque fue superado por Rust y JavaScript en este caso particular.

## Factores que afectan el rendimiento en Zig:
Compilación nativa (LLVM): Genera código optimizado para el hardware.
Ausencia de recolector de basura: No hay pausas para liberar memoria.
Control manual de memoria: Puede ser más propenso a errores, pero más predecible.
Sin sobrecarga oculta: No hay excepciones ni RTTI (información de tipo en tiempo de ejecución).

## Comparación con otros lenguajes compilados

| Característica | Zig | Rust |
|----------------|-----|------|
| Recolector de basura | No | No |
| Compilación | LLVM | LLVM |
| Seguridad de memoria | Manual (con opciones de seguridad) | Ownership (garantizada en compilación) |
| Curva de aprendizaje | Moderada | Alta |

## Cómo reproducir las pruebas empíricas
Asegúrate de tener Zig instalado correctamente.
Descarga el archivo collatz.zig desde este repositorio.
Ejecuta el programa al menos 3 veces y calcula el promedio de los tiempos.
Registra los resultados en la tabla comparativa del informe.

## Enlaces de interés
- [Conjetura de Collatz - Wikipedia](https://es.wikipedia.org/wiki/Conjetura_de_Collatz)
- [Documentación oficial de Zig](https://ziglang.org/documentation/0.13.0/)
- [Descargar Zig](https://ziglang.org/download/)

## Créditos
Asignatura: Lenguajes y Compiladores (UNEG)
Grupo: Los ASTronautas
Actividad: II - Benchmarking y análisis morfosintáctico
