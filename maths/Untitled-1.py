from tkinter import *
import tkinter as tk
from math import *
import math as m



#calculation as global variable so we can manipulate it inside of the function
def add_symbol(symbol):
    global calculation
    calculation += str(symbol)
    input_field.delete(1.0, "end")
    input_field.insert(1.0, calculation)


#For evaluating the string input. eg. "10 - 3*(9+4**2)"
def eval_input():
    global calculation
    try:
        calculation = str(eval(calculation))
        input_field.delete(1.0, "end")
        input_field.insert(1.0, calculation)
    except:
        clearthebox()
        input_field.insert(1.0, "error")


#For clearing the input_field
def clearthebox():
    global calculation
    calculation = ""
    input_field.delete(1.0, "end")


root = tk.Tk()
root.geometry("430x270")
root.title("Calculator")
root.resizable(False, False)

#canvas1 = tk.Canvas(root, height=270, width=430, bg="#bcbcbc")
#canvas1.grid(columnspan=5)


input_field = tk.Text(root, height=1.4, width=36, font=("JetBrains Mono", 15))
input_field.grid(columnspan=5)

b1 = tk.Button(root, text="Mod", command=lambda: add_symbol("+"), height=1, width=5, font=("JetBrains Mono", 15))
b1.grid(row=2, column=0)
b2 = tk.Button(root, text="GCD", command=lambda: add_symbol("+"), height=1, width=5, font=("JetBrains Mono", 15))
b2.grid(row=2, column=1)
b3 = tk.Button(root, text="LCM", command=lambda: add_symbol("+"), height=1, width=5, font=("JetBrains Mono", 15))
b3.grid(row=2, column=2)
b4 = tk.Button(root, text="Totient", command=lambda: add_symbol("+"), height=1, width=5, font=("JetBrains Mono", 15))
b4.grid(row=3, column=0)
b5 = tk.Button(root, text="^", command=lambda: add_symbol("+"), height=1, width=5, font=("JetBrains Mono", 15))
b5.grid(row=3, column=1)
b6 = tk.Button(root, text="+", command=lambda: add_symbol("+"), height=1, width=5, font=("JetBrains Mono", 15))
b6.grid(row=3, column=2)
b7 = tk.Button(root, text="-", command=lambda: add_symbol("+"), height=1, width=5, font=("JetBrains Mono", 15))
b7.grid(row=4, column=0)
b8 = tk.Button(root, text="/", command=lambda: add_symbol("+"), height=1, width=5, font=("JetBrains Mono", 15))
b8.grid(row=4, column=1)
b9 = tk.Button(root, text="*", command=lambda: add_symbol("+"), height=1, width=5, font=("JetBrains Mono", 15))
b9.grid(row=4, column=2)
b0 = tk.Button(root, text="//", command=lambda: add_symbol("+"), height=1, width=5, font=("JetBrains Mono", 15))
b0.grid(row=5, column=1)



root.mainloop()