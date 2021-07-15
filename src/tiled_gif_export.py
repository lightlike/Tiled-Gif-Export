import shutil
import tkinter as tk

from settings import Settings
from ui import getMissingSettings
from command_caller import *

root = tk.Tk()
root.withdraw()

settings = Settings()
if not settings.console:
    settings = getMissingSettings(settings)

generateFrames(settings)
generateGif(settings)

shutil.rmtree(settings.temp)
