# Actividad I - Matriz de Paradigmas

## Responsable: Antoima Mariangel



Matriz Descriptiva y Análisis de Paradigmática: Los estudiantes deben elaborar un marco analítico donde expliquen en detalle los paradigmas clásicos y emergentes de la programación. Más allá de enumerar características, el informe debe documentar el fenómeno contemporáneo de la convergencia multiparadigma, demostrando cómo lenguajes de amplio propósito general adoptan características funcionales u orientadas a objetos simultáneamente para responder a las demandas del mercado. Debe completarse la estructura conceptual usando como guía los siguientes ejes temáticos por cada paradigma:



• Paradigma Imperativo/Estructural: Gestión explícita del estado del sistema, secuenciación de instrucciones, mutabilidad de memoria y efectos secundarios.



• Paradigma Orientado a Objetos (POO): Modelos de encapsulamiento, polimorfismo, herencia vs. composición, y abstracción basada en datos y comportamiento combinados. Paradigma Funcional: Inmutabilidad de datos, funciones como ciudadanos de primer orden, evaluación perezosa (lazy evaluation), transparencia referencial y eliminación programática de efectos colaterales.



• Paradigma Lógico/Declarativo: Programación basada en relaciones, unificación, resolución de cláusulas de Horn y abstracción total del flujo de control por parte del programador. Paradigma Concurrente/Actores (Emergente): Modelos de paso de mensajes, aislamiento estricto de estado entre entidades concurrentes y mitigación de condiciones de carrera a nivel de diseño lingüístico.


### Inicio de la Actividad I

#### 1. Matriz Comparativa de Paradigmas de Programación

La siguiente tabla sintetiza los cinco paradigmas fundamentales abordados en esta investigación, destacando sus principios, ventajas, limitaciones y manifestación en lenguajes modernos (Sebesta, 2016).

| Paradigma | Principios Fundamentales | Ventajas Clave | Limitaciones | Lenguajes Representativos |
|-----------|--------------------------|----------------|--------------|---------------------------|
| *Imperativo / Estructural* | Gestión explícita del estado, secuencialidad de instrucciones, mutabilidad de memoria, efectos secundarios, estructuras de control básicas (bucle, condicionales) | Control preciso del hardware, eficiencia en sistemas embebidos, modelo mental sencillo | Complejidad en sistemas grandes, difícil mantenimiento, errores por estado mutable | C, Pascal, Zig |
| *Orientado a Objetos (POO)* | Encapsulamiento, polimorfismo, herencia vs composición, abstracción basada en datos y comportamiento combinados, envío de mensajes | Reutilización, modelado del mundo real, mantenibilidad, escalabilidad | Complejidad añadida, sobreingeniería, problemas con herencia múltiple | Java, C++, Python |
| *Funcional* | Inmutabilidad de datos, funciones como ciudadanas de primer orden, evaluación de la referencia, transparencia referencial, ausencia de efectos colaterales | Código fiable, prueba y depuración, concurrencia natural por diseño | Curva de aprendizaje pronunciada, overhead por inmutabilidad, no intuitivo para problemas con estado intensivo | Haskell, Elixir, Rust, JavaScript |
| *Lógico Declarativo* | Programación basada en relaciones, unificación, cláusulas de Horn, abstracción total del flujo de control por parte del programador | Alto nivel de abstracción, demostración automática de teoremas, ideal para sistemas de reglas | Bajo rendimiento en problemas grandes, ecosistema reducido, poca aplicación comercial | Prolog, Datalog |
| *Concurrencia Actores* | Paso de mensajes entre entidades, aislamiento estricto de estado, mitigación de condiciones de carrera a nivel de diseño lingüístico, modelo "no share" | Concurrencia segura por diseño, ausencia de locks y deadlocks, escalabilidad horizontal | Overhead del paso de mensajes, depuración compleja, riesgo de desbordamiento de buzones | Erlang, Rust (vía librerías) |

#### 2. Análisis Detallado por Paradigma

##### 2.1 Paradigma Imperativo / Estructural

###### Fundamento teórico

El paradigma imperativo concibe el programa como una secuencia de instrucciones que modifican explícitamente el estado del sistema. La memoria es mutable por defecto y los efectos secundarios (modificación de variables, entrada/salida) constituyen el mecanismo normal de operación (Sebesta, 2016). Este paradigma se basa directamente en el modelo de la máquina de von Neumann: memoria, unidad aritmético-lógica, unidad de control y contador de programa (Aho et al., 2008).

###### Caso de estudio: Zig como representante moderno

Zig fue seleccionado en esta investigación como exponente contemporáneo del enfoque imperativo estructurado por las siguientes razones (Equipo de Documentación de Zig, 2024):

- **Ausencia de variables ocultas:** No existe sobrecarga de operadores, ni preprocesador, ni flujo de control implícito (como excepciones no declaradas). Todo es explícito.
- **Control directo de memoria:** El programador debe gestionar explícitamente la memoria mediante un `allocator`, sin recolector de basura.
- **Metaprogramación en tiempo de compilación:** La palabra clave `comptime` permite ejecutar código en tiempo de compilación, eliminando overhead en tiempo de ejecución sin recurrir a macros complejas al estilo de C preprocesador.

###### Relación con compiladores

Los compiladores de lenguajes imperativos (incluyendo Zig) realizan intensos análisis de flujo de datos para detectar variables no inicializadas, usos después de liberación y código inalcanzable (Aho et al., 2008). La optimización de saltos condicionales y la predicción de bifurcaciones son críticas para el rendimiento.

###### Ejemplo ilustrativo en Zig

```zig
const std = @import("std");

pub fn main() !void {
    var x: i32 = 10;
    while (x > 0) {
        std.debug.print("{}\n", .{x});
        x -= 1;  // Mutación explícita del estado
    }
}
```

##### 2.2 Paradigma Orientado a Objetos (POO)

###### Fundamento teórico

La POO organiza el software como una colección de objetos discretos que combinan estado (atributos) y comportamiento (métodos). Los cuatro pilares clásicos son: encapsulamiento (ocultamiento de la representación interna), abstracción (modelado de entidades del dominio), herencia (reutilización mediante jerarquías) y polimorfismo (una interfaz, múltiples implementaciones) (Sebesta, 2016).

###### Debate contemporáneo: Herencia vs Composición

En la ingeniería de software moderna existe consenso en preferir la **composición sobre la herencia** (principio "Composition over Inheritance"). La herencia crea acoplamiento fuerte entre clases base y derivadas, mientras que la composición delega comportamiento a objetos independientes, incrementando la flexibilidad y el mantenimiento (Matsakis y Klock, 2014). Lenguajes como Rust han eliminado la herencia clásica en favor de **traits** (similares a interfaces con implementaciones por defecto), mientras que Python y JavaScript mantienen herencia pero promueven el uso de mixins y composición.

###### Convergencia multiparadigma en Python

Python, uno de los cuatro lenguajes de trabajo de esta investigación, ejemplifica la convergencia multiparadigma al integrar POO con características funcionales: permite definir clases, herencia múltiple y polimorfismo, pero también incluye funciones lambda, `map`, `filter`, `reduce` y comprensiones de listas típicamente asociadas al paradigma funcional (Python Software Foundation, 2024).

###### Ejemplo ilustrativo en Python (composición preferida a herencia)

```python
# Enfoque de composición (recomendado)
class Motor:
    def encender(self):
        return "Motor encendido"

class Vehiculo:
    def __init__(self):
        self.motor = Motor()  # Composición
    
    def arrancar(self):
        return self.motor.encender()
```

##### 2.3 Paradigma Funcional

###### Fundamento teórico

La programación funcional trata la computación como evaluación de funciones matemáticas, evitando estado mutable y datos mutables. Se basa en el **cálculo lambda** (Church, 1930s) como fundamento formal (Sebesta, 2016). Cuatro conceptos son esenciales:

- **Inmutabilidad:** Una vez que un símbolo recibe un valor, este nunca cambia. Las "actualizaciones" crean nuevos valores sin modificar los originales.
- **Funciones de primer orden:** Las funciones pueden ser asignadas a variables, pasadas como argumentos y retornadas desde otras funciones (funciones de orden superior).
- **Transparencia referencial:** Una función con los mismos argumentos retorna siempre el mismo valor, sin efectos colaterales.
- **Evaluación perezosa (lazy evaluation):** Las expresiones no se evalúan hasta que su valor es realmente necesario.

###### Caso de estudio: Rust y el estilo funcional

Rust, otro de los lenguajes de trabajo, incorpora un potente subsistema funcional basado en iteradores perezosos. Su sistema de ownership no entra en conflicto con la inmutabilidad; de hecho, las variables son inmutables por defecto (`let x = 5`), requiriendo `mut` explícito para mutabilidad (Fundación Rust, 2024).

###### Ejemplo ilustrativo en Rust (iteradores funcionales)

```rust
fn main() {
    let suma_pares_cuadrados: i32 = (1..=10)
        .filter(|x| x % 2 == 0)   // Evaluación perezosa
        .map(|x| x * x)           // Evaluación perezosa
        .sum();                   // Evaluación forzada aquí
    
    println!("{}", suma_pares_cuadrados); // 220 (4+16+36+64+100)
}
```

##### 2.4 Paradigma Lógico / Declarativo

###### Fundamento teórico

A diferencia de los paradigmas anteriores, la programación lógica no especifica *cómo* resolver un problema, sino *qué* se quiere resolver. El programador declara hechos y reglas, y un motor de inferencia encuentra soluciones mediante unificación y backtracking (Sebesta, 2016).

###### Abstracción del flujo de control

El programador no escribe bucles ni condicionales explícitos. La recursión y la búsqueda son gestionadas automáticamente por el intérprete lógico. Esto representa el nivel más alto de abstracción entre los paradigmas analizados (Van Roy y Haridi, 2004).

###### Limitaciones y aplicación actual

Aunque el rendimiento es bajo para problemas de gran escala, la programación lógica encuentra aplicación en sistemas expertos, motores de reglas de negocio, procesamiento de grafos de conocimiento y verificación formal de software.

###### Ejemplo ilustrativo (Prolog conceptual)

```prolog
% Hechos
genera_solar(100).   % Generación solar: 100 kW
demanda_industrial(80).  % Demanda: 80 kW

% Regla de balance energético
balance_positivo :- genera_solar(X), demanda_industrial(Y), X > Y.

% Consulta
?- balance_positivo.  % Responde: true
```

##### 2.5 Paradigma Concurrente / Actores

###### Fundamento teórico

El modelo de actores (Hewitt, Bishop y Steiger, 1973) resuelve los problemas de la concurrencia clásica (locks, deadlocks, condiciones de carrera) mediante un diseño radicalmente diferente: los actores son entidades autónomas que poseen estado privado, se comunican exclusivamente mediante mensajes asíncronos, procesan un mensaje a la vez, y pueden crear otros actores (Armstrong, 2013).

###### Comparación con threading clásico

| Característica | Threads con memoria compartida | Modelo de Actores |
|----------------|--------------------------------|-------------------|
| Compartición de estado | Memoria compartida explícita | Ninguna (paso de mensajes) |
| Sincronización | Locks, semáforos, monitores | Por diseño (cola de mensajes) |
| Riesgos principales | Deadlocks, race conditions, livelocks | Overflow de buzón, mensajes huérfanos |
| Escalabilidad en multicore | Limitada por contención de locks | Alta (sin bloqueo global) |

###### Convergencia multiparadigma en los lenguajes de trabajo

- **Rust:** No tiene actores en la biblioteca estándar, pero ofrece canales (`std::sync::mpsc`) para paso de mensajes y librerías como `actix` que implementan el modelo completo (Fundación Rust, 2024).
- **JavaScript:** Web Workers + `postMessage` proporcionan aislamiento de estado y paso de mensajes, esencial para aplicaciones web con procesamiento en paralelo (Mozilla Developer Network, 2024).
- **Python:** El módulo `multiprocessing` con `Queue` implementa un estilo similar a actores aunque con mayor overhead (Python Software Foundation, 2024).

###### Ejemplo ilustrativo conceptual (JavaScript con Web Worker)

```javascript
// worker.js
self.onmessage = function(event) {
    let resultado = procesar(event.data);
    self.postMessage(resultado);
};

// main.js
const worker = new Worker('worker.js');
worker.postMessage(datos);
worker.onmessage = function(event) {
    console.log('Resultado:', event.data);
};
```
