# notification_service/main.py
from fastapi import FastAPI
import threading
from consumer import consume_delivery_started
import uvicorn

app = FastAPI()

@app.get("/")
def root():
    return {"message": "🔔 Notification Service is running!"}

# Start Kafka consumer in a separate thread
threading.Thread(target=consume_delivery_started, daemon=True).start()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8003, reload=True)
