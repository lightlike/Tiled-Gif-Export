from tkinter import filedialog
import easygui
import os

from settings import Settings

def getMissingSettings(settings: Settings):
    if settings.file is None:
        settings.file = filedialog.askopenfilename()

    if settings.output is None:
        file_name, f_ext = os.path.splitext(settings.file)

        settings.output = easygui.enterbox("Enter the output file Path.", default = file_name + ".gif")

    settings.duration = int(easygui.enterbox("Enter the frame duration.", default = settings.duration))
    settings.frames = int(easygui.enterbox("Enter the number of frames.", default = settings.frames))

    return settings