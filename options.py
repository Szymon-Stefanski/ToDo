TODO_FILE = "todo_tasks.txt"

def show():
    try:
        with open(TODO_FILE, "r") as file:
            return [task.strip() for task in file.readlines()]
    except FileNotFoundError:
        return []

def add(task):
    task = task.capitalize()
    tasks = show()

    if task not in tasks:
        with open(TODO_FILE, "a") as file:
            file.write(task + "\n")
        print(f"{task} was added to the list.\n")
    else:
        print(f"WARNING!: {task} is already in the list.\n")

def modify(old_task, new_task):
    old_task, new_task = old_task.capitalize(), new_task.capitalize()
    tasks = show()

    with open(TODO_FILE, "w") as file:
        for task in tasks:
            file.write(new_task + "\n" if task == old_task else task + "\n")

    print(f"{old_task} was modified to {new_task}.\n")

def delete(task):
    task = task.capitalize()
    tasks = show()

    with open(TODO_FILE, "w") as file:
        for t in tasks:
            if t != task:
                file.write(t + "\n")

    print(f"{task} was deleted from the list.\n")

def exit_program():
    print("Exiting program...")
