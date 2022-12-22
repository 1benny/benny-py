import customtkinter as ttkk
import requests
import socket

ttkk.set_appearance_mode("dark")
ttkk.set_default_color_theme("dark-blue")

class App(ttkk.CTk):
    def __init__(self):
        super().__init__()
        self.title("List Editor Program")
        self.geometry("430x250")
    


if __name__ == "__main__":
    app = App()
    app.mainloop()