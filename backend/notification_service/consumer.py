# ✅ notification_service/consumer.py
from kafka import KafkaConsumer
import json
import os

def consume_delivery_started():
    try:
        consumer = KafkaConsumer(
            'delivery_started',
            bootstrap_servers='kafka:9092',
            value_deserializer=lambda m: json.loads(m.decode('utf-8')),
            auto_offset_reset='earliest',
            group_id='notification-group',
        )

        print("🔔 NotificationService: Kafka Consumer started.")
        for message in consumer:
            delivery = message.value
            print(f"📨 Notification: Your order {delivery['order_id']} has been {delivery['status']}!")
    except Exception as e:
        print("❌ NotificationService: Kafka consumer error:", e)
