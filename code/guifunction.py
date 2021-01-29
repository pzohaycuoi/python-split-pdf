import os
import PySimpleGUI as sg


class GuiFunction():
    def add_files_in_folder(source_folder):
        files = os.listdir(source_folder)
        file_name = []

        for i in files:
            if i.endswith(".pdf"):
                file_name.append(i)
        return file_name

    def check_box_generator(file_name):
        return sg.Checkbox(file_name, size=(20, 1), default=False)
