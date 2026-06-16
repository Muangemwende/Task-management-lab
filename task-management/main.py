from task_manager.task_utils import *

def main():

    while True:

        print("\nTask Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":

            title = input("Title: ")
            description = input("Description: ")
            due_date = input("Due Date (YYYY-MM-DD): ")

            add_task(title, description, due_date)

        elif choice == "2":

            index = int(input("Task number: "))
            mark_task_as_complete(index)

        elif choice == "3":

            view_pending_tasks()

        elif choice == "4":

            print("Progress:", calculate_progress(), "%")

        elif choice == "5":

            break

        else:

            print("Invalid choice")


if __name__ == "__main__":
    main()