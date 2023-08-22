import argparse
import configparser
from dataclasses import dataclass
import os
from os.path import exists

@dataclass
class Settings:
    rasterizer: str = "tmxrasterizer"
    magick: str = "magick"
    temp: str = "temp"
    
    file: str = None
    output: str = None
    duration: int = None
    frames: int = None

    @staticmethod
    def get_config_path() -> str:
        return os.path.join(os.path.dirname(os.path.realpath(__file__)), "config.ini")

    @classmethod
    def load_config(cls) -> 'Settings':
        config_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "config.ini")
        if not exists(config_path):
            cls.generate_config(config_path)
            return None
        result = cls()
        return result.load_from_file()

    @classmethod
    def load_from_file(cls) -> 'Settings':
        result = cls()
        config = configparser.ConfigParser()
        config.read(result.get_config_path())

        result.rasterizer = config['TOOLPATHS']['tmxrasterizer']
        result.magick = config['TOOLPATHS']['magick']
        result.temp = config['SETTINGS']['tempdir']

        return result

    @classmethod
    def generate_config(cls) -> None:
        data = cls()
        config = configparser.ConfigParser()

        config['TOOLPATHS'] = {}
        toolpaths = config['TOOLPATHS']
        toolpaths['tmxrasterizer'] = data.rasterizer
        toolpaths['magick'] = data.magick

        config['SETTINGS'] = {}
        settings = config['SETTINGS']
        settings['tempdir'] = data.temp

        with open(cls.get_config_path(), 'w') as configfile:
            config.write(configfile)

        print("Config Generated. Please edit and restart this program.")

    @classmethod
    def parse_args(cls):
        result = cls()
        parser = argparse.ArgumentParser()

        parser.add_argument("-r", "--rasterizer",
            default = result.rasterizer,
            help = "Path to tmxrasterizer")
        parser.add_argument("-m", "--magick",
            default = result.magick,
            help = "Path to magick/convert")
        parser.add_argument("--temp",
            default = result.temp,
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

        result.rasterizer = args.rasterizer
        result.magick = args.magick
        result.temp = args.temp
        result.duration = args.duration
        result.frames = args.frames
        result.file = args.file
        result.output = args.output
