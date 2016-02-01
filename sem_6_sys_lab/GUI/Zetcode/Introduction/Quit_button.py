#!/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import Tk, BOTH
from ttk import Frame, Button, Style

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)   
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Quit button")
        
        # Styling the frame 
        self.style = Style()
        self.style.theme_use("default")
        self.pack(fill=BOTH, expand=1)

        quitButton = Button(self, text="Quit",command=self.quit)
        quitButton.place(x=100, y=100)


def main():
  
    root = Tk()
    root.geometry("250x250+300+300")
    app = Example(root)
    root.mainloop()  


if __name__ == '__main__':
    main()