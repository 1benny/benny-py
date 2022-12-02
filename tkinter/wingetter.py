import tkinter as tk
from tkinter import *
import subprocess as sub
from time import sleep
import threading


def ls():
    print(sub.getoutput("winget list"))
    sleep(1)
    print(f"\n\nFinished")
    return

def startit():
    x = threading.Thread(target=ls)
    x.start()
    print(threading.active_count)
    sleep(0.9)
    return



root = tk.Tk()
root.geometry("280x130")
root.title("Winget Runner")

label1 = tk.Label(root, text="Search for package", font=("Consolas", 9))
label1.place(x=13, y=1)

entry1 = tk.Entry(root, width=35, font=("Consolas", 9))
entry1.place(x=13, y=26)

button_search = tk.Button(root, text="Search", command=startit, font=("Consolas", 8))
button_search.place(x=160, y=2)

text1 = tk.Text(root, width=41, height=5, font=("Consolas", 8))
text1.place(x=13, y=50)

root.mainloop()