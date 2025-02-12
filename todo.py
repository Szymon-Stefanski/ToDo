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
            options.Show()

        elif answer.startswith("Add"):
            options.Add()

        elif answer.startswith("Modify"):
            options.Modify()

        elif answer.startswith("Delete"):
            options.Delete()

        elif answer.startswith("Exit"):
            options.Exit()
            break

    except ValueError:
        print("Invalid input")

    except IndexError:
        print("Invalid index")