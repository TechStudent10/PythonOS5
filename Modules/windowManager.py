"""
Window Manager for the operating system
Author: TechStudent10
Email: mohammeddam1@outlook.com
"""

from tkinter import *
from PIL import Image, ImageTk
from .taskbarBtn import TaskbarButton

class WindowManager(Frame):
    def __init__(self, master, taskbar, **kwargs):
        super().__init__(**kwargs)

        self.master = master
        self.taskbar = taskbar

        self.windows = {}

    def createWindow(self, window):
        '''
        Adds a window to WindowManager
        :param window: Window
        :return: None
        '''
        window.place(x=window.x, y=window.y)
        taskbarBtn = TaskbarButton(self.taskbar, text=window.name)  # , image=window.image)
        taskbarBtn.config(command=lambda: window.minimize(taskbarBtn))
        window.taskbarBtn = taskbarBtn
        self.windows[window.name] = {'taskbarBtn': taskbarBtn, 'window': window, 'icon_path': window.icon_path}

    def getWindows(self):
        '''
        Returns all windows added to the window manager
        :return: dict
        '''
        return self.windows
