from time import sleep
import tkinter as tk
from tkinter import *


def loopit(): 
    i = 1
    while i < 20:
        print("\r /", end='')
        sleep(0.5)
        print("\r  ~", end='')
        sleep(0.5)
        print("\r   \\", end='')
        sleep(0.5)
        print("\r    |", end='')
        sleep(0.5)
        print("\r     /", end='')
        sleep(0.5)
        print("\r      ~", end='')
        sleep(0.5)
        print("\r       \\", end='')
        sleep(0.5)
        print("\r        |", end='')
        sleep(0.5)
        print("\r       \\ ", end='')
        sleep(0.5)
        print("\r      ~   ", end='')
        sleep(0.5)
        print("\r     /    ", end='')
        sleep(0.5)
        print("\r    |     ", end='')
        sleep(0.5)
        print("\r   \\     ", end='')
        sleep(0.5)
        print("\r  ~       ", end='')
        sleep(0.5)
        print("\r /        ", end='')
        sleep(0.5)
        print("\r|         ", end='')
        sleep(0.5)
        i += 1
    return

def ready():
    print("\rready... 3", end='')
    sleep(1)
    print("\rready... 2", end='')
    sleep(1)
    print("\rready... 1", end='')
    sleep(1)
    return



def immatryitout():
    print(l.get())



m = tk.Tk()
m.geometry("300x300")

l = tk.Entry(m, width=5, bg="#D3D3D3")
l.pack()

b = Button(m, command=immatryitout, width=5)
b.pack(pady=5)

m.mainloop()