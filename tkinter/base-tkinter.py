import tkinter as tk
from tkinter import *

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

master = tk.Tk()
master.geometry()


canvas1 = Canvas(master)
canvas1.place()

entry1 = Entry(canvas1)
entry1.place()

button1 = Button(canvas1, command=None)
button1.place()


master.mainloop()