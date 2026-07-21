import sys
import os
import time

# Permitir importar los archivos generados desde el subdirectorio generated
sys.path.append(os.path.join(os.path.dirname(__file__), "generated"))

from antlr4 import FileStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener
from DockerComposeLexer import DockerComposeLexer
from DockerComposeParser import DockerComposeParser

class VerboseErrorListener(ErrorListener):
    def __init__(self):
        super(VerboseErrorListener, self).__init__()
        self.has_errors = False

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.has_errors = True
        sys.stderr.write(f"Error sintáctico en línea {line}:{column} - {msg}\n")

def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py <archivo.yml>")
        sys.exit(1)

    file_path = sys.argv[1]
    if not os.path.exists(file_path):
        print(f"Error: Archivo no encontrado {file_path}")
        sys.exit(1)

    # 1. Leer archivo de texto a memoria (excluido de la medición interna)
    input_stream = FileStream(file_path, encoding='utf-8')
    
    # 2. Configurar lexer y parser
    lexer = DockerComposeLexer(input_stream)
    error_listener = VerboseErrorListener()
    lexer.removeErrorListeners()
    lexer.addErrorListener(error_listener)

    tokens = CommonTokenStream(lexer)
    parser = DockerComposeParser(tokens)
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)

    # 3. Medición precisa del tiempo de parseo puro
    t_start = time.perf_counter()
    tree = parser.dockerComposeFile()
    t_end = time.perf_counter()

    parse_time_ms = (t_end - t_start) * 1000.0

    if error_listener.has_errors or parser.getNumberOfSyntaxErrors() > 0:
        print(f"PARSE_TIME: {parse_time_ms:.4f}")
        sys.exit(1)

    print(f"PARSE_TIME: {parse_time_ms:.4f}")
    sys.exit(0)

if __name__ == "__main__":
    main()
