import sys
from tkinter import *
import tkinter as tk
import os
import subprocess as sub

def doit():
    p = sub.getoutput("winget search spotify")
    text1.insert(1.0, p)
    text1.delete(1.0, 2.0)

root = tk.Tk()
root.geometry("700x500")

frame1 = Frame(root)
frame1.place(relwidth=0.8, relheight=0.8)

h_scroll = Scrollbar(frame1, orient="horizontal")
h_scroll.pack(side=BOTTOM, fill=X)

text1 = Text(frame1, font=("Consolas", 7), wrap='none', xscrollcommand=h_scroll.set)
text1.place(x=0, y=30)

h_scroll.config(command=text1.xview)

button1 = Button(frame1, text="Click this", command=doit)
button1.place(x=0, y=0)


root.mainloop()