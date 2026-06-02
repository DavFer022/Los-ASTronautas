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

## Discusión de Resultados

Los resultados obtenidos muestran diferencias significativas en el rendimiento de los cuatro lenguajes al ejecutar el mismo algoritmo de Collatz con N = 100,000.

**JavaScript (Node.js) fue el más rápido con 22 ms.** Esto se debe a su motor V8, que implementa compilación JIT (Just-In-Time). El JIT analiza el código en tiempo de ejecución, identifica las rutas calientes (código que se ejecuta repetidamente) y las compila a código nativo altamente optimizado. Además, V8 ha sido objeto de intensas optimizaciones por parte de Google durante más de una década.

**Rust obtuvo el segundo lugar con 26 ms.** Rust es un lenguaje compilado a nativo mediante LLVM, sin recolector de basura. Su sistema de ownership y borrowing elimina la necesidad de overhead en tiempo de ejecución. La ligera diferencia con JavaScript (4 ms) puede atribuirse a las optimizaciones del JIT en este caso particular, pero en escenarios de cómputo más intensivo o con mayor uso de memoria, Rust suele superar a JavaScript.

**Zig alcanzó 47 ms.** También es compilado a nativo mediante LLVM, pero su diseño prioriza el control explícito sobre el rendimiento. La diferencia con Rust (aproximadamente 2x más lento) puede deberse a que Zig no realiza tantas optimizaciones automáticas como Rust, dejando más decisiones al programador.

**Python fue el más lento con 895 ms (aproximadamente 40 veces más lento que JavaScript).** Esto se explica porque Python es un lenguaje interpretado (CPython) con tipado dinámico y un recolector de basura con overhead significativo. Además, el GIL (Global Interpreter Lock) limita la concurrencia. Sin embargo, su propósito de diseño no es la velocidad bruta, sino la legibilidad y la productividad del programador.

**Conclusión del benchmarking:** La elección del lenguaje debe basarse en los requisitos del proyecto. Para aplicaciones con restricciones de tiempo real o cómputo intensivo, Rust o Zig son más adecuados. Para desarrollo web o aplicaciones donde la productividad y el ecosistema son clave, JavaScript y Python siguen siendo opciones válidas, asumiendo las compensaciones en rendimiento.


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
