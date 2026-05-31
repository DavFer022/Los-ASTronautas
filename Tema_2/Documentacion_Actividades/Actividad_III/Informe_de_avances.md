# Diseño DSL para Sistemas lógicos - físicos Críticos

### Planteamiento del problema

Se nos pide diseñar el *Lenguaje L*, un DLS de de programación de alto nivel para resolver problemas de HMI de un ECO-GRID, un **Sistema de Gestión de Microrredes Eléctricas Inteligentes y Almacenamiento de Energía**, el *Lenguaje L* debe ser capaz de controlar los componentes integrados mediante un driver de bajo nivel.

#### Componentes integrados a controlar
1. Arreglos de Paneles Solares y Turbinas Eólicas (Generadores)
2. Bancos de Baterías de Litio de Respaldo
3. Sensores de Flujo Eléctrico y Caudal de Carga (Inversores)
4. Sensores Térmicos de Celda (Baterias)
5. Conmutadores Electrónicos de Red (Relés de Alta Potencia)

### Objetivos a desarrollar
1. Especificación del Alfabeto y Reglas Léxicas:
2. Palabras Clave Obligatorias
3. Gramática Sintáctica Abstracta
4. Prueba de viabilidad en dos escenarios 
	1. Escenario Operativo A (Prevención de Fuga Térmica y Gestión de Alivio de Carga)
	2. Escenario Operativo B (Balance de Carga y Optimización Energética Autónoma)

## Fase 1: Diseño del Alfabeto y Reglas Léxicas (Morfología)

Aquí definimos los caracteres que pueden ser usados en el lenguaje, que representan y como se usaran, también definimos las reglas críticas como identificadores, delimitadores y terminadores, esto con el propósito de darle robustez al lenguaje
## Fase 2: Diseño de la Gramática Sintáctica Abstracta
Aquí defines cómo se combinan las palabras clave para formar oraciones lógicas.

## Fase 3: Redacción de los Escenarios (El Código)
En esta fase ponemos a prueba el lenguaje creado resolviendo dos problemas operativos específicos dentro de la planta.
