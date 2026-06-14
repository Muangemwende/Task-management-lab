from datetime import datetime
from task_manager.validation import validate_task_title, validate_task_description, validate_due_date

tasks = []

def add_task(title, description, due_date):
    valid, msg = validate_task_title(title)
    if not valid:
        print(f"Invalid title: {msg}")
        return False
    valid, msg = validate_task_description(description)
    if not valid:
        print(f"Invalid description: {msg}")
        return False
    valid, msg = validate_due_date(due_date)
    if not valid:
        print(f"Invalid due date: {msg}")
        return False
    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }
    tasks.append(task)
    print("Task added successfully!")

def mark_task_as_complete(index, tasks=tasks):
    if index < 0 or index >= len(tasks):
        print("Invalid task index.")
        return False
    tasks[index]["completed"] = True
    print("Task marked as complete!")

def view_pending_tasks(tasks=tasks):
    pending = [t for t in tasks if not t["completed"]]
    if not pending:
        print("No pending tasks.")
    else:
        for i, task in enumerate(pending):
            print(f"{i + 1}. {task['title']} - {task['description']} (Due: {task['due_date']})")

def calculate_progress(tasks=tasks):
    if len(tasks) == 0:
        print("No tasks currently.")
        progress = 0
    else:
        completed = sum(1 for t in tasks if t["completed"])
        progress = (completed / len(tasks)) * 100
        print(f"Progress: {completed}/{len(tasks)} tasks completed ({progress:.1f}%)")
    return progress