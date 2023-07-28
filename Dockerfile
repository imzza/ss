# Use the official Python image as the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Install Flask and pymongo
RUN pip install Flask pymongo psycopg2-binary

# Copy the Flask app file and the modified test_db_connections.py script
COPY app.py .
COPY test_db_connections.py .

# Expose the port for Flask to listen on
EXPOSE 5000

# Run the Flask app when the container starts
CMD ["python", "app.py"]
