from task_manager import get_upcoming_tasks

tasks = get_upcoming_tasks()

if not tasks:
    print("📭 No upcoming tasks within 24 hours.")
else:
    print("📌 Upcoming Tasks:")
    for task in tasks:
        print(f"- {task['title']} (Due: {task['due_datetime']})")
