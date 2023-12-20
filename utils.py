import chardet
from datetime import datetime

# Reconoce codificación automaticamente
def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        rawdata = f.read()
    result = chardet.detect(rawdata)
    return result['encoding']

# Convierte la fecha al formato: yyyy-mm-dd
def convert_date_to_yyyy_mm_dd(date_string, current_format):
    try:
        if current_format == "dd/mm/yyyy":
            return datetime.strptime(date_string, '%d/%m/%Y').strftime('%Y-%m-%d')

        elif current_format == "dd-mm-yyyy":
            return datetime.strptime(date_string, '%d-%m-%Y').strftime('%Y-%m-%d')

        elif current_format == "dd/MM/yyyy HH:mm":
            return datetime.strptime(date_string, '%d/%m/%Y %H:%M').strftime('%Y-%m-%d')

        elif current_format == "yyyy-MM-dd HH:mm:ss":
            return datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')
            
    except ValueError:
        pass
    

    return date_string