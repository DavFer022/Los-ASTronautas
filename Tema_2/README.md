# Tema 2 - Los Lenguajes de Programación

**Grupo:** Los ASTronautas  
**Eslogan:** "Explorando el universo de los lenguajes, un nodo a la vez"  
**Asignatura:** Lenguajes y Compiladores (UNEG)  
**Profesor:** Ing. Félix Márquez, Msc  
**Fecha de entrega:** Junio 2026

---

## Resumen del Tema 2

Este trabajo aborda el estudio de los lenguajes de programación desde cuatro dimensiones estructurales: paradigmas, propósito, estructuras morfológicas y estructuras sintácticas. Se realizó un análisis comparativo de cuatro lenguajes (Zig, Python, Rust y JavaScript) mediante un benchmark basado en la Conjetura de Collatz (N=100,000), midiendo tiempos de ejecución y consumo de memoria. Como innovación, se diseñó el Lenguaje L, un DSL para sistemas de microrredes eléctricas críticas (ECO-GRID).

---

## Resultados del Benchmarking

| Lenguaje | Paradigma Dominante | Mecanismo de Ejecución | Tiempo (ms) | Memoria (MB) |
|----------|---------------------|------------------------|-------------|--------------|
| **Zig** | Imperativo / Estructurado | Compilación Nativa (LLVM) | 47 | ~2.5 |
| **Python** | Multiparadigma (OO, Imperativo) | Interpretado (CPython) | 895 | ~45 |
| **Rust** | Multiparadigma (Funcional, Imperativo) | Compilación Nativa (LLVM) | 26 | ~2.0 |
| **JavaScript** | Multiparadigma (Prototípico, Funcional) | JIT (V8 Engine) | 22 | ~35 |

> **Hardware utilizado:** AMD Ryzen 5 3600, 16GB RAM, Windows 11 Pro

---

## Estructura del repositorio (Tema 2)

Tema_2/
├── Documentacion_Actividades/
│   ├── Actividad_I/
│   │   └── actividad_I.md
│   ├── Actividad_II/
│   │   └── actividad_II.md
│   ├── Actividad_III/
│   │   └── actividad_III.md
│   └── distribucion.md
├── codigos/
│   ├── python/
│   │   ├── collatz.py
│   │   └── README.md
│   ├── javascript/
│   │   ├── collatz.js
│   │   └── README.md
│   ├── zig/
│   │   ├── collatz.zig
│   │   └── README.md
│   └── rust/
│       ├── Cargo.toml
│       ├── src/
│       │   └── main.rs
│       └── README.md
├── Informe_Tema_2_LosASTronautas.pdf
├── Presentación_Tema2_LosASTronautas.pdf
└── README.md

---

## Documentación del proceso (Documentacion_Actividades)

La carpeta `Documentacion_Actividades/` contiene los registros internos del equipo, el proceso de trabajo colaborativo, incluyendo la distribución de tareas entre los integrantes (distribucion.md) y los borradores o notas de cada actividad. Esta documentación evidencia la planificación y el seguimiento del proyecto.

--

## Cómo ejecutar los códigos

Cada subcarpeta dentro de `codigos/` contiene un `README.md` con instrucciones específicas.

| Lenguaje | Comando rápido |
|----------|----------------|
| Python | `python collatz.py` |
| JavaScript | `node collatz.js` |
| Zig | `zig run collatz.zig` |
| Rust | `cargo run` (dentro de la carpeta `rust/`) |

---

## Entregables

| Entregable | Enlace |
|------------|--------|
| **Informe de investigación (PDF)** | [Ver PDF](./Informe_Tema_2_LosASTronautas.pdf) |
| **Presentación (PDF)** | [Ver PDF](./Presentación_Tema2_LosASTronautas.pdf) |
| **Video de defensa** | [Ver en Google Drive](https://drive.google.com/file/d/1YH5h397YiS5jljZpGYH9kemG2oMjMssQ/view) |
| **Códigos fuente** | [Carpeta `codigos/`](./codigos) |

---

## Integrantes

| Nombre | Cédula | Sección |
|--------|--------|---------|
| Alburquerque Sheen | V-25.933.680 | 1 |
| Antoima Mariangel | V-30.907.427 | 1 |
| García Carlos | V-28.475.271 | 1 |
| Varguillas Génesis | V-24.848.424 | 2 |

---

## Enlaces de interés

- [Conjetura de Collatz - Wikipedia](https://es.wikipedia.org/wiki/Conjetura_de_Collatz)
- [Documentación de Zig](https://ziglang.org/documentation/)
- [Documentación de Python](https://docs.python.org/3/)
- [Documentación de Rust](https://doc.rust-lang.org/book/)
- [Documentación de Node.js](https://nodejs.org/es/docs/)

---

**© 2026 - Los ASTronautas**  
*Universidad Nacional Experimental de Guayana (UNEG)*
