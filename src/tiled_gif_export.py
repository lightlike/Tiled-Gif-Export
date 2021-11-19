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

generateFrames(settings)
generateGif(settings)

shutil.rmtree(settings.temp)

if not settings.console:
    input('Press ENTER to exit')