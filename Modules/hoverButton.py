"""
Tkinter Button that has a hover effect
Author: TechStudent10
Source: Stack Overflow: https://stackoverflow.com/questions/49888623/tkinter-hovering-over-button-color-change
Email: mohammeddam1@outlook.com
"""

from tkinter import *

class HoverButton(Button):
    def __init__(self, master, **kw):
        Button.__init__(self, master=master, **kw)
        self.defaultBackground = self["background"]
        self.activebackground = self["activebackground"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self.config(bg=self.activebackground)

    def on_leave(self, e):
        self.config(bg=self.defaultBackground)