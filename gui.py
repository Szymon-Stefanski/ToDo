import FreeSimpleGUI

label = FreeSimpleGUI.Text("What you want to do?")
input_box = FreeSimpleGUI.InputText()

show_button = FreeSimpleGUI.Button("Show")
add_button = FreeSimpleGUI.Button("Add")
modify_button = FreeSimpleGUI.Button("Modify")
delete_button = FreeSimpleGUI.Button("Delete")
exit_button = FreeSimpleGUI.Button("Exit")

window = FreeSimpleGUI.Window('To_do',
                              layout=[[label], [input_box],
                                      [show_button],
                                      [add_button],
                                      [modify_button],
                                      [delete_button],
                                      [exit_button]],
                              font=('Arial', 12))
while True:
    event, values = window.read()
    print(event)
    print(values)
    '''match event:
        case "Show":

        case "Add":

        case "Modify":

        case "Delete":

        case "Exit":
        '''
