# Escenario Operativo A: Prevención de Fuga Térmica y Gestión de Alivio de Carga 

``El programa debe monitorizar de forma continua e iterativa la temperatura de un banco de baterías específico empleando estructuras repetitivas. Si la temperatura registrada supera un umbral crítico de seguridad (por ejemplo, 55 grados Celsius), el programa debe activar de forma inmediata los sistemas de refrigeración auxiliar, desconectar las líneas de carga solar para detener el ingreso de energía térmica y desviar el consumo del sector industrial hacia la red comercial de respaldo para aliviar el estrés del componente. El ciclo debe terminar o emitir alertas de emergencia recurrentes si el peligro persiste tras un período determinado.``

### Diagrama de flujo
```mermaid
graph TD
    %% Configuración de Estilos Generales
    style Start_A fill:#0EA5E9,stroke:#0284C7,stroke-width:2px,color:#FFF
    style Init_A fill:#1E293B,stroke:#38BDF8,stroke-width:2px,color:#FFF
    style While_A fill:#8B5CF6,stroke:#7C3AED,stroke-width:2px,color:#FFF
    style Read_A fill:#1E293B,stroke:#38BDF8,stroke-width:2px,color:#FFF
    style If_A fill:#8B5CF6,stroke:#7C3AED,stroke-width:2px,color:#FFF
    style Action_A1 fill:#1E293B,stroke:#EC4899,stroke-width:2px,color:#FFF
    style Action_A2 fill:#1E293B,stroke:#EC4899,stroke-width:2px,color:#FFF
    style Action_A3 fill:#1E293B,stroke:#EC4899,stroke-width:2px,color:#FFF
    style Warn_A fill:#1E293B,stroke:#F59E0B,stroke-width:2px,color:#FFF
    style If_Fail_A fill:#8B5CF6,stroke:#7C3AED,stroke-width:2px,color:#FFF
    style Crit_A fill:#1E293B,stroke:#EF4444,stroke-width:2px,color:#FFF
    style Shut_A fill:#1E293B,stroke:#EF4444,stroke-width:2px,color:#FFF
    style Stop_A fill:#EF4444,stroke:#DC2626,stroke-width:2px,color:#FFF

    subgraph ESCENARIO_A ["Escenario Operativo A: Prevención de Fuga Térmica"]
        Start_A([Inicio]) --> Init_A["init_grid();"]
        Init_A --> While_A{"¿estado_alarma < 5?"}
        
        While_A -- Sí --> Read_A["temp_celda = leer_dispositivo(TERMICO, BAT_01);"]
        Read_A --> If_A{"¿temp_celda > 55?"}
        
        If_A -- Sí --> Action_A1["conmutar_linea(REFRIGERACION_AUX, ENCENDIDO);"]
        Action_A1 --> Action_A2["conmutar_linea(CARGA_SOLAR, APAGADO);"]
        Action_A2 --> Action_A3["conmutar_linea(SECTOR_INDUSTRIAL, RESPALDO_COMERCIAL);"]
        %% Cambiamos el formato del comentario para evitar el error del parser
        Action_A3 --> Warn_A["notificar_alarma('...');<br/>estado_alarma++"]
        Warn_A --> While_A
        
        If_A -- No --> While_A
        
        While_A -- No --> If_Fail_A{"¿estado_alarma == 5?"}
        If_Fail_A -- Sí --> Crit_A["notificar_alarma('CRITICO: Peligro persiste');"]
        Crit_A --> Shut_A["conmutar_linea(BANCO_BATERIAS, APAGADO);"]
        Shut_A --> Stop_A["parada_emergencia();"]
        
        If_Fail_A -- No --> End_Normal_A([Fin Ejecución])
    end
```

#### Bloque de código
```
init_grid;

while estado_alarma < 5 do
    temp_celda = leer_dispositivo(TERMICO, BAT_01);
    
    if temp_celda > 55 then
        conmutar_linea(REFRIGERACION_AUX, ENCENDIDO);
        conmutar_linea(CARGA_SOLAR, APAGADO);
        conmutar_linea(SECTOR_INDUSTRIAL, RESPALDO_COMERCIAL);
        
        notificar_alarma("Advertencia: Posible fuga termica en BAT_01. Mitigacion activada.");
    end_if;
end_while;

if estado_alarma == 5 then
    notificar_alarma("CRITICO: El peligro persiste tras multiples intentos. Abortando.");
    conmutar_linea(BANCO_BATERIAS, APAGADO);
    parada_emergencia();
end_if;
```


#### Explicación paso a paso

| Paso n | Código                                                                                                                                                                      | Descripción                                  | Lógica                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| :----: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1    | `init_grid;`                                                                                                                                                                | Inicialización del sistema                   | Este script ejecuta la directiva de arranque. Indicando al intérprete que abra los canales de comunicación con los drivers de los relés y los sensores térmicos de la planta.                                                                                                                                                                                                                                                                                                                         |
|   2    | `while estado_alarma < 5 do ... end_while;`                                                                                                                                 | Bucle de monitoreo                           | Utilizamos la variable global reservada `estado_alarma`. Mientras el sistema tenga menos de 5 alarmas acumuladas, el ciclo seguirá evaluando la planta                                                                                                                                                                                                                                                                                                                                                |
|   3    | `temp_celda = leer_dispositivo(TERMICO, BAT_01);`                                                                                                                           | Lectura del componente físico                | En cada iteración del bucle, se invoca la función de lectura general. Se le pasa el tipo de sensor (`TERMICO`) y el identificador de la constante física (`BAT_01`). El valor numérico retornado se asigna a la variable local `temp_celda`.                                                                                                                                                                                                                                                          |
|   4    | `if temp_celda > 55 then ... end_if;`                                                                                                                                       | Evaluación léxica del umbral crítico         | Si la variable `temp_celda` supera el literal numérico `55`, el flujo de control entra al bloque de mitigación. Si es menor o igual, el bloque se ignora y el bucle vuelve a empezar silenciosamente.                                                                                                                                                                                                                                                                                                 |
|   5    | 1. `conmutar_linea(REFRIGERACION_AUX, ENCENDIDO);`<br><br>2. `conmutar_linea(CARGA_SOLAR, APAGADO);`<br><br>3. `conmutar_linea(SECTOR_INDUSTRIAL, RESPALDO_COMERCIAL);`<br> | Activación de mitigación (Actuadores)        | Si la temperatura es superior a 55 grados, el intérprete ejecuta las tres acciones de contingencia obligatorias de manera secuencial:<br><br>1. Activa los sistemas de refrigeración auxiliar.<br>        <br>2. Desconecta físicamente las líneas de entrada de los paneles para detener el ingreso térmico.<br>        <br>3. Usa el conmutador de transferencia para desviar el consumo de los sectores industriales hacia la red eléctrica comercial, aliviando el estrés sobre las baterías.<br> |
|   6    | `notificar_alarma("...");`                                                                                                                                                  | Acumulación de persistencia                  | Por cada ciclo en el que la temperatura siga sin bajar de 55°C, se emite una alerta recurrente a la consola del operador. Esta función suma automáticamente `+1` a la variable `estado_alarma`.                                                                                                                                                                                                                                                                                                       |
|   7    | `if estado_alarma == 5 then ... parada_emergencia(); end_if;`                                                                                                               | Parada de emergencia por peligro persistente | Si la refrigeración no hizo efecto y el bucle repitió la advertencia 5 veces el bucle se rompen, el sistema lanza un mensaje crítico final, aísla físicamente todo el banco de baterías por seguridad (usando `APAGADO`) y ejecuta la palabra reservada `parada_emergencia();` la cual detiene la ejecución del intérprete de forma definitiva.                                                                                                                                                       |

----
# Escenario Operativo B: Balance de Carga y Optimización Energética Autónoma
```
El script en Lenguaje L debe evaluar el estado de carga actual de los sistemas de almacenamiento de la planta. Si el nivel de carga de la batería es óptimo (superior al 90%) y la generación de los paneles solares excede la demanda interna actual detectada por los sensores de flujo, el lenguaje debe permitir ejecutar comandos para accionar los relés automáticos y vender/inyectar el excedente energético hacia la red eléctrica pública general. En caso contrario, si las baterías descienden de un límite crítico (menor al 20%) durante horas de alta demanda nocturna, el script debe aislar los sectores no esenciales de la fábrica para preservar el suministro en las áreas médicas o de servidores críticos de la organización.
```

### Diagrama de flujo

``` mermaid;
graph TD
%% Configuración de Estilos Generales (Mapeados al Escenario B) 
style Start_B fill:#0EA5E9,stroke:#0284C7,stroke-width:2px,color:#FFF
style Init_B fill:#0EA5E9,stroke:#0284C7,stroke-width:2px,color:#FFF  
style Read_B fill:#1E293B,stroke:#38BDF8,stroke-width:2px,color:#FFF 
style If_Opt_B fill:#1E293B,stroke:#38BDF8,stroke-width:2px,color:#FFF 
style Inject_B fill:#8B5CF6,stroke:#7C3AED,stroke-width:2px,color:#FFF 
style Info_B fill:#1E293B,stroke:#EC4899,stroke-width:2px,color:#FFF
style Disconnect_B fill:#1E293B,stroke:#F59E0B,stroke-width:2px,color:#FFF
style If_Crit_B fill:#1E293B,stroke:#EC4899,stroke-width:2px,color:#FFF 
style Isolate_B fill:#8B5CF6,stroke:#7C3AED,stroke-width:2px,color:#FFF
style Alert_B fill:#1E293B,stroke:#EF4444,stroke-width:2px,color:#FFF  
style End_B fill:#EF4444,stroke:#DC2626,stroke-width:2px,color:#FFF

    
subgraph ESCENARIO_B ["Escenario Operativo B: Balance de Carga Autónomo"]
    Start_B([Inicio]) --> Init_B[init_grid;]
    

    Init_B --> Read_B["porcentaje_bateria = leer_dispositivo(CARGA_BAT, BAT_01);<br>generacion_solar = leer_dispositivo(FLUJO_IN, PANEL_SUR);<br>demanda_interna = leer_dispositivo(FLUJO_OUT, PLANTA_INDUSTRIAL);"]
    
    Read_B --> If_Opt_B{"¿porcentaje_bateria > 90<br>Y<br>generacion_solar > demanda_interna?"}
    
    Inject_B --> Info_B["notificar_alarma('Info: Inyectando excedente');"]
    
    If_Opt_B -- Sí (Condición Óptima) --> Inject_B["conmutar_linea(INTERCONEXION_PUBLICA, ENCENDIDO);"]
    Info_B --> End_B([Fin])
    
    If_Opt_B -- No --> Disconnect_B["conmutar_linea(INTERCONEXION_PUBLICA, APAGADO);"]
    Disconnect_B --> If_Crit_B{"¿porcentaje_bateria < 20<br>Y<br>generacion_solar == 0?"}
    
    If_Crit_B -- Sí (Emergencia Nocturna) --> Isolate_B["conmutar_linea(SECTORES_NO_ESENCIALES, APAGADO);"]
    Isolate_B --> Alert_B["notificar_alarma('Alerta: Reserva critica nocturna');"]
    Alert_B --> End_B
    
    If_Crit_B -- No --> End_B
end
```


#### Bloque de codigo
```
init_grid;

porcentaje_bateria = leer_dispositivo(CARGA_BAT, BAT_01);
generacion_solar = leer_dispositivo(FLUJO_IN, PANEL_SUR);
demanda_interna = leer_dispositivo(FLUJO_OUT, PLANTA_INDUSTRIAL);

if porcentaje_bateria > 90 Y generacion_solar > demanda_interna then
    conmutar_linea(INTERCONEXION_PUBLICA, ENCENDIDO);
    notificar_alarma("Info: Bateria optima. Inyectando excedente a la red publica.");
else
    conmutar_linea(INTERCONEXION_PUBLICA, APAGADO);
    
    if porcentaje_bateria < 20 Y generacion_solar == 0 then
        conmutar_linea(SECTORES_NO_ESENCIALES, APAGADO);
        notificar_alarma("Alerta: Reserva critica nocturna. Aislando areas no esenciales.");
    end_if;
end_if;
```


### Paso a paso de la resolución (Explicación algorítmica)

| Paso n | Código                                                                 | Descripción                                   | Lógica                                                                                                                                                                                                                                                                                                                                                |
| :----: | ---------------------------------------------------------------------- | --------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1    | `init_grid;`                                                           | Inicialización del sistema                    | Este script ejecuta la directiva de arranque.                                                                                                                                                                                                                                                                                                         |
|   2    | `leer_dispositivo(...)`.                                               | Recolección del estado global (Sensores)      | El script evalúa el estado de carga actual de los sistemas de almacenamiento para tomar una decisión de balanceo, evaluando tres variables: <br>- Cuánta energía tienen las baterías (`CARGA_BAT`)<br>-Cuánta energía está entrando por los paneles solares (`FLUJO_IN`)<br>- Cuánta energía está consumiendo la planta en tiempo real (`FLUJO_OUT`). |
|   3    | `if porcentaje_bateria > 90 Y generacion_solar > demanda_interna then` | Evaluación del umbral de excedente            | Usando el operador `Y` se evalúa que: <br>- El nivel de carga de la batería es superior al 90%<br>- La generación de los paneles solares excede la demanda interna actual .                                                                                                                                                                           |
|   4    | `conmutar_linea(INTERCONEXION_PUBLICA, ENCENDIDO);`                    | Inyección a la red pública (Venta de energía) | Si la condición anterior es verdadera, se envían comandos para accionar los relés automáticos e inyecta el excedente energético hacia la red eléctrica pública general. Además, se emite una notificación informativa a la consola.                                                                                                                   |
|   5    | `else ... conmutar_linea(INTERCONEXION_PUBLICA, APAGADO);`<br>         | Bifurcación del flujo (El caso contrario)     | Si no hay excedente, el sistema corta preventivamente cualquier inyección a la red pública para no vaciar las baterías.<br>                                                                                                                                                                                                                           |
|   6    | `if porcentaje_bateria < 20 Y generacion_solar == 0 then`              | Evaluación del umbral crítico                 | Dentro del bloque `else`, se hace una segunda evaluación. El script verifica si las baterías descienden de un límite crítico menor al 20% durante horas de alta demanda nocturna. El lenguaje infiere matemáticamente que es de noche comprobando que la lectura del sensor solar (`generacion_solar`) es exactamente `0` kW.                         |
|   7    | `conmutar_linea(SECTORES_NO_ESENCIALES, APAGADO);`                     | Aislamiento de cargas no esenciales           | Si se confirma la emergencia nocturna, se accionan los relés para aislar los sectores no esenciales de la fábrica. Al apagar esta zona, se reduce drásticamente la variable `demanda_interna`, logrando preservar el suministro en las áreas críticas de la organización.                                                                             |
