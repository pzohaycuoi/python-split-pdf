import PySimpleGUI as sg

sg.theme('DarkAmber')

# layout = [  [sg.Text('Some text on Row 1')],
#             [sg.Text('Source file', size=(15,1)), sg.popup_get_file('con cac')], #After choosing source file path will display here
#             [sg.Text('Split at every', size=(15,1)), sg.InputText()],
#             [sg.Text('Destination folder', size=(15,1)), sg.InputText(), sg.FileBrowse()], #After choosing destination folder path will display here
#             [sg.Button('Ok'), sg.Button('Cancel')] ]

layout = [
    [sg.Text('Source file', size=(15, 1), justification='right'),
     sg.In(), sg.FileBrowse()],
    [sg.Text('Destination folder', size=(15, 1),
             justification='right'), sg.In(), sg.FolderBrowse()],
    [sg.Text('Input file name', size=(15, 1), justification='right'),
     sg.Input(size=(8, 1))],
    [sg.Button('Ok'), sg.Button('Cancel')]
]


window = sg.Window('Window Title', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    print('You entered ', values[0])

window.close()
