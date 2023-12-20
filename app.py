import pandas as pd
import json
import utils


#todo: Mod.
input = "csv_input/estimations-actives-APOLLON.csv"
output = "csv_output/estimations-actives-APOLLON.csv__MODIFICADO.csv"
name_json = "json/estimation.json"
delimiter_value = ","


# Lectura CSV & JSON
with open(name_json, 'r', encoding='utf-8') as archivo_json:
            jsonRules = json.load(archivo_json)

file_CSV = input
encoding = utils.detect_encoding(file_CSV)

try:
    datos = pd.read_csv(file_CSV, encoding=encoding, delimiter=delimiter_value)
except UnicodeDecodeError:
    print(f"Error al decodificar con la codificación detectada '{encoding}'. Intenta con otra codificación.")

#?##################################
    
#crea la columna si no existe 
if 'mig_id' in jsonRules and jsonRules['mig_id'].get('create', False):
    if 'mig_id' not in datos.columns:
        datos['mig_id'] = None

#?##################################
    

for column_name, rules in jsonRules.items():

    #** REMOVE WHITE SPACE
    if rules.get("removeWhitespace"):
        if column_name in datos.columns:  # Verifica si la columna está presente en los datos
            datos[column_name] = datos[column_name].apply(lambda x: x.replace(" ", "") if isinstance(x, str) else x)

    #** FECHA
    if rules.get("isDate", False):
        current_format = None
        for fmt in rules["current_format"]:
            if fmt.get("flag"):
                current_format = fmt

        if current_format:  # Si se encontró un formato válido
            format_key = next(iter(current_format))
            datos[column_name] = datos[column_name].apply(lambda x: utils.convert_date_to_yyyy_mm_dd(x, current_format[format_key]))

    #** VALORES - TEXTO
    if rules.get("changeText", False):
        values_to_change = rules.get("values")
        if values_to_change:
            for value_set in values_to_change:
                current_value = value_set.get("current_value")
                modified_value = value_set.get("modified_value")



                print(value_set.get("modified_value"))


                
                if current_value and modified_value:
                    if column_name in datos.columns:
                        datos.loc[datos[column_name] == current_value, column_name] = modified_value

    #** REMOVE PREFIXE
    if rules.get("removePrefixe", False):
        if column_name in datos.columns: 
            datos[column_name] = datos[column_name].apply(lambda x: x[2:] if isinstance(x, str) and x.startswith("33") else x)
            datos[column_name] = datos[column_name].apply(lambda x: x[1:] if isinstance(x, str) and x.startswith("+") else x)
    
    #** GENERA NÚMEROS PARA EL MIG_ID
    if column_name == 'mig_id':
        datos['mig_id'] = list(range(1, len(datos) + 1))        

#?##################################
                        

# Mostrar los datos modificados
print("\nDatos modificados:")
print(datos)

columnas_especificas = ['id', 'dcreat', 'dmodif', 'idtbien', 'cheminee', 'mig_id']
datos_especificos = datos[columnas_especificas]

print("\nESPECIFICOS:")
print(datos_especificos)

# Guardar los cambios en un nuevo archivo CSV
res = output
datos.to_csv(res, index=False)
print(f"\nGuardado en '{res}'")

#?##################################