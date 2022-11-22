import tkinter as tk
from tkinter import *
import requests

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

class Manager:
    def __init__(self, user, passwd, keywd):
        self.user = user
        self.passwd = passwd
        self.keywd = keywd

    def build(self):
        user = user_entry.get()
        passwd = pass_entry.get()
        keywd = key_entry.get()
        new_cred = '{}\n{}\n{}\n'.format(user, passwd, keywd)
        label_insert.configure(text=new_cred)


master = tk.Tk()
master.title("Credential Store")
master.geometry("300x420")

canvas1 = tk.Canvas(master, bg="#D3D3D3")
canvas1.place(relwidth=0.96, relheight=0.96, relx=0.02, rely=0.02)

label1 = tk.Label(canvas1, text="Enter credentials to store:", font=("Consolas", 9), bg="#D3D3D3")
label1.place(x=2, y=2)

user_label = tk.Label(canvas1, text="Username:", font=("Consolas", 9), bg="#D3D3D3").place(x=2, y=23)
pass_label = tk.Label(canvas1, text="Password:", font=("Consolas", 9), bg="#D3D3D3").place(x=2, y=48)
key_label = tk.Label(canvas1, text="Keyword:", font=("Consolas", 9), bg="#D3D3D3").place(x=2, y=73)

user_entry = tk.Entry(canvas1)
user_entry.place(x=70, y=25)

pass_entry = tk.Entry(canvas1)
pass_entry.place(x=70, y=50)

key_entry = tk.Entry(canvas1)
key_entry.place(x=70, y=75)

build_button = tk.Button(canvas1, text="Build credential   ", font=("Consolas", 8), command=Manager.build(), height=0, width=19)
build_button.place(x=70, y=100)

label_insert = tk.Label(canvas1, font=("Consolas", 9), bg="#D3D3D3")
label_insert.place(x=2, y=120)

master.mainloop()

