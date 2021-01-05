if __name__ == "__main__":
    from Modules.window import Window
else:
    from .Modules.window import Window

from tkinter import *
from PIL import Image, ImageTk

class Finder(Window):
    def __init__(self, windowManager):
        super().__init__(windowManager, name="Finder")
        Label(self.surface, text="This is my app!").pack()
        self.img = Image.open("logo.png" if __name__ == "__main__" else "Apps\\FileFinder\\logo.png")

        self.image = ImageTk.PhotoImage(self.img)

def main():
    mainScreen = Tk()
    mainScreen.config(bg="orange")
    mainScreen.wm_attributes("-fullscreen", 1)

    finder = Finder(mainScreen)
    finder.pack()

    mainScreen.mainloop()

if __name__ == "__main__":
    main()
