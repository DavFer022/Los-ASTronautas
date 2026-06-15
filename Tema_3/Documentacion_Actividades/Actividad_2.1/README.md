# Actividad 2.1 - Fundamentos y Jerarquía (Teoría Aplicada)

**Responsable:** Mariangel Antoima

### 2.1.1.- Relación Gramática-Lenguaje

Indique el concepto y al menos un ejemplo práctico de la relación entre Gramáticas y Lenguajes Formales. Explique detalladamente el mecanismo mediante el cual una gramática genera un lenguaje.

### 2.1.2.- Jerarquía de Chomsky

Explique los 4 tipos de gramáticas de la Jerarquía de Chomsky. Para cada tipo, proporcione un ejemplo práctico representado en notación BNF (Backus-Naur Form).

#Desarrollo

# Fundamentos y Jerarquía de las Gramáticas Formales

## Relación Gramática-Lenguaje

### Concepto de Gramática Formal

Una gramática formal es un conjunto finito de reglas de producción que
permiten generar cadenas de símbolos siguiendo una estructura definida.
Formalmente, una gramática se define como una cuádrupla G = (N, Σ, P,
S), donde (Hopcroft & Ullman, 1979):

- **N** es un conjunto finito de símbolos no terminales (variables)
- **Σ** es un conjunto finito de símbolos terminales (el alfabeto del
  lenguaje)
- **P** es un conjunto finito de reglas de producción de la forma α → β
- **S** ∈ N es el símbolo inicial o axioma de la gramática

Los **símbolos terminales** son los elementos básicos que aparecen en
las cadenas finales del lenguaje (como letras, dígitos o palabras
reservadas). Los **símbolos no terminales** son variables auxiliares que
guían el proceso de generación y deben ser reemplazadas eventualmente
por terminales.

### Concepto de Lenguaje Formal

Un lenguaje formal L es un subconjunto de Σ*, donde Σ* representa el
conjunto de todas las cadenas finitas posibles formadas a partir del
alfabeto Σ. En otras palabras, un lenguaje formal es un conjunto
matemático de cadenas válidas que cumplen ciertas reglas estructurales
(Sipser, 2012).

### Relación entre Gramática y Lenguaje

La relación fundamental es que **la gramática genera el lenguaje**.
Específicamente, el lenguaje generado por una gramática G, denotado como
L(G), se define como (Linz & Rodger, 2022):

*L(G) = { w ∈ Σ* | S ⇒* w }*

Es decir, el lenguaje L(G) es el conjunto de todas las cadenas w de
terminales que pueden ser derivadas desde el símbolo inicial S aplicando
cero o más reglas de producción.

### Mecanismo de Generación (Derivación)

El proceso mediante el cual una gramática genera una cadena se
llama **derivación**. Una derivación es una secuencia de pasos donde, en
cada paso, se reemplaza un no terminal por el lado derecho de una regla
de producción que lo tenga como lado izquierdo. La notación ⇒ indica un
paso de derivación, mientras que ⇒* indica cero o más pasos (Hopcroft,
Motwani & Ullman, 2006).

**Ejemplo práctico de derivación:**

Considere la gramática G1 = (N, Σ, P, S) donde:

- N = {S, NP, VP}
- Σ = {grows, rice, wheat}
- P = { S → NP VP, NP → rice, NP → wheat, VP → grows }

Para generar la cadena "rice grows", se realiza la siguiente
derivación:

1.  S ⇒ NP VP (aplicando S → NP VP)
2.  ⇒ rice VP (aplicando NP → rice)
3.  ⇒ rice grows (aplicando VP → grows)

De igual forma, para "wheat grows":  
S ⇒ NP VP ⇒ wheat VP ⇒ wheat grows

El lenguaje generado por esta gramática es L(G1) = {rice grows, wheat
grows}.
