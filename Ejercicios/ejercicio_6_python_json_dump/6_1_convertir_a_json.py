# =============================================
# EJEMPLO: Convertir diccionarios a JSON (tema: motor y física)
# =============================================
# Usamos el módulo json para convertir un diccionario en una cadena JSON.
# Esto es útil cuando queremos enviar datos estructurados (por ejemplo, telemetría de un motor)
# a través de una API o almacenarlos en un archivo.

import json

# Ejemplo funcional:
# Datos simulados de un motor en pruebas
motor_data = {
    'Motor': 'V8 Turbo',
    'Temperatura_C': 95.6,          # Temperatura en grados Celsius
    'Presion_Barra': 2.3,           # Presión en bares
    'RPM': 7200,                    # Revoluciones por minuto
    'Sensores': ['Temperatura', 'Presión', 'RPM']  # Lista de sensores activos
}

# Mostramos el tipo original del objeto
print("Tipo original:", type(motor_data))

# Convertimos el diccionario a JSON
json_str = json.dumps(motor_data)
print("Cadena JSON:", json_str)
print("Tipo después de convertir:", type(json_str))

# =============================================
# EJERCICIOS:
# 1. Convierte el diccionario anterior a JSON con indentación (usa indent=4).
# 2. Crea un segundo diccionario con datos de otro motor (por ejemplo, eléctrico) y conviértelo también a JSON.
# 3. ¿Qué pasa si añades una lista de valores (por ejemplo, temperaturas históricas) como valor en el diccionario? Prueba.
# 4. Imprime el tipo de cada objeto antes y después de la conversión para entender la transformación.

json__str_ind = json.dumps(motor_data, indent=4)
print("Cadena JSON con indentación:", json__str_ind)
print("Tipo después de convertir:", type(json__str_ind))

motor2_data = {
    'Motor': 'Electrico',
    'Temperatura_C': 95.6,          # Temperatura en grados Celsius
    'Presion_Barra': 2.3,           # Presión en bares
    'RPM': 7200,                    # Revoluciones por minuto
    'Sensores': ['Temperatura', 'Presión', 'RPM']  # Lista de sensores activos
}
print("Tipo original:", type(motor2_data))
json_str_ind = json.dumps(motor2_data, indent=4)
print("Cadena JSON con indentación:", json_str_ind)
print("Tipo después de convertir:", type(json_str_ind))


motor3_data = {
    'Motor': 'Electrico',
    'Temperatura_C': [95.6, 76, 58],         # Temperatura en grados Celsius
    'Presion_Barra': 2.3,           # Presión en bares
    'RPM': 7200,                    # Revoluciones por minuto
    'Sensores': ['Temperatura', 'Presión', 'RPM']  # Lista de sensores activos
}
print("Tipo original:", type(motor3_data))
json_str_ind = json.dumps(motor3_data, indent=4)
print("Cadena JSON con indentación:", json_str_ind)
print("Tipo después de convertir:", type(json_str_ind))
