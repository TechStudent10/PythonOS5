from tkinter import Menu

class VmMenu(Menu):
	def __init__(self, parent, name="", tearoff=False, **kw):
		super().__init__(parent, tearoff=tearoff, **kw)
		self.name = name
		self.tearoff = tearoff