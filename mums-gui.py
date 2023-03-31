import customtkinter as ttkk
import os

ttkk.set_appearance_mode("dark")


class App(ttkk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Spending")
        self.geometry("1600x900")
        self.minsize(1350, 750)
        self.maxsize(1650, 950)

        self.frame1






if __name__ == "__main__":
    app = App()
    app.mainloop()