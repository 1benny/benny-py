from tkinter import *
import tkinter as tk
from unittest import result


def conf_label(event):
    the_exp = entry1.get().format()
    label2.configure(text=str(conf_label))
    return conf_label


root = tk.Tk()
root.geometry("200x100")


label1 = tk.Label(root, text="Enter value for testing: ", font=("Consolas", 10))
label1.pack(expand=TRUE)


entry1 = tk.Entry(root, bg="#BCBCBC")
entry1.pack(expand=TRUE)
entry1.bind("<Return>", conf_label)

button1 = tk.Button(text="Return", command=conf_label)

label2 = tk.Label(root)
label2.pack(side=BOTTOM)

root.mainloop()

