# # inventory_service/consumer.py
# from kafka import KafkaConsumer, KafkaProducer
# import json

# consumer = KafkaConsumer(
#     'order_placed',
#     bootstrap_servers='localhost:9092',
#     value_deserializer=lambda m: json.loads(m.decode('utf-8')),
#     auto_offset_reset='earliest',
#     group_id='inventory-group',
# )

# producer = KafkaProducer(
#     bootstrap_servers='localhost:9092',
#     value_serializer=lambda v: json.dumps(v).encode('utf-8')
# )

# print("✅ Inventory Service is running...")

# for message in consumer:
#     order = message.value
#     print(f"🛒 Inventory checked for Order ID: {order['order_id']}")
    
#     # simulate stock check
#     inventory_status = {
#         "order_id": order['order_id'],
#         "status": "available"
#     }
#     producer.send("inventory_checked", value=inventory_status)
#     print("✅ Sent to topic: inventory_checked")

# inventory_service/consumer.py
from kafka import KafkaConsumer
import json
from producer import send_inventory_event
import os
PENDING_ORDERS = []

def consume_order_placed():
    consumer = KafkaConsumer(
        'order_placed',
        bootstrap_servers='kafka:9092',
        value_deserializer=lambda m: json.loads(m.decode('utf-8')),
        auto_offset_reset='earliest',
        group_id='inventory-group'
    )
    for msg in consumer:
        order_data = msg.value
        print("Received order for inventory check:", order_data)
        PENDING_ORDERS.append(order_data)  # add to manual approval list

