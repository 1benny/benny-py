import tkinter as tk
from pytube import YouTube
from pytube import Search
import os
from time import sleep
from tkinter import filedialog
from tkinter import *
import requests
from PIL import ImageTk, Image

#functions




def search():           #yt
    get_query = entry2.get()
    s = Search(get_query)
    len(s.results)
    print(s.results)
    
    for v in s.results:
        if var3.get() == 1:
            s_results = f"~ {v.title}\n {v.watch_url}\n"
            s_results_text.insert(1.0, str(s_results))       
        elif var3.get() == 0:
            s_results = f"~ {v.title}\n"
            s_results_text.insert(1.0, str(s_results))

    return


def download_vid():     #yt
    global vid_dl
    dl_label.after(5000) 
    url = entry1.get()
    vid_dl = YouTube(url)
    do_download = vid_dl.streams.get_highest_resolution()
    vid_title = vid_dl.title
    format_path = os.path.join(set_path, vid_title).replace("\\", "/")
    ext_path = (str(format_path) + r".mp4")
    try: 
        do_download.download(set_path)
    except NameError: dl_label.configure(text="Error: No directory selected")
    else:
        do_download.download(set_path)  

    if os.path.exists(ext_path):
        dl_label.configure(text="Success")
    else:
        dl_label.configure(text="Download failed")

    if var2.get() == 1:
        open_finish()
    elif var1.get() == 1:
        mp3()
    else:
        pass        
    return 


def mp3():              #yt
    audio_only = vid_dl.streams.filter(only_audio=True).first()
    audio_out = audio_only.download(output_path=set_path)
    base, ext = os.path.splitext(audio_out)
    new_file = base + '.mp3'
    os.rename(audio_out, new_file)
    return


def open_finish():      #yt
    os.startfile(set_path)
    return


def animation2():       ###
    text = r'-\|/-\|/-'
    while True:
        for rod in r'-\|/-\|/-':
            text += rod + '\r'
            sleep(0.25)


def ask_directory():    #yt
    global set_path
    do_openfolder = tk.Tk()
    do_openfolder.withdraw()
    set_path = filedialog.askdirectory()
    path_label.configure(text="Path set to: " + set_path)
    return



def sms_slave():

    def bye():
        slave2.withdraw()
        master.deiconify()
        
    
    def write_key():       
        to_write = key_entry.get()
        with open("writeout.txt", "w") as f:
            f.write(to_write)
            f.close()
        return

    def send():             
        f = open("writeout.txt", "r")
        if var2.get() == 1: 
            key = f.read()
        else:  
            key = key_entry.get()
        print(key)
        url = 'https://textbelt.com/text'
        entry_number = phone_entry.get()
        phonenum = ("+61" + entry_number)
        req = requests.post(url,    {
            "phone": phonenum,
            "message": text1.get(1.0, "end"),
            "key": key
            })
        result = req.json()
        print(phonenum)
        dl_label.configure(text=result)
        if var1.get() == 1:
            write_key()
        else:
            pass
        f.close()
        print(result)
        return

    def check_key():
        f = open("writeout.txt", "r")
        if var2.get() == 1:
            qkey = f.read()
        else:
            qkey = key_entry.get()
        quota = requests.get(f'https://textbelt.com/quota/{qkey}')
        response = quota.json()
        text1.delete(1.0, "end")
        text1.insert(1.0, response)
        f.close()
        return


    def manual_key():
        nkeywin = tk.Tk()
        nkeywin.title("Manually import API Key")
        nkeywin.geometry("200x80")
        return




    master.withdraw()

    slave2 = tk.Tk()
    slave2.geometry("480x260")
    slave2.resizable(False, False)
    slave2.title("SMSvP")

    canvas1 = tk.Canvas(slave2, bg="#D3D3D3")
    canvas1.place(relwidth=2, relheight=2, relx=0, rely=0.1)

    label1 = tk.Label(slave2, text="<<      SMS via Post Request      >>", font=("Consolas", 10))
    label1.place(x=107, y=2)

    phone_label = tk.Label(canvas1, text="Enter mobile phone number:", font=("Consolas", 9), bg="#D3D3D3")
    phone_label.place(x=2, y=5)
    lbl_61 = tk.Label(canvas1, text="+61", font=("Consolas", 10), bg="#D3D3D3")
    lbl_61.place(x=2, y=24)

    key_label = tk.Label(canvas1, text="Enter API Key:", font=("Consolas", 9), bg="#D3D3D3")
    key_label.place(x=2, y=55)

    dl_label = tk.Label(slave2, font=("Consolas", 7), bg="#D3D3D3", wraplength=220)
    dl_label.place(x=5, y=200)

    phone_entry = tk.Entry(canvas1, width=26, font=("Consolas", 10))
    phone_entry.place(x=27, y=25)

    key_entry = tk.Entry(canvas1, width=29, font=("Consolas", 10))
    key_entry.place(x=5.5, y=75)

    var1 = IntVar()
    var2 = IntVar()

    save_key = tk.Checkbutton(canvas1, text="Save Key as default", font=("Consolas", 9), onvalue=1, offvalue=0, variable=var1, bg="#D3D3D3")
    save_key.place(x=2, y=100)
    open_key = tk.Checkbutton(canvas1, text="Use default Key", font=("Consolas", 9), onvalue=1, offvalue=0, variable=var2, bg="#D3D3D3")
    open_key.place(x=2, y=125)

    btn_kill = tk.Button(canvas1, text="Quit", font=("Consolas", 8), command=master.quit, height=0, width=16)
    btn_kill.place(x=2, y=210)

    btn_back = tk.Button(canvas1, text="Back", command=bye, font=("Consolas", 8), height=0, width=16)
    btn_back.place(x=110, y=210)

    btn_send = tk.Button(canvas1, text="Send", command=send, font=("Consolas", 8), height=0, width=37)
    btn_send.place(x=240, y=159)

    btn_check = tk.Button(canvas1, command=check_key, text="Check Quota", font=("Consolas", 8), height=0, width=37)
    btn_check.place(x=240, y=183)

    label4 = tk.Label(canvas1, text="Enter message to send:", font=("Consolas", 9), bg="#D3D3D3")
    label4.place(x=237, y=5)

    text1 = tk.Text(slave2, font=("Consolas", 8), bg="#D3D3D3", width=38, height=10)
    text1.place(x=239, y=51)

    slave2.mainloop()
    return


master = tk.Tk()
master.geometry("480x260")
master.resizable(False, False)
master.title("YRip")
#master.iconbitmap("bitmap.ico")

canvas1 = tk.Canvas(master, bg="#D3D3D3")
canvas1.place(relwidth=2, relheight=1.5, relx=0, rely=0.1)

label1 = tk.Label(master, text="YRip ~ v0.0.2", font=("Consolas", 10))
label1.place(x=0, y=2)

button3 = tk.Button(canvas1, text="Exit", command=master.quit, font=("Consolas", 8), height=0, width=16)
button3.place(x=4.5, y=210)

switch_apps = tk.Button(canvas1, command=sms_slave, text="SMSvP ~>>", font=("Consolas", 8), height=0, width=16)
switch_apps.place(x=112, y=210)

label2 = tk.Label(canvas1, text="Enter URL:", font=("Consolas", 9), bg="#D3D3D3")
label2.place(x=1, y=5)

dl_label = tk.Label(canvas1, font=("Consolas", 8), bg="#D3D3D3")
dl_label.place(x=1 , y=140)

dl_except = tk.Label(canvas1, font=("Consolas", 8), bg="#D3D3D3")
dl_except.place(x=1, y=160)

path_label = tk.Label(canvas1, font=("Consolas", 8), bg="#D3D3D3")
path_label.place(x=1, y=110)

entry1 = tk.Entry(canvas1, width=30, font=("Consolas", 10))
entry1.place(x=4.5, y=23)

button1 = tk.Button(canvas1, text="Download", font=("Consolas", 8), command=download_vid, height=0, width=16)
button1.place(x=4.5, y=46)
button2 = tk.Button(canvas1, text="Open folder", command=ask_directory, font=("Consolas", 8), height=0, width=16)
button2.place(x=4.5, y=71)
var1 = tk.IntVar()
var2 = tk.IntVar()

mp3_box = tk.Checkbutton(canvas1, text="Download as mp3",variable=var1, onvalue=1, offvalue=0, bg="#D3D3D3")
mp3_box.place(x=118, y=45.4)

open_box = tk.Checkbutton(canvas1, text="Open on finish",variable=var2, onvalue=1, offvalue=0, bg="#D3D3D3")
open_box.place(x=118, y=68.6)

canvas2 = tk.Canvas(master,bg="#C3C3C3")
canvas2.place(relwidth=0.45, relheight=0.4,x=260, y=103)

search_results = tk.Label(master, font=("Consolas", 7), bg="#C3C3C3", wraplength=200, justify="left")
search_results.place(x=263 , y=110)

s_results_text = tk.Text(master, font=("Consolas", 8), bg="#C3C3C3", width=35, height=11)
s_results_text.place(x=262, y=105)

s_label = tk.Label(canvas1, text="Search:", font=("Consolas", 9), bg="#D3D3D3")
s_label.place(x=257, y=5)

entry2 = tk.Entry(canvas1, width=30, font=("Consolas", 10))
entry2.place(x=261, y=23)

s_button = tk.Button(canvas1, text="Search", font=("Consolas", 8), width=17, command=search)
s_button.place(x=262, y=46)

var3 = tk.IntVar()

s_checkbox = tk.Checkbutton(canvas1, text="Include URL", variable=var3, onvalue=1, offvalue=0, font=("Consolas", 8), bg="#D3D3D3")
s_checkbox.place(x=380, y=46)

master.mainloop()



#####################################