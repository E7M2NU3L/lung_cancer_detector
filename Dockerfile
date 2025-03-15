# Use an official Python image
FROM python:3.7.5-slim

WORKDIR /app

COPY requirements.txt .

# Upgrade pip before installing dependencies
RUN pip install --upgrade pip 

# Install required system dependencies
RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["sh", "-c", "python /app/services/manage.py makemigrations && python /app/services/manage.py migrate && python /app/services/manage.py runserver 0.0.0.0:8000"]