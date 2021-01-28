import PySimpleGUI as sg
import sys
import os
from main import pdf_function as splitFunc

# GUI
sg.theme("DarkAmber")

split_Func_Tab = [
    [
        sg.Text("Source file", size=(15, 1)),
        sg.InputText(size=(20, 1), key="split_inpt_source_file"),
        sg.FileBrowse(),
    ],
    [
        sg.Text("Destination folder", size=(15, 1)),
        sg.InputText(size=(20, 1), key="split_inpt_destination_folder"),
        sg.FolderBrowse(),
    ],
    [
        sg.Text("File name"),
        sg.InputText(size=(8, 1),
                     key="split_inpt_file_name",
                     enable_events=True),
        sg.Text("Start number"),
        sg.InputText(size=(4, 1),
                     key="split_inpt_file_number",
                     enable_events=True),
        sg.Text("Split range"),
        sg.InputText(size=(4, 1), key="split_inpt_step", enable_events=True),
    ],
    [
        sg.Radio("Ascending",
                 "rad1",
                 pad=((0, 20), (0, 0)),
                 key="split_inpt_sorting_asc"),
        sg.Radio("Descending", "rad1", key="split_inpt_sorting_desc"),
    ],
    [sg.Button("OK")],
]

Merge_Func_Tab = [
    [
        sg.Text("Source Folder", size=(15, 1)),
        sg.InputText(size=(20, 1), key="Merge_inpt_source_folder"),
        sg.FolderBrowse(),
    ],
    [
        sg.Text("Merged Folder", size=(15, 1)),
        sg.InputText(size=(20, 1), key="Merge_inpt_merged_folder"),
        sg.FolderBrowse(),
    ],
    [
        sg.Button("Select File", key="Nerge_inpt_select_file"),
        sg.Button("Sorting File", key="Merge_inpt_sorting_file"),
    ],
    [sg.Button("OK")],
]

Check_Missing_Func_Tab = [[
    sg.Text("con cac dmm"),
    sg.InputText(), sg.FolderBrowse()
]]

layout = [[
    sg.TabGroup([[
        sg.Tab("Split PDF", split_Func_Tab),
        sg.Tab("Merge PDF", Merge_Func_Tab),
        # sg.Tab("Check Missing File", Check_Missing_Func_Tab),
    ]])
]]

split_window = sg.Window("Nam Beo", layout)
merge_select_file_window = False
merge_sorting_file_window = False

# GUI Function
while True:
    event, value = split_window.read()
    if event == sg.WINDOW_CLOSED:
        break

    # split_window GUI Function
    source_file = value["split_inpt_source_file"]
    destination_folder = value["split_inpt_destination_folder"]
    file_name = value["split_inpt_file_name"]
    file_number = value["split_inpt_file_number"]
    file_step = value["split_inpt_step"]
    sorting_asc = value["split_inpt_sorting_asc"]
    sorting_desc = value["split_inpt_sorting_desc"]
    if (event == "split_inpt_file_name" and file_name
            and file_name[-1] in ("'*<>?\|/:"
                                  ".,`")):
        split_window["split_inpt_file_name"].update(file_name[:-1])
    if (event == "input_file_number" and file_number
            and file_number[-1] not in ("0123456789")):
        split_window["split_inpt_file_number"].update(file_number[:-1])
    if (event == "split_inpt_file_number" and file_step
            and file_step[-1] not in ("0123456789")):
        split_window["split_inpt_file_number"].update(file_step[:-1])
    if event in ("OK"):
        if not str(destination_folder).endswith("/"):
            destination_folder = str(destination_folder) + "/"

        file_number_int = int(file_number)
        file_step_int = int(file_step)
        output_file_path = "{}{}".format(destination_folder, file_name)
        sorting = [sorting_asc, sorting_desc]
        splitFunc.split_at_every(source_file, output_file_path,
                                 file_number_int, file_step_int, sorting)

    # merge_select_file_window GUI Function
    if event == "Nerge_inpt_select_file" and not merge_select_file_window:
        merge_select_file_window is True
        Tree_Data = sg.TreeData()

        def display_file_in_folder(parent, source_folder):
            files = os.listdir(source_folder)
            for i in files:
                File_Fullname = os.path.join(source_folder, i)
                if os.path.isdir(File_Fullname):
                    Tree_Data.Insert(parent, File_Fullname, i, values=[])
                    display_file_in_folder(File_Fullname, File_Fullname)
                else:
                    if i.endswith(".pdf"):
                        Tree_Data.Insert(
                            parent,
                            File_Fullname,
                            i,
                            values=[os.stat(File_Fullname).st_size])

        Merge_Source_Folder = value["Merge_inpt_source_folder"]
        display_file_in_folder('', Merge_Source_Folder)

        Merge_Select_File_split_window = [
            [sg.Text("Select File")],
            [
                sg.Tree(
                    data=Tree_Data,
                    auto_size_columns=True,
                    headings=[
                        "Modified Time",
                    ],
                    num_rows=15,
                    col0_width=30,
                    key="Merge_Select_File_Tree",
                    show_expanded=False,
                    enable_events=True,
                )
            ],
            [
                sg.Button("OK", key="Merge_Select_split_window_OK"),
                sg.Button("Cancel", key="Merge_Select_split_window_Cancel")
            ]
        ]

        merge_select_file_window = sg.Window(
            "Select File", Merge_Select_File_split_window)
        split_window.Hide()

    while True:
        event2, value2 = merge_select_file_window.read()
        if event2 in (sg.WINDOW_CLOSED,
                      "Merge_Select_split_window_Cancel"):
            merge_select_file_window.Close()
            merge_select_file_window = False
            split_window.UnHide()
            break

    # merge_sorting_file_window GUI Function
    if event == "input_sorting_file":
        merge_sorting_file_window = True

        merge_sorting_split_window = []

split_window.close()
