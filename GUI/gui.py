import PySimpleGUI as sg
from modules import features


layout = [
    [sg.Text("Enter to do item",background_color="black",border_width=2,justification='center')],
    [sg.Input(key='INPUT'), sg.Button("Add")]
]
sg.theme('gray gray gray')
window = sg.Window("To-Do App",layout=layout)
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case sg.WINDOW_CLOSED:
            break
        case 'Add':
            features.add(values['INPUT'])

window.close()
