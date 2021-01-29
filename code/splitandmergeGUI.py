import PySimpleGUI as sg
from guifunction import GuiFunction as gf
from main import PdfFunction as pf

# GUI
sg.theme("DarkAmber")

split_Func_Tab = [
    [
        sg.Text("Source file", size=(15, 1)),
        sg.InputText(size=(20, 1), key="split_src_file"),
        sg.FileBrowse(),
    ],
    [
        sg.Text("Destination folder", size=(15, 1)),
        sg.InputText(size=(20, 1), key="split_des_folder"),
        sg.FolderBrowse(),
    ],
    [
        sg.Text("File name"),
        sg.InputText(size=(8, 1), key="split_file_name", enable_events=True),
        sg.Text("Start number"),
        sg.InputText(size=(4, 1), key="split_file_number", enable_events=True),
        sg.Text("Split range"),
        sg.InputText(size=(4, 1), key="split_step", enable_events=True),
    ],
    [
        sg.Radio("Ascending",
                 "rad1",
                 pad=((0, 20), (0, 0)),
                 key="split_sort_asc"),
        sg.Radio("Descending", "rad1", key="split_sort_desc"),
    ],
    [sg.Button("OK", key="split_ok")],
]

Merge_Func_Tab = [
    [
        sg.Text("Source Folder", size=(15, 1)),
        sg.InputText(size=(20, 1), key="merge_src_folder"),
        sg.FolderBrowse(),
    ],
    [
        sg.Text("Merged Folder", size=(15, 1)),
        sg.InputText(size=(20, 1), key="merge_des_folder"),
        sg.FolderBrowse(),
    ],
    [
        sg.Button("Select File", key="merge_select_file"),
        sg.Button("Sorting File", key="merge_sorting_file"),
    ],
    [sg.Button("OK", key="merge_ok")],
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
select_file_window = False
sorting_file_window = False

# GUI Function
while True:
    event, value = split_window.read()
    if event == sg.WINDOW_CLOSED:
        break

    # split_window GUI Function
    split_src_file = value["split_src_file"]
    split_des_folder = value["split_des_folder"]
    split_file_name = value["split_file_name"]
    split_file_number = value["split_file_number"]
    step = value["split_step"]
    split_sort_asc = value["split_sort_asc"]
    split_sort_desc = value["split_sort_desc"]

    if (event == "split_file_name" and split_file_name
            and split_file_name[-1] in ("'*<>\\?|/:"
                                        ".,`")):
        split_window["split_file_name"].update(split_file_name[:-1])
    if (event == "split_file_numer" and split_file_name
            and split_file_number[-1] not in ("0123456789")):
        split_window["split_file_number"].update(split_file_name[:-1])
    if (event == "split_file_number" and step
            and step[-1] not in ("0123456789")):
        split_window["split_file_number"].update(step[:-1])
    if event in ("split_ok"):

        file_number_int = int(split_file_number)
        file_step_int = int(step)
        split_sort = [split_sort_asc, split_sort_desc]

        pf.split_at_every(split_src_file, split_des_folder, split_file_name,
                          file_number_int, file_step_int, split_sort)

    # merge_select_file_window
    #  GUI Function
    if event == "merge_select_file" and not select_file_window:
        select_file_window is True

        merge_src_folder = value["merge_src_folder"]
        file_name = gf.add_files_in_folder(merge_src_folder)

        merge_select_window = [[
            sg.Text("Select File")
        ], [gf.check_box_generator(fn) for fn in file_name],
                               [
                                   sg.Button("OK", key="merge_select_file_ok"),
                                   sg.Button("Cancel",
                                             key="merge_select_file_cancel")
                               ]]

        merge_select_file_window = sg.Window("Select File",
                                             merge_select_window)
        split_window.Hide()

    while True:
        event2, value2 = merge_select_file_window.read()
        if event2 == "merge_select_file_ok":
            print(file_name)
        if event2 in (sg.WIN_CLOSED, "merge_select_file_cancel"):
            merge_select_file_window.Close()
            merge_select_file_window = False
            split_window.UnHide()
            break

    # merge_sorting_file_window GUI Function
    if event == "input_sorting_file":
        merge_sorting_file_window = True
        merge_sorting_split_window = []

split_window.close()
