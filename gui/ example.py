import PySimpleGUI as sg

sg.theme('DarkAmber')

layout = [
    [sg.Text('Source file', size=(15, 1)),
     sg.InputText(size=(20, 1), key='input_source_file'), sg.FileBrowse()],
    [sg.Text('Destination folder', size=(15, 1)),
     sg.InputText(size=(20, 1), key='input_destination_folder'), sg.FolderBrowse()],
    [sg.Text('File name'), sg.InputText(size=(10, 1), key='input_file_name', enable_events=True),
     sg.Text('Start number'), sg.InputText(size=(10, 1), key='input_file_number', enable_events=True)],
    [sg.Radio('Ascending', 'rad1', pad=((0, 20), (0, 0)), key='sorting_asc'),
     sg.Radio('Descending', 'rad1', key='sorting_desc')],
    [sg.Button('OK'), sg.Button('Cancel')]
]

window = sg.Window('Title', layout)

while True:
    event, values = window.read()

    source_file = values['input_source_file']
    destination_folder = values['input_destination_folder']
    file_name = values['input_file_name']
    file_number = values['input_file_number']

    if event in (sg.WINDOW_CLOSED, 'Cancel'):
        break
    if event == 'input_file_name' and file_name and file_name[-1] in ("'*<>?\|/:"".,`"):
        window['input_file_name'].update(file_name[:-1])
    if event == 'input_file_number' and file_number and file_number[-1] not in ('0123456789'):
        window['input_file_number'].update(file_number[:-1])
    if event in ('OK'):
        if str(destination_folder).endswith("/"):
            break
        else:
            destination_folder = str(destination_folder) + '/'
        print(source_file)
        print(destination_folder)

        output_file_path = '{}{}_{}.pdf'.format(
            destination_folder, file_name, file_number)

        print(output_file_path)

window.close()
