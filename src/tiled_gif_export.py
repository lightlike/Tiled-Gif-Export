import shutil
import sys

from settings import Settings
from command_caller import *
from ui import UI

settings = Settings()

if len(sys.argv) > 1:
    settings.parseArgs()
else:
    ui = UI()
    isSubmit = ui.showSettingsForm(settings)
    if not isSubmit:
        exit()

print("Generating Frames")
generateFrames(settings)
print("Packing Gif")
generateGif(settings)
print("finished generating. Cleaning up.")
shutil.rmtree(settings.temp)

if not len(sys.argv) > 1:
    input('Press ENTER to exit')