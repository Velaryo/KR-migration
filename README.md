# INSTALACIÓN:
- Descargar Python: https://www.python.org/downloads/
- Instalar Python: https://www.youtube.com/watch?v=UiQGhWZ7UHU
- Descargar e instalar VS Code: https://code.visualstudio.com/download
- Descarga del script: https://github.com/Velaryo/KR-migration

# ACTIVACIÓN DEL ENTORNO VIRTUAL:
1. Descomprimir el script en una carpeta e ingresar en ella. Ubicarse hasta ver el archivo 'app.py'.

2. Abrir el terminal/CMD/consola y escribir:
```
pip install virtualenv
```

3. Escribir:
```
Set-ExecutionPolicy Unrestricted -Scope Process
```

4. Activar el entorno virtual:
```
venv\Scripts\activate
```

5. Instalación de dependencias:
```
pip install -r requirements.txt
```

# Básico:
- Colocar el archivo a manipular en la carpeta "csv_input".
- El resultado se generará en la carpeta "csv_output".
- El nombre de entrada y salida, el delimitador y el nombre del archivo .json' deben ser asignados en el archivo 'app.py'.

# Consideraciones.
- Algunas propiedades son de importancia para el proceso aunque no se utilcen. Guiarse de los ejemplos ubicados en '/json/estimation.json'.
- Se recomienda revisar constantemente el resultado mientras vaya configurando el archivo JSON.
- Al configurar el JSON, tener cuidado con que si el valor es un string, numérico o un booleano. Si es string, lleva comillas; esto es a nivel del formato que tenga en el CSV, puede suceder que el supuesto número (1, 2), en realidad sea un texto ("1", "2").
```json
{
    ...
    "values": [
            {"current_value": 1, "modified_value": "Appartement"},
    ...
}
```


# /JSON


- @Modifications: Realiza modificaciones.
    - cleanLinebreak: Ordena la limpieza de los santos de linea.
        - flag: Ordena la limpieza.
        - value_to_remplace: Valores a reemplazar "\N" y "\n".

```json
{
    "modifications": {
        "cleanLinebreak": {
            "flag": true,
            "value_to_remplace": ["\\N", "\\n"]
        }
    },
}
```

- mig_id: Para crear la columna "mig_id".
    - create: Crea el campo *mig_id* siempre y cuando no exista.
    - generateNumbers: Luego genera números de forma correlativa.

```json
{
    "mig_id": {
        "create": true,
        "generateNumbers": true
    },
}
```

***

## Reemplazar texto por otro:
### La primera propiedad representa el nombre de la columna.

- changeText: [bool] - Cambia el valor de una celda. 
    - values: Contiene los valores actuales y por cambiar. Permite ingresar varios valores para modificar.

```json
{
    "nombreColumna": {
        "changeText": true,
        "values": [
                    {"current_value": "YES", "modified_value": "oui"},
                    {"current_value": "NO", "modified_value": "non"},
                    {"current_value": "t", "modified_value": "oui"},
                    {"current_value": "n", "modified_value": "non"},
                    {"current_value": "Y", "modified_value": "oui"},
                    {"current_value": "N", "modified_value": "non"},
                ]
    },
    ...
}
```


## Para números de teléfono:

- removeWhitespace [Bool]: Indica si se debe eliminar los espacios en blanco.
```json
{
    "nombreColumna": {
            "removeWhitespace": true,
            ...
    },
    ...
}
```

- removePrefixe: [Bool] - Elimina los 2 primeros números, siempre y cuando empiece con 33. Si existe el simbolo "+", lo elimina. Se recomienda usar junto con removeWhitespace.

```json
{
    "removeWhitespace":true,
    "removePrefixe": true,
}
```

## Para fechas:

- isDate: [Bool] - Indica si la celda es una fecha y que debe formatearse.
    - current_format: Almacena las propiedades con los formatos de fecha que tiene la celda actualmente. **SOLO escoger 1**.
```json
{
    "isDate": true,
    "current_format": [
        {"format_1": "dd/mm/yyyy", "flag": false},
        {"format_2": "dd-mm-yyyy", "flag": false},
        {"format_3": "dd/MM/yyyy HH:mm", "flag": true},
        {"format_4": "yyyy-MM-dd HH:mm:ss", "flag": false}
    ]
}
```
