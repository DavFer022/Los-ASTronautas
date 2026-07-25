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

**Representación textual del AST:**

