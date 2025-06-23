# delivery_service/consumer.py

from kafka import KafkaConsumer
import json
from producer import send_delivery_event

consumer = KafkaConsumer(
    'inventory_checked',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='earliest',
    group_id='delivery-group',
)

print("✅ Delivery Service is running...")

for message in consumer:
    inventory = message.value
    print(f"📦 Delivery started for Order ID: {inventory['order_id']}")

    delivery_data = {
        "order_id": inventory['order_id'],
        "status": "dispatched"
    }

    send_delivery_event("delivery_started", delivery_data)
