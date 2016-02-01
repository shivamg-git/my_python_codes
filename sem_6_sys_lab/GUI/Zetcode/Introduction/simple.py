#!/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import *

# inherited from Frame
class Example(Frame):
	def __init__(self,parent):
		Frame.__init__(self,parent,background="white")
		self.parent = parent
		self.initUI()

	def initUI(self):
		self.parent.title("Simple")
		self.pack(fill=BOTH,expand=1)

def main():
	root =Tk()
	root.geometry("250x250+300+300")
	app = Example(root)
	root.mainloop()

if __name__ == '__main__':
	main()