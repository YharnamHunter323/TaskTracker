# Task Tracker CLI

A simple command-line task manager that helps you track todo, in-progress, and done tasks.

https://roadmap.sh/projects/task-tracker

## Features

- Add, update, and delete tasks
- Mark tasks as todo/in-progress/done
- Filter tasks by status
- Persistent storage in JSON format

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/YharnamHunter323/TaskTracker
   cd TaskTracker
   ```
2. Ensure Python 3.x is installed

## Usage

# Add a task

python TaskTracker.py add "Buy groceries"

# Update a task

python TaskTracker.py update 1 "Buy groceries and cook dinner"

# Mark a task

python TaskTracker.py mark done 1

# List tasks

python TaskTracker.py list
python TaskTracker.py list done
python TaskTracker.py list in-progress

# Delete a task

python TaskTracker.py delete 1
