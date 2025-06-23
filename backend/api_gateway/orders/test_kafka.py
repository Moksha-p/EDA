from kafka import KafkaProducer
import json
import time

producer = None

# Try to connect with retries
for _ in range(10):
    try:
        producer = KafkaProducer(
            bootstrap_servers="localhost:9092",  # <-- Make sure this matches
            value_serializer=lambda v: json.dumps(v).encode("utf-8"),
        )
        print("✅ Kafka Producer connected.")
        break
    except Exception as e:
        print("⏳ Waiting for Kafka broker...", str(e))
        time.sleep(5)

data = {
    "order_id": 123,
    "item": "pizza",
    "quantity": 2,
    "status": "placed"
}

producer.send("order_placed", value=data)
producer.flush()
print("✅ Message sent to Kafka!")

# from kafka import KafkaProducer
# import json

# producer = KafkaProducer(
#     bootstrap_servers='localhost:9092',
#     value_serializer=lambda v: json.dumps(v).encode('utf-8')
# )

# producer.send('test_topic', {'message': 'Hello from host!'})
# producer.flush()
# print("✅ Message sent!")

