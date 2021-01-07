from tkinter import Menu
from Menus.fileMenu import FileMenu

class Menus(Menu):
	def __init__(self, master):
		super().__init__(master)
		master.config(menu=self)
		self.fileMenu = FileMenu(self)
		self.add_cascade(label=self.fileMenu.name, menu=self.fileMenu)