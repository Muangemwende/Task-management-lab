"""
main.py - Main script for the Task Management System.
Provides a menu-based interface for managing tasks.
"""

from task_manager.task_utils import (
    add_task,
    mark_task_complete,
    view_pending_tasks,
    track_progress,
    calculate_progress
)


def display_menu():
    """Display the main menu options."""
    print("\n===== Task Management System =====")
    print("1. Add Task")
    print("2. Mark Task as Complete")
    print("3. View Pending Tasks")
    print("4. Track Progress")
    print("5. Exit")
    print("==================================")


def main():
    """Main function to run the task management system."""
    tasks = []

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            title = input("Enter task name: ").strip()
            description = input("Enter task description: ").strip()
            due_date = input("Enter due date (YYYY-MM-DD): ").strip()
            tasks = add_task(tasks, title, description, due_date)

        elif choice == "2":
            view_pending_tasks(tasks)
            if len(tasks) > 0:
                try:
                    task_num = int(input("Enter task number to mark as complete: ").strip())
                    tasks = mark_task_complete(tasks, task_num - 1)
                except ValueError:
                    print("Error: Please enter a valid number.")

        elif choice == "3":
            view_pending_tasks(tasks)

        elif choice == "4":
            track_progress(tasks)

        elif choice == "5":
            print("Goodbye! Stay productive!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()