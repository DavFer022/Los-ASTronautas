/*
ALGORITMO DE COLLATZ - BENCHMARKING
Grupo: Los ASTronautas

Enunciado:
Demostrar la conjetura de Collatz para todos los números menores que N.
Para cada número n, se aplica:
- si n es par: n = n / 2
- si n es impar: n = 3 * n + 1
El proceso termina cuando n = 1.

Este programa mide el tiempo de ejecución para N = 100,000
y calcula el total de pasos realizados.
*/
// Función que calcula los pasos de Collatz para un número
function pasosCollatz(numero) {
    let pasos = 0;
    while (numero > 1) {
        if (numero % 2 === 0) {
            // Si es par, se divide entre 2
            numero = numero / 2;
        } else {
            // Si es impar, se multiplica por 3 y se suma 1
            numero = 3 * numero + 1;
        }
        pasos++;
    }
    return pasos;
}

// Función principal
function main() {
    // Cantidad de números a probar (desde 1 hasta N)
    const N = 100000;
    
    // Medimos el tiempo de inicio (en milisegundos)
    const inicio = Date.now();
    
    // Variable para acumular todos los pasos
    let totalPasos = 0;
    
    // Recorremos todos los números desde 1 hasta N
    for (let i = 1; i <= N; i++) {
        totalPasos += pasosCollatz(i);
    }
    
    // Medimos el tiempo de finalización
    const fin = Date.now();
    
    // Calculamos el tiempo transcurrido
    const tiempoMs = fin - inicio;
    
    // Mostramos los resultados
    console.log(`Lenguaje: JavaScript (Node.js)`);
    console.log(`Números procesados: 1 hasta ${N}`);
    console.log(`Tiempo de ejecución: ${tiempoMs} milisegundos`);
    console.log(`Total de pasos acumulados: ${totalPasos}`);
}

// Ejecutamos la función principal
main();
