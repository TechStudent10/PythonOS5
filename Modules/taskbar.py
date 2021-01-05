"""
Taskbar for the operating system
Author: TechStudent10
Email: mohammeddam1@outlook.com
"""

from tkinter import *

class Taskbar(Frame):
    def __init__(self, screen, bg="black", **kw):
        super().__init__(screen, bg=bg, **kw)

        self.btnXAdd = 100
        self.btnX = -self.btnXAdd

        self.width = screen.winfo_screenwidth()
        self.bg = bg

        self.config(width=self.width, height=40)
        self.pack(side=BOTTOM, fill=X)

    def getX(self):
        self.btnX += self.btnXAdd
        return self.btnX