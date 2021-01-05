from tkinter import *

class AppMenuFrame(Frame):
    def __init__(self, master, width=900, height=500, bg="black"):  # Change the width to something else.
        super().__init__(master, width=width, height=height, bg=bg)

        self.width = width
        self.height = height
        self.bg = bg

        self.place(x=0, y=0, relx=0.5, rely=0.5, anchor="center")
