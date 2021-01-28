import os
import PySimpleGUI as sg


class GuiFunction():
    def add_files_in_folder(source_folder):
        files = os.listdir(source_folder)
        file_path = []
        file_name = []

        for i in files:
            file_path = os.path.join(source_folder, i)
            if i.endswith(".pdf"):
                file_path.append(file_path)
                file_name.append(i)

    def check_box_generator(file_name):
        for i in file_name:
            return sg.Checkbox(i, size=(20, 1), default=False)
