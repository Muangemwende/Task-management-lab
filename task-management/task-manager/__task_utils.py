"""
task_utils.py - Utility functions for the Task Management System.
"""

from task_manager.validation import validate_task_name, validate_task_index


def add_task(tasks, title, description, due_date):
    """
    Add a new task to the tasks list.
    Each task is stored as a dictionary with title, description, due_date, completed.
    Returns the updated tasks list.
    """
    try:
        validate_task_name(title)
    except ValueError as e:
        print(f"Error: {e}")
        return tasks

    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }
    tasks.append(task)
    print("Task added successfully!")
    return tasks


def mark_task_complete(tasks, task_index):
    """
    Mark a task as complete by its index (0-based).
    Returns the updated tasks list.
    """
    try:
        if not validate_task_index(task_index, tasks):
            return tasks
    except ValueError as e:
        print(f"Error: {e}")
        return tasks

    if tasks[task_index]["completed"]:
        print("Task is already marked as complete.")
    else:
        tasks[task_index]["completed"] = True
        print("Task marked as complete!")
    return tasks


def view_pending_tasks(tasks):
    """
    Display all pending (incomplete) tasks.
    """
    pending = [task for task in tasks if not task["completed"]]

    if len(pending) == 0:
        print("No pending tasks.")
        return

    print("\n--- Pending Tasks ---")
    for i, task in enumerate(tasks):
        if not task["completed"]:
            print(f"{i + 1}. {task['title']} (Due: {task['due_date']}) - {task['description']}")
    print("---------------------")


def calculate_progress(tasks):
    """
    Calculate and return the percentage of completed tasks as a float.
    Prints 'No working currently.' if no tasks exist.
    """
    if len(tasks) == 0:
        print("No working currently.")
        return 0.0

    completed = sum(1 for task in tasks if task["completed"])
    total = len(tasks)
    percentage = (completed / total) * 100
    return percentage


def track_progress(tasks):
    """
    Display overall progress of tasks.
    """
    if len(tasks) == 0:
        print("No working currently.")
        return

    total = len(tasks)
    completed = sum(1 for task in tasks if task["completed"])
    pending = total - completed
    percentage = (completed / total) * 100

    print("\n--- Progress Report ---")
    print(f"Total Tasks   : {total}")
    print(f"Completed     : {completed}")
    print(f"Pending       : {pending}")
    print(f"Progress      : {percentage:.1f}%")
    print("-----------------------")