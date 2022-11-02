import requests
import tkinter as tk
from tkinter import *
import os


def sms():
    phone = entry_phone.get()
    message = entry_msg.get()
    key = entry_key.get()
    url = "https://textbelt.com/text"
    resp = requests.post(url,  {
        'phone': phone,
        'message': message,
        'key': key
    })
    print(resp.json())


root = tk.Tk()
root.geometry("530x350")
root.title("SMS-by-Post")
root.iconbitmap('C:\\Users\\Ben\\Documents\\Icons\\ICONFORSMS.ico')
root.resizable(False, False)
root.configure(bg="#DFDFDF")

image1 = tk.PhotoImage(file="C:\\Users\\Ben\\tayk.png")


frame1 = tk.Frame(root, height=340, width=225, bg="#D3D3D3")
frame1.place(relx=0.01, rely=0.06)

frame2 = tk.Frame(root, height=340, width=225, bg="#DFDFDF", PhotoImage=image1)
frame2.place(relx=0.56, rely=0.06)




label1 = tk.Label(root, text="~~ SMS-by-Post", bg="#DFDFDF")
label1.place(relx=0.02, rely=0.008)

label2 = tk.Label(frame1, text="Enter recipient details and API Key below:", bg="#DFDFDF")
label2.pack()

entry_phone = tk.Entry(root)


entry_msg = tk.Entry(root)


entry_key = tk.Entry(root)


#button1 = tk.Button(root, bg="#DFDFDF", width=20)
#button1.pack()


root.mainloop()