import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename
from typing import Text

from settings import Settings

class UI:
    def __init__(self):
        self.isSubmit = False
    def showSettingsForm(self, settings: Settings):

        def showRasterizerFileDialog():
            rasterizer.delete(0, END)
            filename = askopenfilename()
            rasterizer.insert(0, filename)

        def showMagickFileDialog():
            magick.delete(0, END)
            filename = askopenfilename()
            magick.insert(0, filename)

        
        window = tk.Tk()
        window.title("tiled_gif_export.py")
        Label(window, text="Frame duration (ms)").grid(row=0, column=0)
        Label(window, text="Number of Frames").grid(row=1, column=0)
        Label(window, text="Input File").grid(row=2, column=0)
        Label(window, text="Output File").grid(row=3, column=0)
        duration = Entry(window)
        duration.grid(row=0, column=1)
        frames = Entry(window)
        frames.grid(row=1, column=1)
        infile = Entry(window)
        infile.grid(row=2, column=1)
        outfile = Entry(window)
        outfile.grid(row=3, column=1)

        Label(window, text="Tiled Rasterizer").grid(row=4, column=0)
        rasterizer = Entry(window)
        rasterizer.grid(row=4, column=1)
        rasterizer.insert(0, settings.rasterizer)
        Button(window, text="Browse", command=showRasterizerFileDialog).grid(row=4, column=2)

        Label(window, text="magick").grid(row=5, column=0)
        magick = Entry(window, text=settings.magick)
        magick.grid(row=5, column=1)
        magick.insert(0, settings.magick)
        Button(window, text="Browse", command=showMagickFileDialog).grid(row=5, column=2)


        def submit():
            settings.duration = duration.get()
            settings.frames = frames.get()
            settings.file = infile.get()
            settings.output = outfile.get()
            settings.rasterizer = rasterizer.get()
            settings.magick = magick.get()

            if not settings.isValid():
                tk.messagebox.showwarning("Values missing", "The values entered are not valid. Try again.")
                return

            self.isSubmit = True
            window.destroy()
        tk.Button(window, text="Submit", command=submit).grid(row=6, column=2)

        window.mainloop()
        return self.isSubmit
