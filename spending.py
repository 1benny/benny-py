import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Spending")
        self.geometry("270x400")
        self.config(bg="#292929")

        self.frame = tk.Frame(self, bg="#3D3D3D")
        self.frame.pack(padx=10, pady=6, expand=True, fill="both")

        self.label1 = tk.Label(self.frame, 
                               text="Date -/-/-", 
                               font=("Consolas", 9), 
                               bg="#3D3D3D", 
                               fg="#dcdccc")
        self.label1.place(x=1, y=2)



if __name__ == "__main__":
    app = App()
    app.mainloop()