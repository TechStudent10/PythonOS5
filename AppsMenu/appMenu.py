from tkinter import *

if __name__ == "__main__":
    from menu import AppMenuFrame
else:
    from .menu import AppMenuFrame

import sys

class Bar(Frame):
    def __init__(self, master, bg="grey"):
        super().__init__(master, bg=bg)

        self.master = master

class AppMenu(AppMenuFrame):
    def __init__(self, master):
        super().__init__(master)

        self.master = master
        self.taskbarButton = None

        self.disappear()

    def show(self):
        self.place(x=0, y=0, relx=0.5, rely=0.5, anchor="center")

    def disappear(self, e=None):
        self.place_forget()
