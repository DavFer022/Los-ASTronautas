# GLC para dibujo basada en el genoma (Sigma = {a, c, g, t})

Proyecto de investigación: **Derivación y Modelado** de una **Gramática
Libre de Contexto (GLC)** que modela una herramienta de dibujo
("turtle graphics" / Sistemas-L), usando como alfabeto las cuatro
bases del ADN:

```
Sigma = { a, c, g, t }
```

Cada cadena generada por la gramática se interpreta como una secuencia
de instrucciones para una "tortuga gráfica":

| Símbolo | Acción de dibujo                                   | Equivalente turtle |
|:-------:|------------------------------------------------------|:------------------:|
|   `a`   | Avanzar dibujando un segmento                         |        `F`         |
|   `c`   | Girar (sentido horario)                               |        `+`         |
|   `g`   | Abrir rama (guardar posición/orientación en una pila) |        `[`         |
|   `t`   | Cerrar rama (recuperar posición/orientación)          |        `]`         |

## Contenido del repositorio

```
.
├── docs/
│   ├── gramatica.md      # Definicion formal G = (N, Sigma, P, S)
│   └── derivaciones.md   # 5 derivaciones paso a paso + interpretacion
├── src/
│   ├── core.py            # Logica de interpretacion (independiente de UI)
│   ├── interprete.py       # Intérprete interactivo con turtle (GUI)
│   └── generar_imagenes.py # Genera previsualizaciones PNG con matplotlib
├── examples/               # Cadenas terminales de las 5 derivaciones
│   ├── cuadrado.txt
│   ├── arbol_simple.txt
│   ├── arbol_ramificado.txt
│   ├── arbol_simetrico.txt
│   └── cubo.txt
├── images/                 # Previsualizaciones generadas (PNG)
└── requirements.txt
```

## Las 5 figuras (casos de derivación)

| Figura | Cadena | Documento |
|---|---|---|
| Cuadrado | `acacacac` | `docs/derivaciones.md` (Derivación 1) |
| Árbol con una rama y hojas | `agaatcaa` | Derivación 2 |
| Árbol con ramificación anidada | `agagaatcaatcaa` | Derivación 3 |
| Árbol con doble ramificación simétrica | `agaatgaatcaa` | Derivación 4 |
| Cubo (rep. 2D simplificada) | `acacacacgacacacactaaaa` | Derivación 5 |

## Cómo ejecutarlo

### 1. Generar previsualizaciones (sin interfaz gráfica)

```bash
pip install -r requirements.txt
cd src
python3 generar_imagenes.py
```

Esto crea/actualiza los archivos PNG en `images/` para las 5 figuras.

### 2. Intérprete interactivo (con interfaz gráfica, usa `turtle`)

```bash
cd src
python3 interprete.py
```

Muestra un menú para elegir una de las 5 figuras o introducir una
cadena propia formada solo por `{a, c, g, t}`.

### 3. Usar la lógica de interpretación en otro programa

```python
from core import generar_segmentos

segmentos = generar_segmentos(
    "acacacac",
    step=60, angle_turn=90, angle_branch=0
)
# segmentos: lista de tuplas (x1, y1, x2, y2)
```

## Fundamento teórico

Este proyecto aplica conceptos de **Teoría de Lenguajes Formales y
Autómatas / Compiladores**:

- Definición formal de una Gramática Libre de Contexto `G = (N, Sigma, P, S)`.
- Derivaciones paso a paso (aplicación sucesiva de producciones).
- Traducción de cadenas terminales a acciones gráficas, en la línea de
  los **Sistemas-L (L-Systems)** usados para modelar estructuras
  ramificadas (plantas, fractales), aquí aplicados sobre el alfabeto
  del genoma como caso práctico de bioinformática.

Ver `docs/gramatica.md` para la definición formal completa y
`docs/derivaciones.md` para las 5 derivaciones detalladas.
