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

<E> ::= <E> + <E> | <E> * <E> | id

**Cadena ambigua:** id + id * id

**Árbol de derivación 1** (interpretación: (id + id) * id):

           <E>
         /  |  \
       <E>  *  <E>
      / | \     |
    <E> + <E>  id
     |     |
    id    id
       
**Árbol de derivación 2** (interpretación: id + (id * id)):
       
       <E>
      / | \
    <E> + <E>
     |   / | \
    id <E> * <E>
        |     |
       id    id

**Solución:** Reescribir la gramática introduciendo niveles de precedencia:

<E> ::= <E> + <T> | <T>
<T> ::= <T> * <F> | <F>
<F> ::= id | "(" <E> ")"

Esta gramática elimina la ambigüedad porque fuerza la precedencia de los operadores: la multiplicación (*) tiene mayor prioridad que la suma (+) (Aho et al., 2008).


## b) Recursividad por la Izquierda

Un problema común en los analizadores sintácticos descendentes (top-down) es la recursividad por la izquierda. Una gramática es recursiva por la izquierda si contiene una regla de la forma A → A α. Esto provoca bucles infinitos en los analizadores recursivos.

**Ejemplo de gramática con recursividad por la izquierda:**

<E> ::= <E> + <T> | <T>
<T> ::= id

**Cadena problemática:** id + id + id

**Algoritmo de eliminación de recursividad por la izquierda:**

Dada una regla de la forma A → A α | β (donde β no comienza con A), se transforma en:

A  → β A'
A' → α A' | ε


**Aplicación paso a paso a la gramática anterior:**

1.	Identificar la regla problemática: <E> → <E> + <T> | <T>

Aquí A = <E>, α = + <T>, β = <T>

2.	Aplicar la transformación:

<E> → <T> <E'>
<E'> → + <T> <E'> | ε

3.	La gramática resultante (sin recursividad por la izquierda) es:

**<E>  → <T> <E'>
<E'> → + <T> <E'> | ε
<T>  → id**


Esta gramática puede ser procesada sin problemas por un analizador descendente (Hopcroft, Motwani & Ullman, 2007).


## c) Factorización por la Izquierda

Es una técnica que se aplica cuando dos o más reglas de un mismo no terminal comparten un prefijo común. Esto causa ambigüedad temporal en el analizador, que no sabe qué regla elegir hasta leer más tokens.

**Ejemplo de gramática que requiere factorización:**

<A> ::= id = <E> | id ( <E> )


Ambas reglas comienzan con el prefijo común id. El analizador no puede decidir qué regla aplicar hasta leer el siguiente token (= o ().

**Algoritmo de factorización por la izquierda:**

Dadas las reglas de la forma A → α β₁ | α β₂ | ... | α βₙ, se transforman en:

A  → α A'
A' → β₁ | β₂ | ... | βₙ


**Aplicación a la gramática anterior:**

1.	Identificar el prefijo común: α = id
2.	Identificar los sufijos: β₁ = = <E> y β₂ = ( <E> )
3.	Aplicar la transformación.

**Gramática optimizada resultante:**

**<A>  → id <A'>
<A'> → = <E> | ( <E> )**


Esta gramática factorizada permite al analizador leer el token id y luego decidir qué camino tomar basándose en el siguiente token (si es = o () (Aho et al., 2008).


