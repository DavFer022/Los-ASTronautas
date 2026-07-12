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



