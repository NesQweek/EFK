FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

# Command to run the Flask application using Gunicorn
CMD ["gunicorn", "-c", "/app/gunicorn_config.py", "-b", "0.0.0.0:8000", "app:app"]
