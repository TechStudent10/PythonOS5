import os

from classes import *
from Apps.Terminal.terminal import Terminal
from Apps.FileFinder.finder import Finder
from PIL import Image, ImageTk

from threading import Thread


class AppsMenu(AppMenu):
    def __init__(self, master, wmManager, apps, appsMenuButton):
        super().__init__(master)

        self.wmManager = wmManager
        self.apps = apps
        self.appsMenuButton = appsMenuButton

    def showApps(self):
        for app in self.apps:
            app = self.apps.get(app)
            image = ImageTk.PhotoImage(Image.open(app.get('icon_path')))
            self.image = image
            win = app.get('window')(self.wmManager)
            HoverButton(self, activebackground="grey", bd=200000000000000000000000000000000000000000000000, image=image,
                        bg=self.bg, compound="top", text="Terminal", fg="white",
                        command=lambda: self.showAppFromAppMenu(win)).place(x=50, y=50)

    def showApplicationFromAppsMenu(self, window):
        self.wmManager.createWindow(window)
        self.destroyAppsMenu()

    def showAppFromAppMenu(self, win):
        self.showApplicationFromAppsMenu(win)
        win.configCostum(taskbarBtn=self.wmManager.windows.get(win.name).get('taskbarBtn'))

    def showAppsMenu(self):
        self.show()
        self.appsMenuButton.config(command=self.destroyAppsMenu)
        self.showApps()

    def destroyAppsMenu(self):
        self.disappear()
        self.appsMenuButton.config(command=self.showAppsMenu)


class AppMenuButton(HoverButton):
    def __init__(self, master, activebackground="grey", bd=200000000000000000000000000000000000000000000000, image=None,
                 bg="black", compound="top", text="App", fg="white", command=lambda: print("App")):
        super().__init__(master, activebackground=activebackground, bd=bd, image=image, bg=bg, compound=compound,
                         text=text, fg=fg, command=command)

        self.master = master
        self.activebackground = activebackground
        self.bd = bd
        self.image = image
        self.bg = bg
        self.compound = compound
        self.text = text
        self.fg = fg
        self.command = command


class DesktopButton(HoverButton):
    def __init__(
            self,
            master,
            text="",
            image=None,
            compound="top",
            activebackground="grey",
            bd=2000000000000000000000000000000000000,
            **kw
    ):
        super().__init__(master, text=text, image=image, compound=compound, activebackground=activebackground, bd=bd,
                         **kw)

        self.master = master
        self.text = text
        self.image = ImageTk.PhotoImage(Image.open("Modules\\default.png")) if image == None else image
        self.compound = compound
        self.activebackground = activebackground
        self.bd = bd


class Spawner:
    def __init__(self):
        self.spawnedWindows = {}

    def spawn(self, windowManager, windowRef, **kw):
        win = windowRef(windowManager, **kw)
        windowManager.createWindow(win)
        win.configCostum(taskbarBtn=windowManager.windows.get(win.name).get('taskbarBtn'))

        self.spawnedWindows[win.name] = win

        return win


class TerminalSpawner(Spawner):
    def spawn(self, windowManager, **kw):
        terminal = super().spawn(windowManager, Terminal, **kw)
        return terminal


class FinderSpawner(Spawner):
    def spawn(self, windowManager, **kw):
        finder = super().spawn(windowManager, Finder, **kw)
        return finder


'''
NameOfApp = 'Whatever your app name is with a capitalized beginning'
FunctionOfApp = 'The class that you used to make your app'
class [NameOfApp]Spawner(Spawner):
    def spawn(self, windowManager, **kw):
        [NameOfApp] = super().spawn(windowManager, [FunctionOfApp], **kw)
'''


class MainScreen(Screen):
    def __init__(self):
        super().__init__()

        self.taskbar = Taskbar(self)
        self.taskbar.pack(side="bottom", fill=X)
        self.wmManager = WindowManager(self, self.taskbar)
        self.loadWindowManager()
        self.appsMenu = AppMenu(self)

        self.terminalSpawner = TerminalSpawner()
        self.fileFinderSpawner = FinderSpawner()
        self.spawner = Spawner()

        self.appsMenuButton = TaskbarButton(self.taskbar, text="Apps", width=5, command=self.showAppsMenu)
        self.appsMenu.taskbarButton = self.appsMenuButton

        self.image = ImageTk.PhotoImage(Image.open("Apps\\Terminal\\logo.png"))
        DesktopButton(self, text="Terminal", image=self.image,
                      command=lambda: self.showApp(self.terminalSpawner)).place(x=25, y=25)
        self.loadWindowManager()
        self.loadWindowManager()

    def run(self):
        super().run()

    def showAppsMenu(self):
        self.appsMenu.show()
        self.appsMenuButton.config(command=self.destroyAppsMenu)
        self.showAppMenuContents()

    def showAppMenuContents(self):
        """
        image = ImageTk.PhotoImage(Image.open("Apps\\Terminal\\logo.png"))
        self.image = image
        AppMenuButton(self.appsMenu, image=image,
                      bg=self.appsMenu.bg, text="Terminal",
                      command=lambda: self.showApplicationFromAppsMenu(self.terminalSpawner)).place(x=50, y=50)

        image = ImageTk.PhotoImage(Image.open("Apps\\FileFinder\\logo.png"))
        self.image = image
        AppMenuButton(self.appsMenu, image=image,
                      bg=self.appsMenu.bg, text="File Finder",
                      command=lambda: self.showAppUsingSpawnerFromAppsMenuRef(self.fileFinderSpawner)).place(x=150, y=70)
        """
        terminalButton = self.showAppMenuButton(
            "Terminal",
            "Apps\\Terminal\\logo.png",
            lambda: self.showApplicationFromAppsMenu(
                self.terminalSpawner
            )
        )
        terminalButton.place(x=50, y=50)

        fileFinderButton = self.showAppMenuButton(
            "File Finder",
            "Apps\\FileFinder\\logo.png",
            lambda: self.showAppUsingSpawnerFromAppsMenuRef(
                self.fileFinderSpawner
            )
        )
        fileFinderButton.place(x=150, y=70)

    def showAppMenuButton(self, buttonName, buttonImage, menuButtonOnClicked):
        image = ImageTk.PhotoImage(Image.open(buttonImage))
        self.image = image
        return AppMenuButton(self.appsMenu, image=image,
                             bg=self.appsMenu.bg, text=buttonName,
                             command=menuButtonOnClicked)

    def showApplicationFromAppsMenu(self, spawner, **kw):
        spawner.spawn(self.wmManager, **kw)
        self.destroyAppsMenu()

    def showAppUsingSpawnerRef(self, spawner, ref=None, **kw):
        spawner.spawn(self.wmManager, **kw) if ref is None else spawner.spawn(self.wmManager, ref, **kw)

    def showAppUsingSpawnerFromAppsMenuRef(self, spawner, ref=None, **kw):
        self.showAppUsingSpawnerRef(spawner, ref, **kw)
        self.destroyAppsMenu()

    def showApp(self, spawner, **kw):
        spawner.spawn(self.wmManager, **kw)

    def showAppRef(self, ref, **kw):
        self.spawner.spawn(self.wmManager, ref, **kw)

    def showAppRefFromAppMenu(self, ref, **kw):
        self.spawner.spawn(self.wmManager, ref, **kw)
        self.destroyAppsMenu()

    def all_children(self, wid):
        _list = wid.winfo_children()

        for item in _list:
            if item.winfo_children():
                _list.extend(item.winfo_children())

        return _list

    def destroyAppsMenu(self):
        self.appsMenu.disappear()
        self.appsMenuButton.config(command=self.showAppsMenu)

    def loadWindowManager(self):
        self.wmManager.pack(fill=BOTH, expand=1, side="top")


def main():
    operatingSystem = MainScreen()
    operatingSystem.run()


if __name__ == "__main__":
    main()
