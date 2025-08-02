import json
import os
import sys
def write_to_json(tasks_dict):
    with open("tasks.json","w") as f:
           json.dump(tasks_dict,f,indent=4)

def help():
    print("add [task text] - adds a new task")
    print("upd [task ID]['desc'/'status'][new text/status] - updates a task")
    print("dlt [task ID] - deletes a task")
    print("lists - list all tasks")
    print("listdone - list all completed tasks")
    print("listnotdone - list all uncompleted tasks")
    print("listprog - list all tasks in progress")
    print("end - exits the program")
    
def add(tasks_dict,addition):
    new_task = {
        "text": addition,
        "status": "not done"
        }
    new_id = str(int(max(tasks_dict.keys(), default="0")) + 1)
    tasks_dict[new_id] = new_task

def upd(tasks_dict, task_id, choice, new_value):
    if task_id in tasks_dict:
        if choice == "desc":
            new_text = new_value
            tasks_dict[task_id]["text"] = new_text
        elif choice == "status":
            new_status = new_value.strip().lower()
            if new_status in ["not done", "in progress", "done"]:
                tasks_dict[task_id]["status"] = new_status
            else:
                print("Invalid status entered.")
        else:
            print("Invalid choice.")
    else:
        print("Task ID not found.")

def dlt(tasks_dict,task_id):
    if task_id in tasks_dict:
        tasks_dict.pop(task_id)
    else:
        print("Task ID not found.")

def lists(tasks_dict):
    for task_id, task_data in tasks_dict.items():
        print(f"[{task_id}] {task_data['text']} - {task_data['status']}")
    
def list_tasks_by_status(tasks_dict, wanted_value):
    tasks_status = {}
    for task_id, task_data in tasks_dict.items():
        if task_data["status"] == wanted_value:
            tasks_status[task_id] = task_data
    lists(tasks_status)    
    
    
    
if os.path.exists("tasks.json"):
    with open("tasks.json", "r") as f:
        tasks_dict = json.load(f)
else:
    tasks_dict = {}

if len(sys.argv) < 2:
    print("No command provided. Use 'help' for options.")
    sys.exit()
    
command = sys.argv[1].lower() if len(sys.argv) > 1 else ""

if command == "help":
    help()
    
elif command == "add":
    if len(sys.argv) < 3:
        print("Error: missing task description.")
    else:
        addition = " ".join(sys.argv[2:])
        add(tasks_dict, addition)
        write_to_json(tasks_dict)

elif command == "upd":
    if len(sys.argv) < 5:
        print("Usage: upd [task ID] ['desc'/'status'] [new value]")
    else:
        upd(tasks_dict, sys.argv[2], sys.argv[3], " ".join(sys.argv[4:]))
        write_to_json(tasks_dict)

elif command == "dlt":
    if len(sys.argv) < 3:
        print("Error: missing task ID.")
    else:
        dlt(tasks_dict, sys.argv[2])
        write_to_json(tasks_dict)
    
elif command == "lists":
    lists(tasks_dict)
    
elif command == "listdone":
    list_tasks_by_status(tasks_dict,"done")
    
elif command == "listnotdone":
    list_tasks_by_status(tasks_dict,"not done")
    
elif command == "listprog":
    list_tasks_by_status(tasks_dict,"in progress")
    
else:
    print(f"{command} is not a command")