# Actividad II - Benchmarking y Análisis Morfosintáctico

## Responsables: Alburquerque Sheen (Zig, Python) y Varguillas Génesis (Rust, JavaScript)



Estudio Morfológico, Sintáctico y Benchmarking en Procesamiento Intensivo Para contrastar las filosofías de diseño de lenguajes con diferentes propósitos y arquitecturas internas, se seleccionará cuatro entornos con aproximaciones tecnológicas profundamente diferenciadas:



1\. Zig: Representante moderno del enfoque de sistemas, diseñado para sustituir a C, con control explícito de memoria, ausencia de variables ocultas y meta-programación en tiempo de compilación (comptime).



2\. Python:Lenguaje interpretado de alto nivel, conocido por su sintaxis clara y legible. Es extremadamente popular en ciencia de datos e IA, aunque sufre penalizaciones de rendimiento debido a su naturaleza dinámica y el GIL (Global Interpreter Lock).



3\. Rust:Lenguaje compilado de sistemas diseñado para la seguridad de memoria y el alto rendimiento. Su modelo de "propiedad" (ownership) permite gestionar recursos sin necesidad de un recolector de basura, compitiendo en velocidad con C++. F: Rust representa por su seguridad el nuevo estandar para la construccion de kernel Linux.



4\. Javascript: Originalmente diseñado para la web, se ejecuta principalmente sobre motores de alto rendimiento como V8. Es un lenguaje dinámico y basado en eventos, que ha ganado terreno en el lado del servidor (Node.js) con un modelo asíncrono no bloqueante.



Análisis Morfológico (Léxico): Detallar cómo cada uno de los tres lenguajes maneja la estructura de tokens. Esto implica describir el conjunto de palabras reservadas, las reglas de construcción de identificadores, los tipos de literales soportados y el tratamiento de elementos irrelevantes (como la indentación significativa en contraposición al uso de delimitadores explícitos de bloque como llaves o palabras clave de cierre). F:La tonkenización en lenguajes es formales diferente a la realizada para los LLM en procesamiento de lenguaje Natural.



Análisis Sintáctico: Gráficar o documentar mediante la notación formal disponible la jerarquía sintáctica de las estructuras de control esenciales empleadas en su código (bucles, condicionales y definiciones de subprogramas).



Benchmarking y Tabla de Tiempos: Ejecutar el algoritmo bajo condiciones controladas (especificando las características del hardware: CPU, memoria RAM, sistema operativo). Deben presentar los resultados estructurados en una tabla comparativa formal. Lenguaje de Programación. F: EL benchmarking es una herramienta comparativa interesante para ingeniero de software alto nivel.



Importante seleccione un algoritmo que genera carga de procesamiento, ejemplos: 1) calculo de cadenas de bloques simulando blockchain para entrada en cada bloque de mensajes fijos en una tabla con n mensajes, donde cada bloque ademas del mensaje contiene el hash del bloque anterior (hash + mensaje). 2) cálculo de ecuación de segundo grado para vectores a,b,c con cantidad de elemento n para n=200. 3) demostración de la conjetura de collatz para todos los números menores que n, para un n>50. Trabajar con uno de estos ejemplos. F: sería ideal hacer una gráfica del benchmarking.



Ejemplo de tabla benchmarking.



| Lenguaje de Programación | Paradigma Dominante | Mecanismo de Ejecución y Compilación | Tiempo de Ejecución Promedio (ms) | Consumo de Memoria Pico (MB) |

| :--- | :--- | :--- | :---: | :---: |

| \*\*Zig\*\* | Imperativo / Estructurado | Compilación Nativa (LLVM) | | |

| \*\*Python\*\* | Multiparadigma (OO, Imperativo) | Interpretado (CPython / VM) | | |

| \*\*Rust\*\* | Multiparadigma (Funcional, Imperativo) | Compilación Nativa (LLVM) | | |

| \*\*JavaScript\*\* | Multiparadigma (Prototípico, Funcional) | JIT (Just-In-Time) / V8 Engine | | |



La entrega debe incluir los archivos fuentes completamente funcionales adjuntos en el repositorio, con instrucciones explícitas en un archivo README acerca de cómo compilar, configurar los entornos y reproducir el escenario de pruebas empíricas.

