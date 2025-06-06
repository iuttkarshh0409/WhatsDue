import mysql.connector
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

def get_connection():
    """Establish and return a connection to the MySQL database."""
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS"),
            database=os.getenv("DB_NAME"),
            port=3306,
            use_pure=True
        )
        if connection.is_connected():
            print("Connected to the MySQL database successfully!")
        return connection
    except mysql.connector.Error as err:
        print(f"❌ Error: {err}")
        return None
