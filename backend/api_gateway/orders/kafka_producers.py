from kafka import KafkaProducer

import json
from decouple import config

producer = KafkaProducer(
    bootstrap_servers=config("KAFKA_BROKER", default="localhost:9092"),
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)                         

def send_order_event(event_data):
    print(f"[Kafka] Sending: {event_data}")
    producer.send("order_placed",event_data)
    producer.flush()