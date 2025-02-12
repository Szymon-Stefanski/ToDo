def Show():
    with open("todo_tasks.txt", "r") as file:
        todo = file.read().strip()

    print(todo if todo else "Lista jest pusta.")
    print("\n")


def Add():
    add = input("Please enter your task:").capitalize()

    with open("todo_tasks.txt", "a") as file:
        file.write(add + "\n")

    print(add + " was added to the list." + "\n")
    file.close()


def Modify():
    modify = input("Which task do you want to modify?:").capitalize()

    with open("todo_tasks.txt", "r") as file:
        tasks = file.readlines()

    with open("todo_tasks.txt", "w") as file:
        for task in tasks:
            if task.strip() != modify:
                file.write(task)

    newTodo = input("Please enter a new task:").capitalize()

    with open("todo_tasks.txt", "a") as file:
        file.write(newTodo + "\n")

    print(newTodo + " was added." + "\n")


def Delete():
    delete = input("Which task do you want to delete?: ").capitalize()

    with open("todo_tasks.txt", "r") as file:
        tasks = file.readlines()

    with open("todo_tasks.txt", "w") as file:
        for task in tasks:
            if task.strip() != delete:
                file.write(task)

    print(delete + " was deleted from the list.\n")

def Exit():
    with open("todo_tasks.txt", "w") as file:
        file.write('')