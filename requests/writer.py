import os
from time import sleep
import tkinter as tk
from tkinter import*


#def openit():
#    text_file = open("sample.txt", 'r')
#    text_file.read()
#
#    text_file.close()



#def readit():
#    tfile = open("new.txt", 'r')
#    tfile.read()
#    store_info = tfile
#    tfile.close()
#    sleep(3)
#    print(store_info)

#def writeit():
#    data = input(">> ")
#    with open("new.txt", 'w') as file:
#        var = file.write(str(data))
#        print(var)
#        file.close()
#        keyfile = file
#        print(keyfile)
#        pass
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


def yrip_slave():
    slave1 = tk.Tk()
    slave1.geometry("480x260")
    slave1.resizable(False, False)
    slave1.title("YRip")
    slave1.iconbitmap("bitmap.ico")

    canvas1 = tk.Canvas(slave1, bg="#D3D3D3")
    canvas1.place(relwidth=2, relheight=1.5, relx=0, rely=0.1)

    label1 = tk.Label(slave1, text="YRip ~ v0.0.2", font=("Consolas", 10))
    label1.place(x=0, y=2)

    button3 = tk.Button(canvas1, text="Exit", command=slave1.quit, font=("Consolas", 8), height=0, width=16)
    button3.place(x=4.5, y=210)

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

    canvas2 = tk.Canvas(slave1,bg="#C3C3C3")
    canvas2.place(relwidth=0.45, relheight=0.4,x=260, y=103)

    search_results = tk.Label(slave1, font=("Consolas", 7), bg="#C3C3C3", wraplength=200, justify="left")
    search_results.place(x=263 , y=110)

    s_results_text = tk.Text(slave1, font=("Consolas", 8), bg="#C3C3C3", width=35, height=11)
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

    slave1.mainloop()
    return


def sms_slave():
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

    save_key = tk.Checkbutton(canvas1, text="Save Key as default", font=("Consolas", 9), onvalue=1, offvalue=0,
                            variable=var1, bg="#D3D3D3").place(x=2, y=100)
    open_key = tk.Checkbutton(canvas1, text="Use default Key", font=("Consolas", 9), onvalue=1, offvalue=0,
                            variable=var2, bg="#D3D3D3").place(x=2, y=125)

    btn_kill = tk.Button(canvas1, text="Quit", font=("Consolas", 8), command=slave2.quit, height=0, width=16)
    btn_kill.place(x=2, y=210)

    btn_back = tk.Button(canvas1, text="Back", font=("Consolas", 8), height=0, width=16)
    btn_back.place(x=110, y=210)

    btn_send = tk.Button(canvas1, text="Send", font=("Consolas", 8), height=0, width=37)
    btn_send.place(x=240, y=159)

    btn_check = tk.Button(canvas1, text="Check Quota", font=("Consolas", 8), height=0, width=37)
    btn_check.place(x=240, y=183)

    label4 = tk.Label(canvas1, text="Enter message to send:", font=("Consolas", 9), bg="#D3D3D3")
    label4.place(x=237, y=5)

    text1 = tk.Text(slave2, font=("Consolas", 8), bg="#D3D3D3", width=38, height=10)
    text1.place(x=239, y=51)


    slave2.mainloop()
    return

master = tk.Tk()
master.geometry("200x100")

Button(master, text="YRip", command=yrip_slave, width=30, height=3).pack(expand=True)
Button(master, text="SMSvP", command=sms_slave, width=30, height=3).pack(expand=True)


master.mainloop()