"""
validation.py - Input validation functions for the Task Management System.
"""


def validate_task_name(task_name):
    """
    Validate the task name input.
    Returns True if valid, raises ValueError otherwise.
    """
    if len(task_name) == 0:
        raise ValueError("Task name cannot be empty.")
    if len(task_name) > 100:
        raise ValueError("Task name cannot exceed 100 characters.")
    return True


def validate_task_index(index, tasks):
    """
    Validate that the task index is within range.
    Returns True if valid, False if no tasks, raises ValueError if out of range.
    """
    if len(tasks) == 0:
        print("No working currently.")
        return False
    if index < 0 or index >= len(tasks):
        raise ValueError(f"Invalid task number. Please enter a number between 1 and {len(tasks)}.")
    return True