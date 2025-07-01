import argparse

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
    print(args)

if __name__ == "__main__":
    main()