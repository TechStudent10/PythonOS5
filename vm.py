import os

class VM:
	def __init__(self, vmName: str):
		self.vmName = vmName

		if self.vmName in os.listdir("VMs"):
			self.vm = self.vmName
		else:
			self.vm = self.createVm(self.vmName)

	def createVm(self, name):
		os.mkdir(os.path.join("VMs", name))