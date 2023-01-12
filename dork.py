import customtkinter as ttkk
import requests
import os, sys
import subprocess
import threading

ttkk.set_default_color_theme("dark-blue")
ttkk.set_appearance_mode("dark")

class UI(ttkk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Dork Search")
        self.geometry("450x230")

        self.frame1 = ttkk.CTkFrame(self, fg_color="#3f3f3f")
        self.frame1.pack(fill="both", expand=True, padx=15, pady=15)




if __name__ == "__main__":
    app = UI()
    app.mainloop()