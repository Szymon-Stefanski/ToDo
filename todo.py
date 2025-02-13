import options

while True:
    try:
        answer = (input("What do you want to do?: " + "\n"
                        + "Show" + "\n"
                        + "Add" + "\n"
                        + "Modify" + "\n"
                        + "Delete" + "\n"
                        + "Exit" + "\n")).capitalize()

        if answer.startswith("Show"):
            options.show()

        elif answer.startswith("Add"):
            action = input("Please enter your task:")
            options.add(action)

        elif answer.startswith("Modify"):
            action = input("Which task do you want to modify?:")
            options.modify(action)

        elif answer.startswith("Delete"):
            action = input("Which task do you want to delete?: ")
            options.delete(action)

        elif answer.startswith("Exit"):
            options.exit()
            break

    except ValueError:
        print("Invalid input")

    except IndexError:
        print("Invalid index")