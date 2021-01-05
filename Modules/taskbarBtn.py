"""
Button for the taskbar
Author: TechStudent10
Email: mohammeddam1@outlook.com
"""

from tkinter import *
from .hoverButton import HoverButton

class TaskbarButton(HoverButton):
    def __init__(self, taskbar, width=15, activebackground="grey", bd=20000000000000000000000000000, bg="black", fg="white", **kw):
        super().__init__(taskbar, width=width, activebackground=activebackground, bd=bd, bg=bg, fg=fg, **kw)

        self.taskbar = taskbar
        self.width = width
        self.activebackground = activebackground
        self.bd = bd
        self.bg = bg
        self.fg = fg

        self.height = 2
        self.config(width=self.width, height=self.height)

        self.place(x=self.taskbar.getX(), y=0)