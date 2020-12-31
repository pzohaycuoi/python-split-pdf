import tkinter
import PySimpleGUI as sg

sg.theme('DarkAmber')

layout = [  [sg.Text('Some text on Row 1')],
            [sg.Text('Source file'), sg.InputText(), sg.FileBrowse()], #After choosing source file path will display here
            [sg.Text('Split at every'), sg.InputText()],
            [sg.Text('Destination folder'), sg.InputText(), sg.FileBrowse()], #After choosing destination folder path will display here
            [sg.Button('Ok'), sg.Button('Cancel')] ]


window = sg.Window('Window Title', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': 
        break
    print('You entered ', values[0])

window.close()