# inventory_service/producer.py

from kafka import KafkaProducer
import json

KAFKA_BROKER = 'kafka:9092'  # inside Docker, 'kafka' hostname works

try:
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BROKER,
        value_serializer=lambda v: json.dumps(v).encode("utf-8")
    )
    print("✅ InventoryService: Kafka Producer connected.")
except Exception as e:
    print("❌ InventoryService: Kafka Producer connection failed:", e)
    producer = None


def send_inventory_event(topic: str, data: dict):
    if not producer:
        print("❌ Kafka producer not available.")
        return
    try:
        producer.send(topic, value=data)
        producer.flush()
        print(f"📤 Sent inventory event to '{topic}': {data}")
    except Exception as e:
        print(f"❌ Failed to send inventory event to '{topic}':", e)
