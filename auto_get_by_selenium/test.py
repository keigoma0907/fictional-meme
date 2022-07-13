import tkinter
from tkinter import *
from tkinter import simpledialog


class CustomDialog(simpledialog.Dialog):
	def __init__(self,master,title = None) -> None:
		super(CustomDialog,self).__init__(parent = master,title = title)

	def body(self,master) -> None:
		self.label: label = Label(master,text = '取得中です。')
		self.label.grid(column = 0,row = 0)

		def buttonbox(self):
			box = Frame(self)

			self.button1 = Button(box,text = "OK",width = 10,command = self.ok,state = DISABLED)
			self.button1.pack(side = LEFT,padx = 5,pady = 5)
			self.button2 = Button(box,text = "Cancel",width = 10,command = enable)
			self.button2.pack(side = LEFT,padx = 5,pady = 5)

			box.pack()

		def enable(self):
			self.button1['state'] = NORMAL


if __name__ == "__main__":
	root = tkinter.Tk()


	def display_dialog():
		CustomDialog(root)


	button = Button(root)
	button["text"] = "データ取得"
	button["command"] = display_dialog
	button.grid(column = 0,row = 0,padx = 10,pady = 10)

	root.mainloop()
