# Tiled-Gif-Export

## Setup

Requirements:
- [Tiled Editor](https://www.mapeditor.org/)
- [ImageMagick](https://imagemagick.org/index.php)

A `config.ini` gets generated automatically.

Here are all the values:
- `tmxrasterizer`: path to the Tiled `tmxrasterizer.exe` (you will probably need to edit this)
- `magick`: path to the ImageMagick `magick.exe` or `convert.exe` (should be in PATH if selected during install)
- `frametime`: time between animation frames in ms (default: 100ms). The value has to be cleanly devisible by 10 to work the way I wrote it.
- `tempdir`: name of the temporary directory to create the frames in (should not need to be changed but does not really matter) 

## Basic Commands used

`x: frame duration`

`tmxrasterizer --advance-animations {x+1} "{Tiled-File}" "{Png Files}"`

`magick -delay {x/10} -loop 0 *.png {outfile}`

## Stuff that I need to do

- [ ] ignoring UI when using arguments
- [ ] proper error handling
- [ ] Build Pipeline for Pyinstaller
