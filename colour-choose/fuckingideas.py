from curses import use_default_colors
from importlib.metadata import entry_points
import tkinter as tk
from tkinter import * 


root = tk.Tk()

# Maybe 2 functions one for grabbing and computing the original value and one of displaying it
#def riphex():
#    rip_it = 
#    xxxx = store it in a variable to use later
#    compute the hex number with the variable then store that
#    in a variable.

def compute(r, g, b):
    return ("{:X}{:X}{:X}").format(r, g, b)



def put_it_in():
    val = hex_computed
label1 = tk.Label(text=f"{val}, is your value")

entry1 = tk.Entry(root)
entry1.pack()

button1 = tk.Button(root, text="compute", command=hexxit)
button1.pack()

label1 = tk.Label(root)
label1.pack()


root.mainloop()