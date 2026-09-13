import json

FILE_NAME = "To-Do-List/tasks.json"

# Load tasks from file
def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

# Add a task
def add_task(tasks):
    task_name = input("Enter task: ")

    task = {
        "task": task_name,
        "completed": False
    }

    tasks.append(task)
    save_tasks(tasks)

    print("Task added successfully!")

# View tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    print("\n===== YOUR TASKS =====")

    for index, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else "✗"
        print(f"{index}. {task['task']} [{status}]")

# Update task
def update_task(tasks):
    view_tasks(tasks)

    if not tasks:
        return

    try:
        number = int(input("Enter task number to update: "))

        if 1 <= number <= len(tasks):
            new_task = input("Enter new task: ")
            tasks[number - 1]["task"] = new_task

            save_tasks(tasks)
            print("Task updated successfully!")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")

# Delete task
def delete_task(tasks):
    view_tasks(tasks)

    if not tasks:
        return

    try:
        number = int(input("Enter task number to delete: "))

        if 1 <= number <= len(tasks):
            deleted_task = tasks.pop(number - 1)

            save_tasks(tasks)
            print(f"Deleted: {deleted_task['task']}")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")

# Main program
tasks = load_tasks()

while True:

    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task(tasks)

    elif choice == "2":
        view_tasks(tasks)

    elif choice == "3":
        update_task(tasks)

    elif choice == "4":
        delete_task(tasks)

    elif choice == "5":
        print("Tasks saved. Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")