"""
from tkinter import *

class DraggableWidget(Frame):
    def __init__(self, master, width=25, height=500, bg=None, name="", **kw):
        super().__init__(master, width=width, height=height, bg=bg, **kw)

        self.grip = Label(self, text=name, bg="grey" if bg != "grey" else "white" if bg != "white" else "black", width=width)
        self.grip.pack(side=TOP, fill=X, expand=1)

        self.grip.bind("<Button-1>", self.onclick)
        self.grip.bind("<B1-Motion>", self.onmove)

        self.surface = Frame(self, bg=self.grip["bg"])
        self.surface.pack(expand=1)

    def onclick(self, event):
        # print("Clicked")

        # widget = event.widget
        self._drag_start_x = event.x
        self._drag_start_y = event.y

    def onmove(self, event):
        # print("Moving")

        # widget = event.widget
        x = self.winfo_x() - self._drag_start_x + event.x
        y = self.winfo_y() - self._drag_start_y + event.y
        '''
        if x < 0:
            if y > self.winfo_width():
                self.place(x=0, y=0)
            else:
                self.place(x=0, y=y)
        else:
            self.place(x=x, y=0)
        '''
        self.place(x=x, y=y)

if __name__ == "__main__":
    win = Tk()

    win.wm_attributes("-fullscreen", 1)

    dw = DraggableWidget(win, name="TestWin")
    dw.pack()

    surface = Frame(dw.surface, bg=dw.surface["bg"])
    surface.pack(expand=1)

    Label(surface, text="Hi").pack()

    win.mainloop()
"""

"""
import importlib
main = importlib.import_module("main")
screen = main.MainScreen()
screen.run()
"""