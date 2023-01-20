import requests
import os
import customtkinter as ttkk

ttkk.set_default_color_theme("dark-blue")
ttkk.set_appearance_mode("dark")


class aroflo(ttkk.CTk):
    def __init__(self):
        super().__init__()
        self.title("AroFlo")
        self.geometry("1150x740")

        self.frame = ttkk.CTkFrame(self, 
                                   fg_color="#292929")
        self.frame.pack(padx=13, pady=13, fill="both", expand=True)





if __name__ == "__main__":
    app = aroflo()
    app.mainloop()