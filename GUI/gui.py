import PySimpleGUI as sg
import layout as lay
from modules import guifeat
import time
import os

if not os.path.exists("list.txt"):
    with open('list.txt','w') as f:
        pass


sg.theme('Black')
window = sg.Window("To-Do App",layout=lay.Layout)

while True:
    event, values = window.read(500)
    window['clock'].update(time.strftime("%b %d, %Y  %H:%M:%S"))
    try:
        match event:

            case sg.WINDOW_CLOSED:
                break
            case 'Exit':
                break

            case 'Add':
                td = guifeat.read_todo()
                new_ele = values['INPUT'] + '\n'
                if new_ele != '\n' and new_ele not in td:
                    td.append(new_ele)
                elif new_ele == '\n':
                    sg.popup_ok("Enter an element",auto_close=True,auto_close_duration=2,title="Error")
                else:
                    result = sg.popup_yes_no("Add a duplicate?")
                    if result == 'Yes':
                        td.append(new_ele)
                    else:
                        continue
                guifeat.write_todo(td)
                window['todos'].update(values=td)
                window['INPUT'].update(value='')

            case 'todos':
                window['INPUT'].update(value=values['todos'][0].strip('\n'))

            case 'Edit':
                td = guifeat.read_todo()
                edit_todo = values['todos'][0]
                new_todo = values['INPUT']
                i = td.index(edit_todo)
                td[i] = new_todo + '\n'
                guifeat.write_todo(td)
                window['INPUT'].update(value="")
                window['todos'].update(values=td)

            case 'Remove':
                td = guifeat.read_todo()
                element = values['todos'][0]
                td.remove(element)
                guifeat.write_todo(td)
                window['todos'].update(values=td)
                window['INPUT'].update(value="")

            case 'Completed':
                td = guifeat.read_todo()
                element = values['todos'][0]
                td.remove(element)
                guifeat.write_todo(td)
                window['todos'].update(values=td)
                window['INPUT'].update(value="")
    except IndexError as e:
        sg.popup_ok("Select an element",title="Error",auto_close=True,auto_close_duration=2)
window.close()
