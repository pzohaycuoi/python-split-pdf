import PySimpleGUI as sg

sg.theme('DarkAmber')

layout = [
    [sg.Text('Source file', size=(15, 1)),
     sg.InputText(size=(20, 1)), sg.FileBrowse()],
    [sg.Text('Destination folder', size=(15, 1)),
     sg.InputText(size=(20, 1)), sg.FileBrowse()],
    [sg.Text('File name'), sg.InputText(size=(10, 1)), sg.Text(
        'Start number'), sg.InputText(size=(10, 1))],
    [sg.Radio('Ascending', 'rad1', pad=((0, 20), (0, 0))),
     sg.Radio('Descending', 'rad1')],
    [sg.Button('OK'), sg.Button('Cancel')]
]

window = sg.Window('Title', layout)

#event, values = window.read()
while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, 'Cancel'):
        break

window.close()
