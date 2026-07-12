# Manual de Usuario de Flex (Metacompilador)

## 1. Introducción a Flex

Flex, cuyo nombre proviene de _Fast Lexical Analyzer Generator_, es una herramienta de software libre ampliamente utilizada en la construcción de compiladores, traductores e intérpretes. Se clasifica como un **metacompilador** porque, en lugar de procesar un lenguaje de programación de alto nivel, su entrada es una descripción formal de los patrones léxicos de un lenguaje, y su salida es código fuente en C que implementa un analizador léxico (lexer) completamente funcional.

La principal ventaja de Flex es que automatiza el tedioso proceso de construcción manual de autómatas finitos deterministas (AFD). El programador solo debe especificar, mediante expresiones regulares, cómo se componen los tokens del lenguaje objetivo, y Flex se encarga de generar la tabla de transiciones, el bucle de lectura y la gestión de estados. Esto no solo reduce drásticamente el tiempo de desarrollo, sino que también minimiza los errores humanos, ya que el código generado es altamente optimizado y confiable.

Flex es la versión mejorada y más moderna de Lex, su predecesor. Es la herramienta estándar en entornos Unix y Linux, y su integración con el compilador GCC permite obtener ejecutables ligeros y rápidos.

## 2. Instalación de Flex

La instalación de Flex es sencilla y varía ligeramente según el sistema operativo.

- **En distribuciones Debian/Ubuntu**:
  Se utiliza el gestor de paquetes APT. Basta con abrir una terminal y ejecutar:

  ```bash
  sudo apt update
  sudo apt install flex
  ```

- **En macOS (con Homebrew)**:
  Se utiliza el gestor de paquetes Homebrew:

  ```bash
  brew install flex
  ```

- **Instalación de Flex en Windows (con MinGW)**

### 2.1. Descarga e instalación de MinGW

Instala **Flex** y **Bison** en Windows descargando los binarios de **GnuWin32**. Instálalos en `C:\GnuWin32` y añade la ruta de la carpeta `bin` a tus Variables de Entorno de Windows para poder usar los comandos desde cualquier terminal.
Pasos para la instalación:

1. **Descarga los archivos:**  
   Ve a las páginas oficiales de GnuWin32 y descarga los paquetes binarios para ambos programas:
   - Descarga Flex en [GnuWin32 Flex](https://www.google.com/url?sa=i&source=web&rct=j&url=https://gnuwin32.sourceforge.net/packages/flex.htm&ved=2ahUKEwjykOrU1MmVAxUIkYkEHY_4IMYQy_kOegoIAggACAAICBAE&opi=89978449&cd&psig=AOvVaw210aNRZ1lIs-NMgx9ZsSj8&ust=1783826224376000).
2. **Instala los programas:**
   - Ejecuta los instaladores descargados.
   - Al elegir la ruta, asegúrate de instalarlos en **`C:\GnuWin32`** para evitar problemas con espacios en los nombres de las carpetas.
3. **Configura las Variables de Entorno:**
   - Presiona la tecla **Windows** y escribe `Variables de entorno`, luego selecciona **Editar las variables de entorno del sistema**.
   - En la ventana emergente, haz clic en el botón **Variables de entorno**
   - En la sección **Variables del sistema**, busca la variable llamada **`Path`**, selecciónala y haz clic en **Editar...**.
   - Haz clic en **Nuevo** y agrega la siguiente ruta: `C:\GnuWin32\bin`.
   - Haz clic en **Aceptar** en todas las ventanas para guardar los cambios.
4. **Verifica la instalación:**
   - Abre una nueva ventana de terminal (CMD o PowerShell) y escribe `flex --version` y `bison --version` para confirmar que el sistema reconoce los comandos
5. **Descargar el instalador de MinGW** desde el sitio oficial:  
   Visita [https://www.mingw-w64.org](https://www.mingw-w64.org/) o, más directamente, descarga el instalador desde [SourceForge](https://sourceforge.net/projects/mingw-w64/).  
   Para simplificar, se recomienda usar el instalador **mingw-w64-install.exe** (versión para 64 bits).
6. **Ejecutar el instalador**:
   - **IMPORTANTE**: Especificar la carpeta de instalación como `C:\mingw64` (o simplemente `C:\mingw`). **Evitar** rutas con espacios (como `C:\Program Files (x86)\mingw`) porque Flex y GCC pueden tener problemas al compilar debido a espacios en las rutas.
7. **Seleccionar los paquetes necesarios**:
   - En el instalador, asegurarse de marcar los paquetes `mingw32-gcc-g++` (para el compilador C/C++) y `mingw32-make` (para utilidades de compilación). También se puede incluir `mingw32-base` y `mingw32-gcc-objc` si se desea, aunque no son estrictamente necesarios.
8. **Completar la instalación**: El proceso descargará e instalará los archivos en la carpeta elegida.

**Compilación de un lexer con Flex en Windows**

```
flex archivo_lexer.l
gcc lex.yy.c -o analizador_lexico
```

## 3. Estructura de un Archivo de Especificación (\*.l)

El corazón de Flex es el archivo de especificación, que convencionalmente tiene la extensión `.l`. Este archivo se divide en **tres secciones** bien diferenciadas, separadas por dos marcas de porcentaje (`%%`).

### 3.1. Sección de Definiciones (Primera sección)

Esta sección abarca desde el inicio del archivo hasta la primera marca `%%`. En ella se colocan:

- **Código C embebido**: Todo lo que esté entre `%{` y `%}` se copia textualmente al inicio del archivo generado `lex.yy.c`. Generalmente se usa para incluir librerías (`#include <stdio.h>`), declarar variables globales o funciones auxiliares.
- **Opciones de Flex**: Comienzan con `%option`. Por ejemplo:
  - `%option noyywrap`: Indica que no se usará la función `yywrap` (que permite procesar múltiples archivos), simplificando el enlace.
  - `%option yylineno`: Habilita el conteo automático de líneas, almacenado en la variable `yylineno`.
- **Definiciones de expresiones regulares**: Se pueden asignar nombres a patrones complejos para reutilizarlos luego. Por ejemplo:
  ```
  DIGITO    [0-9]
  LETRA     [a-zA-Z_]
  IDENT     ({LETRA})({LETRA}|{DIGITO})*
  ```

### 3.2. Sección de Reglas (Segunda sección)

Esta sección está delimitada por la primera marca `%%` y la segunda marca `%%`. Es el núcleo del analizador. Aquí se listan las reglas léxicas, cada una compuesta por un **patrón** (expresión regular) y una **acción** (código C entre llaves).

Cuando Flex ejecuta el analizador, recorre el texto de entrada buscando coincidencias. Al encontrar un patrón, ejecuta la acción asociada. La acción típicamente imprime el token reconocido o devuelve un valor a un analizador sintáctico.

Por ejemplo:

```
"fn"        { printf("Palabra clave: fn"); }
[0-9]+      { printf("Número entero: %s", yytext); }
```

### 3.3. Sección de Código de Usuario (Tercera sección)

Comienza después de la segunda marca `%%`. Aquí se escribe el código C que se copiará tal cual al final del archivo generado. Es el lugar ideal para definir la función `main`, funciones auxiliares de procesamiento de archivos, o la implementación de `yywrap` si no se usó la opción `noyywrap`.

## 4. Componentes Clave: Patrones y Acciones

### 4.1. Patrones (Expresiones Regulares)

Flex utiliza una sintaxis de expresiones regulares muy similar a la de herramientas como `grep` o `sed`. Los elementos más utilizados son:

- **Caracteres literales**: Se escriben entre comillas dobles para evitar que sean interpretados como metacaracteres. Ejemplo: `"if"`, `"+"`.
- **Clases de caracteres**: Entre corchetes `[]`. Ejemplo: `[a-zA-Z]` (cualquier letra), `[0-9]` (cualquier dígito).
- **Cuantificadores**:
  - `*` : Cero o más ocurrencias (Ej: `[a-z]*`).
  - `+` : Una o más ocurrencias (Ej: `[0-9]+`).
  - `?` : Cero o una ocurrencia.
- **Agrupación**: Se usan paréntesis `()` para aplicar cuantificadores a un grupo. Ejemplo: `(ab)+` reconoce `ab`, `abab`, etc.
- **Alternancia**: El operador `|` permite elegir entre varias opciones. Ejemplo: `"true"|"false"`.

### 4.2. Acciones (Código en C)

Cuando un patrón coincide, Flex ejecuta la acción asociada. Dentro de la acción, Flex pone a disposición varias variables especiales:

- **`yytext`**: Es un puntero al carácter que inicia el lexema reconocido. Almacena la cadena completa que coincidió con el patrón.
- **`yyleng`**: Es un entero que contiene la longitud del lexema.
- **`yylineno`**: (Si se activó con `%option yylineno`) contiene el número de línea actual del archivo fuente.

Un ejemplo típico de acción es imprimir el tipo de token y su valor:

```c
{ printf("TOKEN_ENTERO: %s (longitud %d)\n", yytext, yyleng); }
```

## 5. Proceso de Compilación y Ejecución

Trabajar con Flex implica un flujo de trabajo de dos pasos principales:

1. **Generación del analizador en C**:
   Se ejecuta el comando `flex` sobre el archivo de especificación:

   ```bash
   flex rust_lexer.l
   ```

   Esto produce un archivo llamado `lex.yy.c`, que contiene el código fuente del analizador léxico en lenguaje C.

2. **Compilación del ejecutable**:
   Se compila el archivo `lex.yy.c` utilizando GCC (o cualquier compilador C estándar). Es necesario enlazar con la biblioteca de Flex (`-lfl`) en caso de que se haya definido `yywrap` manualmente, aunque con la opción `%option noyywrap` generalmente no es necesaria:

   ```bash
   gcc lex.yy.c -o analizador_lexico
   ```

3. **Ejecución**:
   El ejecutable resultante (`analizador_lexico` en nuestro caso) puede recibir un archivo de texto como argumento:
   ```bash
   ./analizador_lexico ./Pruebas/nombre_archivo_prueba
   ```
   o simplemente ejecutar el .exe, este despliega un menú con las opciones disponibles.

## 6. Variables y Funciones Automáticas Relevantes

Además de las ya mencionadas (`yytext`, `yyleng`, `yylineno`), existen otros elementos que controlan el comportamiento del lexer:

- **`yyin`**: Es un puntero a `FILE` que indica el archivo de entrada. Por defecto apunta a `stdin`, pero se puede redirigir a un archivo específico usando `yyin = fopen("archivo", "r")`.
- **`yyout`**: Puntero a `FILE` para la salida estándar del lexer. Por defecto apunta a `stdout`.
- **`yylex()`**: Es la función principal que ejecuta el análisis léxico. Se invoca una vez para procesar toda la entrada hasta el final del archivo o hasta que se encuentre un error fatal.
- **`yywrap()`**: Es una función que Flex llama al llegar al final del archivo. Si retorna `1`, el análisis termina; si retorna `0`, Flex intenta leer otro archivo (útil para procesar múltiples archivos). La opción `%option noyywrap` proporciona una implementación por defecto que siempre retorna `1`, evitando conflictos de enlace.

## 7. Reglas de Prioridad y Resolución de Conflictos

Una de las características más importantes de Flex es cómo resuelve las ambigüedades cuando una misma cadena podría coincidir con varios patrones:

- **Regla de la coincidencia más larga**: Flex siempre selecciona el patrón que consume la mayor cantidad de caracteres de la entrada. Por ejemplo, si tenemos `"i32"` y `[a-zA-Z][a-zA-Z0-9]*`, la cadena `i32` será reconocida como `"i32"` (palabra clave) porque ambos coinciden, pero la primera regla es más específica y en este caso no genera conflicto si está ordenada correctamente.
- **Regla de primer coincidente (en caso de empate)**: Si dos patrones consumen la misma cantidad de caracteres, Flex elige aquel que aparece primero en el archivo `.l`. Esta regla es crucial para que las **palabras clave** (que son específicas) se coloquen **antes** que la regla general de **identificadores**. Si no se hace así, la palabra `fn` sería reconocida como un identificador en lugar de una palabra reservada.

## 8. Ejemplo Práctico de Uso en el Proyecto

En el contexto de esta actividad, hemos utilizado Flex para construir el analizador léxico del lenguaje _L_ (subconjunto de Rust). El archivo `rust_lexer.l` contiene, por ejemplo:

- En la sección de definiciones: `%option yylineno` para depurar errores con números de línea.
- En la sección de reglas: una lista exhaustiva de palabras clave (`fn`, `let`, `mut`, etc.) antes del patrón de identificadores general `[a-zA-Z_][a-zA-Z0-9_]*`.
- En las acciones: se llama a la función `imprimir_token()` para mostrar el token en formato tabla.

El uso de Flex nos permitió pasar de una especificación teórica (expresiones regulares) a un programa ejecutable en minutos, demostrando el poder de los metacompiladores. Basta con modificar el archivo `.l` para ajustar el lenguaje, sin necesidad de reescribir el bucle de control de estados ni la lógica de lectura de caracteres.

## 9. Ventajas de Usar Flex

Flex ofrece una combinación inmejorable de eficiencia y simplicidad para el desarrollo de analizadores léxicos:

- **Productividad**: Se escribe menos código y se evitan errores comunes en la gestión manual de buffers y transiciones.
- **Optimización**: El código generado es extremadamente rápido, ya que utiliza tablas de transición compactas y técnicas de compresión de autómatas.
- **Mantenibilidad**: Es más fácil actualizar un lenguaje modificando unas líneas en el archivo `.l` que reescribiendo cientos de líneas de C.
- **Integración**: Se combina perfectamente con herramientas de análisis sintáctico como Yacc/Bison, formando el tándem clásico para la construcción de compiladores completos.
