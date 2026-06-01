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
use std::time::Instant;

// Función que calcula los pasos de Collatz para un número
fn pasos_collatz(mut numero: u64) -> u64 {
    let mut pasos = 0;
    while numero > 1 {
        if numero % 2 == 0 {
            // Si es par, se divide entre 2
            numero /= 2;
        } else {
            // Si es impar, se multiplica por 3 y se suma 1
            numero = 3 * numero + 1;
        }
        pasos += 1;
    }
    pasos
}

// Función principal
fn main() {
    // Cantidad de números a probar (desde 1 hasta N)
    let n = 100_000;
    
    // Medimos el tiempo de inicio
    let inicio = Instant::now();
    
    // Variable para acumular todos los pasos
    let mut total_pasos = 0;
    
    // Recorremos todos los números desde 1 hasta N
    for i in 1..=n {
        total_pasos += pasos_collatz(i);
    }
    
    // Medimos el tiempo transcurrido en milisegundos
    let tiempo_ms = inicio.elapsed().as_millis();
    
    // Mostramos los resultados
    println!("Lenguaje: Rust");
    println!("Números procesados: 1 hasta {}", n);
    println!("Tiempo de ejecución: {} milisegundos", tiempo_ms);
    println!("Total de pasos acumulados: {}", total_pasos);
}
