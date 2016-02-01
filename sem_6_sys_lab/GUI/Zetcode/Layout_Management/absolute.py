#!/usr/bin/python
# -*- coding: utf-8 -*-
from PIL import Image, ImageTk
from Tkinter import Tk, Label, BOTH
from ttk import Frame, Style

class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
        self.parent = parent
        self.initUI()

        
    def initUI(self):
      
        self.parent.title("Absolute positioning")
        self.pack(fill=BOTH, expand=1)
        
        Style().configure("TFrame", background="#333")
        
        bard = Image.open("image1.jpg")
        bard = bard.resize((250, 250), Image.ANTIALIAS)
        bardejov = ImageTk.PhotoImage(bard)
        label1 = Label(self, image=bardejov)
        label1.image = bardejov
        label1.place(x=20, y=20)
        
        rot = Image.open("image2.jpg")
        rot = rot.resize((250, 250), Image.ANTIALIAS)
        rotunda = ImageTk.PhotoImage(rot)
        label2 = Label(self, image=rotunda)
        label2.image = rotunda
        label2.place(x=40, y=160)        
        
        minc = Image.open("image3.jpg")
        minc = minc.resize((250, 250), Image.ANTIALIAS)
        mincol = ImageTk.PhotoImage(minc)
        label3 = Label(self, image=mincol)
        label3.image = mincol
        label3.place(x=170, y=50)        
              

def main():
  
    root = Tk()
    root.geometry("500x500+100+100")
    app = Example(root)
    root.mainloop()  

if __name__ == '__main__':
    main()  