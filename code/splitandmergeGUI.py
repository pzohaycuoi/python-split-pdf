import PySimpleGUI as sg
import sys

from main import pdf_function as splitFunc

sg.theme("DarkAmber")

split_Func_Tab = [
    [
        sg.Text("Source file", size=(15, 1)),
        sg.InputText(size=(20, 1), key="input_source_file"),
        sg.FileBrowse(),
    ],
    [
        sg.Text("Destination folder", size=(15, 1)),
        sg.InputText(size=(20, 1), key="input_destination_folder"),
        sg.FolderBrowse(),
    ],
    [
        sg.Text("File name"),
        sg.InputText(size=(8, 1), key="input_file_name", enable_events=True),
        sg.Text("Start number"),
        sg.InputText(size=(4, 1), key="input_file_number", enable_events=True),
        sg.Text("Split range"),
        sg.InputText(size=(4, 1), key="input_step", enable_events=True),
    ],
    [
        sg.Radio("Ascending", "rad1", pad=((0, 20), (0, 0)), key="input_sorting_asc"),
        sg.Radio("Descending", "rad1", key="input_sorting_desc"),
    ],
    [
        sg.Button("OK")    
    ]
]

Merge_Func_Tab = [
    [
        sg.Text("Source Folder", size=(15, 1)),
        sg.InputText(size=(20, 1), key="input_source_folder"),
        sg.FolderBrowse(),
    ],
    [
        sg.Text("Merged Folder", size=(15, 1)),
        sg.InputText(size=(20, 1), key="input_merged_folder"),
        sg.FolderBrowse(),
    ],
    [
        sg.Button("Select File", key="input_select_file")
    ],
    [
        sg.Button("OK")
    ]
]

Check_Missing_Func_Tab = [
    [sg.Text("con cac dmm"), sg.InputText(), sg.FolderBrowse()]
]

Merge_Func_Window = [
    [sg.Text("con cac dmm"), sg.InputText(), sg.FolderBrowse()]
]

layout = [
    [
        sg.TabGroup(
            [
                [
                    sg.Tab("Split PDF", split_Func_Tab),
                    sg.Tab("Merge PDF", Merge_Func_Tab),
                    sg.Tab("Check Missing File", Check_Missing_Func_Tab),
                ]
            ]
        )
    ]
]

window = sg.Window("Nam Beo", layout)
window2 = False

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break
    if event == "input_select_file":
        window2 = sg.Window("WTF is this shit", Merge_Func_Window)

    # source_file = values["input_source_file"]
    # destination_folder = values["input_destination_folder"]
    # file_name = values["input_file_name"]
    # file_number = values["input_file_number"]
    # file_step = values["input_step"]
    # sorting_asc = values["input_sorting_asc"]
    # sorting_desc = values["input_sorting_desc"]

    # if (
    #     event == "input_file_name"
    #     and file_name
    #     and file_name[-1] in ("'*<>?\|/:" ".,`")
    # ):
    #     window["input_file_name"].update(file_name[:-1])
    # if (
    #     event == "input_file_number"
    #     and file_number
    #     and file_number[-1] not in ("0123456789")
    # ):
    #     window["input_file_number"].update(file_number[:-1])
    # if (
    #     event == "input_file_number"
    #     and file_step
    #     and file_step[-1] not in ("0123456789")
    # ):
    #     window["input_file_number"].update(file_step[:-1])
    # if event in ("OK"):
    #     if not str(destination_folder).endswith("/"):
    #         destination_folder = str(destination_folder) + "/"

    #     file_number_int = int(file_number)
    #     file_step_int = int(file_step)

    #     output_file_path = "{}{}".format(destination_folder, file_name)

    #     sorting = [sorting_asc, sorting_desc]

    #     splitFunc.split_at_every(
    #         source_file, output_file_path, file_number_int, file_step_int, sorting
    #     )

window.close()
