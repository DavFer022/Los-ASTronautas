# Actividad 3 - Definir un lenguaje L subconjunto de lenguaje Rust, construya un lexer para L utilizando metacompilador

**Responsable:** Carlos García

En el informe incorpore:

1. manual de usuario completo con sus propias palabras del metacompilador seleccionado
2. descripción de su lenguaje L diseñado
3. documentar proceso decreación de su lexer incorporar en repositorio con su respectivo archivo marckdown de documentación y pasos a detalle de instalación o implementación del lexer.

## Desarrollo

## Documentación del proceso de creación del lexer

La construcción del analizador léxico para el lenguaje **L** (subconjunto de Rust) se llevó a cabo siguiendo una metodología incremental, apoyada en la herramienta Flex y el compilador GCC, bajo el sistema operativo Windows con MinGW. A continuación, se detalla el proceso completo, desde la definición del lenguaje hasta la integración del menú interactivo y la organización del repositorio.

## Definición del lenguaje objetivo

El primer paso consistió en delimitar el subconjunto de Rust que sería reconocido por el lexer. Se optó por un conjunto representativo que incluyera las categorías léxicas más comunes, pero sin llegar a cubrir todas las características del lenguaje completo, para mantener la implementación manejable y educativa. La selección se basó en el análisis de programas Rust típicos y en la experiencia previa con el lenguaje.

- **Palabras clave**: se incluyeron 35 palabras reservadas que abarcan estructuras de control (`if`, `else`, `loop`, `while`, `for`), declaraciones (`fn`, `let`, `mut`, `const`, `static`), manejo de visibilidad (`pub`, `use`, `mod`, `crate`), conceptos de orientación a objetos (`struct`, `enum`, `impl`, `trait`) y operadores especiales (`match`, `return`, `break`, `continue`, `async`, `await`, `move`, `ref`, `dyn`, `where`, `in`, entre otras).
- **Tipos primitivos**: se seleccionaron los tipos numéricos con signo y sin signo de 8 a 128 bits (`i8`, `i16`, `i32`, `i64`, `i128`, `u8`, `u16`, `u32`, `u64`, `u128`), los de punto flotante (`f32`, `f64`), y los tipos `bool`, `char`, `str`, `String`, `Vec`, `Option` y `Result`.
- **Literales**: se definieron patrones para enteros decimales con y sin sufijo de tipo, flotantes, booleanos, caracteres y cadenas con escapes básicos.
- **Operadores y delimitadores**: se incluyeron todos los operadores aritméticos, lógicos, de comparación, de asignación compuesta, de bits, así como los operadores de rango (`..`, `...`), flecha (`->`, `=>`), doble dos puntos (`::`) y los delimitadores estándar: paréntesis, llaves, corchetes, punto y coma, coma, dos puntos y punto.
- **Comentarios**: se soportan los comentarios de línea (`//`) y de bloque (`/* ... */`) en su forma no anidada.
- **Manejo de errores**: se contempla un token de error para cualquier carácter que no encaje en los patrones definidos.

Esta definición se formalizó en una tabla que sirvió como guía para la escritura de las reglas en el archivo `.l`.

### Estructuración del archivo de especificación Flex

El archivo `rust_lexer.l` se organizó en las tres secciones estándar de Flex:

- **Sección de definiciones**: se colocaron las opciones `%option noyywrap` y `%option yylineno`, y se incluyó la cabecera `<stdio.h>` y las declaraciones de funciones auxiliares. Se definieron macros para simplificar patrones, aunque en la práctica se optó por escribir los patrones completos para mayor claridad.
- **Sección de reglas**: se listaron todas las reglas en orden de prioridad. Primero, las palabras clave (cada una en su propia línea para evitar problemas de escape y prioridad), luego los tipos primitivos, los literales booleanos, los números con sufijo, los flotantes, los enteros, los caracteres y cadenas, los operadores de varios caracteres (de mayor a menor longitud para que coincidan correctamente), los operadores de un solo carácter y símbolos, y finalmente la regla general para identificadores. Se incluyeron las reglas para comentarios y espacios en blanco, cuyas acciones están vacías, y al final la regla de error para cualquier otro carácter.
- **Sección de código de usuario**: se implementó la función `imprimir_token()` para dar formato de tabla a la salida, la función `procesar_archivo()` que abre un archivo, establece `yyin` y ejecuta `yylex()`, y la función `main()` que, si recibe un argumento, procesa ese archivo; en caso contrario, muestra un menú interactivo que lista los archivos de prueba disponibles en la carpeta `Pruebas/`.

### Integración del menú interactivo

Para facilitar las pruebas y demostraciones, se añadió un menú que permite seleccionar entre varios archivos de prueba ubicados en una subcarpeta `Pruebas`. Este menú se implementó usando la biblioteca estándar de C (`dirent.h` para listar directorios, que funciona en entornos Unix y también en Windows con MinGW). El flujo es:

1. Si no se proporciona ningún argumento al ejecutable, se listan todos los archivos regulares dentro de `Pruebas/`.
2. Se muestra un listado numerado y se espera la selección del usuario.
3. Al elegir una opción, se construye la ruta completa y se llama a `procesar_archivo()`.
4. El análisis se repite hasta que el usuario elija salir (opción 0).

Este enfoque hace que el lexer sea autónomo y fácil de usar para evaluar múltiples ejemplos sin necesidad de reescribir comandos.

### Pruebas y depuración

Se prepararon tres archivos de prueba (`prueba1`, `prueba2`, `prueba3`) que contienen fragmentos de código Rust con diferentes combinaciones de tokens. Cada prueba se diseñó para verificar aspectos específicos:

- **Prueba 1**: declaración de variables con tipos y asignaciones.
- **Prueba 2**: funciones con parámetros, retorno y operadores aritméticos y de comparación.
- **Prueba 3**: uso de comentarios, literales con sufijos y errores léxicos deliberados (símbolos no reconocidos).

Durante las pruebas iniciales, se detectaron errores de prioridad entre los tipos y los identificadores, así como problemas con la regla de comentarios de bloque, que se corrigieron ajustando el orden de las reglas y simplificando el patrón del comentario de bloque.

### Compilación y generación del ejecutable

Una vez depurado el archivo `.l`, se procedió a la compilación:

```bash
flex rust_lexer.l
gcc lex.yy.c -o analizador_lexico
```

En Windows, se utilizó la terminal de MinGW (o CMD con las variables de entorno configuradas) y se verificó que tanto `flex` como `gcc` estuvieran accesibles. El binario resultante se llamó `analizador_lexico.exe` (en Windows) y se ubicó en el directorio raíz del proyecto.

### Organización del repositorio

Para cumplir con el requerimiento de entregar un repositorio con código fuente, ejecutable e informe, se estructuró de la siguiente manera:

```
/rust-lexer/
├── rust_lexer.l          # Archivo de especificación Flex
├── lex.yy.c              # (generado) Código C generado por Flex
├── analizador_lexico.exe # Ejecutable compilado (Windows)
├── Pruebas/              # Carpeta con los archivos de prueba
│   ├── prueba1
│   ├── prueba2
│   └── prueba3
├── README.md             # Documentación del proyecto (pasos de instalación y uso)
```

El archivo `README.md` contiene instrucciones detalladas para la instalación de Flex y MinGW en Windows (con advertencia sobre evitar rutas con espacios), la compilación del lexer y la ejecución del menú interactivo. También se incluyen ejemplos de salida esperada y una breve explicación del lenguaje L.

### Lecciones aprendidas

Durante el proceso, se reforzaron conceptos clave como la prioridad de reglas en Flex, la importancia de colocar las palabras clave antes que los identificadores, y el manejo de caracteres especiales en expresiones regulares. La decisión de implementar un menú interactivo no solo mejoró la experiencia de usuario sino que también demostró la flexibilidad de Flex para integrarse con código C adicional. Asimismo, se comprobó que la instalación en Windows requiere cuidado con las rutas, y que el uso de `%option noyywrap` evita problemas de enlace.

La documentación del proceso, junto con el código funcional y los casos de prueba, constituye la entrega completa que permite verificar el correcto funcionamiento del analizador léxico para el lenguaje L.
