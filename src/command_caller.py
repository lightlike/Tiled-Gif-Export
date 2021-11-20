import os
import subprocess

from settings import Settings

def generateFrames(settings: Settings):
    command = "{exe} --advance-animations {frame} \"{infile}\" \"{outfile}\""

    exe = settings.rasterizer
    duration = settings.duration
    frames = settings.frames
    tempdir = settings.temp
    infile = settings.file

    if not os.path.isdir(tempdir):
        os.mkdir(tempdir)

    for c in range(frames):
        frame = duration * c + 1
        outfile = os.path.join(tempdir, "{number}.png".format(number = c))
        execute = command.format(exe = exe, frame = frame, infile = infile, outfile = outfile)
        subprocess.run(execute)

def generateGif(settings: Settings):
    command = "{exe} -delay {delay} -dispose previous -loop 0 {files} \"{outfile}\""
    
    exe = settings.magick
    tempdir = settings.temp
    delay = int(int(settings.duration) / 10)
    frames = settings.frames
    outfile = settings.output

    files = ""

    for c in range(frames):
        files += os.path.join(tempdir, "{number}.png".format(number = c)) + " "

    files = files.strip()

    execute = command.format(exe = exe, delay = delay, files = files, outfile = outfile)
    subprocess.run(execute)