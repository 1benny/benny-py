import tkinter as tk
from tkinter import IntVar
import customtkinter as ttkk
import subprocess as sub
import threading

# create/open/write entered information to a file

# create a class for an object that has the properties "date" "ammount" "item"

# create a GUI to enter these values as data

# have the data written to text file in a specific format

class Spending():

    def __init__(self, date, amount, item):
        self.date = date
        self.amount = amount
        self.item = item

    def write(self):
        format = (f"\n{self.date}    ::    {self.amount}    ::    {self.item}")
        with open("spending.txt", "a") as f:
            f.write(format)

            f.close
        if f.closed == False:
            f.close
        return

ttkk.set_appearance_mode("dark")
ttkk.set_default_color_theme("dark-blue")

class App(ttkk.CTk):


    global font1
    font1 = "Montserrat Medium"

    def __init__(self):
        super().__init__()
        self.title("Spending")
        self.geometry("1280x800")
        self.configure(bg="#292929")
        self.minsize(1120, 700)
        self.resizable(False, False)

        radio_var = IntVar()

        self.top_bg_frame= ttkk.CTkFrame(master=self,
                                    bg_color="black",
                                    corner_radius=0)
        self.top_bg_frame.pack(expand=0, fill="both")
        #]
        self.top_left_frame = ttkk.CTkFrame(master=self.top_bg_frame,             # Top background frame
                                   fg_color="#3D3D3D",
                                   height=40)
        self.top_left_frame.pack(padx=(10, 0), pady=7, side="left", anchor="n", expand=True, fill="x")
        #]        
        self.top_right_frame = ttkk.CTkFrame(master=self.top_bg_frame, 
                                             fg_color="#3d3d3d", 
                                             height=40,
                                             width=170)
        self.top_right_frame.pack(pady=7, padx=(10, 10), side="right", anchor=("ne"), expand=False)

        self.top_right_entry = ttkk.CTkEntry(self.top_right_frame,
                                             fg_color="#3d3d3d",
                                             font=("Montserrat Medium", 16),
                                             height=40,
                                             placeholder_text="      . .  /  . .  /  . .")
        self.top_right_entry.pack(padx=(0, 0))
#       
#        
        self.bottom_bg_frame = ttkk.CTkFrame(master=self,
                                   fg_color="#212121",
                                   corner_radius=0)
        self.bottom_bg_frame.pack(fill="both", expand=True)

        for row in range(12):
            self.bottom_bg_frame.grid_rowconfigure(row, minsize=24)
            for col in range(12):
                self.bottom_bg_frame.grid_columnconfigure(col, minsize=24)

        self.bottom_main_frame = ttkk.CTkFrame(master=self.bottom_bg_frame,
                                               fg_color="#3d3d3d")
        self.bottom_main_frame.pack(padx=10, pady=5, fill="x")
        
        self.date_label = ttkk.CTkLabel(master=self.bottom_main_frame,
                                        text="Date",
                                        font=("Montserrat Medium", 20),
                                        height=10,
                                        width=40)
        self.date_label.grid(row=0, column=0, pady=(10, 0))

        self.date_entry = ttkk.CTkEntry(master=self.bottom_main_frame, 
                                        placeholder_text="   ..  /  ..  /  ..",
                                        height=40,
                                        width=140,
                                        fg_color="#292929",
                                        border_width=0,
                                        font=("Montserrat Medium", 18), 
                                        corner_radius=10)
        self.date_entry.grid(row=1, column=0, pady=10, padx=(15, 0))

        self.paymethod_label = ttkk.CTkLabel(self.bottom_main_frame, 
                                            text="Pay Method", 
                                            font=("Montserrat Medium", 20),
                                            height=10,
                                            width=40)
        self.paymethod_label.grid(row=0, column=1, pady=(10,0))

        self.paymethod = ttkk.CTkOptionMenu(self.bottom_main_frame, 
                                          height=40, 
                                          width=170,
                                          fg_color="#292929",
                                          font=("Montserrat Medium", 16),
                                          dropdown_font=("Montserrat Medium", 15),
                                          dropdown_fg_color="#3d3d3d", 
                                          corner_radius=10,
                                          values=["Eftpos", "Cash", "PayPal"])
        self.paymethod.grid(row=1, column=1, padx=(10, 0))

        self.category_label = ttkk.CTkLabel(self.bottom_main_frame, 
                                            text="Category", 
                                            height=10,
                                            width=40,
                                            font=("Montserrat Medium", 20))
        self.category_label.grid(row=0, column=2, pady=(10,0))

        self.category = ttkk.CTkOptionMenu(self.bottom_main_frame, 
                                           height=40, 
                                           width=170,
                                           fg_color="#292929",
                                           font=("Montserrat Medium", 16),
                                           dropdown_font=("Montserrat Medium", 15),
                                           dropdown_fg_color="#3d3d3d", 
                                           corner_radius=10,
                                           values=["Meals", "Snacks", "Toiletries", "Cleaning", "Fuel", "Smokes"])
        self.category.grid(row=1, column=2, padx=(10, 0))

        self.amount_label = ttkk.CTkLabel(self.bottom_main_frame, 
                                          text="Amount", 
                                          height=40,
                                          font=("Montserrat Medium", 20))
        self.amount_label.grid(row=0, column=3, pady=(10, 0))

        self.amount_entry = ttkk.CTkEntry(self.bottom_main_frame, 
                                           placeholder_text="$  ", 
                                           height=40, 
                                           width=140, 
                                           fg_color="#292929", 
                                           border_width=0, 
                                           font=("Montserrat Medium", 18),
                                           corner_radius=10)
        self.amount_entry.grid(row=1, column=3, padx=(10, 0))
      
        self.search_bar = ttkk.CTkEntry(self.bottom_main_frame, 
                                        font=("Montserrat Medium", 18),
                                        corner_radius=10,
                                        fg_color="#292929", 
                                        border_color="#292929",
                                        width=515, 
                                        height=40,
                                        placeholder_text="Search...")
        self.search_bar.grid(row=1, column=4, padx=(10, 0))

        self.search_button = ttkk.CTkButton(self.bottom_main_frame,
                                            width=50,
                                            height=40,
                                            text="<~>", 
                                            font=("Montserrat Medium", 16),
                                            corner_radius=10)
        self.search_button.grid(row=1, column=5, padx=(5,0), sticky="w")

        self.list_only_eft = ttkk.CTkRadioButton(self.bottom_main_frame,
                                                 height=20, 
                                                 width=10,
                                                 radiobutton_width=15,
                                                 radiobutton_height=15,
                                                 font=("Montserrat Medium", 16), 
                                                 text="Show only Eftpos", 
                                                 variable=radio_var, value=1)
        self.list_only_eft.grid(row=0, column=4, pady=(10, 0), padx=(15, 0), sticky="w")

        self.list_only_cash = ttkk.CTkRadioButton(self.bottom_main_frame, 
                                                 height=20,
                                                 width=10,
                                                 radiobutton_height=15,
                                                 radiobutton_width=15, 
                                                 font=("Montserrat Medium", 16),
                                                 text="Show only Cash", 
                                                 variable=radio_var, value=2)
        self.list_only_cash.grid(row=0, column=4, pady=(10, 0), padx=(15, 0))

        self.list_only_paypal = ttkk.CTkRadioButton(self.bottom_main_frame, 
                                                 height=20,
                                                 radiobutton_height=15,
                                                 radiobutton_width=15, 
                                                 font=("Montserrat Medium", 16), 
                                                 text="Show only Paypal", 
                                                 variable=radio_var, value=3)
        self.list_only_paypal.grid(row=0, column=4, pady=(10, 0), padx=(20, 0), sticky="e")

#~~~~~
#~~~~~
        self.middle_bg_frame = ttkk.CTkFrame(self.bottom_bg_frame,
                                             fg_color="#3d3d3d", 
                                             height=40,
                                             width=900)
        self.middle_bg_frame.pack(padx=10, pady=2, anchor="nw")

        self.middle_right_frame = ttkk.CTkFrame(self.bottom_bg_frame,
                                                fg_color="#3d3d3d",
                                                height=40)
        self.middle_right_frame.pack(padx=(0,10), side="top")

#~~~~~
#~~~~~
        self.bottom_second_frame = ttkk.CTkFrame(self.bottom_bg_frame, 
                                                 fg_color="#3d3d3d")
        self.bottom_second_frame.pack(padx=10, pady=(5, 10), fill="both", expand=True)

        self.record_frame = ttkk.CTkFrame(self.bottom_second_frame, 
                                          fg_color="#292929",
                                          width=140, 
                                          corner_radius=10)
        self.record_frame.pack(padx=(15, 5), pady=10, side="left", fill="y")

        self.record_frame2 = ttkk.CTkFrame(self.bottom_second_frame, 
                                          fg_color="#292929",
                                          width=1080, 
                                          corner_radius=10)
        self.record_frame2.pack(padx=(0, 15), pady=10, side="right", fill="y")

#~~~~~
#~~~~~
    def call_entry(self):
        def result():
            f = open("spending.txt", "r")
            check = f.readlines()[-1]
            if date and amount and item in check.split():
                self.success_label.configure(text="success...")
            else:
                self.success_label.configure(text="failed...")
            f.close()

            return
        def delete():
                    self.date_box.delete(0, "end")
                    self.amount_box.delete(0, "end")
                    self.item_box.delete(0, "end")
                    return
        def clear_res():
            self.success_label.configure(text="")
            return

        date = self.date_box.get()
        amount = self.amount_box.get()
        item = self.item_box.get()

        timeout = 1000
        new_line = Spending(self.date_box.get(), self.amount_box.get(), self.item_box.get())
        new_line.write()

        self.after(timeout, result)
        self.success_label.after(5000, clear_res)
        self.after_idle(delete)

    def display_list(self):
        self.list_display.configure(state="normal")
        with open("spending.txt", "r") as f:
            out = f.read()
            f.close()

            if f.closed == False:
                f.close()

        self.list_display.insert(1.0, out)
        self.list_display.configure(state="disabled")
        return


if __name__ == "__main__":
    app = App()
    app.mainloop()