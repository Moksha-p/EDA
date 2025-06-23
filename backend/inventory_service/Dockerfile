# backend/inventory_service/Dockerfile

FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy dependency file and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . .

# Run the Kafka consumer
CMD ["python", "consumer.py"]
