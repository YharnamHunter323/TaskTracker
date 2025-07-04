import argparse
import json
import os
from datetime import datetime

def load_tasks():
    if not os.path.exists("tasks.json"):
        return []
    with open("tasks.json", "r") as f:
        return json.load(f)
    
def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=2)

def create_task(description):
    return {
        "id": int(datetime.now().timestamp()),
        "description": description,
        "status": "todo",
        "createdAt":datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat()
    }

def update_task(tasks, task_id, new_description):

    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            task["updatedAt"] = datetime.now().isoformat()
            return True

    return False

def delete_task(tasks, task_id):
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            del tasks[i]
            return True
    return False

def mark_task(tasks, task_id, status):
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            task["updatedAt"] = datetime.now().isoformat()
            return True
    return False

def filter_tasks(tasks, status=None):
    if status:
        return [task for task in tasks if task["status"] == status]
    else:
        return tasks


def main():
    parser = argparse.ArgumentParser(description="Task Tracker CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", help="Description of the task")

    # Update command
    update_parser = subparsers.add_parser("update", help="Update a task")
    update_parser.add_argument("id", type=int, help="ID of the task to update")
    update_parser.add_argument("description", help="New description of the task")

    # Delete command
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("id", type=int, help="ID of the task to delete")

    # Mark commands
    mark_parser = subparsers.add_parser("mark", help="Mark a task as in-progress or done")
    mark_parser.add_argument("status", choices=["in-progress", "done"], help="Status to mark the task")
    mark_parser.add_argument("id", type=int, help="ID of the task to mark")

    # List commands
    list_parser = subparsers.add_parser("list", help="List tasks")
    list_parser.add_argument("status", nargs="?", choices=["todo", "in-progress", "done"], help="Filter tasks by status")

    args = parser.parse_args()

    if args.command == "add":
        tasks = load_tasks()
        task = create_task(args.description)
        tasks.append(task)
        save_tasks(tasks)
        print(f"Task added successfully (ID: {task['id']})")
    elif args.command == "update":
        tasks = load_tasks()
        if update_task(tasks, args.id, args.description):
            save_tasks(tasks)
            print(f"Task {args.id} updated successfully")
        else:
            print(f"Task {args.id} not found") 
    elif args.command == "delete":
        tasks = load_tasks()
        if delete_task(tasks, args.id):
            save_tasks(tasks)
            print(f"Task {args.id} deleted successfully")
        else:
            print(f"Task {args.id} not found")
    elif args.command == "mark":
        tasks = load_tasks()
        if mark_task(tasks, args.id, args.status):
            save_tasks(tasks)
            print(f"Task {args.id} marked as {args.status}")
        else:
            print(f"Task {args.id} not found")
    elif args.command == "list":
            tasks = load_tasks()
            filtered_tasks = filter_tasks(tasks, args.status)
            for task in filtered_tasks:
                print(f"{task['id']}: {task['description']} ({task['status']})")
    else:
        print(args)



if __name__ == "__main__":
    main()