# Fase 1: Diseño del Alfabeto y Reglas Léxicas (Morfología)

A continuación se detallan los caracteres aceptados por el lenguaje, así como sus delimitadores y reglas para crear identificadores.
## 1. Especificación Léxica 
El analizador léxico procesa la entrada basándose en las siguientes reglas estructurales:
 * **Caracteres Válidos:** Letras mayúsculas y minúsculas *A-Z, a-z*, dígitos *0-9*, para números decimales se usa el punto (`.`), el guion bajo (`_`) se usa para concatenar palabras.
 * **Identificadores (Variables locales):** Deben iniciar con letra minúscula. Pueden incluir números (excepto al inicio) y guiones bajos para la separación de palabras (Snake_Case).
	   - **Ejemplos válidos:** temp_actual, lectura_2, bateria_full.
 * **Delimitadores de Parámetros:** Paréntesis `()`  para agrupar y comas (`,`)  para separar argumentos.
 * **Terminador de Sentencia:** Todas instrucciones deben finalizar estrictamente con punto y coma (`;`), haciendo de este lenguaje uno de tipado fuerte.
 * **Espacios/Tabulaciones:** Ignorados semánticamente; se usan solo para legibilidad.
## 2. Tipos de Datos y Literales Aceptados
Valores duros que el lenguaje entiende de forma nativa:

| **Tipo**  | **Literales Aceptados**                                                     | **Descripcion**                                                                                                                                                                                                                                                                                                                                                                                                                                |
| :-------: | --------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Numéricos | Enteros`` (90, 55)`` y Flotantes ``(14.5)``                                 | Usados para cálculos o para representar valores                                                                                                                                                                                                                                                                                                                                                                                                |
| Booleanos | - ENCENDIDO<br><br>- APAGADO<br><br>- RESPALDO_COMERCIAL<br><br>- MICRO_RED | - Circuito normalmente cerrado permitiendo el flujo de energía hacia el sector o dispositivo.<br>- Circuito normalmente abierto cortando el flujo de energía de manera absoluta.<br>- Desconecta el sector de la red interna y lo conecta directamente a la red eléctrica pública<br>- Aísla un sector de las dependencias externas configurándolo para que se alimente de los activos de almacenamiento y generación propios de la planta<br> |

| **Constantes globales** | **Tipo de Dato** | **Descripción**               |
| ------------------- | ------------ | ------------------------- |
| TERMICO             | Flotante     | Mide la temperatura en °C |
| FLUJO_OUT           | Flotante     | Carga consumida (kW)      |
| FLUJO_IN            | Flotante     | Entrada de red (kW)       |
| CARGA_BAT           | Entero       | Capacidad batería (%)     |

 * **Cadenas de Texto (Strings):** Únicamente permitidas dentro del comando de alertas (``notificar_alarma()``), delimitadas por comillas dobles "Mensaje".
 * **Identificadores de Hardware (Constantes):** Nombres globales en mayúsculas que referencian equipos físicos. Ej: BAT_01, PANEL_SUR, RELE_PRINCIPAL.

## 3. Operadores

|            Operador            | Descripción                                                                                     |
| :----------------------------: | ----------------------------------------------------------------------------------------------- |
|               =                | Asignación: Guarda el resultado de una lectura en una variable                                  |
| ><br><<br>>=<br><=<br>==<br>!= | - Mayor que<br>- Menos que<br>- Mayor o igual<br>- Menor o igual<br>- Igual a<br>- Diferente de |
|          Y<br>O<br>NO          | - And<br>- OR<br>- NOT                                                                          |


## 4. Diccionario de Palabras Clave y Comandos (Lenguaje L)
Al ser un sistema critico, el analizador léxico del Lenguaje L procesará un conjunto restringido de palabras clave estructuradas de forma compacta, minimizando la ambigüedad y permitiendo un mapeo directo hacia los drivers de bajo nivel de la planta.

|      **Categoría**      | **Palabra Clave / Sintaxis**       | **Descripción Técnica**                                                                                                                                                             | **Ejemplo de Uso en el Script**                                 |
| :---------------------: | ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
|   **Inicialización**    | `init_grid;`                       | Inicializa los drivers de comunicación HMI y establece enlace con los sensores y actuadores físicos de la planta.                                                                   | `init_grid;`                                                    |
| **Monitoreo (Lectura)** | `leer_dispositivo(TIPO, id);`      | Consulta el estado de un hardware específico y retorna un valor numérico. Los tipos válidos son: `TERMICO` (°C), `FLUJO_IN` (kW), `FLUJO_OUT` (kW) y `CARGA_BAT` (%).               | `temp_bateria = leer_dispositivo(TERMICO, BAT_01);`             |
|  **Control (Acción)**   | `conmutar_linea(id, ESTADO);`      | Envía una señal eléctrica para cambiar físicamente la posición de un relé o switch de transferencia. Estados permitidos: `ENCENDIDO`, `APAGADO`, `RESPALDO_COMERCIAL`, `MICRO_RED`. | `conmutar_linea(LINEA_INDUSTRIAL, RESPALDO_COMERCIAL);`         |
|  **Control de Flujo**   | `if` / `then` / `else` / `end_if;` | Estructura condicional compacta para la toma de decisiones lógicas basadas en los umbrales de los sensores.                                                                         | `if carga < 20 then conmutar_linea(SECTOR_B, APAGADO); end_if;` |
|      **Iteración**      | `while` / `do` / `end_while;`      | Bucle iterativo que repite un bloque de instrucciones continuamente mientras la condición lógica sea verdadera.                                                                     | `while estado_alarma < 3 do ... end_while;`                     |
|      **Seguridad**      | `notificar_alarma("Msg");`         | Envía de forma persistente un hilo de texto a la consola de la HMI e incrementa de forma automática en **+1** el contador global `estado_alarma`.                                   | `notificar_alarma("Fuga termica detectada en celda 1");`        |
|      **Seguridad**      | `estado_alarma`                    | Palabra reservada del sistema que expone de solo lectura el número de alarmas acumuladas en el ciclo de ejecución actual.                                                           | `if estado_alarma >= 3 then parada_emergencia(); end_if;`       |
|      **Seguridad**      | `parada_emergencia();`             | Detiene inmediatamente la ejecución de cualquier script operativo y activa un protocolo de aislamiento de hardware seguro en toda la microred.                                      | `parada_emergencia();`                                          |
