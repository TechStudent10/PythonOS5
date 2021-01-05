"""
Main screen for operating system
Author: TechStudent10
Email: mohammeddam1@outlook.com
"""

from tkinter import *

class Screen(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1200x700")

        # self.wm_attributes("-fullscreen", 1)

    def run(self):
        self.mainloop()