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

        # Work in progress..
        elif answer.startswith("Modify"):

            modify = int(input("Which task do you want to modify?:").capitalize())


            newTodo = input("Please enter a new task:").capitalize()

            print(newTodo + " was added." + "\n")

        # Work in progress..
        elif answer.startswith("Delete"):
            delete = input("Which task do you want to delete?:").capitalize()

            print(delete + " was deleted from the list." + "\n")

        elif answer.startswith("Exit"):
            break

    except ValueError:
        print("Invalid input")

    except IndexError:
        print("Invalid index")