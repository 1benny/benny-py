import customtkinter as ttkk
import subprocess as sub
from elevate import elevate
import threading

#elevate(show_console=False)

def search():
    value = entry_search.get()
    package_s = sub.getoutput(f'winget search {value}')
    text1.insert(1.0, package_s)
    #print(package_s)
    return

def install():
    pname = entry_search.get()
    package_i = sub.getoutput(f"winget install {pname} --accept-package-agreements --accept-source-agreements")
    text1.insert(1.0, package_i)
    return

def wlist():
    w_list = sub.Popen('winget.exe')
    text1.insert(1.0, w_list)
    threading.Thread.join()
    return

ttkk.set_appearance_mode("dark")
ttkk.set_default_color_theme("dark-blue")

root = ttkk.CTk()
#root.geometry("415x240")
root.geometry("490x240")
root.title("Installer")
#root.resizable(False, False)

frame = ttkk.CTkFrame(master=root)
frame.pack(pady=10,
           padx=15,
           fill="both",  
           expand=True)

seperator = ttkk.CTkLabel(frame, text="____________________________________________________________", 
                          fg_color="#292929",
                          text_color="#FFFFFF")
seperator.place(x=10, y=10)

title = ttkk.CTkLabel(frame,
                     text="Search for a package and install", 
                     text_font=("Consolas", 10),
                     fg_color="#292929")
title.place(x=75, y=0)

entry_search = ttkk.CTkEntry(frame, 
                            width=245, 
                            height=0, 
                            border_color="#292929")
entry_search.place(x=3, y=32)
entry_search.bind("<Return>", search)

search_button = ttkk.CTkButton(frame, 
                               height=0, 
                               width=10,
                               border_width=0,
                               text="Search", 
                               text_font=("Consolas", 9), 
                               fg_color="#292929",
                               command=search)
search_button.place(x=247, y=33)

install_button = ttkk.CTkButton(frame, 
                                height=0, 
                                width=20, 
                                border_width=0, 
                                text="Install", 
                                text_font=("Consolas", 9), 
                                fg_color="#292929", 
                                command=install)
install_button.place(x=312, y=33)

extra_button = ttkk.CTkButton(frame, 
                              height=0,
                              width=10, 
                              border_width=0, 
                              text="List", 
                              text_font=("Consolas", 9),
                              fg_color="#292929", 
                              command=wlist)
extra_button.place(x=385, y=33)

h_scroll = ttkk.CTkScrollbar(frame, 
                            orientation='horizontal', 
                            fg_color="#292929")
h_scroll.pack(side='bottom', 
              fill='x', 
              padx=10, 
              pady=2)

text1 = ttkk.CTkTextbox(frame, 
                        width=382, 
                        height=140, 
                        fg_color="#292929", 
                        text_font=("Consolas", 9), 
                        wrap='none',
                        xscrollcommand=h_scroll.set)
text1.place(x=1, y=55)

h_scroll.configure(command=text1.xview)


root.mainloop()