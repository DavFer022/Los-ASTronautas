# Actividad 1 - Defina y presente ejemplos de autónoma de pilas.

**Responsable:** Mariangel Antoima

En el Informe indicar lo antes descrito, incorporar un conclusión de las utilidades del autómata de pila, aborde su importancia relacionado a su poder con relación a los AFD y AFND.

---

## 1.1. Definición Formal de Autómata de Pila (AP)

Un **Autómata de Pila** (también conocido como **Pushdown Automaton - PDA**) es un modelo matemático de computación que extiende el Autómata Finito No Determinístico (AFND) añadiéndole una **pila** como memoria auxiliar de tipo LIFO (Last-In, First-Out).

Formalmente, un Autómata de Pila se define como una **7-tupla**:

**P = (Q, Σ, Γ, δ, q₀, Z₀, F)**

Donde cada componente tiene el siguiente significado:

| Símbolo | Nombre | Descripción |
|---------|--------|-------------|
| **Q** | Conjunto finito de estados | Representa todos los posibles estados en los que puede estar el autómata durante su ejecución. |
| **Σ** | Alfabeto de entrada | Conjunto finito de símbolos que pueden ser leídos de la cinta de entrada. |
| **Γ** | Alfabeto de pila | Conjunto finito de símbolos que pueden ser almacenados en la pila. |
| **δ** | Función de transición | **δ: Q × (Σ ∪ {ε}) × Γ → P(Q × Γ\*)** <br> Es el corazón del autómata. Toma el estado actual, un símbolo de entrada (o ε = transición épsilon sin consumir entrada) y el símbolo en la cima de la pila, y devuelve un conjunto de posibles nuevos estados y una cadena de símbolos que reemplazarán a la cima de la pila. |
| **q₀ ∈ Q** | Estado inicial | El estado en el que el autómata comienza su ejecución. |
| **Z₀ ∈ Γ** | Símbolo inicial de pila | El símbolo que se encuentra en el fondo de la pila al inicio. Marca el "fondo" de la pila. |
| **F ⊆ Q** | Conjunto de estados finales o de aceptación | Estados en los que, al terminar de leer la entrada y vaciar (o no) la pila, el autómata acepta la cadena. |

### Interpretación de la Función de Transición

La función de transición se interpreta de la siguiente manera:
δ(q, a, X) = {(p₁, γ₁), (p₂, γ₂), ..., (pₙ, γₙ)}


**Significado:** Si el autómata está en el estado `q`, lee el símbolo `a` de la entrada, y el símbolo en la cima de la pila es `X`, entonces puede:

- Cambiar al estado `pᵢ`.
- Reemplazar el símbolo `X` en la cima de la pila por la cadena `γᵢ`.

**Casos especiales:**
- Si `γ = ε`, se **desapila** el símbolo `X`.
- Si `γ = X`, la pila no cambia.
- Si `γ = YX`, se apila `Y` y luego `X`, quedando `Y` en la cima.


## 1.2. Ejemplos de Autómatas de Pila

### 1.2.1. Ejemplo 1: Lenguaje de Paréntesis Balanceados (aⁿbⁿ)

#### Descripción del Lenguaje

El lenguaje **L₁ = { aⁿ bⁿ | n ≥ 1 }** consiste en cadenas con un número igual de 'a's y 'b's, donde todas las 'a's preceden a todas las 'b's.

**Ejemplos de cadenas válidas:** `ab`, `aabb`, `aaabbb`

**Ejemplos de cadenas inválidas:** `a`, `abb`, `aab`, `aba`

#### Definición Formal del AP

Definimos un Autómata de Pila `P₁ = (Q, Σ, Γ, δ, q₀, Z₀, F)`:

| Componente | Valor |
|------------|-------|
| **Q** | {q₀, q₁, q₂, qₐ} |
| **Σ** | {a, b} |
| **Γ** | {A, Z₀} |
| **q₀** | q₀ |
| **Z₀** | Z₀ |
| **F** | {qₐ} |

#### Función de Transición (δ)

| Transición | Interpretación |
|------------|----------------|
| `δ(q₀, a, Z₀) = {(q₁, A Z₀)}` | Lee la primera 'a', apila 'A' sobre el fondo Z₀, pasa a q₁. |
| `δ(q₁, a, A) = {(q₁, A A)}` | Lee 'a' adicional, apila otra 'A'. |
| `δ(q₁, b, A) = {(q₁, ε)}` | Lee una 'b', desapila una 'A'. |
| `δ(q₁, ε, Z₀) = {(q₂, Z₀)}` | Cuando no hay más entrada y solo queda el fondo, pasa a q₂. |
| `δ(q₂, ε, Z₀) = {(qₐ, Z₀)}` | Transición final al estado de aceptación. |

#### Representación Gráfica

      a, Z₀ → AZ₀        a, A → AA         b, A → ε          ε, Z₀ → Z₀
   ┌──────────────┐   ┌────────────┐   ┌────────────┐   ┌────────────┐
   │              ▼   │            ▼   │            ▼   │            ▼
 ┌─┴─┐           ┌─┴─┐         ┌─┴─┐         ┌─┴─┐         ┌─────┐
 │q₀│───────────▶│q₁│─────────▶│q₁│─────────▶│q₁│─────────▶│ q₂  │───▶ qₐ
 └─┬─┘           └─┬─┘         └───┘         └───┘         └──┬──┘    (aceptación)
   │               │                                             │
   └───────────────┴─────────────────────────────────────────────┘
                     ε, Z₀ → Z₀


#### Simulación de la Cadena "aaabbb"

| Paso | Estado | Entrada Restante | Pila (cima → fondo) | Transición Aplicada |
|------|--------|------------------|---------------------|---------------------|
| 1 | q₀ | aaabbb | Z₀ | δ(q₀, a, Z₀) = (q₁, A Z₀) |
| 2 | q₁ | aabbb | A Z₀ | δ(q₁, a, A) = (q₁, A A) |
| 3 | q₁ | abbb | A A Z₀ | δ(q₁, a, A) = (q₁, A A A) |
| 4 | q₁ | bbb | A A A Z₀ | δ(q₁, b, A) = (q₁, A A Z₀) |
| 5 | q₁ | bb | A A Z₀ | δ(q₁, b, A) = (q₁, A Z₀) |
| 6 | q₁ | b | A Z₀ | δ(q₁, b, A) = (q₁, Z₀) |
| 7 | q₁ | ε | Z₀ | δ(q₁, ε, Z₀) = (q₂, Z₀) |
| 8 | q₂ | ε | Z₀ | δ(q₂, ε, Z₀) = (qₐ, Z₀) |

**Resultado: ¡Cadena ACEPTADA!**

### 1.2.2. Ejemplo 2: Palíndromos de Longitud Par (wwᴿ)

#### Descripción del Lenguaje

El lenguaje **L₂ = { w wᴿ | w ∈ {0,1}* }** consiste en cadenas que son palíndromos de longitud par (una cadena seguida de su reverso).

**Ejemplos de cadenas válidas:** `00`, `11`, `0110`, `101101`, `001100`

**Ejemplos de cadenas inválidas:** `01`, `10`, `010`, `1100`

#### Idea del Funcionamiento

1. El autómata lee la primera mitad de la cadena y **apila** cada símbolo.
2. En el punto medio (que se determina de forma no determinística), cambia de estado.
3. Lee la segunda mitad y **desapila** un símbolo por cada símbolo leído, verificando que coincidan.
4. Si al final la pila está vacía y se ha consumido toda la entrada, la cadena es aceptada.

#### Definición del AP

`P₂ = (Q, Σ, Γ, δ, q₀, Z₀, F)`

| Componente | Valor |
|------------|-------|
| **Q** | {q₀, q₁, qₐ} |
| **Σ** | {0, 1} |
| **Γ** | {0, 1, Z₀} |
| **q₀** | q₀ |
| **Z₀** | Z₀ |
| **F** | {qₐ} |

#### Transiciones

- **Fase de apilado (q₀):**
  - `δ(q₀, 0, Z₀) = {(q₀, 0 Z₀)}` y `δ(q₀, 0, 0) = {(q₀, 0 0)}`, `δ(q₀, 0, 1) = {(q₀, 0 1)}`
  - `δ(q₀, 1, Z₀) = {(q₀, 1 Z₀)}` y `δ(q₀, 1, 0) = {(q₀, 1 0)}`, `δ(q₀, 1, 1) = {(q₀, 1 1)}`

- **Cambio de fase (no determinístico):**
  - `δ(q₀, ε, 0) = {(q₁, 0)}` y `δ(q₀, ε, 1) = {(q₁, 1)}` (supone que ya estamos en la segunda mitad)

- **Fase de desapilado y verificación (q₁):**
  - `δ(q₁, 0, 0) = {(q₁, ε)}` (si lee 0 y la cima es 0, desapila)
  - `δ(q₁, 1, 1) = {(q₁, ε)}` (si lee 1 y la cima es 1, desapila)

- **Aceptación:**
  - `δ(q₁, ε, Z₀) = {(qₐ, Z₀)}`

#### Simulación de "0110"

| Paso | Estado | Entrada | Pila | Acción |
|------|--------|---------|------|--------|
| 1 | q₀ | 0110 | Z₀ | Lee 0, apila 0 → Pila: 0 Z₀ |
| 2 | q₀ | 110 | 0 Z₀ | Lee 1, apila 1 → Pila: 1 0 Z₀ |
| 3 | q₀ | 10 | 1 0 Z₀ | **Transición ε**: asume que ya está en la segunda mitad |
| 4 | q₁ | 10 | 1 0 Z₀ | Lee 1, coincide con cima (1), desapila → Pila: 0 Z₀ |
| 5 | q₁ | 0 | 0 Z₀ | Lee 0, coincide con cima (0), desapila → Pila: Z₀ |
| 6 | q₁ | ε | Z₀ | Transición ε: pasa a qₐ |

**Resultado: ¡Cadena ACEPTADA!**

### 1.2.3. Ejemplo 3: Expresiones Aritméticas con Paréntesis Anidados

#### Descripción

Consideremos el lenguaje de expresiones aritméticas simples con paréntesis balanceados.

**L₃ = { cadenas con paréntesis '(' y ')' correctamente balanceados }**

Este es un problema práctico que cualquier compilador debe resolver.

#### AP Simplificado para Paréntesis Balanceados

| Componente | Valor |
|------------|-------|
| **Q** | {q₀, qₐ} |
| **Σ** | {(, )} |
| **Γ** | {(, Z₀} |
| **q₀** | q₀ |
| **Z₀** | Z₀ |
| **F** | {qₐ} |

#### Transiciones

- `δ(q₀, (, Z₀) = {(q₀, ( Z₀)}` → Abre paréntesis, lo apila
- `δ(q₀, (, () = {(q₀, ( ()}` → Abre paréntesis anidado, apila otro
- `δ(q₀, ), () = {(q₀, ε)}` → Cierra paréntesis, desapila uno
- `δ(q₀, ε, Z₀) = {(qₐ, Z₀)}` → Si la pila solo tiene el fondo, acepta

#### Simulación de "(()())"

1. Lee '(' → apila '('
2. Lee '(' → apila '('
3. Lee ')' → desapila '('
4. Lee '(' → apila '('
5. Lee ')' → desapila '('
6. Lee ')' → desapila '(' (solo queda Z₀)
7. Fin de entrada, transición ε → acepta

## 1.3. Relación con AFD y AFND: Poder Computacional

Es fundamental comprender por qué el Autómata de Pila es más poderoso que los Autómatas Finitos.

| Característica | AFD / AFND | Autómata de Pila (AP) |
|----------------|------------|----------------------|
| **Memoria** | Finita (estados) | Ilimitada (pila) |
| **Tipo de Memoria** | Sin memoria adicional | Pila LIFO |
| **Lenguajes Reconocidos** | Lenguajes Regulares (Tipo 3) | Lenguajes Libres de Contexto (Tipo 2) |
| **Capacidad de Contar** | No puede contar más allá de un número fijo | Puede contar con la pila (ej: aⁿbⁿ) |
| **Estructuras Anidadas** | No puede reconocer anidamiento profundo | Puede reconocer anidamiento arbitrario |
| **Ejemplo Clásico** | Reconocer tokens (identificadores, números) | Reconocer expresiones con paréntesis balanceados |
| **Complejidad** | Lineal (O(n)) | Lineal (O(n)) |

### ¿Por qué AFD no puede reconocer aⁿbⁿ?

Un Autómata Finito tiene un número fijo de estados. Para reconocer aⁿbⁿ, necesitaría un estado para cada posible valor de 'n'. Como 'n' puede ser arbitrariamente grande, necesitaría infinitos estados, lo cual no está permitido en un AFD. El Autómata de Pila, en cambio, utiliza la pila para "contar" las 'a's y luego verificar que haya el mismo número de 'b's.

### El Autómata de Pila en la Jerarquía de Chomsky

La Jerarquía de Chomsky clasifica los lenguajes formales en cuatro niveles:
Lenguajes Recursivamente Enumerables (Máquinas de Turing) - Tipo 0
                    ↑
Lenguajes Sensibles al Contexto (Autómatas Linealmente Acotados) - Tipo 1
                    ↑
Lenguajes Libres de Contexto (Autómatas de Pila) - Tipo 2    ← ¡Aquí estamos!
                    ↑
Lenguajes Regulares (Autómatas Finitos) - Tipo 3

El Autómata de Pila es el modelo teórico que reconoce exactamente los Lenguajes Libres de Contexto, que son la base de la mayoría de los lenguajes de programación modernos.
