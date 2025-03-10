# Use an official Python image
FROM python:3.7.5

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file first (to optimize caching)
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application files
COPY . .

# Apply migrations (removing unnecessary CD command)
RUN python /app/services/manage.py makemigrations && python manage.py migrate

# Expose port 8000 (Django default)
EXPOSE 8000

# Run Django server
CMD ["python", "/app/services/manage.py", "runserver"]