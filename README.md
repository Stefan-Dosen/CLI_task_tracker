# CLI Task Tracker

This is a simple command-line task tracker written in Python. It allows you to add, update, delete, and list tasks, each with a status (`not done`, `in progress`, or `done`). Tasks are stored in a local `tasks.json` file.

This was a project excersise on: https://roadmap.sh/projects/task-tracker

## Features

- Add new tasks
- Update task descriptions or status
- Delete tasks
- List all tasks
- List tasks filtered by status

## Commands

add [task text]                                 - adds a new task
upd [task ID]['desc'/'status'][new text/status] - updates a task
dlt [task ID]                                   - deletes a task
lists                                           - list all tasks
listdone                                        - list all completed tasks
listnotdone                                     - list all uncompleted tasks
listprog                                        - list all tasks in progress

## Usage

Run the script from the command line with:

```bash
python CLI_task_tracker.py [command] [arguments...]

