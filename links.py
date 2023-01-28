import requests
import os
import customtkinter as ttkk

ttkk.set_default_color_theme("dark-blue")
ttkk.set_appearance_mode("dark")

class Links(ttkk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Links")
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
                                         text="Pinned/Important Links", 
                                         text_font=("Consolas", 12))
        self.title_label.pack()

        self.entry1 = ttkk.CTkEntry(self.frame2, 
                                    width=410,
                                    height=0,
                                    text_font=("Montserrat Medium", 8))
        self.entry1.place(x= 10, y=10)

        self.button1 = ttkk.CTkButton(self.frame2, 
                                      width=410,
                                      height=0, 
                                      text_font=("Montserrat", 10), 
                                      text="Show context")
        self.button1.place(x=10, y=35)

        self.button2 = ttkk.CTkButton(self.frame2,
                                      width=410, 
                                      height=0,
                                      text_font=("Montserrat", 10),
                                      text="Add link")
        self.button2.place(x=10, y=65)


        self.label2 = ttkk.CTkLabel(self.frame2, 
                                    text="")




if __name__ == "__main__":
    app = Links()
    app.mainloop()