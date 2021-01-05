
import os, sys

name = input("Name of the app: ")
author = input("Author: ")

print("Checking paths")
paths = os.listdir()
if name in paths:
    print(f"{name} already exists in current directory.")
    sys.exit()

print(name + "/")
os.mkdir(name)
os.chdir(name)

print(name + "\\__init__.py")

init = open(os.path.join(name, "__init__.py"), "w")
init.write("# This is where you add all of your app imports.")
init.close()

print(name + "\\app.py")

app = open(os.path.join(name, "__init__.py"), "w")
app.write("# You can write your app code here.\nfrom .Modules.window import Window")
app.close()

os.mkdir("Modules")
os.chdir("Modules")

windowCode = """from tkinter import *

class Window(Frame):
    def __init__(self, master, width=25, height=25, bg=None, name="", topbarBg="grey", **kw):
        super().__init__(master, width=width, height=height, bg=bg, **kw)

        self.width = width
        self.height = height
        self.bg = bg
        self.name = name
        self.topbarBg = topbarBg

        self.grip = Label(self, text=name, bg=topbarBg if bg != "grey" else "white" if bg != "white" else "black", width=width)
        self.packGrip()

        self.bindMovement()

        self.exitBtn = Button(self, text="X", command=self.destroy, bd=200000000000000000000000000000000000, bg=topbarBg)
        self.maximizeBtn = Button(self, text="|_|", command=self.maximize, bd=200000000000000000000000000000000000, bg=topbarBg)
        #self.minimizeBtn = Button(self, text="X", command=self.destroy)
        
        self.exitBtn.place(relx=1, x=0, y=-1, anchor=NE)
        #self.maximizeBtn.place(relx=0.9, x=0, y=-1, anchor=NE)

        self.surface = Frame(self, bg=bg)
        self.surface.pack(expand=1)

    def packGrip(self):
        self.grip.pack(side=TOP, fill=X, expand=1)

    def unbindMovement(self):
        self.grip.unbind("<Button-1>")
        self.grip.unbind("<B1-Motion>")

    def bindMovement(self):
        self.grip.bind("<Button-1>", self.onclick)
        self.grip.bind("<B1-Motion>", self.onmove)

    def maximize(self):
        self.maximizeBtn.config(command=self.un_maximize)
        self.pack(fill=BOTH, expand=1)
        self.unbindMovement()
        self.packGrip()

    def un_maximize(self):
        self.config(width=self.width, height=self.height)
        self.pack()
        self.packGrip()
        self.bindMovement()
        self.maximizeBtn.config(command=self.maximize)

    def onclick(self, event):
        self._drag_start_x = event.x
        self._drag_start_y = event.y

    def onmove(self, event):
        x = self.winfo_x() - self._drag_start_x + event.x
        y = self.winfo_y() - self._drag_start_y + event.y
        self.place(x=x, y=y)

if __name__ == "__main__":
    win = Tk()
    win.wm_attributes("-fullscreen", 1)

    mainWin = Window(win)
    testWin.pack()
    
    Label(mainWin.surface, text="To put tk widgets on the main window, use the 'surface' variable defined in the Window class as the 'master' widget.").pack() 

    win.mainloop()"""

print(name + "\\Modules\\window.py")

window = open(os.path.join(name, "Modules", "window.py"), "w")
window.write(windowCode)
window.close()

print(name + "\\README.md")

readme = open(os.path.join(name, "README.md"), "w")
readme.write("# " + name)
readme.write("Name of app: " + name)
readme.write("Author: " + author)
readme.close()

print("Wrote 4 Files. \nProject build successfully.")