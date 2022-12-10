import time, threading
from tkinter import *
from tkinter import messagebox

class App(object):
    def __init__(self, master):
        master.geometry("200x200")
        master.title("My GUI Title")
        lbCommand = Label(master, text="Hello world", 
                          font=("Courier New", 16)).place(x=20, y=20)

def InfiniteProcess():
    while not finish:
        print("Infinite Loop")
        time.sleep(7)

finish = False
Process = threading.Thread(target=InfiniteProcess)
Process.start()

mainWindow = Tk()
app = App(mainWindow)
mainWindow.mainloop()
#When the GUI is closed we set finish to "True"
finish = True
Process.join()