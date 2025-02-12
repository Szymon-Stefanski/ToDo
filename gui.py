import FreeSimpleGUI

label = FreeSimpleGUI.Text("What you want to do?")
input_box = FreeSimpleGUI.InputText()
add_button = FreeSimpleGUI.Button("Add")

window = FreeSimpleGUI.Window('To_do', layout=[[label], [input_box], [add_button]])
window.read()
window.close()
