def show():
    with open("todo_tasks.txt", "r") as file:
        todo = file.read().strip()

    print(todo if todo else "Lista jest pusta.")
    print("\n")


def add(answer):
    answer = answer.capitalize()

    with open("todo_tasks.txt", "r") as file:
        tasks = [task.strip() for task in file.readlines()]

    if answer not in tasks:
        with open("todo_tasks.txt", "a") as file:
            file.write(answer + "\n")
        print(answer + " was added to the list." + "\n")
    else:
        print("WARNING!: " + answer + " is already in the list." + "\n")


def modify(answer):
    answer = answer.capitalize()

    with open("todo_tasks.txt", "r") as file:
        tasks = file.readlines()

    with open("todo_tasks.txt", "w") as file:
        for task in tasks:
            if task.strip() != answer:
                file.write(task)

    new_todo = input("Please enter a new task:").capitalize()

    with open("todo_tasks.txt", "a") as file:
        file.write(new_todo + "\n")

    print(new_todo + " was added." + "\n")


def delete(answer):
    answer = answer.capitalize()

    with open("todo_tasks.txt", "r") as file:
        tasks = file.readlines()

    with open("todo_tasks.txt", "w") as file:
        for task in tasks:
            if task.strip() != answer:
                file.write(task)
            print(answer + " was deleted from the list.\n")


def exit():
    with open("todo_tasks.txt", "w") as file:
        file.write('')
