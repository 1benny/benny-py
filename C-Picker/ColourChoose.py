import tkinter as tk
from tkinter import LEFT, ttk
from tkinter.colorchooser import askcolor
from turtle import left

root = tk.Tk()
root.geometry("320x190")


def change_colour():
    colours = askcolor(title="Colour Selection")
    button1.configure(bg=colours[1])
    print(colours.index)


label = tk.Label(root, text="Pick a color and return it's", font=("Consolas", 12))
label.pack()
label2 = tk.Label(root, text="Hex Value", font=("Consolas", 12))
label2.pack()
label3 = tk.Label(root, text="↓")
label3.pack()
button1 = tk.Button(root, padx=70, pady=10, command=change_colour)
button1.pack(expand=True)

newhex_label = tk.Label(root)
newhex_label.place(x=123, y=160)

root.mainloop()
