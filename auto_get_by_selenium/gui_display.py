from tkinter import *
from tkinter import ttk


def display(time):
	root = Tk()
	root.title('表示')

	root.geometry("250x90")

	label1 = ttk.Label(
		root,
		text = f'今月の残業時間は{time}'
	)
	label1.pack(padx = 20,pady = 10)

	button1 = ttk.Button(
		root,
		text = 'Check',
		command = lambda: root.quit())
	button1.pack(padx = 20,pady = 10)

	button2 = ttk.Button(
		root,
		text = 'OK',
		command = lambda: root.quit())
	button2.pack(padx = 20,pady = 10)

	root.mainloop()
