from tkinter import *
from PIL import Image, ImageTk

class Window(Frame):
    def __init__(self, master, width=25, height=25, bg=None, title="", topbarBg="grey", iconPath=None, taskbarBtn=None, **kw):
        super().__init__(master, width=width, height=height, bg=bg, **kw)

        self.x = 0
        self.y = 0

        self.width = width
        self.height = height
        self.bg = bg
        self.title = title
        self.name = title
        self.topbarBg = topbarBg
        self.icon = False

        if taskbarBtn != None:
            self.taskbarBtn = taskbarBtn

        self.grip = Label(self, text=self.title, bg=topbarBg if bg != "grey" else "white" if bg != "white" else "black", width=width)
        self.packGrip()

        self.bindMovement()

        self.exitBtn = Button(self, text="X", command=self.destroy, bd=200000000000000000000000000000000000, bg=topbarBg)
        self.maximizeBtn = Button(self, text="|_|", command=self.maximize, bd=200000000000000000000000000000000000, bg=topbarBg)
        #self.minimizeBtn = Button(self, text="X", command=self.destroy)
        """
        if iconPath is not None or iconPath != "":
            self.icon_path = iconPath
            self.icon = True
            #self.icon_path = open(self.icon_path, "r")
            self.image = ImageTk.PhotoImage(Image.open(self.icon_path))
            #self.icon_path.close()
        else:
            self.icon_path = "default.png" if __name__ == "__main__" else "Modules\\default.png"
            self.icon = True
            self.image = ImageTk.PhotoImage(Image.open(self.icon_path))

        self.windowIcon = ImageTk.PhotoImage(Image.open("default.png" if iconPath is not None or iconPath != "" else iconPath).resize((20, 20)))

        Label(self, image=self.windowIcon).place(x=0, y=0)
        """

        self.exitBtn.place(relx=1, x=0, y=-1, anchor=NE)
        #self.maximizeBtn.place(relx=0.9, x=0, y=-1, anchor=NE)

        self.surface = Frame(self, bg=bg)
        self.surface.pack(expand=1)

        # Uncomment below if you want to add an icon
        """
        if self.icon:
            self.icon = ImageTk.PhotoImage(Image.open(self.iconPath))
            Label(self, image=self.icon).place(x=0, y=0)
        """

    def run(self):
        self.build()
        return self

    def build(self):
        Label(self.surface, text="I am in the build method.").pack()

    def packGrip(self):
        self.grip.pack(side=TOP, fill=X, expand=1)

    def configCostum(self, **kw):
        for kwarg in kw:
            if kwarg == 'taskbarBtn':
                self.taskbarBtn = kw.get('taskbarBtn')

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

    def minimize(self, btn):
        self.place_forget()
        btn.config(command=lambda: self.un_minimize(btn))

    def un_minimize(self, btn):
        self.place(x=self.x, y=self.y)
        btn.config(command=lambda: self.minimize(btn))

    def destroy(self):
        super().destroy()
        try:
            self.taskbarBtn.destroy()
        except:
            pass

    def onclick(self, event):
        self._drag_start_x = event.x
        self._drag_start_y = event.y

    def onmove(self, event):
        self.x = self.winfo_x() - self._drag_start_x + event.x
        self.y = self.winfo_y() - self._drag_start_y + event.y
        self.place(x=self.x, y=self.y)

if __name__ == "__main__":
    win = Tk()
    win.wm_attributes("-fullscreen", 1)

    testWin = Window(win)
    testWin.pack()

    win.mainloop()