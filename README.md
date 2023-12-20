# INSTALACIÓN
- Descargar Python: https://www.python.org/downloads/
- Instalar Python: https://www.youtube.com/watch?v=UiQGhWZ7UHU
- Descargar e instalar VS Code: https://code.visualstudio.com/download
- Descarga del script: ##################

# ACTIVACIÓN DEL ENTORNO VIRTUAL
1. Descomprimir el script en una carpeta e ingresar a la carpeta. Ubicarse hasta ver la carpeta "venv".

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

# BÁSICO
- Colocar el archivo a manipular en la carpeta "csv_input".
- El resultado se generará en la carpeta "csv_output".
- El nombre de entrada y salida, el delimitador y el nombre del archivo .json' deben ser asignados en el archivo 'app.py'


# /JSON

- Primera propiedad: Almacena el nombre de la columna

```json
{
    "nombreColumna": {
            "removeWhitespace":false,
            ...
    },
    ...
}
```

- removeWhitespace: [Bool] - Indica si se debe eliminar los espacios en blanco.

```json
{
    "removeWhitespace": true
}
```

- changeText: [String] - Cambio de valor de una celda normal. Permite un array de datos para ingresar el valor a reemplazar y el valor nuevo.

```json
{
    "changeText": true,
    "values": [
                {"current_value": "oui", "modified_value": "YES"},
                {"current_value": "non", "modified_value": "NO"}
            ]
}
```

- isDate: [Bool] - Indica si la celda es una fecha y que debe formatearse según lo indicado en la propiedad current_format. Debe escogerse **SOLO** un formato.

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

- removePrefixe: [Bool] - Elimina los 2 primeros números, siempre y cuando empiece con 33. Si existe el simbolo "+", lo elimina. Se recomienda usar junto con removeWhitespace.

```json
{
    "removeWhitespace":true,
    "removePrefixe": true,
}
```


# Consideraciones.
- Todas las propiedades deben ser usadas siempre (excepto current_format y values). Si una propiedad no es necesaria, dar el valor **false**.
- Se recomienda revisar constantemente el resultado mientras vaya configurando el archivo JSON.
