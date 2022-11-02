import tkinter as tk
from math import *

def evaluate(event):
    res.configure(text = "Result: " + str(eval(entry1.get())))
    
root = tk.Tk()
root.geometry("250x100")
root.title("Calc")

tk.Label(root, text="Enter Expression:").pack()


entry1 = tk.Entry(root)
entry1.bind("<Return>", evaluate)
entry1.pack()


res = tk.Label(root)
res.pack()


root.mainloop()