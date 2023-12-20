import pandas as pd
import json
import utils


#todo: Mod.
input = "csv_input/contact.csv"
output = "csv_output/con_mod.csv"
name_json = "json/acq_BAK.json"
delimiter_value = ";"


# Ruta y nombre del archivo CSV
file_CSV = input

# JSON con las reglas para la modificación de varias columnas
with open(name_json, 'r') as archivo_json:
    jsonRules = json.load(archivo_json)


# Detectar la codificación del archivo CSV
encoding = utils.detect_encoding(file_CSV)

# Intentar leer el archivo CSV con la codificación detectada
try:
    datos = pd.read_csv(file_CSV, encoding=encoding, delimiter=delimiter_value)
except UnicodeDecodeError:
    print(f"Error al decodificar con la codificación detectada '{encoding}'. Intenta con otra codificación.")


for column_name, rules in jsonRules.items():

    #** REMOVE WHITE SPACE
    if rules.get("removeWhitespace"):
        if column_name in datos.columns:  # Verifica si la columna está presente en los datos
            datos[column_name] = datos[column_name].apply(lambda x: x.replace(" ", "") if isinstance(x, str) else x)

    #** FECHA
    if rules["isDate"]:
        current_format = None
        for fmt in rules["current_format"]:
            if fmt.get("flag"):
                current_format = fmt

        if current_format:  # Si se encontró un formato válido
            format_key = next(iter(current_format))
            datos[column_name] = datos[column_name].apply(lambda x: utils.convert_date_to_yyyy_mm_dd(x, current_format[format_key]))

    #** VALORES - TEXTO
    if rules.get("changeText"):
        values_to_change = rules.get("values")
        if values_to_change:
            for value_set in values_to_change:
                current_value = value_set.get("current_value")
                modified_value = value_set.get("modified_value")
                if current_value and modified_value:
                    if column_name in datos.columns:  # Verifica si la columna está presente en los datos
                        datos.loc[datos[column_name] == current_value, column_name] = modified_value

    #** REMOVE PREFIXE
    
    if rules.get("removePrefixe"):
        if column_name in datos.columns:  # Verifica si la columna está presente en los datos
            datos[column_name] = datos[column_name].apply(lambda x: x[2:] if isinstance(x, str) and x.startswith("33") else x)
            datos[column_name] = datos[column_name].apply(lambda x: x[1:] if isinstance(x, str) and x.startswith("+") else x)

                        

# Mostrar los datos modificados
print("\nDatos modificados:")
print(datos)

# Guardar los cambios en un nuevo archivo CSV
res = output
datos.to_csv(res, index=False)
print(f"\nLos datos modificados se han guardado en '{res}'")
