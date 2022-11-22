import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog, commondialog, colorchooser
from time import sleep
import os

def dark_mode():
    if var_dark.get() == 0:
        canvas1.configure(bg="#FFFFFF")
        title_label.configure(bg="#FFFFFF", fg="#000000")
        label_line.configure(bg="#FFFFFF", fg="#000000")
    elif var_dark.get() == 1:
        canvas1.configure(bg="#3F3F3F")
        title_label.configure(bg="#3F3F3F", fg="#dcdccc")
        label_line.configure(bg="#3F3F3F", fg="#dcdccc")

def save_as():
    with open("list.txt", "r+") as f:
        saveas = filedialog.asksaveasfile(initialfile=".txt")
    return

def create_list():
    with open("list.txt", "w") as f:
        f.write("My First List...")
        f.close()

def addtask():
    return

def opentask():
    return

def get_help():
    messagebox.showinfo("About", """List Constructor is a program that
enables you to create a list,

~ write to that list 
~ delete the list,
~ open an existing list 
~ do other shit with the list 

and other things involving lists.          
Extremely simple.""")


master = tk.Tk()
master.title("List Creation Tool")
master.geometry("500x600")
master.resizable(False, False)


canvas1 = tk.Canvas(master, bg="#3F3F3F")
canvas1.place(relwidth=1, relheight=1)

menubar = tk.Menu(master)

# MENU -- FILE
filem = tk.Menu(menubar, tearoff=0)
filem.add_command(label="New", command=create_list)
filem.add_command(label="Open...", command=None)
filem.add_command(label="Save As...", command=save_as)
filem.add_command(label="Export As...", command=None)
filem.add_separator()
filem.add_command(label="New File...", command=None)
filem.add_separator()
filem.add_command(label="Close Window...", command=master.quit)
menubar.add_cascade(label="File", menu=filem)

# MENU -- EDIT
editm = tk.Menu(menubar, tearoff=0)
editm.add_command(label="Undo", command=None)
editm.add_command(label="Redo", command=None)
editm.add_separator()
editm.add_command(label="Cut", command=None)
editm.add_command(label="Copy", command=None)
editm.add_command(label="Paste", command=None)
editm.add_separator()
editm.add_command(label="Find", command=None)
editm.add_command(label="Replace", command=None)
editm.add_command(label="Find in Files", command=None)
menubar.add_cascade(label="Edit", menu=editm)

# MENU -- VIEW
var_dark = tk.IntVar()
viewm = tk.Menu(menubar, tearoff=0)
viewm.add_checkbutton(label="Dark Mode", command=dark_mode, onvalue=1, offvalue=0, variable=var_dark)
menubar.add_cascade(label="View", menu=viewm)


# MENU -- HELP
helpm = tk.Menu(menubar, tearoff=0)
helpm.add_command(label="About...", command=get_help)
menubar.add_cascade(label="Help", menu=helpm)

master.config(menu=menubar)

label_line = tk.Label(canvas1, text="________________________________________________________________________________________", bg="#3F3F3F", fg="#dcdccc")
label_line.place(x=24, y=19)

title_label = tk.Label(canvas1, font=("Consolas", 11), text="Add or Remove Items to List", bg="#3F3F3F", fg="#dcdccc")
title_label.place(relx=0.27, y=23)

text1 = tk.Label(canvas1, text="""Continue with functions regarding save-as option, where the file saves and how
Creating entries and labels/ styling the widget
Incorporating the buttons with functions into adding and removing tasks to and from the list

## // Will using those buttons and adding/removing tasks affect the external 
file, or will they only render in the widget until the user saves 
the list to file??""")
text1.pack(side="bottom")

master.mainloop()