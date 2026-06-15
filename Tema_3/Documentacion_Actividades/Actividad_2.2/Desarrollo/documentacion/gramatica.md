# Gramática Libre de Contexto (GLC) para dibujo basada en el genoma

## 1. Contexto

Caso práctico: se modela una herramienta de dibujo (estilo "turtle
graphics" / Sistemas-L) cuyo alfabeto de entrada coincide con las
cuatro bases del ADN:

```
Sigma = { a, c, g, t }
```

Cada cadena generada por la gramática es interpretada por una
"tortuga gráfica" que se desplaza sobre un plano, y el resultado es
una figura (cuadrado, árbol con ramas, cubo, etc.).

## 2. Tabla de equivalencias símbolo -> acción de dibujo

| Símbolo | Acción de dibujo (semántica)                                   | Equivalente turtle |
|:-------:|------------------------------------------------------------------|:------------------:|
|   `a`   | Avanzar dibujando un segmento de línea unitario                  |        `F`         |
|   `c`   | Girar (sentido horario), sin dibujar                              |        `+`         |
|   `g`   | Abrir rama: guardar posición/orientación actuales en una pila     |        `[`         |
|   `t`   | Cerrar rama: recuperar de la pila la posición/orientación guardadas |      `]`         |

## 3. Definición formal de la gramática G

```
G = (N, Sigma, P, S)
```

- **N** (no terminales):
  `{ S, CUADRADO, LADO, ARBOL, RAMA, HOJA, CUBO, CARA, DIAGONAL }`
- **Sigma** (terminales): `{ a, c, g, t }`
- **S**: símbolo inicial
- **P** (producciones):

```
(1)  S        -> CUADRADO
(2)  CUADRADO -> LADO LADO LADO LADO
(3)  LADO     -> a c

(4)  S        -> ARBOL
(5)  ARBOL    -> a RAMA
(6)  RAMA     -> HOJA
(7)  RAMA     -> g ARBOL t c ARBOL
(8)  RAMA     -> g ARBOL t g ARBOL t c ARBOL
(9)  HOJA     -> a

(10) S        -> CUBO
(11) CUBO     -> CARA g CARA t DIAGONAL
(12) CARA     -> CUADRADO
(13) DIAGONAL -> a a a a
```

## 4. Notas sobre la interpretación gráfica

- El intérprete (ver `src/core.py`) traduce cada cadena terminal en
  una lista de segmentos de línea, aplicando la tabla de equivalencias
  anterior.
- Como Sigma solo tiene 4 símbolos (sin un símbolo dedicado a "girar a
  la izquierda"), el intérprete usa una convención adicional: cada vez
  que aparece `g` se alterna el sentido del giro de apertura de rama
  (`angle_branch` con signo `+` en aperturas impares y `-` en
  aperturas pares). Esto permite que ramas "hermanas" (como en la
  producción 8, `RAMA -> g ARBOL t g ARBOL t c ARBOL`) se distingan
  visualmente como ramas simétricas.
- Los parámetros de dibujo (`step`, `angle_turn`, `angle_branch`) son
  configurables y no forman parte de la gramática formal; son
  parámetros del intérprete que permiten ajustar la apariencia final
  de cada figura.
- La figura del cubo se representa como una visualización conceptual
  simplificada en 2D (dos cuadrados superpuestos con un giro,
  representando la cara frontal y la cara posterior, más las aristas
  de profundidad), no como una proyección 3D exacta.

Ver `documentacion/derivaciones.md` para las 5 derivaciones completas paso a
paso y `ejemplos/` para las cadenas terminales resultantes.
