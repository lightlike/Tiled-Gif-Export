import argparse
import configparser
import os
from os.path import exists


class Settings:
    def __init__(self):
        if not exists('config.ini'):
            self.generateConfig()
        self.parseSettings()

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

        print("Config Generated. Exiting...")
        exit()

    def parseSettings(self):
        config = configparser.ConfigParser()
        config.read('config.ini')

        parser = argparse.ArgumentParser()

        parser.add_argument('-c', '--console', action='store_true',
            help = "Block UI from showing up")

        parser.add_argument("-r", "--rasterizer",
            default = config['TOOLPATHS']['tmxrasterizer'],
            help = "Path to tmxrasterizer")
        parser.add_argument("-m", "--magick",
            default = config['TOOLPATHS']['magick'],
            help = "Path to magick/convert")
        parser.add_argument("--temp",
            default = config['SETTINGS']['tempdir'],
            help = "Temporary Directory")

        parser.add_argument("-d", "--duration",
            default = 100, type = int,
            help = "Frame duration in ms (has to be devisible by 10)")
        parser.add_argument("-n", "--frames",
            type = int,
            help = "Number if Frames to render")
        parser.add_argument("-f", "--file",
            help = "Input file (Tiled file '.tmx' or '.world'")
        parser.add_argument("-o", "--output",
            help = "Output file (.gif)")

        args = parser.parse_args()

        self.console = args.console

        self.rasterizer = args.rasterizer
        self.magick = args.magick
        self.temp = args.temp
        self.duration = args.duration
        self.frames = args.frames
        self.file = args.file
        self.output = args.output
