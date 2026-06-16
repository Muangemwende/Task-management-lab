from task_manager.validation import *

tasks = []

def add_task(title, description, due_date):
    if validate_task_title(title) and \
       validate_task_description(description) and \
       validate_due_date(due_date):

        task = {
            "title": title,
            "description": description,
            "due_date": due_date,
            "completed": False
        }

        tasks.append(task)
        print("Task added successfully!")
    else:
        print("Invalid task information.")


def mark_task_as_complete(index, tasks=tasks):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print("Task marked as complete!")
    else:
        print("Invalid task number.")


def view_pending_tasks(tasks=tasks):
    for i, task in enumerate(tasks):
        if not task["completed"]:
            print(i, task)


def calculate_progress(tasks=tasks):
    if len(tasks) == 0:
        return 0

    completed = 0

    for task in tasks:
        if task["completed"]:
            completed += 1

    return (completed / len(tasks)) * 100