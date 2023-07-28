from flask import Flask, render_template
import psycopg2
from pymongo import MongoClient

app = Flask(__name__)

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
        conn.close()
        return True
    except Exception:
        return False

def test_mongodb_connection():
    try:
        # Replace these with your actual MongoDB connection string
        client = MongoClient('mongodb://mongo-host:27017/')
        db = client['mydatabase']

        # Add a new collection to MongoDB
        db['mycollection'].insert_one({'name': 'John Doe', 'age': 30})

        # List collections in the database
        collections = db.list_collection_names()

        client.close()
        return True, collections
    except Exception:
        return False, []

@app.route('/')
def index():
    postgres_connected = test_postgres_connection()
    mongo_connected, mongo_collections = test_mongodb_connection()
    return render_template('index.html', postgres_connected=postgres_connected, mongo_connected=mongo_connected, mongo_collections=mongo_collections)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
