import tkinter as tk
import customtkinter as ttkk
import subprocess as sub
import threading

# create/open/write entered information to a file 

# create a class for an object that has the properties "date" "ammount" "item"

# create a GUI to enter these values as data

# have the data written to text file in a specific format

class Spending(object):
    
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

class Manipulate(Spending):
    def __init__(self, date, amount, item):
        self.date = date
        self.amount = amount
        self.item = item


ttkk.set_appearance_mode("dark")
ttkk.set_default_color_theme("dark-blue")

class App(ttkk.CTk):

    global font1
    font1 = "Montserrat Medium"

    def __init__(self):
        super().__init__()
        self.title("Spending")
        self.geometry("430x245")
        self.configure(bg="#292929")
        self.resizable(False, True)
        self.maxsize(430,745)
        self.minsize(430, 245)

        

        self.frame = ttkk.CTkFrame(master=self,                         # primary frame
                                   fg_color="#3D3D3D") 
        self.frame.pack(padx=15, pady=10, fill="x")
        #
        self.frame2 = ttkk.CTkFrame(master=self.frame,                  # secondary frame
                                    fg_color="#292929",
                                    width=360, 
                                    height=70)
        self.frame2.pack(side="top", pady=40)
        #       
        self.frame3 = ttkk.CTkFrame(master=self, 
                                    fg_color="#3d3d3d", 
                                    width=360, 
                                    height=900)
        self.frame3.pack(padx=15, pady=(0, 10), fill="both")           
        #
        self.pull_down = ttkk.CTkLabel(master=self.frame3, 
                                       text="...",
                                       width=0, 
                                       height=0)
        self.pull_down.place(relx=0.485, rely=0.7, anchor="w")
        #
        self.list_display = ttkk.CTkTextbox(master=self.frame3,
                                            state="disabled",
                                            border_width=0,
                                            width=360,
                                            height=690,
                                            text_font=("Consolas", 8),
                                            fg_color="#3D3D3D")
        self.list_display.pack(expand=True, padx=(25, 0), pady=(0, 10))


        self.title_label = ttkk.CTkLabel(master=self.frame,             # title label
                                         text="Write a new entry for spendings", 
                                         text_font=("Montserrat Medium", 12), 
                                         text_color="#dcdccc")
        self.title_label.place(x=60, y=6)    
        #        
        self.date_label = ttkk.CTkLabel(master=self.frame,              # label
                                        text="Date",
                                        bg_color="#292929", 
                                        width=0,
                                        text_font=("Montserrat Medium", 10))
        self.date_label.place(x=67, y=45)
        #
        self.amount_label = ttkk.CTkLabel(master=self.frame,            # label
                                          text="Amount",
                                          bg_color="#292929", 
                                          text_font=("Montserrat Medium", 10))
        self.amount_label.place(x=130, y=45)
        #
        self.item_label = ttkk.CTkLabel(master=self.frame,              # label
                                        text="Item", 
                                        bg_color="#292929",
                                        width=0, 
                                        text_font=("Montserrat Medium", 10))
        self.item_label.place(x=295, y=45)


        self.date_box = ttkk.CTkEntry(master=self.frame,                # entry field
                                      width=80, 
                                      height=25, 
                                      text_font=("Montserrat Medium", 8), 
                                      border_color="#292929",
                                      fg_color="#3d3d3d",
                                      bg_color="#292929")
        self.date_box.place(x=45, y=70)
        #       
        self.amount_box = ttkk.CTkEntry(master=self.frame,              # entry field
                                        width=50, 
                                        height=25,
                                        text_font=("Montserrat Medium", 8), 
                                        border_color="#292929", 
                                        fg_color="#3d3d3d",
                                        bg_color="#292929")
        self.amount_box.place(x=175, y=70)
        #       
        self.item_box = ttkk.CTkEntry(master=self.frame,                # entry field
                                      width=80, 
                                      height=25,
                                      text_font=("Montserrat Medium", 8), 
                                      border_color="#292929", 
                                      fg_color="#3d3d3d",
                                      bg_color="#292929")
        self.item_box.place(x=273, y=70)
        #
        ttkk.CTkLabel(master=self.frame,                                # seperator "::"
                      text="::", 
                      bg_color="#292929",
                      width=0,
                      text_font=("Montserrat Medium", 10)).place(x=145, y=67)        
        ttkk.CTkLabel(master=self.frame,                                # seperator "::"
                      text="::",
                      bg_color="#292929", 
                      width=0,
                      text_font=("Montserrat Medium", 10)).place(x=245, y=67)


        self.click_write = ttkk.CTkButton(master=self.frame,
                                          text="Add entry",
                                          text_font=(font1, 10),
                                          height=0,
                                          width=178,
                                          #fg_color="#292929",
                                          command=self.call_entry)
        self.click_write.place(x=20, y=115)
        #
        self.print_list = ttkk.CTkButton(master=self.frame,
                                         text="Print list", 
                                         text_font=(font1, 10),
                                         height=0, 
                                         width=177.8, 
                                         command=self.display_list)
        self.print_list.place(x=203, y=115)
        #
        self.success_label = ttkk.CTkLabel(master=self.frame,
                                           text="", 
                                           text_font=("Montserrat Italic", 9), 
                                           width=0,
                                           height=20)
        self.success_label.pack(side="bottom")
        #   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   #

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