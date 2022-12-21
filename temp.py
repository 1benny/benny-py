import requests
import tkinter as tk

class sms(object):
    
    def __init__(self, endpoint, *args, **kwargs):
        self.endpoint = endpoint

    @classmethod
    def check(cls, key):
        endpoint = 
        


sms.check(key="textbelt")



class App(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.title("SMS API")
        self.geometry("280x150")
        self.configure(bg="#292929")

        self.frame = tk.Frame(self, 
                              bg="#3d3d3d")
        self.frame.pack(padx=15, pady=10, fill="both", expand=True)

        self.entry = tk.Entry(self.frame, 
                              width=20, 
                              font=("Consolas", 9))
        self.entry.pack()


if __name__ == "__main__":
    app = App()
    app.mainloop()


