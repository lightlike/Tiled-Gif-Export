from os.path import exists
import shutil
import sys

from settings import Settings
from command_caller import *
from ui import UI

def main():
    if len(sys.argv) <= 1:
        if not exists(Settings.get_config_path()):
            Settings.generate_config()
            return
        settings = Settings.load_from_file()

        ui = UI()
        isSubmit = ui.showSettingsForm(settings)
        if not isSubmit:
            return
    else:
        settings = Settings.parse_args()

    print("Generating Frames")
    generateFrames(settings)
    print("Packing Gif")
    generateGif(settings)
    print("Finished generating. Cleaning up.")
    shutil.rmtree(settings.temp)

    if not len(sys.argv) > 1:
        input('Press ENTER to exit')

if __name__ == "__main__":
    main()
