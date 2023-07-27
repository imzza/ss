# Use the official Python image as the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Install the necessary packages
RUN pip install psycopg2-binary pymongo

# Copy the script to test the database connections
COPY test_db_connections.py .

# Run the script when the container starts
CMD ["python", "test_db_connections.py"]

import psycopg2
from pymongo import MongoClient

def test_postgres_connection():
    try:
        # Replace these with your actual PostgreSQL database credentials
        conn = psycopg2.connect(
            host='postgres-host',
            port='5432',
            dbname='postgres-db',
            user='postgres-user',
            password='postgres-password'
        )
        print("Successfully connected to PostgreSQL!")
        conn.close()
    except Exception as e:
        print(f"Error connecting to PostgreSQL: {e}")

def test_mongodb_connection():
    try:
        # Replace these with your actual MongoDB connection string
        client = MongoClient('mongodb://mongo-host:27017/')
        db = client['mydatabase']
        print("Successfully connected to MongoDB!")
        client.close()
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")

if __name__ == "__main__":
    test_postgres_connection()
    test_mongodb_connection()




new_revision=$(grep -oP '"revision": \K[^,]*' /tmp/new_task_definition.json)

# Step 4: Update the ECS service to use the new task definition revision
aws ecs update-service \
    --cluster my-cluster \
    --service my-service \
    --task-definition my-task-family:$new_revision

# Clean up temporary file
rm /tmp/new_task_definition.json


docker build --file Dockerfile --tag dbcon:latest --platform linux/arm64 ~/Documents/test

