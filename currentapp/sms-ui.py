import tkinter as tk
import requests
from time import sleep
import os

global keyfile

def manual_key():
    nkeywin = tk.Tk()
    nkeywin.title("Manually import API Key")
    nkeywin.geometry("200x80")
    return


def send():
    url = 'https://textbelt.com/text'
    req = requests.post(url,    {
        "phone": phone_entry.get(),
        "message": text1.get(1.0, "end"),
        "key": key_entry.get()
        })
    result = req.json()
    text1.insert(1.0, result)

    if var1.get() == 1:
        save_def()
  
    return

def check():
    qkey = key_entry.get()
    quota = requests.post(f'https://textbelt.com/quota/{qkey}')
    text1.delete(1.0, "end")
    text1.insert("end", quota.json())
    return



## Once written to a local file needs to be able to use that local file to read from
## in order to use a "default" key. 
## ~~> Somewhere in code needs to be pointing at the text/list file: eg. the open() or 
## something like x = r"C:\Users\Ben\Desktop\shit\Python\bdives-main\currentapp"

def save_def():       
    global keyfile
    key_data = key_entry.get()
    with open("new_keyg.list", 'w') as file:
        var = file.write(str(key_data))
        print(var)
        file.close()
        keyfile = file
        pass
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

phone_label = tk.Label(canvas1, text="Enter mobile phone number:", font=("Consolas", 9), bg="#D3D3D3")
phone_label.place(x=2, y=5)
lbl_61 = tk.Label(canvas1, text="+61", font=("Consolas", 10), bg="#D3D3D3")
lbl_61.place(x=2, y=24)

key_label = tk.Label(canvas1, text="Enter API Key:", font=("Consolas", 9), bg="#D3D3D3")
key_label.place(x=2, y=60)

dl_label = tk.Label(root, font=("Consolas", 8), bg="#D3D3D3")
dl_label.place(x=5, y=230)

phone_entry = tk.Entry(canvas1, width=26, font=("Consolas", 10))
phone_entry.place(x=27, y=25)

key_entry = tk.Entry(canvas1, width=29, font=("Consolas", 10))
key_entry.place(x=5.5, y=80)

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