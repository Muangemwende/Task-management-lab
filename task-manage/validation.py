from datetime import datetime

def validate_task_title(title):
    if not title or len(title) == 0:
        return False, "Title cannot be empty."
    if len(title) < 3:
        return False, "Title must be at least 3 characters."
    return True, ""

def validate_task_description(description):
    if not description or len(description) == 0:
        return False, "Description cannot be empty."
    if len(description) < 5:
        return False, "Description must be at least 5 characters."
    return True, ""

def validate_due_date(due_date):
    if not due_date or len(due_date) == 0:
        return False, "Due date cannot be empty."
    try: