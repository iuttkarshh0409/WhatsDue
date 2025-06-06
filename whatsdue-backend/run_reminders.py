import datetime
from db_config import get_connection
from whatsapp_bot import send_whatsapp_message  # Your Twilio send function

def fetch_upcoming_tasks():
    """
    Fetch tasks with due_datetime within the next 24 hours and no reminder sent yet.
    """
    conn = get_connection()
    if not conn:
        print("❌ DB connection failed")
        return []

    cursor = conn.cursor(dictionary=True)
    now = datetime.datetime.now()
    next_24h = now + datetime.timedelta(hours=24)

    query = """
        SELECT id, title, due_datetime
        FROM tasks
        WHERE due_datetime BETWEEN %s AND %s
        AND reminder_sent = FALSE
    """

    cursor.execute(query, (now, next_24h))
    tasks = cursor.fetchall()
    cursor.close()
    conn.close()
    return tasks

def mark_reminder_sent(task_id):
    """
    Mark a task as reminder sent in the database.
    """
    conn = get_connection()
    if not conn:
        print("❌ DB connection failed while updating")
        return

    cursor = conn.cursor()
    query = "UPDATE tasks SET reminder_sent = TRUE WHERE id = %s"
    cursor.execute(query, (task_id,))
    conn.commit()
    cursor.close()
    conn.close()

def build_message(task):
    """
    Build a WhatsApp reminder message for the task.
    """
    due_str = task['due_datetime'].strftime("%Y-%m-%d %H:%M")
    return f"⏰ Reminder: Your assignment '{task['title']}' is due by {due_str}. Stay on track!"

def run_reminders():
    tasks = fetch_upcoming_tasks()
    if not tasks:
        print("📭 No upcoming tasks within 24 hours.")
        return

    for task in tasks:
        message = build_message(task)
        success, sid = send_whatsapp_message(message)
        if success:
            print(f"✅ Reminder sent for task ID {task['id']}. Message SID: {sid}")
            mark_reminder_sent(task['id'])
        else:
            print(f"❌ Failed to send reminder for task ID {task['id']}.")

if __name__ == "__main__":
    run_reminders()
