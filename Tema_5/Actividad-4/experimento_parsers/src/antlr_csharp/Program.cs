using System;
using System.Diagnostics;
using System.IO;
using Antlr4.Runtime;

namespace DockerComposeParserApp
{
    public class CustomErrorListener : BaseErrorListener, IAntlrErrorListener<int>
    {
        public bool HasErrors { get; private set; } = false;

        public override void SyntaxError(TextWriter output, IRecognizer recognizer, IToken offendingSymbol, int line, int charPositionInLine, string msg, RecognitionException e)
        {
            HasErrors = true;
            Console.Error.WriteLine($"Error sintáctico en línea {line}:{charPositionInLine} - {msg}");
        }

        public void SyntaxError(TextWriter output, IRecognizer recognizer, int offendingSymbol, int line, int charPositionInLine, string msg, RecognitionException e)
        {
            HasErrors = true;
            Console.Error.WriteLine($"Error léxico en línea {line}:{charPositionInLine} - {msg}");
        }
    }

    class Program
    {
        static int Main(string[] args)
        {
            if (args.Length < 1)
            {
                Console.WriteLine("Uso: dotnet run <archivo.yml>");
                return 1;
            }

            string filePath = args[0];
            if (!File.Exists(filePath))
            {
                Console.WriteLine($"Error: Archivo no encontrado {filePath}");
                return 1;
            }

            // 1. Cargar archivo (excluido de medición interna)
            ICharStream stream = CharStreams.fromPath(filePath);

            // 2. Configurar lexer y parser
            DockerComposeLexer lexer = new DockerComposeLexer(stream);
            CustomErrorListener errorListener = new CustomErrorListener();
            lexer.RemoveErrorListeners();
            lexer.AddErrorListener(errorListener);

            CommonTokenStream tokens = new CommonTokenStream(lexer);
            DockerComposeParser parser = new DockerComposeParser(tokens);
            parser.RemoveErrorListeners();
            parser.AddErrorListener(errorListener);

            // 3. Medir tiempo de parseo interno
            Stopwatch sw = Stopwatch.StartNew();
            var tree = parser.dockerComposeFile();
            sw.Stop();

            double parseTimeMs = sw.Elapsed.TotalMilliseconds;

            if (errorListener.HasErrors || parser.NumberOfSyntaxErrors > 0)
            {
                Console.WriteLine($"PARSE_TIME: {parseTimeMs.ToString("F4", System.Globalization.CultureInfo.InvariantCulture)}");
                return 1;
            }

            Console.WriteLine($"PARSE_TIME: {parseTimeMs.ToString("F4", System.Globalization.CultureInfo.InvariantCulture)}");
            return 0;
        }
    }
}
