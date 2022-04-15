# Tiled-Gif-Export

## Requirements:
- [Tiled Editor](https://www.mapeditor.org/)
- [ImageMagick](https://imagemagick.org/index.php)

## Download

### Windows

[Single Executable](https://github.com/lightlike/Tiled-Gif-Export/releases/latest/download/tiled_gif_export.exe)

### All Systems

1. download or clone the repository
2. execute `python ./src/tiled_gif_export.py`
3. see [Usage](#Usage)

## Usage

Important: `frametime` is the time between animation frames in ms (default: 100ms). The value has to be cleanly devisible by 10 to work the way I wrote it.

### With UI

1. Start the program for the first time
2. Edit the `config.ini`
```ini
[TOOLPATHS]
tmxrasterizer = tmxrasterizer   ; path to the Tiled `tmxrasterizer.exe` (you will probably need to edit the right side)
magick = magick                 ; path to the ImageMagick `magick.exe` or `convert.exe` (should be in PATH if selected during install)
```
3. Start the program and everything sould work after that

### Console

Run one of these commands:
- `tiled_gif_export.exe ...`
- `python tiled_gif_export.py ...`

```
usage: tiled_gif_export.py [-h] [-r RASTERIZER] [-m MAGICK] [--temp TEMP] -d DURATION -n FRAMES -f FILE -o OUTPUT

optional arguments:
  -h, --help            show this help message and exit
  -r RASTERIZER, --rasterizer RASTERIZER
                        Path to tmxrasterizer
  -m MAGICK, --magick MAGICK
                        Path to magick/convert
  --temp TEMP           Temporary Directory
  -d DURATION, --duration DURATION
                        Frame duration in ms (has to be devisible by 10)
  -n FRAMES, --frames FRAMES
                        Number of Frames to render
  -f FILE, --file FILE  Input file (Tiled file '.tmx' or '.world'
  -o OUTPUT, --output OUTPUT
                        Output file (.gif)
```

## Basic Commands used

`x: frame duration`

`tmxrasterizer --advance-animations {x+1} "{Tiled-File}" "{PNG Files}"`

`magick -delay {x/10} -loop 0 *.png {outfile}`

## Discussions

[![Gitter](https://img.shields.io/gitter/room/lightlike/tiled-gif-export.svg?style=flat-square)](https://gitter.im/lightlike/Tiled-Gif-Export?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)

Or join using [Matrix](https://matrix.to/#/#lightlike_Tiled-Gif-Export:gitter.im)

## Stuff that I need to do

- [x] ignoring UI when using arguments
- [x] proper error handling (mostly?)
- [ ] Build Pipeline for Pyinstaller
- [ ] Icon for executable
