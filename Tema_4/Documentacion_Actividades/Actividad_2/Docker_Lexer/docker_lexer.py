import re

# Lista de tokens: (nombre_token, expresión_regular)
tokens = [
    # Palabras clave de Dockerfile
    ('FROM', r'\bFROM\b'),
    ('RUN', r'\bRUN\b'),
    ('COPY', r'\bCOPY\b'),
    ('ADD', r'\bADD\b'),
    ('WORKDIR', r'\bWORKDIR\b'),
    ('ENV', r'\bENV\b'),
    ('EXPOSE', r'\bEXPOSE\b'),
    ('CMD', r'\bCMD\b'),
    ('ENTRYPOINT', r'\bENTRYPOINT\b'),
    ('ARG', r'\bARG\b'),
    ('LABEL', r'\bLABEL\b'),
    ('VOLUME', r'\bVOLUME\b'),
    ('USER', r'\bUSER\b'),
    ('ONBUILD', r'\bONBUILD\b'),
    ('STOPSIGNAL', r'\bSTOPSIGNAL\b'),
    ('HEALTHCHECK', r'\bHEALTHCHECK\b'),
    ('SHELL', r'\bSHELL\b'),

    # Identificadores (nombres de variables, rutas, etc.)
    ('IDENTIFIER', r'[a-zA-Z0-9_][a-zA-Z0-9_./-]*'),

    # Números
    ('NUMBER', r'\b\d+(\.\d+)?\b'),

    # Operadores y símbolos
    ('EQUALS', r'='),
    ('COMMA', r','),
    ('LBRACKET', r'\['),
    ('RBRACKET', r'\]'),
    ('LBRACE', r'\{'),
    ('RBRACE', r'\}'),
    ('SEMICOLON', r';'),

    # Caracteres especiales válidos en Dockerfile
    ('COLON', r':'),
    ('SLASH', r'/'),
    ('DOT', r'\.'),
    ('DASH', r'-'),
    ('AMPERSAND', r'&'),
    ('QUOTE', r'"'),
    ('PIPE', r'\|'),
    ('GREATER', r'>'),
    ('LESS', r'<'),
    ('AT', r'@'),

    # Comentarios
    ('COMMENT', r'#.*'),

    # Espacios en blanco (se ignoran)
    ('SKIP', r'[ \t]+'),

    # Nueva línea
    ('NEWLINE', r'\n'),

    # ERROR: caracteres no reconocidos (siempre al final)
    ('ERROR', r'.'),
]

def lexer(texto):
    """Analiza el texto y genera tokens."""
    patron = '|'.join(f'(?P<{nombre}>{regex})' for nombre, regex in tokens)
    linea = 1
    inicio_linea = 0

    for coincidencia in re.finditer(patron, texto):
        tipo = coincidencia.lastgroup
        valor = coincidencia.group(tipo)

        if tipo == 'NEWLINE':
            inicio_linea = coincidencia.end()
            linea += 1
        elif tipo == 'SKIP' or tipo == 'COMMENT':
            continue
        elif tipo == 'ERROR':
            columna = coincidencia.start() - inicio_linea + 1
            yield (tipo, valor, linea, columna)
        else:
            columna = coincidencia.start() - inicio_linea + 1
            yield (tipo, valor, linea, columna)

def main():
    import sys
    import os

    # Si se pasa un argumento, usar ese archivo
    if len(sys.argv) > 1:
        nombre_archivo = sys.argv[1]
    else:
        # Si no, usar pruebas/Dockerfile1 por defecto
        nombre_archivo = 'pruebas/Dockerfile1'

    # Verificar si el archivo existe
    if not os.path.exists(nombre_archivo):
        print(f"❌ Error: El archivo '{nombre_archivo}' no fue encontrado.")
        print("📌 Asegúrate de tener archivos en la carpeta 'pruebas/'")
        return

    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
    except Exception as e:
        print(f"❌ Error al leer el archivo: {e}")
        return

    print(f"📄 Analizando: {nombre_archivo}\n")
    print(f"{'TOKEN':<20} {'LEXEMA':<25} {'LÍNEA':<6} {'COLUMNA':<8}")
    print("-" * 65)

    for token in lexer(contenido):
        tipo, valor, linea, columna = token
        if tipo == 'ERROR':
            print(f"\033[91mERROR\033[0m{'':<16} {valor:<25} {linea:<6} {columna:<8}")
        else:
            print(f"{tipo:<20} {valor:<25} {linea:<6} {columna:<8}")

if __name__ == "__main__":
    main()
