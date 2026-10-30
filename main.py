

# Task Manager Application
# This is a simple command-line task manager application that allows users to add, view, mark as completed, delete, and edit tasks. The tasks are stored in a JSON file for persistence.


import json
from pathlib import Path

# Define the path to the JSON file where tasks will be stored

DATA_FILE = Path(__file__).parent / "tasks.json"




def load_tasks():
    """Load saved tasks from the JSON file."""
    if DATA_FILE.exists():          # Check if the file exists
        try:                        
            with DATA_FILE.open("r", encoding="utf-8") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            print("Warning: Could not read saved tasks. Starting with an empty list.")

    return []       # Return an empty list if the file doesn't exist or can't be read

def save_tasks(tasks):      # create a function to save tasks to the JSON file
    """Save tasks to the JSON file."""
    try:                # Open the file in write mode and save the tasks as JSON
        with DATA_FILE.open("w", encoding="utf-8") as file:
            json.dump(tasks, file, indent=4)
    except OSError:             # Handle any errors that occur while trying to save the tasks
        print("Error: Tasks could not be saved.")



def display_tasks(tasks):
    """Display all tasks with their completion status."""
    if not tasks:
        print("No tasks available.")
        return

    print("\nYour Tasks:")

    for number, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{number}. {task['name']} - {status}")

def main():
    tasks = load_tasks()

    print("================================")
    print("          TASK MANAGER")
    print("================================")

# Main loop to display the menu and handle user input

    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Edit Task")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ").strip()

        if choice == "1":
            task_name = input("Enter your task: ").strip()

            if task_name:
                tasks.append({
                    "name": task_name,
                    "completed": False
                })
                save_tasks(tasks)
                print("Task added successfully!")
            else:
                print("Task name cannot be empty.")

        elif choice == "2":
            display_tasks(tasks)

        elif choice == "3":
            if not tasks:
                print("No tasks available to complete.")
                continue

            display_tasks(tasks)

            try:
                task_number = int(
                    input("\nEnter the task number to mark as completed: ")
                )

                if 1 <= task_number <= len(tasks):
                    tasks[task_number - 1]["completed"] = True
                    save_tasks(tasks)
                    print("Task marked as completed!")
                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            if not tasks:
                print("No tasks available to delete.")
                continue

            display_tasks(tasks)

            try:
                task_number = int(
                    input("\nEnter the task number to delete: ")
                )

                if 1 <= task_number <= len(tasks):
                    deleted_task = tasks.pop(task_number - 1)
                    save_tasks(tasks)
                    print(
                        f"Task '{deleted_task['name']}' deleted successfully!"
                    )
                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a valid number.")

        elif choice == "5":
            if not tasks:
                print("No tasks available to edit.")
                continue

            display_tasks(tasks)

            try:
                task_number = int(
                    input("\nEnter the task number to edit: ")
                )

                if 1 <= task_number <= len(tasks):
                    new_name = input("Enter the new task name: ").strip()

                    if new_name:
                        tasks[task_number - 1]["name"] = new_name
                        save_tasks(tasks)
                        print("Task updated successfully!")
                    else:
                        print("Task name cannot be empty.")

                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a valid number.")

        elif choice == "6":
            print("Thank you for using Task Manager!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()

    ## This code implements a simple command-line task manager application. It allows users to add, view, mark as completed, delete, and edit tasks. The tasks are stored in a JSON file for persistence. The application provides a menu-driven interface for user interaction and handles various edge cases such as empty task names and invalid task numbers.