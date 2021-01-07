from tkinter import *
from vm import VM
from main import MainScreen
from classes import Screen, Menus

import os

class VmSpawner:
	def __init__(self):
		self.vms = []

	def spawn(self, master):
		vm = MainScreen(master)
		self.vms.append(vm)
		vm.run()

class VmButton(Frame):
	pass

class MainWindow(Tk):
	def __init__(self):
		super().__init__()

		self.vmNumber = 0
		self.openVMs = {}
		self.vmSpawner = VmSpawner()

		self.vmsFrame = Frame(self)
		self.vmsFrame.pack(fill=BOTH, expand=1)

		self.vms = os.listdir("VMs")
		if len(self.vms) == 0:
			self.vms = ["VM 1"]

		self.vmBtns = []

		for vm in self.vms:
			VM(vm)
			btn = Button(self.vmsFrame, text=vm, command=self.openVm)
			btn.pack()
			self.vmBtns.append(btn)
		
		self.loadMenu()

	def openVm(self):
		self.vmsFrame.destroy()

		operatingSystem = MainScreen(self)
		operatingSystem.run()

		self.config(menu="")

		self.geometry("1200x700")
		self.resizable(False, False)

	def loadMenu(self):
		self.menu = Menus(self)

def main():
	window = MainWindow()
	window.mainloop()

if __name__ == '__main__':
	main()