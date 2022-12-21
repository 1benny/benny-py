import tkinter as tk

class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("test")
        self.geometry("240x145")
        self.resizable(False, False)
        
        self.b = tk.Button(self, text="press", width=5, height=0, command=self.iteration)
        self.b.pack(fill="x") 

        self.text = tk.Text(self, width=200, height=105)
        self.text.pack()
        #self.text.bind("<Return>", self.newline)

    line1 = [0]

#   def newline(self, event):
#       self.line1.append(self.line1[-1]+1)
#       i = self.line1[-1]
#       ind = f"{i}.0"
#       self.text.insert(ind, i)
    def iteration(self):
        mylist = [1]
#       mylist.append(int([0])+1)
        while mylist[-1] < 10:
            mylist.append(mylist[-1]+1)
            print(mylist[-1])
                

        
if __name__ == "__main__":
    app = App()
    app.mainloop()