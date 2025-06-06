# task_manager.py

from db_config import get_connection
from datetime import datetime

def add_task(title, description, due_datetime_str):
    """
    Add a new task to the database.
    due_datetime_str should be in 'YYYY-MM-DD HH:MM' format.
    """
    try:
        due_datetime = datetime.strptime(due_datetime_str, "%Y-%m-%d %H:%M")
    except ValueError:
        print("❌ Error: Incorrect datetime format. Use 'YYYY-MM-DD HH:MM'")
        return

    conn = get_connection()
    if conn is None:
        print("❌ Could not connect to DB.")
        return

    try:
        cursor = conn.cursor()
        sql = "INSERT INTO tasks (title, description, due_datetime) VALUES (%s, %s, %s)"
        cursor.execute(sql, (title, description, due_datetime))
        conn.commit()
        print("✅ Task added successfully!")
    except Exception as e:
        print("❌ DB Error:", e)
    finally:
        conn.close()

from datetime import datetime, timedelta

def get_upcoming_tasks():
    """
    Fetch all tasks due within the next 24 hours.
    """
    conn = get_connection()
    if conn is None:
        print("❌ Could not connect to DB.")
        return []

    try:
        cursor = conn.cursor(dictionary=True)
        now = datetime.now()
        next_24 = now + timedelta(hours=24)

        query = """
        SELECT id, title, description, due_datetime 
        FROM tasks 
        WHERE due_datetime BETWEEN %s AND %s
        ORDER BY due_datetime ASC
        """
        cursor.execute(query, (now, next_24))
        tasks = cursor.fetchall()
        return tasks

    except Exception as e:
        print("❌ DB Error:", e)
        return []
    finally:
        conn.close()
