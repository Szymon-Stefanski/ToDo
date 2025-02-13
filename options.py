def show():
    with open("todo_tasks.txt", "r") as file:
        todo = file.read().strip()

    print(todo if todo else "Lista jest pusta.")
    print("\n")


def add(answer):
    answer = answer.capitalize()

    with open("todo_tasks.txt", "a") as file:
        file.write(answer + "\n")

    print(answer + " was added to the list." + "\n")
    file.close()


def modify(answer):
    answer = answer.capitalize()

    with open("todo_tasks.txt", "r") as file:
        tasks = file.readlines()

    with open("todo_tasks.txt", "w") as file:
        for task in tasks:
            if task.strip() != answer:
                file.write(task)

    newTodo = input("Please enter a new task:").capitalize()

    with open("todo_tasks.txt", "a") as file:
        file.write(newTodo + "\n")

    print(newTodo + " was added." + "\n")


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
