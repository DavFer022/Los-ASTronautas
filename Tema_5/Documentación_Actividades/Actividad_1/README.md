# Actividad 1: Árbol de Sintaxis Abstracta (AST)

## 1.1. Definición

Un **Árbol de Sintaxis Abstracta (AST)** es una representación intermedia del código fuente que abstrae los detalles sintácticos para retener únicamente la estructura esencial del programa. A diferencia del árbol de parsing concreto, el AST elimina elementos como paréntesis, punto y coma, y palabras clave que no afectan la semántica del programa (Aho et al., 2008).

El AST es la estructura de datos central que utilizarán las fases posteriores del compilador: análisis semántico, optimización y generación de código. Su diseño facilita el recorrido para el análisis de tipos, la verificación semántica y la generación de código, permitiendo algoritmos eficientes de visitante (visitor pattern).

## 1.2. Características

| Característica | Descripción |
|----------------|-------------|
| **Abstracción Sintáctica** | Omite elementos gramaticales superfluos (paréntesis, separadores) y conserva solo la estructura operacional y lógica del programa |
| **Jerarquía Semántica** | La estructura del árbol refleja la jerarquía de operaciones y constructos del lenguaje. Los nodos internos representan operaciones o estructuras de control, mientras que las hojas representan operandos, literales o identificadores |
| **Facilidad de Procesamiento** | Su diseño simplifica el recorrido para el análisis de tipos, la verificación semántica y la generación de código |
| **Independencia de la Sintaxis** | Dos programas con diferente estilo de codificación pero idéntica semántica producirán AST equivalentes |

# 1.3. Ejemplos de AST

## Ejemplo 1: Expresión Aritmética

| Código Fuente | AST Resultante |
|---------------|----------------|
| `(5 + 3) * 2` | `├─ operador_binario: * (línea 1)` <br> `│  ├─ operador_binario: + (línea 1)` <br> `│  │  ├─ numero: 5 (línea 1)` <br> `│  │  └─ numero: 3 (línea 1)` <br> `│  └─ numero: 2 (línea 1)` |


**Representación textual del AST:**
```
    [*]
   /   \
 [+]   [2]
 / \
[5] [3]
```


**Explicación:** La expresión `(5 + 3) * 2` se representa como un árbol donde la raíz es el operador `*`, el hijo izquierdo es la operación `+` con sus operandos `5` y `3`, y el hijo derecho es el literal `2`. Esta estructura refleja la precedencia de operadores.


## Ejemplo 2: Sentencia Condicional

| Código Fuente | AST Resultante |
|---------------|----------------|
| `if (x > 0) { y = 1; }` | `├─ if (línea 1)` <br> `│  ├─ operador_comparacion: > (línea 1)` <br> `│  │  ├─ variable: x (línea 1)` <br> `│  │  └─ numero: 0 (línea 1)` <br> `│  └─ asignacion: = (línea 1)` <br> `│     ├─ variable: y (línea 1)` <br> `│     └─ numero: 1 (línea 1)` |

**Representación textual del AST:**
```
 [If]
  /    \
[>]   [Assign]
/ \    /    \
[x][0] [y]  [1]
```
Explicación: La sentencia if se representa como un nodo con dos hijos: la condición (x > 0) y el cuerpo de la sentencia (y = 1). La condición es una operación de comparación y el cuerpo es una asignación.

## 1.4. Implementación

La implementación del AST se realizó en Python, utilizando una estructura de nodos que permite representar diferentes tipos de constructos del lenguaje.

### Código de la implementación:

```python
class NodoAST:
    """
    Clase que representa un nodo del Árbol de Sintaxis Abstracta.
    """

    def __init__(self, tipo, valor=None, hijos=None, linea=0, columna=0):
        self.tipo = tipo  # 'operador', 'numero', 'variable', 'asignacion', 'if', etc.
        self.valor = valor  # '+', 5, 'x', etc.
        self.hijos = hijos if hijos is not None else []
        self.linea = linea  # Para reporte de errores
        self.columna = columna  # Para reporte de errores

    def __str__(self, nivel=0):
        indent = " " * nivel
        resultado = f"{indent}├─ {self.tipo}"
        if self.valor is not None:
            resultado += f": {self.valor}"
        if self.linea > 0:
            resultado += f" (línea {self.linea})"
        resultado += "\n"
        for hijo in self.hijos:
            resultado += hijo.__str__(nivel + 1)
        return resultado
```
### Resultados de la ejecución:

| Ejemplo | Código Fuente | Estado | Observación |
|---------|---------------|--------|-------------|
| 1 | `(5 + 3) * 2` | Correcto | AST generado con operador `*` como raíz |
| 2 | `if (x > 0) { y = 1; }` | Correcto | AST generado con nodo `if` y sus hijos |
| 3 | `while (i < 10) { i = i + 1; }` | Correcto | AST generado con nodo `while` y sus hijos |
