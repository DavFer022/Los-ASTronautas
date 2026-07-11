# Actividad 2 - Construya un lexer para la verificación de archivos docker mediante expresiones regulares.

**Responsable:** Sheen Alburquerque

En el Informe debe indicar paso a paso la construcción de su lexer y 3 ejemplos de ejecución. En el archivo comprimido entregar los código (fuentes y ejecutables).

## Desarrollo de Actividad 2

---

## Objetivo de la actividad

Construir un analizador léxico que verifique archivos Dockerfile, identificando sus instrucciones y componentes, y reportando errores léxicos cuando corresponda.

---

## Tokens reconocidos

| Token | Descripción | Ejemplo |
|-------|-------------|---------|
| `FROM` | Imagen base | `FROM ubuntu:22.04` |
| `RUN` | Ejecutar comando | `RUN apt-get update` |
| `COPY` | Copiar archivos | `COPY . /app` |
| `ADD` | Copiar archivos (con soporte de URLs) | `ADD file.tar.gz /tmp` |
| `WORKDIR` | Directorio de trabajo | `WORKDIR /app` |
| `ENV` | Variable de entorno | `ENV PORT=8080` |
| `EXPOSE` | Puerto expuesto | `EXPOSE 80` |
| `CMD` | Comando por defecto | `CMD ["python", "app.py"]` |
| `ENTRYPOINT` | Punto de entrada | `ENTRYPOINT ["python"]` |
| `ARG` | Argumento de construcción | `ARG VERSION=1.0` |
| `LABEL` | Metadatos | `LABEL version="1.0"` |
| `VOLUME` | Volumen | `VOLUME /data` |
| `USER` | Usuario | `USER root` |
| `ONBUILD` | Instrucción para builds futuros | `ONBUILD RUN echo "..."` |
| `STOPSIGNAL` | Señal de parada | `STOPSIGNAL SIGTERM` |
| `HEALTHCHECK` | Verificación de salud | `HEALTHCHECK CMD curl` |
| `SHELL` | Shell por defecto | `SHELL ["/bin/sh", "-c"]` |
| `IDENTIFIER` | Nombres de variables, rutas | `ubuntu`, `/app`, `python` |
| `NUMBER` | Valores numéricos | `80`, `8080`, `1.0` |
| `EQUALS` | Asignación | `=` |
| `COMMA` | Separador | `,` |
| `LBRACKET` | Corchete izquierdo | `[` |
| `RBRACKET` | Corchete derecho | `]` |
| `LBRACE` | Llave izquierda | `{` |
| `RBRACE` | Llave derecha | `}` |
| `SEMICOLON` | Punto y coma | `;` |
| `COMMENT` | Comentario | `# Esto es un comentario` |
| `SKIP` | Espacios y tabuladores | (ignorado) |
| `NEWLINE` | Nueva línea | (control) |
| `ERROR` | Carácter no reconocido | `@`, `$` |

---

## Requisitos previos

| Herramienta | Versión | Verificación |
|-------------|---------|--------------|
| Python | 3.x | `python --version` |

**Nota:** No requiere dependencias externas, solo el módulo `re` de la biblioteca estándar.

---

## Estructura del repositorio
```
Tema_4/Documentacion_Actividades/Actividad_2/
├── docker_lexer.py # Código fuente del lexer
├── README.md # Este archivo
└── pruebas/
├── Dockerfile1 # Ejemplo 1: Imagen base simple
├── Dockerfile2 # Ejemplo 2: Configuración de entorno
├── Dockerfile3 # Ejemplo 3: Configuración avanzada
└── Dockerfile_error # Ejemplo con errores léxicos
```

---

## Instalación y ejecución

### 1. Clonar o descargar el repositorio

```bash
git clone https://github.com/DavFer022/Los-ASTronautas.git
cd Los-ASTronautas/Tema_4/codigos/Actividad_2
```

### 2. Ejecutar el lexer
Analizar el archivo por defecto (pruebas/Dockerfile1):

python docker_lexer.py

Analizar un archivo específico:

python docker_lexer.py pruebas/Dockerfile2
python docker_lexer.py pruebas/Dockerfile3
python docker_lexer.py pruebas/Dockerfile_error

# Ejemplos de ejecución
Ejemplo 1: Dockerfile1 (imagen base simple)
Entrada (pruebas/Dockerfile1):

```
#### Dockerfile1 - Imagen base simple
FROM ubuntu:22.04
RUN apt-get update
CMD ["echo", "Hola mundo"]
```

### Analizando: pruebas/Dockerfile1

```
TOKEN                LEXEMA                    LÍNEA  COLUMNA
-----------------------------------------------------------------
FROM                 FROM                      2      1
IDENTIFIER           ubuntu                    2      6
NUMBER               22.04                     2      13
RUN                  RUN                       3      1
IDENTIFIER           apt-get                   3      5
IDENTIFIER           update                    3      13
CMD                  CMD                       4      1
LBRACKET             [                         4      5
IDENTIFIER           echo                      4      7
COMMA                ,                         4      12
IDENTIFIER           Hola                      4      15
IDENTIFIER           mundo                     4      20
RBRACKET             ]                         4      26
```

Ejemplo 2: Dockerfile2 (configuración de entorno)
Entrada (pruebas/Dockerfile2):

```
# Dockerfile2 - Configuración de entorno
FROM python:3.12
WORKDIR /app
COPY . /app
ENV PORT=8080
EXPOSE 8080
CMD ["python", "app.py"]
```

Salida:

Analizando: pruebas/Dockerfile2
```
TOKEN                LEXEMA                    LÍNEA  COLUMNA
-----------------------------------------------------------------
FROM                 FROM                      2      1
IDENTIFIER           python                    2      6
NUMBER               3.12                      2      13
WORKDIR              WORKDIR                   3      1
IDENTIFIER           app                       3      10
COPY                 COPY                      4      1
IDENTIFIER           app                       4      9
ENV                  ENV                       5      1
IDENTIFIER           PORT                      5      5
EQUALS               =                         5      9
NUMBER               8080                      5      10
EXPOSE               EXPOSE                    6      1
NUMBER               8080                      6      8
CMD                  CMD                       7      1
LBRACKET             [                         7      5
IDENTIFIER           python                    7      7
COMMA                ,                         7      14
IDENTIFIER           app.py                    7      17
RBRACKET             ]                         7      24
```

Ejemplo 3: Dockerfile_error (errores léxicos)
Entrada (pruebas/Dockerfile_error):

```
FROM ubuntu
RUN apt-get update @
COPY . /app
```

Salida:

Analizando: pruebas/Dockerfile_error
```
TOKEN                LEXEMA                    LÍNEA  COLUMNA
-----------------------------------------------------------------
FROM                 FROM                      1      1
IDENTIFIER           ubuntu                    1      6
RUN                  RUN                       2      1
IDENTIFIER           apt-get                   2      5
IDENTIFIER           update                    2      13
ERROR                @                         2      20
COPY                 COPY                      3      1
ERROR                .                         3      6
ERROR                /                         3      8
IDENTIFIER           app                       3      9
```

## Cómo funciona el código
1. Definición de tokens
Cada token se define como una tupla (nombre, expresión_regular). Las expresiones regulares definen el patrón que debe reconocer el lexer.

2. Función lexer(texto)
Esta función recibe el texto del Dockerfile y:

Combina todos los patrones en una sola expresión regular.

Recorre el texto buscando coincidencias.

Clasifica cada coincidencia según el token que coincide.

Ignora espacios y comentarios.

Devuelve los tokens como un generador.

3. Función main()
Recibe el nombre del archivo como argumento (o usa Dockerfile1 por defecto).

Lee el archivo y llama al lexer.

Muestra los tokens en formato de tabla.

4. Manejo de errores
Cualquier carácter que no coincida con ningún token definido es reportado como ERROR, mostrando la línea y columna donde ocurrió.
