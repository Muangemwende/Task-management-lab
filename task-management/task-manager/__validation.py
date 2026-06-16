from datetime import datetime

def validate_task_title(title):
    return title.strip() != ""

def validate_task_description(description):
    return description.strip() != ""

def validate_due_date(due_date):
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True
    except ValueError:
        return False