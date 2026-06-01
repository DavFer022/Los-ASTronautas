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
2.1 Paradigma Imperativo / Estructural
Fundamento teórico:
El paradigma imperativo concibe el programa como una secuencia de instrucciones que modifican explícitamente el estado del sistema. La memoria es mutable por defecto y los efectos secundarios (modificación de variables, entrada/salida) constituyen el mecanismo normal de operación (Sebesta, 2016). Este paradigma se basa directamente en el modelo de la máquina de von Neumann: memoria, unidad aritmético-lógica, unidad de control y contador de programa (Aho et al., 2008).
Caso de estudio: Zig como representante moderno
Zig fue seleccionado en esta investigación como exponente contemporáneo del enfoque imperativo estructurado por las siguientes razones (Equipo de Documentación de Zig, 2024):
Ausencia de variables ocultas: No existe sobrecarga de operadores, ni preprocesador, ni flujo de control implícito (como excepciones no declaradas). Todo es explícito.
Control directo de memoria: El programador debe gestionar explícitamente la memoria mediante un allocator, sin recolector de basura.
Metaprogramación en tiempo de compilación: La palabra clave comptime permite ejecutar código en tiempo de compilación, eliminando overhead en tiempo de ejecución sin recurrir a macros complejas al estilo de C preprocesador.
Relación con compiladores:
Los compiladores de lenguajes imperativos (incluyendo Zig) realizan intensos análisis de flujo de datos para detectar variables no inicializadas, usos después de liberación y código inalcanzable (Aho et al., 2008). La optimización de saltos condicionales y la predicción de bifurcaciones son críticas para el rendimiento.
Ejemplo ilustrativo en Zig: 
const std = @import("std");
pub fn main() !void {
var x: i32 = 10;
while (x > 0) {
std.debug.print("{}\n", .{x});
x -= 1;  // Mutación explícita del estado
}
}
