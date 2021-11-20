import argparse
import configparser
import os
from os.path import exists

def isNoneOrEmpty(value):
    return value is None or str(value) == ''

class Settings:
    rasterizer = None
    magick = None
    temp = None
    
    file = None
    output = None

    def _get_duration(self):
        return self.__duration
    def _set_duration(self, value):
        if not isinstance(value, int):
            raise TypeError("bar must be set to an integer")
        self.__duration = value
    duration = property(_get_duration, _set_duration)
    def _get_frames(self):
        return self.__frames
    def _set_frames(self, value):
        if not isinstance(value, int):
            raise TypeError("bar must be set to an integer")
        self.__frames = value
    frames = property(_get_frames, _set_frames)

    def __init__(self):
        if not exists('config.ini'):
            self.generateConfig()
        self.loadFromFile()

    def isValid(self) -> bool:
        return (not isNoneOrEmpty(self.rasterizer)
            and not isNoneOrEmpty(self.magick)
            and not isNoneOrEmpty(self.temp)
            and not isNoneOrEmpty(self.duration)
            and not isNoneOrEmpty(self.frames)
            and not isNoneOrEmpty(self.file)
            and not isNoneOrEmpty(self.output))

    def loadFromFile(self):
        config = configparser.ConfigParser()
        config.read('config.ini')

        self.rasterizer = config['TOOLPATHS']['tmxrasterizer']
        self.magick = config['TOOLPATHS']['magick']
        self.temp = config['SETTINGS']['tempdir']

    def generateConfig(self):
        config = configparser.ConfigParser()

        config['TOOLPATHS'] = {}
        toolpaths = config['TOOLPATHS']
        toolpaths['tmxrasterizer'] = "tmxrasterizer"
        toolpaths['magick'] = "magick"

        config['SETTINGS'] = {}
        settings = config['SETTINGS']
        settings['tempdir'] = "temp"

        with open('config.ini', 'w') as configfile:
            config.write(configfile)

        print("Config Generated. Please edit and restart this program.")
        if not settings.console:
            input('Press ENTER to exit')
        exit()

    def parseArgs(self):
        parser = argparse.ArgumentParser()

        parser.add_argument("-r", "--rasterizer",
            default = self.rasterizer,
            help = "Path to tmxrasterizer")
        parser.add_argument("-m", "--magick",
            default = self.magick,
            help = "Path to magick/convert")
        parser.add_argument("--temp",
            default = self.temp,
            help = "Temporary Directory")

        parser.add_argument("-d", "--duration",
            type = int, required=True,
            help = "Frame duration in ms (has to be devisible by 10)")
        parser.add_argument("-n", "--frames",
            type = int, required=True,
            help = "Number of Frames to render")
        parser.add_argument("-f", "--file",
            required=True,
            help = "Input file (Tiled file '.tmx' or '.world'")
        parser.add_argument("-o", "--output",
            required=True,
            help = "Output file (.gif)")

        args = parser.parse_args()

        self.rasterizer = args.rasterizer
        self.magick = args.magick
        self.temp = args.temp
        self.duration = args.duration
        self.frames = args.frames
        self.file = args.file
        self.output = args.output
