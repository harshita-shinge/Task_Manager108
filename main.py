

# Task Manager Application


import json
from pathlib import Path

# Define the path to the JSON file for storing tasks

DATA_FILE = Path(__file__).parent / "tasks.json"


def load_tasks():
    """Load saved tasks from the JSON file."""
    if DATA_FILE.exists():      # Check if the file exists
        try:                    # Try to read the file and load the tasks 
            with DATA_FILE.open("r", encoding="utf-8") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            print("Warning: Could not read saved tasks. Starting with an empty list.")

    return []       # Return an empty list if the file doesn't exist or if there's an error reading it


def save_tasks(tasks):          
    """Save tasks to the JSON file."""
    try:            # Try to write the tasks to the file
        with DATA_FILE.open("w", encoding="utf-8") as file:
            json.dump(tasks, file, indent=4)
    except OSError:         # Handle any errors that occur while writing to the file
        print("Error: Tasks could not be saved.")
    

def display_tasks(tasks):
    """Display all tasks with their completion status."""
    if not tasks:       # Check if there are no tasks to display
        print("No tasks available.")
        return

    print("\nYour Tasks:")

    for number, task in enumerate(tasks, start=1):  # Enumerate through the tasks and display each task with its number and completion status
        status = "Completed" if task["completed"] else "Pending"
        print(f"{number}. {task['name']} - {status}")


def main():         # Main function to run the task manager application
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
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":   # Handle adding a new task
            task_name = input("Enter your task: ").strip()

            if task_name: # Check if the task name is not empty
                tasks.append({
                    "name": task_name,
                    "completed": False
                })
                save_tasks(tasks)
                print("Task added successfully!")
            else:   # If the task name is empty, display an error message
                print("Task name cannot be empty.")

        elif choice == "2":
            display_tasks(tasks)

        elif choice == "3":
            if not tasks:   # Check if there are no tasks to mark as completed
                print("No tasks available to complete.")
                continue

            display_tasks(tasks)

            try:    # Prompt the user to enter the task number to mark as completed and validate the input
                task_number = int(
                    input("\nEnter the task number to mark as completed: ")
                )

                if 1 <= task_number <= len(tasks):  # Check if the task number is valid
                    tasks[task_number - 1]["completed"] = True
                    save_tasks(tasks)
                    print("Task marked as completed!")
                else:       # If the task number is invalid, display an error message
                    print("Invalid task number.")

            except ValueError:      # Handle the case where the user input is not a valid integer
                print("Please enter a valid number.")

        elif choice == "4":     # Handle deleting a task
            if not tasks:
                print("No tasks available to delete.")
                continue

            display_tasks(tasks)

            try:        # Prompt the user to enter the task number to delete and validate the input
                task_number = int(input("\nEnter the task number to delete: "))

                if 1 <= task_number <= len(tasks):
                    deleted_task = tasks.pop(task_number - 1)
                    save_tasks(tasks)
                    print(f"Task '{deleted_task['name']}' deleted successfully!")
                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a valid number.")

        elif choice == "5":     # Handle exiting the application
            print("Thank you for using Task Manager!")
            break

        else:       # Handle invalid menu choices
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":      # Check if the script is being run directly (not imported as a module) and call the main function to start the application
    main()

