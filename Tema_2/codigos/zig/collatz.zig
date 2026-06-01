// ALGORITMO DE COLLATZ - BENCHMARKING
// Grupo: Los ASTronautas
//
// Enunciado:
// Demostrar la conjetura de Collatz para todos los números menores que N.
// Para cada número n, se aplica:
// - si n es par: n = n / 2
// - si n es impar: n = 3 * n + 1
// El proceso termina cuando n = 1.
//
// Este programa mide el tiempo de ejecución para N = 100,000
// y calcula el total de pasos realizados.

const std = @import("std");

// Función que calcula los pasos de Collatz para un número
fn pasosCollatz(numero: u64) u64 {
    var n = numero;
    var pasos: u64 = 0;
    while (n > 1) {
        if (n % 2 == 0) {
            // Si es par, se divide entre 2
            n = n / 2;
        } else {
            // Si es impar, se multiplica por 3 y se suma 1
            n = 3 * n + 1;
        }
        pasos += 1;
    }
    return pasos;
}

// Función principal
pub fn main() !void {
    // Cantidad de números a probar (desde 1 hasta N)
    const N = 100000;
    
    // Medimos el tiempo de inicio (nanosegundos)
    const inicio = std.time.nanoTimestamp();
    
    // Variable para acumular todos los pasos
    var total_pasos: u64 = 0;
    
    // Recorremos todos los números desde 1 hasta N
    var i: u64 = 1;
    while (i <= N) : (i += 1) {
        total_pasos += pasosCollatz(i);
    }
    
    // Medimos el tiempo de finalización
    const fin = std.time.nanoTimestamp();
    
    // Calculamos el tiempo transcurrido en milisegundos
    const tiempo_ns = fin - inicio;
    const tiempo_ms = @as(f64, @floatFromInt(tiempo_ns)) / 1_000_000.0;
    
    // Mostramos los resultados
    std.debug.print("Lenguaje: Zig\n", .{});
    std.debug.print("Numeros procesados: 1 hasta {d}\n", .{N});
    std.debug.print("Tiempo de ejecucion: {d:.2} milisegundos\n", .{tiempo_ms});
    std.debug.print("Total de pasos acumulados: {d}\n", .{total_pasos});
}
