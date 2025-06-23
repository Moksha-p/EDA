# notification_service/consumer.py

from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'delivery_started',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='earliest',
    group_id='notification-group',
)

print("🔔 Notification Service is running...")

for message in consumer:
    delivery = message.value
    print(f"📨 Notification: Your order {delivery['order_id']} has been {delivery['status']}!")
