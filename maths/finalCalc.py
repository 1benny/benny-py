from tkinter import *
import tkinter as tk

from math import *
import math as m

root = tk.Tk()
root.title("calculator")
root.configure(height=340, width=270)



calculation = ""

def add_to_calc(symbol):
    global calculation
    calculation += str(symbol)
    text_res.delete(1.0, "end")
    text_res.insert(1.0, calculation)


def compute():
    global calculation
    try:
        print(calculation)
        result = str(eval(calculation))
        text_res.delete(1.0, "end")
        text_res.insert(1.0, result)
    except:
        clearthebox()
        text_res.insert(1.0, "error")


def clearthebox():
    global calculation
    calculation = ""
    text_res.delete(1.0, "end")



canvas = tk.Canvas(root, height=340, width=270, bg="#bcbcbc")
canvas.pack()


frame = tk.Frame(root, bg="#999999")
frame.place(relheight=0.07, relwidth=0.89, relx=0.057, rely=0.04)


inplabel = tk.Label(frame, text=">>", bg="#999999")
inplabel.pack(side=LEFT)


text_res = tk.Text(frame, font=("JetBrains Mono", 13))
text_res.pack()


calc = tk.Button(root, text="Calculate", padx=40, 
                pady=1, fg="white", bg="#bcbcbc", command=compute)
calc.pack(side=LEFT)

clear = tk.Button(root, text="Clear", padx=50, pady=1, fg="white", bg="#bcbcbc", command=clearthebox)
clear.pack(side=RIGHT)

b1 = tk.Button(canvas, text="5", command=lambda: add_to_calc(5), width=5, font=("JetBrains Mono", 12))
b1.pack()


root.mainloop()