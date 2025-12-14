# =============================================
# EJEMPLO: Flujo completo (dict -> JSON -> bytes -> texto -> dict)
# =============================================
# Objetivo: Ver cómo los datos pasan por diferentes formatos:
# 1. dict (Python) -> 2. str (JSON) -> 3. bytes (binario) -> 4. str -> 5. dict
# =============================================

import json
from datetime import datetime

for e in range(3):
    # PASO 1: Creamos el diccionario con datos simulados
    data = {
        'Proyecto': f'Innovación #{e+1}',
        'Presupuesto': f'{(e+1)*5000} EUR',
        'Estado': 'Aprobado' if e % 2 == 0 else 'En revisión',
        'Fecha': datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Fecha actual
    }
    print("\nDiccionario original:", data)
    print("Tipo:", type(data))  # dict

    # PASO 2: Convertimos el diccionario a JSON (texto)
    data_str = json.dumps(data)
    print("\nTexto JSON:", data_str)
    print("Tipo:", type(data_str))  # str

    # PASO 3: Convertimos el texto a bytes (para enviar por red)
    data_bytes = data_str.encode('utf-8')
    print("\nBytes (para Kafka/red):", data_bytes)
    print("Tipo:", type(data_bytes))  # bytes

    # PASO 4: Simulamos recepción y decodificación (bytes -> texto)
    recibido_str = data_bytes.decode('utf-8')
    print("\nTexto decodificado:", recibido_str)
    print("Tipo:", type(recibido_str))  # str

    # PASO 5: Convertimos el texto decodificado de nuevo a diccionario
    recibido_dict = json.loads(recibido_str)
    print("\nDiccionario reconstruido:", recibido_dict)
    print("Tipo:", type(recibido_dict))  # dict

# =============================================
# EJERCICIOS:
# 1. Cambia el rango a 5 en lugar de 3.
# 2. Añade una lista de sensores al diccionario (por ejemplo ['Temperatura', 'Presión']).
# 3. ¿Qué pasa si añades un emoji en el valor de 'Estado'? ¿Se mantiene con UTF-8?
# 4. Imprime los tipos en cada paso para confirmar la transformación.

for e in range(5):
    # PASO 1: Creamos el diccionario con datos simulados
    data = {
        'Proyecto': f'Innovación #{e+1}',
        'Presupuesto': f'{(e+1)*5000} EUR',
        'Estado': 'Aprobado 😊' if e % 2 == 0 else 'En revisión 🥹',
        'Fecha': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),  # Fecha actual
        'Temperatura_C': 95.6,          # Temperatura en grados Celsius
        'Presion_Barra': 2.3,           # Presión en bares
        'RPM': 7200,                    # Revoluciones por minuto
        'Sensores': ['Temperatura', 'Presión', 'RPM']  # Lista de sensores activos
    }
    print("\nDiccionario original:", data)
    print("Tipo:", type(data))  # dict
    print(f"Iteración {e+1}: Diccionario -> {data}")

    # PASO 2: Convertimos el diccionario a JSON (texto)
    data_str = json.dumps(data)
    print("\nTexto JSON:", data_str)
    print("Tipo:", type(data_str))  # str

    # PASO 3: Convertimos el texto a bytes (para enviar por red)
    data_bytes = data_str.encode('utf-8')
    print("\nBytes (para Kafka/red):", data_bytes)
    print("Tipo:", type(data_bytes))  # bytes

    # PASO 4: Simulamos recepción y decodificación (bytes -> texto)
    recibido_str = data_bytes.decode('utf-8')
    print("\nTexto decodificado:", recibido_str)
    print("Tipo:", type(recibido_str))  # str

    # PASO 5: Convertimos el texto decodificado de nuevo a diccionario
    recibido_dict = json.loads(recibido_str)
    print("\nDiccionario reconstruido:", recibido_dict)
    print("Tipo:", type(recibido_dict))  # dict
    
    
# 5. Muestra todas las iteraciones, no solo la última.
todos_los_diccionarios = []
for e in range(2):
    # PASO 1: Creamos el diccionario con datos simulados
    print(f"\n=== Iteración {e+1} ===")
    data = {
        'Proyecto': f'Innovación #{e+1}',
        'Presupuesto': f'{(e+1)*5000} EUR',
        'Estado': 'Aprobado 😊' if e % 2 == 0 else 'En revisión 🥹',
        'Fecha': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),  # Fecha actual
        'Temperatura_C': 95.6,          # Temperatura en grados Celsius
        'Presion_Barra': 2.3,           # Presión en bares
        'RPM': 7200,                    # Revoluciones por minuto
        'Sensores': ['Temperatura', 'Presión', 'RPM']  # Lista de sensores activos
    }
    print("\nDiccionario original:", data)
    print("Tipo:", type(data))  # dict

    # PASO 2: Convertimos el diccionario a JSON (texto)
    data_str = json.dumps(data)
    print("\nTexto JSON:", data_str)
    print("Tipo:", type(data_str))  # str

    # PASO 3: Convertimos el texto a bytes (para enviar por red)
    data_bytes = data_str.encode('utf-8')
    print("\nBytes (para Kafka/red):", data_bytes)
    print("Tipo:", type(data_bytes))  # bytes

    # PASO 4: Simulamos recepción y decodificación (bytes -> texto)
    recibido_str = data_bytes.decode('utf-8')
    print("\nTexto decodificado:", recibido_str)
    print("Tipo:", type(recibido_str))  # str

    # PASO 5: Convertimos el texto decodificado de nuevo a diccionario
    recibido_dict = json.loads(recibido_str)
    print("\nDiccionario reconstruido:", recibido_dict)
    print("Tipo:", type(recibido_dict))  # dict
    
    # PASO 6: Guardar diccionario reconstruido
    todos_los_diccionarios.append(recibido_dict)
    
print("Imprimir todos los diccionarios reconstruidos")
for dic in todos_los_diccionarios:
    print(dic)