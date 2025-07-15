from fastapi import FastAPI, Body , HTTPException
from producer import send_delivery_event
from consumer import consume_inventory_checked
import threading
from kafka import KafkaProducer
import json

app = FastAPI()

PENDING_DELIVERIES = []
@app.get("/")
def root():
    return {"message": "🚚 Delivery Service is running!"}

@app.post("/delivery/start/{order_id}")
def start_delivery(order_id: int):
    for order in PENDING_DELIVERIES:
        if order["order_id"] == order_id:
            producer = KafkaProducer(
                bootstrap_servers='kafka:9092',
                value_serializer=lambda m: json.dumps(m).encode('utf-8')
            )
            producer.send('delivery_started', {
                **order,
                "status": "delivery_started"
            })
            PENDING_DELIVERIES.remove(order)
            return {"message": "Delivery started and Kafka message sent"}
    raise HTTPException(status_code=404, detail="Order not found")

@app.post("/delivery/update")
def update_delivery_status(order_id: int = Body(...), status: str = Body(...)):
    data = {"order_id": order_id, "status": status}
    send_delivery_event("delivery_started", data)
    return {"message": "📤 Delivery update sent to Kafka", "data": data}

# Start consumer thread
threading.Thread(target=consume_inventory_checked, daemon=True).start()
