# ============================================
# IMPORTACIÓN DE LIBRERÍAS
# ============================================
import time
from json import dumps
from confluent_kafka import Producer

# ============================================
# CONFIGURACIÓN DEL PRODUCTOR
# ============================================
config = {
    'bootstrap.servers': 'localhost:9092',
    'client.id': 'python-producer-extra'
}

producer = Producer(config)

# ============================================
# DEFINICIÓN DEL TÓPICO
# ============================================
topic_kafka = 'alumnos_bigdata'

# ============================================
# ENVÍO DE MENSAJES
# ============================================
data = {
        'Proyecto': f'Innovación #{e+1}',
        'Presupuesto': f'{(e+1)*5000} EUR',
        'Estado': 'Aprobado' if e % 2 == 0 else 'En revisión'
    }



for e in range(100):
    # Creamos un diccionario con datos simulados de negocio.
    data = {
        'Proyecto': f'Innovación #{e+1}',
        'Presupuesto': f'{(e+1)*5000} EUR',
        'Estado': 'Aprobado' if e % 2 == 0 else 'En revisión'
    }

    # Convertimos el diccionario a una cadena JSON (texto estructurado).
    # dumps() transforma un objeto Python (dict) en texto JSON (str)
    # Por defecto, JSON convierte caracteres especiales (como á, ñ, ó) a códigos Unicode (\uXXXX)
    # porque intenta usar solo ASCII (un estándar antiguo que solo incluye letras inglesas).
    # Al poner ensure_ascii=False, mantenemos los acentos y caracteres tal cual.
    data_str = dumps(data, ensure_ascii=False)

    # Convertimos la cadena a bytes porque Kafka trabaja con datos binarios.
    # ¿Por qué binario? Porque es el formato estándar para enviar datos por la red.
    # encode('utf-8') transforma texto (str) en bytes (binario)
    data_bytes = data_str.encode('utf-8')

    # Enviamos el mensaje al tópico definido.
    # IMPORTANTE: produce() es ASÍNCRONO.
    # Esto significa que el mensaje no se envía inmediatamente,
    # sino que se guarda en un buffer interno y se envía en segundo plano.
    producer.produce(topic=topic_kafka, value=data_bytes)

    # Mostramos en pantalla lo que estamos enviando.
    print(f"Enviando datos: {data} al tópico {topic_kafka}")

    # Pausa de 1 segundo entre mensajes para simular un flujo en tiempo real.
    time.sleep(1)


# ============================================
# FLUSH FINAL
# ============================================
# ¿Por qué usamos flush()?
# Como produce() es asíncrono, algunos mensajes pueden quedar en el buffer
# cuando el programa termina. flush() espera a que TODOS los mensajes pendientes
# se envíen al broker antes de cerrar el programa.
pending = producer.flush()
# Comprobamos si hubo mensajes que no se pudieron entregar.
# flush() devuelve el número de mensajes que no se enviaron.
if pending != 0:
    print(f"{pending} mensajes no se pudieron entregar.")