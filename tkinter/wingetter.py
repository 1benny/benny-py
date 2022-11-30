import tkinter as tk
from tkinter import *
import os
import requests
import subprocess as sub

def winget():
    package = entry1.get()
    results = os.system(f"winget search {package}")
    pro = sub.Popen('./wingetter.py', stdout=sub.PIPE,stderr=sub.PIPE)
    output, errors = pro.communicate()
    text1.insert(END, output)
    return results


root = tk.Tk()
root.geometry("280x130")
root.title("Winget Runner")

label1 = tk.Label(root, text="Search for package", font=("Consolas", 9))
label1.place(x=13, y=1)

entry1 = tk.Entry(root, width=35, font=("Consolas", 9))
entry1.place(x=13, y=26)

button_search = tk.Button(root, text="Search", command=winget, font=("Consolas", 8))
button_search.place(x=160, y=2)

text1 = tk.Text(root, width=41, height=5, font=("Consolas", 8))
text1.place(x=13, y=50)

root.mainloop()