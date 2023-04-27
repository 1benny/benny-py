import tkinter as tk
from pytube import YouTube
from pytube import Search
import os
from time import sleep
from tkinter import filedialog
from tkinter import ttk
from pytube import exceptions
#from PIL import ImageTk, Image


def search():
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


def download_vid():
    global vid_dl
    vid_dl = YouTube(entry1.get())
    print(set_path)
    print(vid_dl.title)
#    url = entry1.get()

    print("AFTER FORMATTING: \n")

    sleep(2)
    format_path = os.path.join(set_path, vid_dl.title).replace("\\", "/")
    print(format_path)
    ext_path = (str(format_path) + r".mp4")
    print(ext_path)
    

#    try: 
#        do_download.download(set_path)
#    except NameError: dl_label.configure(text="Error: No directory selected")
#    else:
#        do_download.download(set_path)
#        
#    
#    if os.path.exists(ext_path):
#        dl_label.configure(text="Success")
#    else:
#        dl_label.configure(text="Download failed")
#
#    if var2.get() == 1:
#        open_finish()
#    elif var1.get() == 1:
#        mp3()
#    else:
#        pass        
    return 


def mp3():
    audio_only = vid_dl.streams.filter(only_audio=True).first()
    audio_out = audio_only.download(output_path=set_path)
    base, ext = os.path.splitext(audio_out)
    new_file = base + '.mp3'
    os.rename(audio_out, new_file)
    return


def open_finish():
    os.startfile(set_path)
    return


def animation2():
    text = r'-\|/-\|/-'
    while True:
        for rod in r'-\|/-\|/-':
            text += rod + '\r'
            sleep(0.25)


def ask_directory():
    global set_path
    do_openfolder = tk.Tk()
    do_openfolder.withdraw()
    set_path = filedialog.askdirectory()
    path_label.configure(text="Path set to: " + set_path)
    return


def kill():
    root.quit()
    return

# # // Main widget // # / # / # / # / # / # / # / # / # / # / # / # / # / # / # / # / # / # / # / # / # / # / # / # / # / # / # / # / # / # / # / # / # / # /

root = tk.Tk()
root.geometry("480x260")
root.resizable(False, False)
root.title("YRip")
#root.iconbitmap(r"C:\YRip\bitmap.ico")

canvas1 = tk.Canvas(root, bg="#D3D3D3")
canvas1.place(relwidth=2, relheight=1.5, relx=0, rely=0.1)

label1 = tk.Label(root, text="YRip ~ v0.0.2", font=("Consolas", 10))
label1.place(x=0, y=2)

button3 = tk.Button(canvas1, text="Exit", command=kill, font=("Consolas", 8), height=0, width=16)
button3.place(x=4.5, y=210)

#image1 = ImageTk.PhotoImage(Image.open(r"C:\YRip\colour1.png"))
#img_lbl = tk.Label(canvas1, image=image1)
#img_lbl.place(x=200, y=180)


 # # // Direct download func // # / # / # / # / # / # / # / # / # / # / # / # / # / # / # / # / # / # / # / # / # / # # / # / # / # / # / # / # / # / # / # / 

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



# # // Search func // # / # / # / # / # / # / # / # / # / # / # / # / # / # / # / # / # / # / # / # / # / # / # # / # / # / # / # / # / # / # / # / # / # / # /

canvas2 = tk.Canvas(root,bg="#C3C3C3")
canvas2.place(relwidth=0.45, relheight=0.4,x=260, y=103)

search_results = tk.Label(root, font=("Consolas", 7), bg="#C3C3C3", wraplength=200, justify="left")
search_results.place(x=263 , y=110)

s_results_text = tk.Text(root, font=("Consolas", 8), bg="#C3C3C3", width=35, height=11)
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


# / # / # / # / # / # / # / # / # / # / # / # / # / # / # / # / # / # / # / # / # / # / # / # / # / # / # / # / # /


root.mainloop()