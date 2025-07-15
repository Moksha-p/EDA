# orders/kafka_producers.py

import time
import json
from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable

# Retry logic to wait for Kafka
while True:
    try:
        producer = KafkaProducer(
            bootstrap_servers='kafka:9092',
            value_serializer=lambda v: json.dumps(v).encode("utf-8")
        )
        print("✅ Kafka Producer connected.")
        break
    except NoBrokersAvailable:
        print("⏳ Waiting for Kafka broker...")
        time.sleep(5)

def send_order_event(data):
    producer.send('order_placed', value=data)
    print(f"📤 Sent order_placed event: {data}")
