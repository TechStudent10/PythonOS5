if __name__ == "__main__":
    from Modules.window import Window
else:
    from .Modules.window import Window

from tkinter import *
from tkinter.scrolledtext import ScrolledText

class Logger(ScrolledText):
    def __init__(self, master, border=0, **kwargs):
        super().__init__(master, border=border, **kwargs)

        self.master = master
        self.border = border

        self.disableTyping()

    def log(self, log=""):
        self.enableTyping()
        self.insert(END, log+"\n")
        self.disableTyping()

    def enableTyping(self):
        self.config(state="normal")

    def disableTyping(self):
        self.config(state="disabled")

class Terminal(Window):
    def __init__(self, windowManager, taskbarBtn=None):
        super().__init__(windowManager, height=40, name="Terminal", iconPath="logo.png" if __name__ == "__main__" else "Apps\\Terminal\\logo.png")

        self.output = Logger(self.surface)
        self.output.pack(fill=BOTH, expand=1)

        if taskbarBtn != None:
            self.taskbarBtn = taskbarBtn

        self.output.configure(bg="black", fg="white", font=("Calibri", 12))

        self.output.log("Welcome to Terminal! \nType 'help' to get help on the commands.")

        self.output.log("")

        self.commandVar = StringVar()

        self.commandFrame = Frame(self.surface)
        self.commandFrame.pack(fill=X, expand=1)
        Label(self.commandFrame, text="Console> ", font=("Calibri", 12), bg="black", fg="white").pack(side="left")
        self.commandEntry = Entry(self.commandFrame, textvariable=self.commandVar, bg="black", fg="white", font=('calibri', 12), border=0, insertbackground="white", highlightbackground="black", highlightthickness=0)
        self.commandEntry.pack(fill=X, expand=1, side='left')

        self.commandEntry.bind("<Return>", self.executeCommand)

    def configCostum(self, **kw):
        for kwarg in kw:
            if kwarg == 'taskbarBtn':
                self.taskbarBtn = kw.get('taskbarBtn')

    def execute(self, line):
        if line[:5] == "echo ":
            text = line.replace("echo ", "")
            self.output.log(text)
        elif line[:4] == "help":
            self.output.log("Help command still in progress.")
        elif line[:4] == "exit" or line[:4] == "quit":
            self.destroy()
            try:
                self.taskbarBtn.destroy()
            except:
                pass
        elif "switch user" in line.lower():
            user = "MakingMaster8"
            self.output.log("User switched to {user}".format(user=user))
        else:
            if line == "":
                pass
            else:
                self.output.log("Command not found.")

    def executeCommand(self, e):
        command = self.commandEntry.get()
        self.commandEntry.delete(0, END)
        self.output.log("Console> " + command)
        self.execute(command)

def main():
    win = Tk()
    win.config(bg="orange")
    win.wm_attributes("-fullscreen", 1)

    mainWin = Terminal(win)
    mainWin.pack()

    win.mainloop()

if __name__ == "__main__":
    main()
