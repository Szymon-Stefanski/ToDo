import options
import FreeSimpleGUI


label = FreeSimpleGUI.Text("What do you want to do?")
input_box = FreeSimpleGUI.InputText(key="task_input")
list_box = FreeSimpleGUI.Listbox(values=options.show(), key="todos", enable_events=True, size=(45, 15))

add_button = FreeSimpleGUI.Button("Add")
modify_button = FreeSimpleGUI.Button("Modify")
delete_button = FreeSimpleGUI.Button("Delete")
exit_button = FreeSimpleGUI.Button("Exit")


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
                FreeSimpleGUI.popup("Input box is empty! Insert name of an item to add!")

        case "Modify":
            selected_task = values["todos"]
            if selected_task:
                new_task = FreeSimpleGUI.popup_get_text("Modify task:", default_text=selected_task[0])
                if new_task:
                    options.modify(selected_task[0], new_task)
                    window["todos"].update(values=options.show())
            else:
                FreeSimpleGUI.popup("Please select an item to modify first!")

        case "Delete":
            selected_task = values["todos"]
            if selected_task:
                options.delete(selected_task[0])
                window["todos"].update(values=options.show())
            else:
                FreeSimpleGUI.popup("Please select an item to delete first!")

window.close()
