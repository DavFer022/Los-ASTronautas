# Derivaciones de la GLC (5 ejemplos)

Gramática de referencia: `documentacion/gramatica.md`.
Notación: `S ⇒(n) ...` indica que se aplicó la producción `(n)`.

---

## Derivación 1 — Cuadrado

```
S ⇒(1) CUADRADO
  ⇒(2) LADO LADO LADO LADO
  ⇒(3) a c LADO LADO LADO
  ⇒(3) a c a c LADO LADO
  ⇒(3) a c a c a c LADO
  ⇒(3) a c a c a c a c
```

**Cadena final:** `acacacac`

**Interpretación:** el patrón `ac` se repite 4 veces. Cada `a` traza un
lado de longitud unitaria y cada `c` gira 90°. Como 4 × 90° = 360°, el
trazo regresa al punto y orientación iniciales, cerrando un cuadrado.

Archivo asociado: `ejemplos/cuadrado.txt`
Imagen: `imageness/cuadrado.png`

---

## Derivación 2 — Árbol con una rama lateral y hojas

```
S ⇒(4) ARBOL
  ⇒(5) a RAMA
  ⇒(7) a g ARBOL t c ARBOL
  ⇒(5) a g a RAMA t c ARBOL
  ⇒(6) a g a HOJA t c ARBOL
  ⇒(9) a g a a t c ARBOL
  ⇒(5) a g a a t c a RAMA
  ⇒(6) a g a a t c a HOJA
  ⇒(9) a g a a t c a a
```

**Cadena final:** `agaatcaa`

**Interpretación:** `a` dibuja el tronco; `g` abre una rama lateral,
que se dibuja y termina en una hoja (`aa`); `t` cierra la rama y
regresa al tronco; `c` gira para retomar la dirección del tronco, que
continúa y finaliza también en una hoja (`aa`). Resultado: árbol con
una rama y dos hojas.

Archivo asociado: `ejemplos/arbol_simple.txt`
Imagen: `imagenes/arbol_simple.png`

---

## Derivación 3 — Árbol con ramificación anidada (varias ramas)

```
S ⇒(4) ARBOL
  ⇒(5) a RAMA
  ⇒(7) a g ARBOL t c ARBOL
  ⇒(5) a g a RAMA t c ARBOL
  ⇒(7) a g a g ARBOL t c ARBOL t c ARBOL
  ⇒(5) a g a g a RAMA t c ARBOL t c ARBOL
  ⇒(6) a g a g a HOJA t c ARBOL t c ARBOL
  ⇒(9) a g a g a a t c ARBOL t c ARBOL
  ⇒(5) a g a g a a t c a RAMA t c ARBOL
  ⇒(6) a g a g a a t c a HOJA t c ARBOL
  ⇒(9) a g a g a a t c a a t c ARBOL
  ⇒(5) a g a g a a t c a a t c a RAMA
  ⇒(6) a g a g a a t c a a t c a HOJA
  ⇒(9) a g a g a a t c a a t c a a
```

**Cadena final:** `agagaatcaatcaa`

**Interpretación:** el tronco se ramifica (`g`) en una rama que vuelve
a ramificarse internamente (segunda `g`) antes de terminar en una
hoja; al cerrar esa subrama, la rama original continúa hasta su propia
hoja; al cerrar la rama principal, el tronco original termina en su
propia hoja. Resultado: árbol con tres niveles de ramificación y tres
hojas, análogo a la recursividad de un Sistema-L.

Archivo asociado: `ejemplos/arbol_ramificado.txt`
Imagen: `imagenes/arbol_ramificado.png`

---

## Derivación 4 — Árbol con doble ramificación simétrica

```
S ⇒(4) ARBOL
  ⇒(5) a RAMA
  ⇒(8) a g ARBOL t g ARBOL t c ARBOL
  ⇒(5) a g a RAMA t g ARBOL t c ARBOL
  ⇒(6) a g a HOJA t g ARBOL t c ARBOL
  ⇒(9) a g a a t g ARBOL t c ARBOL
  ⇒(5) a g a a t g a RAMA t c ARBOL
  ⇒(6) a g a a t g a HOJA t c ARBOL
  ⇒(9) a g a a t g a a t c ARBOL
  ⇒(5) a g a a t g a a t c a RAMA
  ⇒(6) a g a a t g a a t c a HOJA
  ⇒(9) a g a a t g a a t c a a
```

**Cadena final:** `agaatgaatcaa`

**Interpretación:** el tronco genera una primera rama lateral
(`g...aa...t`) con hoja; vuelve al punto del tronco y genera una
segunda rama lateral simétrica (`g...aa...t`) con hoja; finalmente `c`
retoma la dirección del tronco, que concluye en su propia hoja.
Resultado: árbol con dos ramas simétricas y tres hojas en total.

Archivo asociado: `ejemplos/arbol_simetrico.txt`
Imagen: `imagenes/arbol_simetrico.png`

---

## Derivación 5 — Cubo (representación 2D simplificada)

```
S  ⇒(10) CUBO
   ⇒(11) CARA g CARA t DIAGONAL
   ⇒(12) CUADRADO g CARA t DIAGONAL
   ⇒(2)  LADO LADO LADO LADO g CARA t DIAGONAL
   ⇒(3×4) a c a c a c a c g CARA t DIAGONAL
   ⇒(12) a c a c a c a c g CUADRADO t DIAGONAL
   ⇒(2)  a c a c a c a c g LADO LADO LADO LADO t DIAGONAL
   ⇒(3×4) a c a c a c a c g a c a c a c a c t DIAGONAL
   ⇒(13) a c a c a c a c g a c a c a c a c t a a a a
```

**Cadena final:** `acacacacgacacacactaaaa`

**Interpretación:** primero se dibuja un cuadrado completo
(`acacacac`) que representa la cara frontal del cubo; `g` desplaza el
punto de referencia (cambiando la orientación) sin perder la posición
original; allí se dibuja un segundo cuadrado idéntico (`acacacac`),
correspondiente a la cara posterior; `t` recupera el punto de
referencia de la cara frontal; y los cuatro símbolos `a` finales
(`aaaa`) representan las aristas de profundidad que conectan ambas
caras. La figura resultante es una representación conceptual en 2D del
cubo (dos caras superpuestas con un giro + aristas de profundidad), no
una proyección 3D exacta.

Archivo asociado: `ejemplos/cubo.txt`
Imagen: `imagenes/cubo.png`
