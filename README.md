# Tiled-Gif-Export

## Setup

Requirements:
- [Tiled Editor](https://www.mapeditor.org/)
- [ImageMagick](https://imagemagick.org/index.php)

A `config.ini` gets generated automatically.

If you do not have Tiled or ImageMagick in $PATH, you need to change the paths in that config.
Frame time is set to 100 ms by default. You can update this accordingly. The value has to be cleanly devisible by 10 to work the way I wrote it.

## Basic Commands used

`x: frame duration`

`tmxrasterizer --advance-animations {x+1} "{Tiled-File}" "{Png Files}"`

`magick -delay {x/10} -loop 0 *.png {outfile}`