# Algoritmo de Collatz - Implementación en 4 lenguajes

Este directorio contiene la implementación del **algoritmo de Collatz** (conjetura 3n+1) en cuatro lenguajes de programación con diferentes paradigmas y mecanismos de ejecución.

## Estructura
```
codigos/
├── python/
│   ├── collatz.py
│   └── README.md
├── javascript/
│   ├── collatz.js
│   └── README.md
├── zig/
│   ├── collatz.zig
│   └── README.md
└── rust/
    ├── Cargo.toml
    ├── src/
    │   └── main.rs
    └── README.md
```

## Comparativa de tiempos (promedio en ms)

| Lenguaje | Mecanismo | Tiempo promedio (ms) |
|----------|-----------|---------------------|
| **Python** | Interpretado (CPython) | ~895 ms |
| **JavaScript** | JIT (V8) | ~22 ms |
| **Zig** | Compilado nativo (LLVM) | ~47 ms |
| **Rust** | Compilado nativo (LLVM) | ~26 ms |

> **Nota:** Resultados obtenidos en AMD Ryzen 5 3600, 16GB RAM, Windows 11 Pro.

## Observaciones clave
- **JavaScript** fue el más rápido (JIT altamente optimizado)
- **Rust** y **Zig** (compilados) mostraron buen rendimiento
- **Python** (interpretado) fue el más lento por su naturaleza dinámica

## Cómo ejecutar cada lenguaje
Para instrucciones detalladas, consulta el `README.md` dentro de cada subcarpeta.

| Lenguaje | Comando rápido |
|----------|----------------|
| Python | `python collatz.py` |
| JavaScript | `node collatz.js` |
| Zig | `zig run collatz.zig` |
| Rust | `cargo run` |

## Créditos
- **Asignatura:** Lenguajes y Compiladores (UNEG)
- **Grupo:** Los ASTronautas
- **Actividad:** II - Benchmarking
