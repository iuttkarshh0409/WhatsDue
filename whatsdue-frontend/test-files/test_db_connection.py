# test_db_connection.py

from db_config import get_connection

def main():
    connection = get_connection()
    if connection:
        print("✅ Database connection test passed.")
        connection.close()
    else:
        print("❌ Database connection test failed.")

if __name__ == "__main__":
    main()
