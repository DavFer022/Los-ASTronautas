# Actividad III - Diseño del DSL Lenguaje L (ECO-GRID)

## Responsable: García Carlos



Diseño de un Lenguaje de Dominio Específico (DSL) para Sistemas logico - físicos Críticos con la finalidad de consolidar la visión de los lenguajes de programación como productos arquitectónicos construidos para fines delimitados, los estudiantes asumirán el rol de diseñadores de lenguajes. Deben plantear un problema de Interfaz Hombre-Máquina (HMI) en un entorno industrializado complejo y proponer la especificación de un lenguaje de programación de alto nivel, denominado formalmente Lenguaje L. Para esta asignación, el dominio de aplicación obligatorio propuesto es un Sistema de Gestión de Microredes Eléctricas Inteligentes y Almacenamiento de Energía (denominado ECO-GRID). F: Un ejercicio creativo para medir su nivel de abstracción en el diseño de un entorno físico con su respectiva comunicación o interfase hombre maquina (lenguaje), su imaginación es el limite!



El sistema físico simulado cuenta con los siguientes componentes integrados controlables mediante un driver de bajo nivel:



1\. Arreglos de Paneles Solares y Turbinas Eólicas: Generadores primarios de energía limpia.



2\. Bancos de Baterías de Litio de Respaldo: Almacenamiento de excedentes de carga.



3\. Sensores de Flujo Eléctrico y Caudal de Carga (Inversores): Mediciones de entrada y salida en kilovatios (kW).



4\. Sensores Térmicos de Celda: Monitoreo de temperatura crítica en los contenedores de las baterías para prevención de fugas térmicas.



5\. Conmutadores Electrónicos de Red (Relés de Alta Potencia): Actuadores mecánicos que permiten conectar o aislar sectores de consumo de la red comercial principal o de la microred local. Los estudiantes deben definir formalmente los siguientes componentes de su Lenguaje L orientado a operadores del sistema ECO-GRID:



• Especificación del Alfabeto y Reglas Léxicas: Listado exhaustivo de tokens válidos, delimitadores y literales numéricos o booleanos aceptados por su analizador léxico conceptual.



• Palabras Clave Obligatorias: El lenguaje debe incorporar palabras reservadas explícitas para el control de flujo y la lectura/acción de dispositivos físicos. Ejemplo básico de primitiva léxica requerida: init\_grid, leer\_temperatura(bateria\_id), estado\_carga(bateria\_id), conmutar\_linea(sector\_id, estado), estructuras condicionales escritas en lenguaje natural estructurado o sintaxis compacta (ej. si\_verdadero ... entonces ... fin\_si), y estructuras de repetición iterativa (ej. mientras ... ejecutar ... fin\_mientras).



• Gramática Sintáctica Abstracta: Descripción en lenguaje natural o mediante pseudo-notación matemática del orden lógico que debe poseer una sentencia válida para que la máquina pueda interpretar el comando sin ambigüedades.



• Finalmente, para demostrar la viabilidad y expresividad de su lenguaje, deberán escribir en el informe dos (02) programas de ejemplo completamente desarrollados en

su Lenguaje L, resolviendo de manera rigurosa los siguientes escenarios operativos específicos dentro de la planta ECO-GRID:



• Escenario Operativo A (Prevención de Fuga Térmica y Gestión de Alivio de Carga): El programa debe monitorizar de forma continua e iterativa la temperatura de un banco de baterías específico empleando estructuras repetitivas. Si la temperatura registrada supera un umbral crítico de seguridad (por ejemplo, 55 grados Celsius), el programa debe activar de forma inmediata los sistemas de refrigeración auxiliar, desconectar las líneas de carga solar para detener el ingreso de energía térmica y desviar el consumo del sector industrial hacia la red comercial de respaldo para aliviar el estrés del componente. El ciclo debe terminar o emitir alertas de emergencia recurrentes si el peligro persiste tras un período determinado.



• Escenario Operativo B (Balance de Carga y Optimización Energética Autónoma): El script en Lenguaje L debe evaluar el estado de carga actual de los sistemas de almacenamiento de la planta. Si el nivel de carga de la batería es óptimo (superior al 90%) y la generación de los paneles solares excede la demanda interna actual detectada por los sensores de flujo, el lenguaje debe permitir ejecutar comandos para accionar los relés automáticos y vender/inyectar el excedente energético hacia la red eléctrica pública general. En caso contrario, si las baterías descienden de un límite crítico (menor al 20%) durante horas de alta demanda nocturna, el script debe aislar los sectores no esenciales de la fábrica para preservar el suministro en las áreas médicas o de servidores críticos de la organización.

