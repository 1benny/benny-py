import tkinter as tk
from tkinter import *
from tkinter.colorchooser import *
from tkinter.ttk import *
from math import *


root = tk.Tk()
root.title("Colour Select")
root.geometry("300x230")
root.iconbitmap('C:\\Users\\Ben\\Documents\\Icons\\cpicker.ico')
#root.resizable(False, False)


def change_colour():
    colours = askcolor(title="Colour Selection")
    button1.configure(bg=colours[1])


def return_rgb(event):
    rgb_label.configure(text="RGB Value: " + entry2.get())
    rgb_label.pack()


def clear_the_hbox():
    global hvalue
    hvalue = ""
    entry1.delete(0, END)


def clear_the_rbox():
    global rgbinput
    rgbinput = ""
    entry2.delete(0, END)


label = tk.Label(root, text="Choose a colour") #font=("Fira Code Medium", 9))
label.pack()

label2 = tk.Label(root, text="↓")
label2.pack()

pic1 = PhotoImage(file="C:\\Users\\Ben\\Documents\\Icons\\smallsize.png")
pic2 = PhotoImage(file="C:\\Users\\Ben\\Documents\\Icons\\smallsize.png")

button1 = tk.Button(root, padx=130, pady=20, command=change_colour)      
button1.pack(expand=False)

frame1 = tk.Frame(root, height=100, width=140, bg="#EEEEEE")
frame1.place(x=6, y=114.4)

frame2 = tk.Frame(root, height=100, width=140, bg="#EEEEEE")
frame2.place(x=149, y=114)

label3 = tk.Label(frame1, text="Convert to Hex: ", font=("Calibri", 9), bg="#EEEEEE")
label3.pack(pady=10, padx=10)

label4 = tk.Label(frame2, text="Convert to RGB: ", font=("Calibri", 9), bg="#EEEEEE")
label4.pack(pady=10, padx=10)

entry1 = tk.Entry(frame1, bg="#E6E6E6")
#entry1.bind("<Return>", RGBToHex(int(x), int(y), int(z)))
entry1.pack(padx=10, pady=1)


#def RGBToHex(r, g, b):
#    r, g, b = x, y, z
#    return '#%02X%02X%02X' % (int(r), int(g), int(b))
#print(RGBToHex(entry1))

#x, y, z = entry1.get().split()
#label_config1 = (RGBToHex(int(x), int(y), int(z)))


entry2 = tk.Entry(frame2, bg="#E6E6E6")
entry2.bind("<Return>", return_rgb)
entry2.pack(padx=10, pady=1)

hex_label = tk.Label(frame1)
hex_label.pack(side=BOTTOM)

rgb_label = tk.Label(frame2)
rgb_label.pack(side=BOTTOM)



clear_box1 = tk.Button(frame1, width=19, text="Clear", font=("Calibri", 9), command=clear_the_hbox)
clear_box1.pack()
clear_box2 = tk.Button(frame2, width=15, text="Clear", font=("Calibri", 9), command=clear_the_rbox)
clear_box2.pack()

#hex_res = tk.Label(frame1)

root.mainloop()