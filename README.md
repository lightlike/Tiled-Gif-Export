# Tiled-Gif-Export

## Setup

Requirements:
- [Tiled Editor](https://www.mapeditor.org/)
- [ImageMagick](https://imagemagick.org/index.php)

## Usage

### Important

- `frametime`: time between animation frames in ms (default: 100ms). The value has to be cleanly devisible by 10 to work the way I wrote it.

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
- `tiled_gif_export.exe -c ...`
- `python tiled_gif_export.py -c ...`

-c is required to not get any UI elements overwriting the console arguments

```
usage: tiled_gif_export.py [-h] [-c] [-r RASTERIZER] [-m MAGICK] [--temp TEMP] [-d DURATION] [-n FRAMES] [-f FILE] [-o OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  -c, --console         Block UI from showing up
  -r RASTERIZER, --rasterizer RASTERIZER
                        Path to tmxrasterizer
  -m MAGICK, --magick MAGICK
                        Path to magick/convert
  --temp TEMP           Temporary Directory
  -d DURATION, --duration DURATION
                        Frame duration in ms (has to be devisible by 10)
  -n FRAMES, --frames FRAMES
                        Number if Frames to render
  -f FILE, --file FILE  Input file (Tiled file '.tmx' or '.world'
  -o OUTPUT, --output OUTPUT
                        Output file (.gif)
```

## Basic Commands used

`x: frame duration`

`tmxrasterizer --advance-animations {x+1} "{Tiled-File}" "{Png Files}"`

`magick -delay {x/10} -loop 0 *.png {outfile}`

## Stuff that I need to do

- [x] ignoring UI when using arguments
- [ ] proper error handling
- [ ] Build Pipeline for Pyinstaller
- [ ] Icon for executable
