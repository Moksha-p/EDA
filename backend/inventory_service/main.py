from fastapi import FastAPI, Body ,HTTPException
from producer import send_inventory_event
from consumer import consume_order_placed
import threading
from kafka import KafkaProducer
import json

app = FastAPI()

PENDING_ORDERS = []

@app.get("/")
def root():
    return {"message": "📦 Inventory Service is running!"}

@app.post("/inventory/approve/{order_id}")
def approve_order(order_id: int):
    for order in PENDING_ORDERS:
        if order["order_id"] == order_id:
            # Send to Kafka topic 'inventory_checked'
            producer = KafkaProducer(
                bootstrap_servers='kafka:9092',
                value_serializer=lambda m: json.dumps(m).encode('utf-8')
            )
            producer.send('inventory_checked', {
                **order,
                "status": "inventory_approved"
            })
            PENDING_ORDERS.remove(order)
            return {"message": "Order approved and sent to Kafka"}

    raise HTTPException(status_code=404, detail="Order not found")

@app.get("/inventory/pending")
def list_pending_orders():
    return {"pending": PENDING_ORDERS}

@app.post("/inventory/add")
def add_test_order(order: dict):
    PENDING_ORDERS.append(order)
    return {"message": "Order added to pending list"}


@app.post("/inventory/update")
def update_inventory(order_id: int = Body(...), status: str = Body(...)):
    data = {"order_id": order_id, "status": status}
    send_inventory_event("inventory_checked", data)
    return {"message": "📤 Inventory update sent to Kafka", "data": data}

# Start consumer thread
# threading.Thread(target=consume_order_placed, daemon=True).start()
