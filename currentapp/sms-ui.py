import tkinter as tk
import requests
from time import sleep
import os

def send():
    url = 'https://textbelt.com/text'
    req = requests.post(url,    {
        "phone": entry1.get(),
        "message": text1.get(1.0, "end"),
        "key": entry2.get()
        })
    result = req.json()
    text1.insert(1.0, result)
  
    return

def check():
    qkey = entry2.get()
    quota = requests.post(f'https://textbelt.com/quota/{qkey}')
    text1.delete(1.0, "end")
    text1.insert(1.0, quota.json())

    return

def show():
    return


# # // Main widget // # / # / # / # / # / # / # / # / # / # / # / # / # / # / # / # / # / # / # / # / # / # / # / # / # / # / # / # / # / # / # / # / # / # /

root = tk.Tk()
root.geometry("480x260")
root.resizable(False, False)
root.title("SMSvP")

canvas1 = tk.Canvas(root, bg="#D3D3D3")
canvas1.place(relwidth=2, relheight=1.5, relx=0, rely=0.1)

label1 = tk.Label(root, text="~~ SMSvP", font=("Consolas", 10))
label1.place(x=0, y=2)

label2 = tk.Label(canvas1, text="Enter mobile phone number:", font=("Consolas", 9), bg="#D3D3D3")
label2.place(x=1, y=5)

label3 = tk.Label(canvas1, text="Enter API Key:", font=("Consolas", 9), bg="#D3D3D3")
label3.place(x=1, y=60)

dl_label = tk.Label(root, font=("Consolas", 8), bg="#D3D3D3")
dl_label.place(x=5, y=230)

entry1 = tk.Entry(canvas1, width=29, font=("Consolas", 10))
entry1.place(x=4.5, y=25)

entry2 = tk.Entry(canvas1, width=29, font=("Consolas", 10))
entry2.place(x=4.5, y=80)

var1 = tk.IntVar
var2 = tk.IntVar

save_key = tk.Checkbutton(canvas1, text="Save current key as default", font=("Consolas", 9), onvalue=1, offvalue=0,
                        variable=var1, bg="#D3D3D3").place(x=2, y=105)
open_key = tk.Checkbutton(canvas1, text="Set a key from file", font=("Consolas", 9), onvalue=1, offvalue=0,
                        variable=var2, bg="#D3D3D3").place(x=2, y=130)

btn_kill = tk.Button(canvas1, text="Quit", font=("Consolas", 8), command=root.quit, height=0, width=16)
btn_kill.place(x=365, y=210)

btn_back = tk.Button(canvas1, text="Back", font=("Consolas", 8), height=0, width=16)
btn_back.place(x=365, y=187)

btn_send = tk.Button(canvas1, text="Send", command=send, font=("Consolas", 8), height=0, width=16)
btn_send.place(x=365, y=164)

btn_check = tk.Button(canvas1, text="Check Quota", font=("Consolas", 8), height=0, width=16)
btn_check.place(x=260, y=210)

btn_check = tk.Button(canvas1, text="Check Quota", font=("Consolas", 8), height=0, width=16)
btn_check.place(x=260, y=210)

label4 = tk.Label(canvas1, text="Enter message to send:", font=("Consolas", 9), bg="#D3D3D3")
label4.place(x=237, y=5)

text1 = tk.Text(root, font=("Consolas", 8), bg="#D3D3D3", width=38, height=10)
text1.place(x=239, y=51)


root.mainloop()