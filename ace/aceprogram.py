# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# For Ace and ensuring organisation of Rinnai contracted installs                                                                                                                       # 
# Ultimately the goal if writing this program will be to ensure that future subcontracted works/ possibly any works in general will have a backup proofreader                           #
# to work as a double-checker of sorts, which will assist in my job and will assist Dustin in organising correct parts delivery as well as help cooperation with Builders who can't     #
# manage the site good enough to make sure the other trades are forming the prerequisites correctly                                                                                     #                                                                                                                                                                                        #
#                                                                                                                                                                                       #
#                                                                                                                                                                                       #
# < Will act like a database that will eventually have a UI for ease of use by all members of staff --                                                                                  #       
#  -- The UI will utilize drop-down boxes for lists as well as checkboxes for double checking [work with ideas later]                                                                   #
#  -- A search box for units that will pass keywords and tags such inventory numbers, order numbers and retail names                                                                    #
#                                                                                                                                                                                       #
# ***For now the program will be raw coded and will operate in the Visual Studio or a command prompt**                                                                                  #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from tkinter import *
import tkinter as tk
from math import *


global unit_750
unit_750 = "Rinnai Flame Fire RDV750"

root = tk.Tk()
root.geometry("1200x750")


canvas1 = tk.Canvas(root, bg="#3F3F3F").place(relwidth=1, relheight=1.6)

label1 = tk.Label(canvas1, text="Enter model or part name or number: ", fg="#DCDCCC", bg="#3F3F3F", font=("Consolas", 10))
label1.place(relx=0.008, rely=0.043)

#def drop_menu1():






def text_input(e):
    global text_get
    text_get = text1.get("1.0", END)
    print(text_get)
    return text_get


text1 = tk.Text(canvas1, font=("Consolas", 10), bg="white", width=35, height=1.2)
text1.place(relx=0.01, rely=0.07)
text1.bind("<Return>", text_input)

label_or = tk.Label(canvas1, text="or", fg="#DCDCCC", bg="#3F3F3F", font=("Consolas", 10))
label_or.place(relx=0.008, rely=0.12)

label2 = tk.Label(canvas1, text="Enter any part number: ", fg="#DCDCCC", bg="#3F3F3F", font=("Consolas", 10))
label2.place(relx=0.008, rely=0.17)


text2 = tk.Text(canvas1, font=("Consolas", 10), bg="white", width=35, height=1.2)
text2.place(relx=0.01, rely=0.2)
text2.bind("<Return>"), #text_input2)


label_alternatively = tk.Label(canvas1, text="Alternatively, Select from the list of known products: ", 
                                fg="#DCDCDC", bg="#3F3F3F", font=("Consolas", 10))
label_alternatively.place(relx=0.008, rely=0.3)

root.mainloop()