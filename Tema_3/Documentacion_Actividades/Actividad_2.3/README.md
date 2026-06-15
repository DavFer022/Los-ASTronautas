# Actividad 2.3 - Higiene y Optimización de Gramáticas

**Responsable:** Sheen Alburquerque

### 2.3.1.- Patologías de las Gramáticas

Las gramáticas mal diseñadas causan errores en los compiladores. Ejemplifique con 3 casos prácticos diferentes:

#### a) Gramática Ambigua. demuestre la ambigüedad con dos árboles de derivación distintos para la misma cadena.

#### b) Un caso de Recursividad por la Izquierda y muestre el algoritmo paso a paso para eliminarla.


#### c) Un caso que requiera Factorización por la Izquierda y muestre la gramática resultante optimizada.


# Respuestas

# Actividad 3: Higiene y Optimización de Gramáticas

Las gramáticas mal diseñadas pueden causar errores en los compiladores, como bucles infinitos, ambigüedad en la interpretación de las cadenas o ineficiencia en el análisis sintáctico. A continuación se presentan tres patologías comunes y sus respectivas soluciones (Hopcroft, Motwani & Ullman, 2007; Aho et al., 2008).

## a) Gramática Ambigua

Una gramática es ambigua si existe al menos una cadena que puede ser derivada mediante dos árboles de derivación distintos. Esto es indeseable en los lenguajes de programación porque un programa no debería tener más de un significado posible.

**Ejemplo de gramática ambigua para expresiones aritméticas:**
