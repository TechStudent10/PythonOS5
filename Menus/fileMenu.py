from tkinter import Menu
if __name__ == "__main__":
	from menu import VmMenu
else:
	from Menus.menu import VmMenu

class FileMenu(VmMenu):
	def __init__(self, parent, **kw):
		super().__init__(parent, name="File", **kw)

		self.add_command(label="New VM", command=lambda: print("Command"))