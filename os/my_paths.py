import tkinter as tk
from tkinter import *
import subprocess as sub
import sys
import customtkinter
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

master = tk.Tk()
master.geometry("700x300")

class Redirect:
    def __init__(self, widget):
        self.widget = widget
    
    def write(self, text):
        self.widget.insert('end', text)


class Ben(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        frame1 = Frame()
        frame1.pack()
       
        self.button1 = Button(text="Search", command=self.clicked)
        self.button1.pack(pady=10)
        
        h_scroll = Scrollbar(frame1, orient='horizontal')
        h_scroll.pack(side='bottom', fill=X)

        self.text1 = Text(width=100, height=30, wrap='none')
        self.text1.pack()
        self.text1.config(xscrollcommand=h_scroll.set)
        
        h_scroll.config(command=self.text1.xview)

    def clicked(self):
        p = sub.getoutput("winget search 7zip")
        self.text1.insert('end', p)
        self.text1.delete(1.0)
    

if __name__ == "__main__":
    app = Ben()
    app.mainloop()