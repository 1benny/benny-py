import tkinter as tk
from tkinter import filedialog


                                                            #  ~ Could have the extra window pop up for solely importing API Key manually
                                                            #  ~ Could be used in conjunction with Menu widget:
def manwindow():                                            #       ~~> Drop down menu that contains
    window = tk.Toplevel()                                  #           + API Keys
    window.geometry('150x150')                              #           + "Contacts"/known numbers stored somewhere on local machine
    newlabel = tk.Label(window, text = "Setting Window")    #           + Connection between YRip and SMSvP
    newlabel.pack()                                         #
#      |                                                     #
#      |                                                     #
#      |
#      L___________________/~~ Secondary tk window that is killed if root process is destroyed             
#           
nkeywin = tk.Tk()                           ## <~~ This is the base "root" tk window
nkeywin.title("Manually import API Key")
nkeywin.geometry("300x80")
nkeywin.resizable(False, False)
#|
nkey_lbl1 = tk.Label(nkeywin, text="Enter Key in input box", font=("Consolas", 9))
nkey_lbl1.pack(side="top")
#|
nkey_ent = tk.Entry(nkeywin, width=35, font=("Consolas", 10), bg="#e2e2e2")
nkey_ent.pack()
#|
nkey_btn = tk.Button(nkeywin, text="Submit", width=34, command=manwindow, height=0, font=("Consolas", 9))
nkey_btn.pack()
#|
nkeywin.mainloop()