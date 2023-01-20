import requests
import os
import customtkinter as ttkk

ttkk.set_default_color_theme("dark-blue")
ttkk.set_appearance_mode("dark")

class git(ttkk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Git")
        self.geometry("450x240")
        self.resizable(True, True)

        self.frame = ttkk.CTkFrame(self, 
                                   fg_color="#3d3d3d", 
                                   height=50)
        self.frame.pack(padx=10, pady=(10, 0), fill="x", expand=False)

        self.frame2 = ttkk.CTkFrame(self, 
                                   fg_color="#3d3d3d", 
                                   height=200)
        self.frame2.pack(padx=10, pady=(10, 10), fill="both", expand=True)


        self.title_label = ttkk.CTkLabel(self.frame, 
                                         text="Pull / Push Tool for version control", 
                                         text_font=("Consolas", 12))
        self.title_label.pack()

        self.entry1 = ttkk.CTkEntry(self.frame2, 
                                    width=30,
                                    height=0,
                                    text_font=("Montserrat Medium", 8))
        self.entry1.pack()

        self.label2 = ttkk.CTkLabel(self.frame2, 
                                    text="")


if __name__ == "__main__":
    app = git()
    app.mainloop()