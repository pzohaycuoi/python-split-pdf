import PySimpleGUI as sg

sg.theme('DarkAmber')

layout = [
    [sg.Text('Source file', size=(15, 1)),
     sg.InputText(size=(20, 1), key='source_file'), sg.FileBrowse()],
    [sg.Text('Destination folder', size=(15, 1)),
     sg.InputText(size=(20, 1), key='destination_folder'), sg.FileBrowse()],
    [sg.Text('File name'), sg.InputText(size=(10, 1), key='file_name'), sg.Text(
        'Start number'), sg.InputText(size=(10, 1), key='file_start_number')],
    [sg.Radio('Ascending', 'rad1', pad=((0, 20), (0, 0)), key='sorting_asc'),
     sg.Radio('Descending', 'rad1', key='sorting_desc')],
    [sg.Button('OK'), sg.Button('Cancel')]
]

window = sg.Window('Title', layout)

while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, 'Cancel'):
        break
    # if event in 

window.close()
