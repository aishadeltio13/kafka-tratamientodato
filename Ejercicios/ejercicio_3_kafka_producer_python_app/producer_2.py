from confluent_kafka import Producer
from json import dumps
import time
import random

# CONFIGURACIÓN
config = {
    'bootstrap.servers': 'localhost:9092',
    'client.id': 'productor-ventas'
}
producer = Producer(config)

# ============================================
# 1. CAMBIO DE NOMBRE DEL TÓPICO
# ============================================
topic_kafka = 'ventas_globales'

# ============================================
# 2. CAMBIO DE RANGO (MENOS MENSAJES)
# ============================================
# En lugar de 100, vamos a enviar solo 20 para probar rápido.
total_mensajes = 20

for e in range(total_mensajes):
    
    # Simulación de datos aleatorios 
    paises = ['España', 'México', 'Francia', 'Alemania', 'Japón']
    pais_destino = random.choice(paises)
    monto = random.randint(50, 1500)

    # ============================================
    # 3. LÓGICA CONDICIONAL
    # ============================================
    # Si el índice 'e' es PAR, pago con Tarjeta. Si es IMPAR, con PayPal.
    if e % 2 == 0:
        metodo_pago = "Tarjeta de Crédito"
        estado_envio = "Procesando"
    else:
        metodo_pago = "PayPal"
        estado_envio = "Verificando pago"

    # ============================================
    # 4. MODIFICACIÓN DEL CONTENIDO (DICCIONARIO)
    # ============================================
    # Cambiamos la estructura totalmente para simular un pedido internacional.
    data = {
        'id_pedido': f'ORD-{2025000 + e}',
        'pais': pais_destino,
        'total': f'{monto} €',
        'metodo_pago': metodo_pago,
        'estado': estado_envio,
        'es_prioritario': monto > 1000 
    }

    # Serialización y envío (Igual que antes)
    data_str = dumps(data, ensure_ascii=False)
    data_bytes = data_str.encode('utf-8')

    producer.produce(topic=topic_kafka, value=data_bytes)

    print(f"📦 Pedido {e+1}/{total_mensajes} enviado: {data['id_pedido']} -> {data['pais']}")
    
    # Hacemos una pausa más corta (0.5 seg) para que vaya fluido
    time.sleep(0.5)

# Esperar a que todo salga del buffer
producer.flush()
print("\n Todos los pedidos han sido procesados.")