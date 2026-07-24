# Informe de la Actividad 4: Experimento de Parsers en Varios Lenguajes

## 1. Introducción

La Actividad 4 del curso de Lenguajes y Compiladores se centró en el diseño, la implementación y la comparación de tres parsers para un subconjunto de archivos YAML de Docker Compose. El objetivo principal fue demostrar, de manera práctica, cómo distintas tecnologías de análisis sintáctico responden ante entradas con crecientes niveles de complejidad.

Este trabajo no se limitó a construir tres analizadores, sino que también incorporó una dimensión experimental: medir tiempos de ejecución, comparar rendimientos y analizar el impacto que tiene la tecnología de implementación sobre la eficiencia del parseo.

La actividad partió de un enunciado base que proponía crear un lexer y un parser para un lenguaje cercano a Docker Compose, y luego evaluar su rendimiento con múltiples archivos de prueba generados sintéticamente. A partir de esa idea, se desarrolló un experimento completo que combina teoría de compiladores, implementación práctica y análisis de desempeño.

---

## 2. Objetivo general de la actividad

El propósito de la actividad fue responder a una pregunta central:

¿Cuál es el comportamiento en términos de rendimiento de distintos parsers al analizar archivos YAML con estructura jerárquica y nivel de indentación significativo?

Para ello se implementaron tres soluciones distintas:

- C, mediante Flex y Bison
- C#, mediante ANTLR 4
- Python, mediante ANTLR 4

Cada una de ellas se evaluó con el mismo conjunto de archivos de prueba, con el fin de comparar tanto el tiempo interno de parseo como el tiempo total de ejecución del proceso.

---

## 3. Alcance técnico del experimento

El alcance del proyecto se definió de forma concreta para que fuera viable y suficientemente representativo. En lugar de intentar soportar todo YAML o toda la sintaxis de Docker Compose, se trabajó con un subconjunto reducido pero significativo.

### 3.1 Estructuras soportadas

El subconjunto de lenguaje validado incluyó:

- la clave version
- el bloque services
- la referencia a imágenes mediante image
- la referencia a redes mediante networks
- el bloque networks, con driver, ipam, config y subnet

Esto permitió trabajar con una gramática que tuviera anidación real y que fuera adecuada para medir comportamiento frente a entradas crecientes.

### 3.2 Restricciones del experimento

Para mantener el experimento controlado, se establecieron varias reglas:

- uso exclusivo de indentación con espacios
- indentación estricta de 2 espacios por nivel
- ausencia de comentarios
- archivos generados sintéticamente para asegurar consistencia

Estas restricciones no solo facilitaron la implementación de los parsers, sino que también hicieron más clara la comparación entre tecnologías.

---

## 4. Diseño del experimento

La actividad se organizó en varias fases, siguiendo un enfoque de laboratorio de compiladores.

### 4.1 Definición del problema

El problema planteado fue comparar el rendimiento de parsers en distintos lenguajes al analizar un lenguaje basado en YAML, que presenta un reto importante: la jerarquía depende de la indentación.

Ese detalle resultó clave, porque el manejo de la indentación no es trivial para herramientas como Bison y Flex, que no manejan directamente estructuras dependientes del espacio en blanco.

### 4.2 Decisiones de implementación

Se tomaron varias decisiones importantes:

1. Se eligió un enfoque de validación, no de construcción de árbol sintáctico completo.
2. Se midieron dos tiempos distintos: tiempo interno de parseo y tiempo total de ejecución.
3. Se generaron archivos sintéticos con complejidad creciente.
4. Se usaron tres tecnologías distintas para mostrar diferencias reales de implementación.

Estas decisiones permitieron que el experimento fuera más útil desde el punto de vista académico y técnico.

---

## 5. Metodología aplicada

### 5.1 Generación de archivos de prueba

Una parte esencial del experimento fue la creación automática de archivos de prueba. Se desarrolló un script en Python que generaba 16 archivos YAML sintéticos, con cantidades crecientes de redes.

Los archivos siguieron una progresión lógica:

- 2 redes en el primer caso
- 4 redes en el segundo
- 6 redes en el tercero
- y así sucesivamente hasta 32 redes

Cada archivo contenía una estructura similar, con:

- un encabezado version: '3.8'
- un bloque services
- un bloque networks

La idea fue que la complejidad de los archivos creciera de manera progresiva para observar cómo se comportaban los parsers en entradas cada vez más grandes.

### 5.2 Implementación del parser en C

La solución en C se construyó con Flex y Bison.

El lexer fue responsable de manejar la indentación, generando tokens especiales como INDENT y DEDENT cuando el nivel de espacios cambiaba. Esta parte fue importante porque el problema de YAML no se puede resolver con un análisis sintáctico clásico sin una capa previa que interprete la estructura basada en espacios.

El parser en Bison definió reglas LALR(1) para reconocer el subconjunto del lenguaje. La implementación en C se eligió como referencia de eficiencia, ya que produce código compilado nativo y suele ofrecer tiempos muy bajos.

### 5.3 Implementación del parser en C#

La solución en C# se construyó con ANTLR 4. La gramática se definió en un archivo .g4 y luego se generó el código correspondiente para C#.

Este enfoque permitió comparar un parser generado por una herramienta de alto nivel con el parser manualmente integrado en C mediante Flex y Bison. La implementación en C# se consideró especialmente interesante porque representa una combinación entre productividad y rendimiento, además de incluir el overhead del runtime .NET.

### 5.4 Implementación del parser en Python

La solución en Python también usó ANTLR 4. La gramática se reutilizó conceptualmente para mantener consistencia entre las implementaciones, aunque cada lenguaje tenía su propia estructura de proyecto y sus propios archivos generados.

La versión en Python fue útil para evaluar el costo de ejecución del intérprete y del runtime de ANTLR en un lenguaje dinámico, en comparación con C y C#.

---

## 6. Medición de rendimiento

Una de las partes más valiosas de la actividad fue la medición.

### 6.1 Tiempo interno de parseo

Esta métrica se midió dentro del mismo programa. Se buscó medir únicamente el tiempo dedicado a ejecutar el parser, excluyendo la lectura del archivo y otros costos externos.

En cada implementación se usó un reloj de alta resolución propio del lenguaje:

- Python: time.perf_counter()
- C#: Stopwatch
- C: clock_gettime o una aproximación equivalente

Esta medición permite observar la eficiencia pura del reconocedor sintáctico.

### 6.2 Tiempo total de ejecución

Además del tiempo interno, se midió el tiempo total del proceso desde fuera del programa. Esto incluyó:

- carga del runtime o máquina virtual
- inicialización del entorno
- ejecución del parser
- finalización del proceso

Esta segunda métrica es muy importante porque refleja el costo real que enfrenta un usuario al ejecutar el programa en la práctica.

### 6.3 Resultado de la medición

Según los resultados documentados en el proyecto, el parser en C fue el más rápido en el tiempo de parseo puro, mientras que las soluciones en C# y Python mostraron un mayor overhead asociado a su entorno de ejecución.

Se observó que:

- C mantuvo tiempos muy bajos y estables
- C# presentó un overhead inicial mayor, aunque se comportó de forma razonable con entradas más grandes
- Python mostró una diferencia más visible en el tiempo total, debido al costo de su entorno interpretado

---

## 7. Análisis de resultados

Los resultados del experimento permitieron extraer varias conclusiones relevantes.

### 7.1 Ventaja de C en parseo puro

El parser en C mostró una eficiencia muy alta. Esto se debe a que el código generado por Flex y Bison se ejecuta de manera muy directa y con poco overhead, y además se compila a código nativo.

### 7.2 Overhead de runtimes y máquinas virtuales

C# y Python, aunque ofrecen mayor facilidad de desarrollo y mayor flexibilidad, requieren un entorno adicional para ejecutar el programa. Ese sobrecosto se refleja claramente en las mediciones de tiempo total.

### 7.3 Importancia de la arquitectura del parser

El experimento también mostró que no solo importa el lenguaje, sino también la forma en que el parser está implementado. El manejo de la indentación fue un elemento determinante, y la forma de resolverlo en cada tecnología tuvo impacto en la complejidad de la implementación.

---

## 8. Reproducibilidad y documentación

Una mejora importante del proyecto fue la transformación de una actividad que inicialmente podía ejecutarse solo en un entorno específico a una propuesta mucho más reproducible.

Se incorporaron varios elementos nuevos para facilitar la ejecución del experimento en otros equipos:

- un Dockerfile para ejecutar el experimento en un contenedor
- un archivo docker-compose.yml como alternativa simplificada
- scripts para ejecución rápida en Linux, Windows y WSL
- un archivo requirements.txt con dependencias fijas
- un archivo .gitignore para evitar artefactos innecesarios

Esto permitió que la actividad no solo fuera un experimento académico, sino también un proyecto más profesional y fácil de reproducir.

---

## 9. Estructura actual del proyecto

El proyecto quedó organizado de una forma clara y modular.

La estructura principal es la siguiente:

- carpeta principal de la actividad
- carpeta experimento_parsers
- subcarpetas para gramáticas, código fuente, scripts, archivos de prueba y resultados

Dentro de la carpeta experimento_parsers se encuentran:

- grammars: gramáticas ANTLR y Bison
- src: implementaciones en Python, C# y C
- test_files: archivos YAML sintéticos de prueba
- scripts: generación de archivos, ejecución del experimento y creación de gráficas
- results: resultados, CSV y figuras generadas

Esta estructura refleja el estado final del proyecto y muestra cómo la actividad pasó de una idea simple a un experimento completo y bien organizado.

---

## 10. Estado actual de la actividad

En su versión actual, la actividad se presenta como un proyecto de laboratorio de compiladores con los siguientes elementos:

- alcance bien definido
- tres implementaciones funcionales de parsers
- archivos de prueba generados automáticamente
- mediciones registradas en un archivo CSV
- gráficas comparativas generadas
- documentación completa para ejecutar y reproducir el experimento

Además, el proyecto quedó preparado para que una persona externa lo ejecute sin necesidad de comprender todo el proceso desde cero, gracias a los scripts y al entorno Docker.

---

## 11. Valor académico de la actividad

Esta actividad es valiosa porque combina varios temas fundamentales del curso:

- diseño de gramáticas
- manejo de lexers y parsers
- tratamiento de indentación en lenguajes basados en espacios
- comparación de tecnologías de implementación
- medición de rendimiento y análisis de resultados
- documentación y reproducibilidad

En ese sentido, la actividad no solo demuestra conocimiento de compiladores, sino también capacidad para organizar un experimento técnico completo y presentar resultados de forma clara.

---

## 12. Conclusión

La Actividad 4 se desarrolló como un experimento práctico y completo sobre el rendimiento de parsers implementados en distintos lenguajes para un subconjunto de YAML de Docker Compose. A lo largo del proceso se definió el alcance, se generaron archivos de prueba sintéticos, se implementaron tres parsers distintos, se midieron tiempos de ejecución y se documentaron los hallazgos.

El resultado principal fue mostrar que la eficiencia del parseo depende no solo del lenguaje de programación, sino también de la arquitectura del parser, del manejo de la indentación y del overhead del entorno de ejecución.

Asimismo, el proyecto evolucionó hacia una versión más madura y reproducible, incorporando herramientas de automatización y contenedores que facilitan su ejecución en diferentes equipos.

Este informe consolida la actividad y representa su estado actual de manera integral, dejando la documentación centralizada en este documento y en el README del proyecto.
