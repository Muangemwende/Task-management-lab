"""
main.py - Entry point for the Task Management System.
"""

from task_manager.task_utils import (
    add_task,
    mark_task_complete,
    view_pending_tasks,
    calculate_progress,
    track_progress,
)

tasks = []


def display_menu():
    print("\n--- Task Manager ---")
    print("1. Add task")
    print("2. Mark task as complete")
    print("3. View pending tasks")
    print("4. Track progress")
    print("5. Exit")
    print("--------------------")


def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            title = input("Enter task title: ").strip()
            description = input("Enter task description: ").strip()
            due_date = input("Enter due date (YYYY-MM-DD): ").strip()
            add_task(tasks, title, description, due_date)

        elif choice == "2":
            view_pending_tasks(tasks)
            if tasks:
                try:
                    task_number = int(input("Enter task number to mark as complete: ").strip())
                    mark_task_complete(tasks, task_number - 1)
                except ValueError:
                    print("Error: Please enter a valid number.")

        elif choice == "3":
            view_pending_tasks(tasks)

        elif choice == "4":
            track_progress(tasks)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()