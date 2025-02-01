todos = []

while True:
    try:
        answer = (input("What do you want to do?: " + "\n"
                        + "Show" + "\n"
                        + "Add" + "\n"
                        + "Modify" + "\n"
                        + "Delete" + "\n"
                        + "Exit" + "\n")).capitalize()

        if answer.startswith("Show"):
            for todo in todos:
                print(todo)

            print("\n")

        elif answer.startswith("Add"):
            add = input("Please enter your task:").capitalize()
            todos.append(add)
            print(add + " was added to the list." + "\n")

        elif answer.startswith("Modify"):
            for index, todo in enumerate(todos):
                print(index + 1, "-", todo)
            modify = int(input("Which task do you want to modify?:").capitalize())
            todos.pop(modify)

            newTodo = input("Please enter a new task:").capitalize()
            todos.insert(modify, newTodo)
            print(newTodo + " was added." + "\n")

        elif answer.startswith("Delete"):
            delete = input("Which task do you want to delete?:").capitalize()
            todos.remove(delete)
            print(delete + " was deleted from the list." + "\n")

        elif answer.startswith("Exit"):
            break

    except ValueError:
        print("Invalid input")

    except IndexError:
        print("Invalid index")