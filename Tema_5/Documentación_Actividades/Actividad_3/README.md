# Actividad 3: Generadores de Analizadores Sintácticos

## 3.1. Resumen de Generadores

Los generadores de analizadores sintácticos (también llamados metacompiladores) son herramientas que, a partir de una especificación formal de una gramática (generalmente en formato BNF o EBNF), generan automáticamente el código fuente de un *parser* completo. Estas herramientas son fundamentales en el desarrollo de compiladores y procesadores de lenguajes (Parr, 2013).

| Generador | Tipo de Parser | Lenguajes de Salida | Características Destacadas |
|-----------|---------------|---------------------|---------------------------|
| **ANTLR** | LL(*) | Java, Python, C#, Go, C++, JavaScript, Swift | Soporte para múltiples lenguajes destino, genera código legible, tiene entorno de desarrollo integrado (ANTLRWorks) |
| **Bison** | LALR(1) | C, C++, Java | Sucesor de Yacc, estándar en entornos Unix/Linux, altamente eficiente |
| **JavaCC** | LL(k) | Java | Generador específico para Java, soporta *lookahead* arbitrario |
| **Flex + Bison** | LALR(1) | C | Combinación clásica, herramientas maduras y de alto rendimiento |
| **SLY** | LALR(1) | Python | Versión moderna de *lex* y *yacc* para Python, enfoque didáctico y práctico |

## 3.2. Gestión de Errores en Analizadores Sintácticos

La gestión de errores es un componente crítico en el diseño de un analizador sintáctico. Un *parser* efectivo no solo debe detectar errores sintácticos, sino también reportarlos de manera clara y recuperarse para continuar el análisis (Aho et al., 2008).

### 3.2.1. Reporte de Errores

El reporte de errores debe proporcionar información precisa para facilitar la depuración:

1. **Ubicación del Error:** Indicar el número de línea y la columna donde ocurrió el error.

2. **Mensaje Descriptivo:** El mensaje debe ser claro y accionable. Por ejemplo: "Se esperaba ')' o ',' pero se encontró '{' en la línea 5, columna 12".

3. **Contexto del Error:** Proporcionar fragmentos del código fuente alrededor del punto de error.

### 3.2.2. Estrategias de Recuperación de Errores

| Estrategia | Descripción | Ventaja | Desventaja |
|------------|-------------|---------|------------|
| **Modo Pánico** | Descarta *tokens* hasta encontrar un sincronizador (ej: `;`) | Fácil de implementar | Puede omitir código significativo |
| **Inserción de Tokens** | Inserta *tokens* faltantes para corregir el error | Análisis más completo | Puede ocultar errores reales |
| **Recuperación a Nivel de Frase** | Correcciones locales en el punto del error | Más preciso | Más complejo |
| **Producciones de Error** | Producciones especiales para patrones de error comunes | Control fino | Aumenta complejidad de la gramática |

## 3.3. Implementación de Técnicas de Manejo de Errores

### 3.3.1. Reporte de Errores con Ubicación

Se implementó un sistema de reporte de errores que muestra la línea y columna exacta donde ocurre el error, junto con un mensaje descriptivo.

**Código de implementación:**

```python
def reportar_error(self, mensaje, token=None):
    if token is None:
        token = self.token_actual
    if token in self.ubicacion:
        linea, columna = self.ubicacion[token]
    else:
        linea, columna = (1, 1)
    print(f"❌ ERROR [Línea {linea}, Columna {columna}]: {mensaje}")
```
**Resultado de la prueba:**

| Entrada | Salida | Estado |
|---------|--------|--------|
| `id, id id;` | Error en línea 1, columna 9: Se esperaba ',' o ';', se encontró 'id' | ✅ |

### 3.3.2. Modo Pánico (Panic Mode)

**Código de implementación:**

```python
def consumir_hasta_sincronizador(self, sincronizadores=[';']):
    tokens_descartados = []
    while self.token_actual and self.token_actual not in sincronizadores:
        tokens_descartados.append(self.token_actual)
        self.avanzar()
    if self.token_actual in sincronizadores:
        self.avanzar()
        return True
    return False
```
**Resultado de la prueba:**

| Entrada | Salida | Estado |
|---------|--------|--------|
| `id, id, error, error2, ;` | Tokens descartados: `error`, `error2`. Recuperado en `;` | ✅ |

### 3.3.3. Sugerencias de Corrección con Cálculo de Confianza

Se implementó un sistema de sugerencias de corrección basado en la distancia de Levenshtein, que calcula la similitud entre un token incorrecto y las palabras clave del lenguaje.

**Código de implementación:**

```python
import difflib

def sugerir_correccion(self, token):
    mejores = difflib.get_close_matches(token, self.palabras_clave, n=1, cutoff=0.6)
    if mejores:
        sugerencia = mejores[0]
        print(f"💡 Sugerencia: '{token}' → '{sugerencia}'")
        return sugerencia
    return token
```
**Resultados de la prueba:**

| Token Incorrecto | Token Correcto | Ratio de Confianza | Decisión |
|------------------|----------------|-------------------|----------|
| `pront` | `print` | 0.80 | ⚠️ Consultar a LLM |
| `prnt` | `print` | 0.89 | ✅ Corregir automáticamente |
| `whil` | `while` | 0.89 | ✅ Corregir automáticamente |
| `retrn` | `return` | 0.91 | ✅ Corregir automáticamente |
| `elese` | `else` | 0.89 | ✅ Corregir automáticamente |
