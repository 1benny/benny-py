import tkinter as tk
from tkinter import *
import subprocess as sub
from time import sleep
import threading


def ls():
    print(sub.getoutput("winget list"))
    sleep(4)
    print(f"\n\nFinished")
    return

def startlist():
    x = threading.Thread(target=ls)
    x.start()

    print(threading.active_count)
    sleep(3)
    return

def search():
    a = entry1.get()
    print(sub.getoutput(f"winget search {a}")) ## 2) <~~ After being called as target by "startsearch", line runs, which in this case gets output of "winget search"
    sleep(4)                                   ## 3) <~~ when "sleep" is called, Python switches its focus back to main thread. This can be done in opposite to return focus back to new thread again.
    print(f"\n\nFinished")
    
def startsearch():
    y = threading.Thread(target=search) ## I) <~~ Creates a new Thread with the new Thread's starting action being the target function"search"  
    y.start()                           ## 1) <~~ Starts the Thread, using the specified target function as its action.
    
    print(threading.active_count)
    sleep(0.5)

def install():
    return

def startinstall():
    return

root = tk.Tk()
root.geometry("400x400")
root.title("Winget Runner")

#label1 = tk.Label(root, text="Search for package", font=("Consolas", 9))
#label1.place(x=13, y=1)

#entry1 = tk.Entry(root, width=35, font=("Consolas", 9))
#entry1.place(x=13, y=26)

entry1 = tk.Entry(root, font=("Consolas", 10))
entry1.pack(padx=10, pady=0)

btn1 = tk.Button(root, text="list", command=startlist, font=("Consolas", 14))
btn1.pack(padx=10, pady=0)

btn2 = tk.Button(root, text="search", command=startsearch, font=("Consolas", 14))
btn2.pack(padx=10, pady=0)

btn3 = tk.Button(root, text="install", command=startinstall, font=("Consolas", 14))
btn3.pack(padx=10, pady=0)

#text1 = tk.Text(root, width=41, height=5, font=("Consolas", 8))
#text1.place(x=13, y=50)

root.mainloop()