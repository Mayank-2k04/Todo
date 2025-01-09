import PySimpleGUI as sg
from modules import guifeat

td = guifeat.read_todo()

title = sg.Text("Enter to do item",background_color="black",border_width=2,justification='center')
inp = sg.Input(key='INPUT')
add_button = sg.Button("Add")
label = sg.Text("Items in To-Do List :",background_color="black",border_width=2,justification='center')
lst = sg.Listbox(values=td, enable_events=True,size=(44,10), key='todos')
edit_button = sg.Button("Edit")
remove_button = sg.Button("Remove")
completed_button = sg.Button("Completed")
ex = sg.Exit()

Layout = [
    [title],
    [inp, add_button],
    [label],
    [lst, edit_button],
    [completed_button,remove_button],
    [ex]
]