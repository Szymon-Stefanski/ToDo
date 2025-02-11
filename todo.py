while True:
    try:
        answer = (input("What do you want to do?: " + "\n"
                        + "Show" + "\n"
                        + "Add" + "\n"
                        + "Modify" + "\n"
                        + "Delete" + "\n"
                        + "Exit" + "\n")).capitalize()

        if answer.startswith("Show"):
            with open("todo_tasks.txt", "r") as file:
                todo = file.read().strip()

            print(todo if todo else "Lista jest pusta.")
            print("\n")

        elif answer.startswith("Add"):
            add = input("Please enter your task:").capitalize()

            with open("todo_tasks.txt", "a") as file:
                file.write(add + "\n")

            print(add + " was added to the list." + "\n")
            file.close()

        elif answer.startswith("Modify"):
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

        elif answer.startswith("Delete"):
            delete = input("Which task do you want to delete?: ").capitalize()

            with open("todo_tasks.txt", "r") as file:
                tasks = file.readlines()

            with open("todo_tasks.txt", "w") as file:
                for task in tasks:
                    if task.strip() != delete:
                        file.write(task)

            print(delete + " was deleted from the list.\n")

        elif answer.startswith("Exit"):
            break

    except ValueError:
        print("Invalid input")

    except IndexError:
        print("Invalid index")