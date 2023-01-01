import os
import customtkinter as ttkk
import threading 
import tkinter as tk

class App(ttkk.CTk):

    def __init__(self):
        super().__init__()
        self.title("APT Dealer")
        self.geometry("420x230")
        self.maxsize(420, 430)

        self.frame = ttkk.CTkFrame(master=self, 
                                   fg_color="#3d3d3d", 
                                   height=100)
        self.frame.pack(fill="x", expand=False, padx=10, pady=10)

        self.frame2 = ttkk.CTkFrame(master=self, 
                                    fg_color="#3d3d3d", 
                                    height=200)
        self.frame2.pack(fill="both", expand=True, padx=10, pady=(0, 10))

        self.title_label = ttkk.CTkLabel(master=self.frame, 
                                         text="Download and install .deb files via APT", 
                                         font=("Consolas", 16),
                                         text_color="#dcdccc")
        self.title_label.pack(pady=5)

        self.pkg_name = ttkk.CTkLabel(master=self.frame2, 
                                      text="Package name:", 
                                      font=("Consolas", 14), 
                                      text_color="#dcdccc")
        self.pkg_name.place(x=10, y=5)

        self.pkg_entry = ttkk.CTkEntry(master=self.frame2, 
                                       width=200,
                                       height=25,
                                       font=("Consolas", 13),
                                       bg_color="#3d3d3d",
                                       fg_color="#292929",
                                       border_width=1,
                                       border_color="#292929")
        self.pkg_entry.place(x=130, y=8)

        self.clear_btn = ttkk.CTkButton(master=self.frame2, 
                                        text="[Clear]",
                                        width=60,
                                        height=24,
                                        font=("Consolas", 12),
                                        bg_color="#3d3d3d",
                                        fg_color="#3d3d3d",
                                        command=None)
        self.clear_btn.place(x=333, y=8)
    
        teevar = ttkk.IntVar()

        self.checkbtn_tee = ttkk.CTkCheckBox(master=self.frame2,
                                             text="Write to file",
                                             font=("Consolas", 12),
                                             checkmark_color="#dcdccc",
                                             width=0,
                                             variable=teevar, 
                                             onvalue=1, 
                                             offvalue=0,
                                             fg_color="#292929",
                                             bg_color="#292929",
                                             border_color="#3d3d3d")
                                            
        self.checkbtn_tee.place(x=8, y=35)

    def apt(command):
        if command == None:
            pass
        process = threading.Thread(f"cmd.exe {command}")


if __name__ == "__main__":
    app = App()
    app.mainloop()