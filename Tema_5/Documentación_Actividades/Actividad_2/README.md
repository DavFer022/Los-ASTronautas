# Actividad 2: Comparación entre Análisis LL y LR

## 2.1. Definición y Características Generales

El análisis sintáctico se puede realizar mediante dos estrategias fundamentales: descendente (LL) y ascendente (LR). Ambas estrategias determinan si una cadena de tokens pertenece al lenguaje definido por una gramática libre de contexto, pero lo hacen desde perspectivas opuestas (Hopcroft, Motwani & Ullman, 2007).

**Análisis LL (Left-to-right, Leftmost derivation):** Es un análisis descendente que comienza desde el símbolo inicial y aplica derivaciones por la izquierda. Es más sencillo de implementar manualmente mediante recursión descendente.

**Análisis LR (Left-to-right, Rightmost derivation):** Es un análisis ascendente que comienza desde los tokens y aplica reducciones construyendo la derivación por la derecha en reversa. Maneja gramáticas más complejas.

## 2.2. Tabla Comparativa LL vs LR

| Criterio | Análisis LL (Descendente) | Análisis LR (Ascendente) |
|----------|---------------------------|--------------------------|
| **Estrategia de Construcción** | Top-Down: Parte del símbolo inicial y expande los no terminales | Bottom-Up: Parte de los tokens y los reduce a no terminales |
| **Tipo de Derivación** | Por la Izquierda (Leftmost) | Por la Derecha (Rightmost) en reversa |
| **Potencia Expresiva** | Menos Potente: Limitaciones con recursión izquierda | Más Potente: Maneja gramáticas más complejas |
| **Complejidad de Implementación** | Más Sencilla: Recursión descendente manual | Más Compleja: Tablas de análisis automáticas |
| **Mecanismo de Decisión** | Predictivo: Basado en conjuntos FIRST y FOLLOW | Reducción basada en contexto y pila de análisis |
| **Manejo de Errores** | Más Sencillo de Localizar | Más Complejo de Localizar |

## 2.3. Evidencia de Uso Actual

| Estrategia | Herramientas Representativas | Aplicaciones Típicas |
|------------|------------------------------|----------------------|
| **LL** | ANTLR, JavaCC, parsers recursivos descendentes | Lenguajes de dominio específico (DSL), herramientas de análisis en IDEs |
| **LR** | Bison, Yacc, SLY, Menhir | Compiladores de lenguajes de propósito general (C, C++, Java, Python) |

## 2.4. Implementación para el Lenguaje L

Se definió un lenguaje L simple que consiste en listas de identificadores separados por comas y terminados en punto y coma. Ejemplo válido: `a, b, c;`.

### Gramática LL(1):
lista_ids -> id cola_lista_ids
cola_lista_ids -> , id cola_lista_ids
cola_lista_ids -> ;


### Gramática LR:

Para el análisis ascendente (LR), se definió la siguiente gramática para el lenguaje L:
lista_ids -> ids PUNTO_Y_COMA
ids -> ids COMA ID
ids -> ID

**Donde:**
- `lista_ids` es el símbolo inicial
- `ids` representa una lista de identificadores
- `PUNTO_Y_COMA` es el terminal `;`
- `COMA` es el terminal `,`
- `ID` es un identificador

## 2.5. Resultados de la Implementación

### 2.5.1. Resultados del Parser LL

| Prueba | Entrada | Resultado Esperado | Resultado Obtenido | Estado |
|--------|---------|-------------------|-------------------|--------|
| 1 | `id, id;` | VÁLIDO | VÁLIDO | ✅ |
| 2 | `id, id, id;` | VÁLIDO | VÁLIDO | ✅ |
| 3 | `id;` | VÁLIDO | VÁLIDO | ✅ |
| 4 | `id, id, id, id;` | VÁLIDO | VÁLIDO | ✅ |
| 5 | `id, ;` | INVÁLIDO | INVÁLIDO | ✅ |
| 6 | `id, id` | INVÁLIDO | INVÁLIDO | ✅ |
| 7 | `, id;` | INVÁLIDO | INVÁLIDO | ✅ |
| 8 | `id id;` | INVÁLIDO | INVÁLIDO | ✅ |
| 9 | `id, id, ;` | INVÁLIDO | INVÁLIDO | ✅ |

**Tasa de éxito: 100% (9/9 pruebas)**

### 2.5.2. Resultados del Parser LR

| Prueba | Entrada | Resultado Esperado | Resultado Obtenido | Estado |
|--------|---------|-------------------|-------------------|--------|
| 1 | `a, b, c;` | VÁLIDO | VÁLIDO | ✅ |
| 2 | `x, y, z, w;` | VÁLIDO | VÁLIDO | ✅ |
| 3 | `id1;` | VÁLIDO | VÁLIDO | ✅ |
| 4 | `a, b;` | VÁLIDO | VÁLIDO | ✅ |
| 5 | `a, b, c, d, e;` | VÁLIDO | VÁLIDO | ✅ |
| 6 | `a, , b;` | INVÁLIDO | INVÁLIDO | ✅ |
| 7 | `a, b, ;` | INVÁLIDO | INVÁLIDO | ✅ |
| 8 | `a b c;` | INVÁLIDO | INVÁLIDO | ✅ |
| 9 | `;` | INVÁLIDO | INVÁLIDO | ✅ |
| 10 | `a, b, c` | INVÁLIDO | INVÁLIDO | ✅ |

**Tasa de éxito: 100% (10/10 pruebas)**

### 2.5.3. Comparativa de Resultados

| Parser | Pruebas Realizadas | Pruebas Exitosas | Tasa de Éxito |
|--------|-------------------|------------------|---------------|
| Parser LL (Recursivo Descendente) | 9 | 9 | **100%** |
| Parser LR | 10 | 10 | **100%** |
