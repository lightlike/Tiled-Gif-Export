import tkinter as tk
from tkinter import filedialog
import configparser
import easygui
import subprocess
import os
from os.path import exists
import shutil

def defineConfig():
    config = configparser.ConfigParser()
    config['TOOLPATHS'] = {}

    toolpaths = config['TOOLPATHS']
    toolpaths['tmxrasterizer'] = "tmxrasterizer"
    toolpaths['magick'] = "magick"

    config['SETTINGS'] = {}

    settings = config['SETTINGS']
    settings['frametime'] = "100"
    settings['tempdir'] = "temp"

    with open('config.ini', 'w') as configfile:
        config.write(configfile)

def getConfig():
    if not exists('config.ini'):
        defineConfig()
    
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config

def generateFrames(infile: str, frames: int, config):
    command = "{exe} --advance-animations {frame} \"{infile}\" \"{outfile}\""

    exe = config['TOOLPATHS']['tmxrasterizer']
    frametime = int(config['SETTINGS']['frametime'])
    tempdir = config['SETTINGS']['tempdir']

    if not os.path.isdir(tempdir):
        os.mkdir(tempdir)

    for c in range(frames):
        frame = frametime * c + 1
        outfile = os.path.join(tempdir, "{number}.png".format(number = c))
        execute = command.format(exe = exe, frame = frame, infile = infile, outfile = outfile)
        subprocess.run(execute)

def generateGif(outfile: str, frames: int, config):
    command = "{exe} -delay {delay} -loop 0 {files} \"{outfile}\""
    
    exe = config['TOOLPATHS']['magick']
    tempdir = config['SETTINGS']['tempdir']
    delay = int(int(config['SETTINGS']['frametime']) / 10)

    files = ""

    for c in range(frames):
        files += os.path.join(tempdir, "{number}.png".format(number = c)) + " "

    files = files.strip()

    execute = command.format(exe = exe, delay = delay, files = files, outfile = outfile)
    subprocess.run(execute)


if __name__ == '__main__':
    config = getConfig()

    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()
    file_name, f_ext = os.path.splitext(file_path)

    out_path = easygui.enterbox("Enter the output file Path.", default = file_name + ".gif")
    frames = int(easygui.enterbox("Enter the number of Frames."))

    generateFrames(file_path, frames, config)
    generateGif(out_path, frames, config)

    shutil.rmtree(config['SETTINGS']['tempdir'])
