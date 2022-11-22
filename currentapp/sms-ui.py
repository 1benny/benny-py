import tkinter as tk
from tkinter import ttk
from tkinter import *
import requests
from time import sleep
import os
from pytube import YouTube

#localfiles
ico = "C:\\Program Files\\bitmap.ico"

#definitions
jsonerror= """JSONDecodeError: [404] ~~ Maybe URL is broken? 
Try checking if Key file is present"""
nameerror = """NameError: Uh oh, the program couldn't read the key file.
Ask Ben"""

#functions
def write_key():
    f = open("sms_key.txt", "w")
    new_key = key_entry.get()
    f.write(new_key)
    f.close()
    return

def send():
    if var2.get() == 1: 
        try:
            f = open("sms_key.txt", "r")
            key = f.read()
        except FileNotFoundError:
            text1.insert(1.0, "You must set an API Key before using  the default option")
    else:
        key = key_entry.get()

    url = 'https://textbelt.com/text'
    entry_number = phone_entry.get()
    phonenum = ("+61" + entry_number)
    req = requests.post(url,    {
        "phone": phonenum,
        "message": text1.get(1.0, "end"),
        "key": key
        })
    result = req.json()
    text1.insert("end", result)
    if var1.get() == 1:
        write_key()
    else:
        pass
    f.close()
    return

def check_key():
    if var1.get() == 1:
        write_key()
        sleep(2)
        existance = (os.getcwd() + "\sms_key.txt")
        if os.path.exists(existance) == True:
            tk.Label.configure(result_label, text="Saved new Key to:")
            tk.Label.configure(result2_label, text=os.getcwd())
        else:
            tk.Label.configure(result_label, text="Failed to write key to file")
    else:
        pass
    if var2.get() == 1:
        i = 1
        while i < 2:
                try:
                    i += 1
                    f = open("sms_key.txt", "r")
                    qkey = f.read()
                    quota = requests.get(f'https://textbelt.com/quota/{qkey}')
                    response = quota.json()
                    text1.insert(1.0, response)
                except FileNotFoundError:
                    text1.insert(1.0, "FileNotFoundError: Key file missing.")
                except requests.exceptions.JSONDecodeError:
                    text1.insert(1.0, """JSONDecodeError: [404], Bad URL
(Key missing from file ~ Make sure to 
 select Save Key as default if you've 
 entered one in the box)""") 
                else:
                    pass
    else:
        pass
    return

def saul():
    if key_entry.get() == "saul":
        secret = "https://www.youtube.com/watch?v=CNcHPxHX63c&ab_channel=Dercury"
        vid_dl = YouTube(secret)
        do_saul = vid_dl.streams.get_highest_resolution()
        out_path = "C:\\Users\\"
        do_saul.download(out_path)  
    else:
        pass
    return

def manual_key():
    nkeywin = tk.Tk()
    nkeywin.title("Manually import API Key")
    nkeywin.geometry("200x80")
    return


#master widget
root = tk.Tk()
root.geometry("520x260")
root.resizable(False, False)
root.title("SMSvP")

canvas1 = tk.Canvas(root, bg="#D3D3D3")
canvas1.place(relwidth=2, relheight=2, relx=0, rely=0.1)

label1 = tk.Label(root, text="<<      SMS via Post Request      >>", font=("Consolas", 10))
label1.place(x=107, y=2)

phone_label = tk.Label(canvas1, text="Enter mobile phone number:", font=("Consolas", 9), bg="#D3D3D3")
phone_label.place(x=2, y=5)
lbl_61 = tk.Label(canvas1, text="+61", font=("Consolas", 10), bg="#D3D3D3")
lbl_61.place(x=2, y=24)

key_label = tk.Label(canvas1, text="Enter API Key:", font=("Consolas", 9), bg="#D3D3D3")
key_label.place(x=2, y=60)

result_label = tk.Label(root, font=("Consolas", 8), bg="#D3D3D3")
result_label.place(x=5, y=180)
result2_label = tk.Label(root, font=("Consolas", 8), bg="#D3D3D3")
result2_label.place(x=5, y=200)

phone_entry = tk.Entry(canvas1, width=26, font=("Consolas", 10))
phone_entry.place(x=27, y=25)

key_entry = tk.Entry(canvas1, width=29, font=("Consolas", 10))
key_entry.place(x=5.5, y=80)

key_combo = ttk.Combobox(canvas1, )

var1 = IntVar()
var2 = IntVar()

save_key = tk.Checkbutton(canvas1, text="Save Key as default", font=("Consolas", 9), onvalue=1, offvalue=0,
                        variable=var1, bg="#D3D3D3").place(x=2, y=105)
open_key = tk.Checkbutton(canvas1, text="Use default Key", font=("Consolas", 9), onvalue=1, offvalue=0,
                        variable=var2, bg="#D3D3D3").place(x=2, y=130)

btn_kill = tk.Button(canvas1, text="Quit", font=("Consolas", 8), command=root.quit, height=0, width=16)
btn_kill.place(x=2, y=210)

btn_back = tk.Button(canvas1, command=saul, text="Back", font=("Consolas", 8), height=0, width=16)
btn_back.place(x=109, y=210)

btn_send = tk.Button(canvas1, text="Send", command=send, font=("Consolas", 8), height=0, width=37)
btn_send.place(x=280, y=159)

btn_check = tk.Button(canvas1, command=check_key, text="Check Quota", font=("Consolas", 8), height=0, width=37)
btn_check.place(x=280, y=182)

label4 = tk.Label(canvas1, text="Enter message to send:", font=("Consolas", 9), bg="#D3D3D3")
label4.place(x=279, y=5)

text1 = tk.Text(root, font=("Consolas", 8), bg="#D3D3D3", width=38, height=10)
text1.place(x=279, y=51)


root.mainloop()