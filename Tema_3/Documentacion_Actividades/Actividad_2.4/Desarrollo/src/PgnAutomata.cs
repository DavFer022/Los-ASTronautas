using System.Text.RegularExpressions;

const string RegexPattern = @"^([a-h][1-8]|[a-h]x[a-h][1-8]|[KQRBN][a-h][1-8]|[KQRBN]x[a-h][1-8]|O-O)\+?$";
var automata = new Regex(RegexPattern, RegexOptions.Compiled | RegexOptions.CultureInvariant);

var examples = new[]
{
    "e4", "d5", "a3",
    "exd5", "cxb2",
    "Nf3", "Nc6", "Ne5",
    "Nxe5", "Nxf2",
    "Bc4", "Bb5", "Be2",
    "Bxc4", "Bxh7",
    "Re1", "Ra8", "Rd3",
    "Rxe5", "Rxa7",
    "Qh5", "Qd2", "Qa4",
    "Qxe5", "Qxh7",
    "Ke2", "Kg1", "Kf7",
    "Kxe2", "Kxf3",
    "O-O",
    "Qh5+", "Nxf7+", "Bc4+", "exd5+"
};

while (true)
{
    Console.Clear();
    Console.WriteLine("PGN simplificado - Pruebas rápidas\n");
    Console.WriteLine("1) Mostrar lista de ejemplos");
    Console.WriteLine("2) Seleccionar ejemplo por número");
    Console.WriteLine("3) Probar movimiento personalizado");
    Console.WriteLine("4) Ejecutar todos los ejemplos");
    Console.WriteLine("0) Salir");
    Console.Write("Opción: ");

    var option = Console.ReadLine()?.Trim();
    Console.WriteLine();

    switch (option)
    {
        case "1":
            PrintExamples();
            WaitForKey();
            break;
        case "2":
            SelectExample();
            break;
        case "3":
            TestCustomMove();
            break;
        case "4":
            RunAllExamples();
            break;
        case "0":
            return;
        default:
            Console.WriteLine("Opción no válida. Presiona una tecla para continuar...");
            WaitForKey();
            break;
    }
}

void PrintExamples()
{
    Console.WriteLine("Ejemplos disponibles:\n");
    for (var i = 0; i < examples.Length; i++)
    {
        Console.WriteLine($"{i + 1,2}. {examples[i]}");
    }
    Console.WriteLine();
}

void SelectExample()
{
    PrintExamples();
    Console.Write("Ingresa el número del ejemplo: ");
    if (!int.TryParse(Console.ReadLine()?.Trim(), out var index) || index < 1 || index > examples.Length)
    {
        Console.WriteLine("Número inválido.");
        WaitForKey();
        return;
    }

    var move = examples[index - 1];
    PrintResult(move);
    WaitForKey();
}

void TestCustomMove()
{
    Console.Write("Movimiento a probar: ");
    var move = Console.ReadLine()?.Trim() ?? string.Empty;
    Console.WriteLine();
    PrintResult(move);
    WaitForKey();
}

void RunAllExamples()
{
    Console.WriteLine("Resultado de todos los ejemplos:\n");
    for (var i = 0; i < examples.Length; i++)
    {
        var move = examples[i];
        var valid = automata.IsMatch(move);
        Console.WriteLine($"{i + 1,2}. {move,-6} => {(valid ? "Válido" : "Inválido"),-8} | {GetMoveClass(move)}");
    }
    Console.WriteLine();
    WaitForKey();
}

void PrintResult(string move)
{
    if (string.IsNullOrWhiteSpace(move))
    {
        Console.WriteLine("No se ingresó ningún movimiento.");
        return;
    }

    var valid = automata.IsMatch(move);
    Console.WriteLine($"Movimiento: {move}");
    Console.WriteLine($"Expresión regular: {RegexPattern}");
    Console.WriteLine($"Resultado: {(valid ? "Válido" : "Inválido")}");
    Console.WriteLine($"Clase estimada: {GetMoveClass(move)}");
}

string GetMoveClass(string move)
{
    if (string.IsNullOrWhiteSpace(move))
        return "Sin movimiento";

    var token = move.Trim();
    var hasPlus = token.EndsWith("+");
    if (hasPlus)
        token = token[..^1];

    if (token == "O-O")
        return "Enroque corto";
    if (token.Length == 2 && IsColumn(token[0]) && IsRow(token[1]))
        return "Peón simple";
    if (token.Length == 5 && IsColumn(token[0]) && token[1] == 'x' && IsColumn(token[2]) && IsRow(token[3]))
        return "Peón con captura";
    if (token.Length == 3 && IsPiece(token[0]) && IsColumn(token[1]) && IsRow(token[2]))
        return "Pieza simple";
    if (token.Length == 4 && IsPiece(token[0]) && token[1] == 'x' && IsColumn(token[2]) && IsRow(token[3]))
        return "Pieza con captura";

    return hasPlus ? "Movimiento con jaque" : "Movimiento no reconocido";
}

bool IsColumn(char c) => c is >= 'a' and <= 'h';
bool IsRow(char c) => c is >= '1' and <= '8';
bool IsPiece(char c) => c is 'K' || c is 'Q' || c is 'R' || c is 'B' || c is 'N';

void WaitForKey()
{
    Console.WriteLine("\nPresiona cualquier tecla para continuar...");
    Console.ReadKey(true);
}
