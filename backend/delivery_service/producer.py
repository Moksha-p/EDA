# delivery_service/producer.py

from kafka import KafkaProducer
import json
import os

KAFKA_BROKER ='kafka:9092'

try:
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BROKER,
        value_serializer=lambda v: json.dumps(v).encode("utf-8")
    )
    print("✅ DeliveryService: Kafka Producer connected.")
except Exception as e:
    print("❌ DeliveryService: Kafka Producer connection failed:", e)
    producer = None


def send_delivery_event(topic: str, data: dict):
    if not producer:
        print("❌ Kafka producer not available.")
        return
    try:
        producer.send(topic, value=data)
        producer.flush()
        print(f"📤 Sent delivery event to '{topic}': {data}")
    except Exception as e:
        print(f"❌ Failed to send delivery event to '{topic}':", e)
