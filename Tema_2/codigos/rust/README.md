# Algoritmo de Collatz en Rust

## Descripción del algoritmo
La **conjetura de Collatz** (también conocida como problema 3n+1) es un problema matemático que establece que, para cualquier número entero positivo, aplicando las siguientes reglas se llega siempre al número 1:

- Si el número es **par**, se divide entre 2.
- Si el número es **impar**, se multiplica por 3 y se suma 1.

Este programa calcula la **cantidad de pasos** que tarda cada número desde 1 hasta N (N = 100,000) en llegar a 1, y acumula el total de pasos de todos los números. Además, mide el **tiempo de ejecución** para evaluar el rendimiento del lenguaje.

## Requisitos previos
| Requisito | Versión mínima | Comando de verificación |
|-----------|---------------|------------------------|
| Rust | 1.70 o superior | `rustc --version` |
| Cargo (opcional) | 1.70 o superior | `cargo --version` |

## Instalación (si no tienes Rust)

### Paso 1: Instalar herramientas de C++ (Windows)
Rust en Windows necesita el compilador de C++ de Microsoft.

1. Ve a [visualstudio.microsoft.com/es/downloads/](https://visualstudio.microsoft.com/es/downloads/)
2. Descarga **"Build Tools para Visual Studio 2022"**
3. Ejecuta el instalador y marca la carga de trabajo **"Desarrollo de escritorio con C++"**
4. Haz clic en **"Instalar"** y espera (puede tardar varios minutos)
5. **Reinicia tu PC**

### Paso 2: Instalar Rust
Ve a la página oficial: [rustup.rs](https://rustup.rs/)

Descarga y ejecuta `rustup-init.exe`. En la terminal, selecciona la opción **1) Proceed with installation (default)** presionando `Enter`.

### Paso 3: Verificar la instalación
Abre una **nueva terminal** y ejecuta:
rustc --version
cargo --version

#### Deberías ver algo como:
rustc 1.96.0 (ac68faa20 2026-05-25)
cargo 1.96.0 (30a34c682 2026-05-25)

## Ejecución del programa
### Paso 1: Abrir terminal
En Windows: Abre PowerShell o el Developer Command Prompt

En Linux/Mac: Abre Terminal

### Paso 2: Navegar a la carpeta del código
cd ruta/donde/guardaste/el/codigo

### Paso 3: Ejecutar el programa
#### Opción 1: Compilar y ejecutar manualmente
rustc src/main.rs
./main.exe

#### Opción 2: Usando Cargo (recomendado)
cargo run

## Ejemplo completo (asumiendo que el proyecto está en el Escritorio)
cd C:\Users\TuUsuario\Desktop\rust
cargo run

## Estructura del proyecto
```
rust/
├── Cargo.toml
├── src/
│   └── main.rs
```
## Resultado esperado
Lenguaje: Rust
Números procesados: 1 hasta 100000
Tiempo de ejecución: 26 milisegundos
Total de pasos acumulados: 10753840

## Hardware utilizado para las pruebas
Procesador: AMD Ryzen 5 3600 6-Core (3.60 GHz)
RAM: 16.0 GB
Sistema operativo: Windows 11 Pro (23H2)

## Análisis de rendimiento
Rust es un lenguaje compilado a nativo mediante LLVM, diseñado para ofrecer seguridad de memoria sin necesidad de un recolector de basura. Su modelo de ownership (propiedad) permite gestionar recursos de manera eficiente y segura, compitiendo en velocidad con C++.

En las pruebas realizadas, Rust obtuvo tiempos de ~26 ms, siendo el segundo más rápido de los cuatro lenguajes (superado solo por JavaScript en este caso particular).

## Factores que afectan el rendimiento en Rust:
Compilación nativa (LLVM): Genera código altamente optimizado.
Sin recolector de basura: No hay pausas para liberar memoria.
Ownership y borrowing: Garantiza seguridad de memoria en tiempo de compilación.
Cero costos de abstracción: Las abstracciones no añaden sobrecarga en tiempo de ejecución.

## Comparación con otros lenguajes compilados

| Característica | Zig | Rust |
|----------------|-----|------|
| Recolector de basura | No | No |
| Compilación | LLVM | LLVM |
| Seguridad de memoria | Manual (con opciones de seguridad) | Ownership (garantizada en compilación) |
| Curva de aprendizaje | Moderada | Alta |

## Cómo reproducir las pruebas empíricas
Asegúrate de tener Rust instalado correctamente.
Descarga todos los archivos de la carpeta rust/ desde este repositorio.
Ejecuta el programa al menos 3 veces y calcula el promedio de los tiempos.
Registra los resultados en la tabla comparativa del informe.

## Enlaces de interés
- [Conjetura de Collatz - Wikipedia](https://es.wikipedia.org/wiki/Conjetura_de_Collatz)
- [Documentación oficial de Rust](https://doc.rust-lang.org/book/)
- [Rust en español](https://rust-lang.es/)
- [Descargar Rust (rustup)](https://rustup.rs/)
- [Build Tools para Visual Studio 2022](https://visualstudio.microsoft.com/es/downloads/)

## Créditos
Asignatura: Lenguajes y Compiladores (UNEG)
Grupo: Los ASTronautas
Actividad: II - Benchmarking y análisis morfosintáctico
