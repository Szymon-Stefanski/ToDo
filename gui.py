import options
import FreeSimpleGUI


FreeSimpleGUI.theme("Reddit")

label = FreeSimpleGUI.Text("What do you want to do?")
input_box = FreeSimpleGUI.InputText(key="task_input")
list_box = FreeSimpleGUI.Listbox(values=options.show(), key="todos", enable_events=True, size=(45, 15))

add_button = FreeSimpleGUI.Button("Add", size=10)
modify_button = FreeSimpleGUI.Button("Modify", size=10)
delete_button = FreeSimpleGUI.Button("Delete", size=10)
exit_button = FreeSimpleGUI.Button("Exit", size=10)


window = FreeSimpleGUI.Window(
    "To-Do List",
    layout=[[label], [input_box], [list_box], [add_button, modify_button, delete_button, exit_button]],
    font=("Arial", 12),
)

while True:
    event, values = window.read()

    match event:
        case FreeSimpleGUI.WINDOW_CLOSED | "Exit":
            options.exit_program()
            break

        case "Add":
            task = values["task_input"].strip()
            if task:
                options.add(task)
                window["todos"].update(values=options.show())
                window["task_input"].update("")
            else:
                FreeSimpleGUI.popup("Input box is empty! Insert name of an item to add!", font=("Arial",12))

        case "Modify":
            selected_task = values["todos"]
            if selected_task:
                new_task = FreeSimpleGUI.popup_get_text("Modify task:", default_text=selected_task[0])
                if new_task:
                    options.modify(selected_task[0], new_task)
                    window["todos"].update(values=options.show())
            else:
                FreeSimpleGUI.popup("Please select an item to modify first!", font=("Arial",12))

        case "Delete":
            selected_task = values["todos"]
            if selected_task:
                options.delete(selected_task[0])
                window["todos"].update(values=options.show())
            else:
                FreeSimpleGUI.popup("Please select an item to delete first!", font=("Arial",12))

window.close()
