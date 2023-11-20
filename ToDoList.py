import json
import os
from datetime import datetime


tasks = []


def add_task():
    task_name = input("Enter the task name: ")
    priority = input("Enter the priority (High/Medium/Low): ").capitalize()
    due_date = input("Enter due date (YYYY-MM-DD): ")
    
    try:
        due_date = datetime.strptime(due_date, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD format.")
        return

    task = {
        "name": task_name,
        "priority": priority,
        "due_date": due_date.strftime("%Y-%m-%d"),
        "completed": False,
    }
    
    tasks.append(task)
    print("Task added!")


def show_tasks():
    if not tasks:
        print("No tasks to display.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, 1):
            status = "✓" if task["completed"] else " "
            print(f"{i}. [{status}] {task['name']} (Priority: {task['priority']}, Due Date: {task['due_date']})")


def complete_task():
    show_tasks()
    if tasks:
        try:
            index = int(input("Enter the task number to mark as completed: ")) - 1
            if 0 <= index < len(tasks):
                tasks[index]["completed"] = True
                print(f"Task '{tasks[index]['name']}' marked as completed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a valid task number.")


def remove_task():
    show_tasks()
    if tasks:
        try:
            index = int(input("Enter the task number to remove: ")) - 1
            if 0 <= index < len(tasks):
                removed_task = tasks.pop(index)
                print(f"Removed task: {removed_task['name']}")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a valid task number.")


def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)
    print("Tasks saved to 'tasks.json'.")


def load_tasks():
    global tasks
    if os.path.isfile("tasks.json"):
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
        print("Tasks loaded from 'tasks.json'.")
    else:
        print("No saved tasks found.")


load_tasks()  

while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. Show tasks")
    print("3. Mark task as completed")
    print("4. Remove a task")
    print("5. Save tasks")
    print("6. Quit")
    
    choice = input("Enter your choice (1/2/3/4/5/6): ")
    
    if choice == '1':
        add_task()
    elif choice == '2':
        show_tasks()
    elif choice == '3':
        complete_task()
    elif choice == '4':
        remove_task()
    elif choice == '5':
        save_tasks()
    elif choice == '6':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
