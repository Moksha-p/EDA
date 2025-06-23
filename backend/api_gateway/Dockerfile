# Use official Python image
FROM python:3.11-slim

# Set work directory
WORKDIR /code

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project files
COPY . .

# Run server (this is overridden by docker-compose command)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
