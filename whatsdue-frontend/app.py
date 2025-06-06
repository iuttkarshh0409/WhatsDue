import sys
import os
from datetime import datetime, timedelta
from flask import Flask, render_template, request, redirect, url_for, flash
import subprocess
import threading  # <--- For async reminder call

# Add backend folder to system path
backend_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../whatsdue-backend'))
if backend_path not in sys.path:
    sys.path.append(backend_path)

from db_config import get_connection

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.template_filter('is_upcoming')
def is_upcoming_filter(due_datetime_str):
    try:
        due_datetime = datetime.strptime(due_datetime_str, '%Y-%m-%d %H:%M')
        now = datetime.now()
        return now <= due_datetime <= now + timedelta(hours=24)
    except ValueError:
        return False

@app.route('/')
def index():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT id, title, description, DATE_FORMAT(due_datetime, '%Y-%m-%d %H:%i') AS due_datetime, reminder_sent
        FROM tasks
        ORDER BY due_datetime ASC
    """)
    tasks = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', tasks=tasks)

def run_reminder_async():
    script_path = os.path.join(backend_path, 'run_reminders.py')
    # Running synchronously here but inside a thread so it doesn't block Flask request
    result = subprocess.run(['python', script_path], capture_output=True, text=True)
    print("=== Reminder Script STDOUT ===")
    print(result.stdout)
    print("=== Reminder Script STDERR ===")
    print(result.stderr)

@app.route('/add-task', methods=['POST'])
def add_task():
    title = request.form.get('title')
    description = request.form.get('description')
    due_datetime = request.form.get('due_datetime')  # e.g. '2025-06-07T10:30'

    if not title or not due_datetime:
        flash('Title and Due Date/Time are required.', 'error')
        return redirect(url_for('index'))

    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tasks (title, description, due_datetime, reminder_sent) VALUES (%s, %s, %s, FALSE)",
            (title, description, due_datetime)
        )
        conn.commit()
        cursor.close()
        conn.close()

        # Convert due_datetime string to datetime object
        due_dt_obj = datetime.strptime(due_datetime, '%Y-%m-%dT%H:%M')
        now = datetime.now()

        # If task due within next 24 hours, run reminder script asynchronously
        if now <= due_dt_obj <= now + timedelta(hours=24):
            threading.Thread(target=run_reminder_async, daemon=True).start()

        flash('✅ Task added successfully!', 'success')
    except Exception as e:
        flash(f'❌ Error adding task: {e}', 'error')

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
