import customtkinter as ttkk

# A GUI program that provides list utilities e.g. Spendings, shopping list, formatted lists, password management, etc...

class Document(object):
    
    type1 = "hello dfriend"
    
    
    def __init__(self, name, format, date):
        self.name = name
        self.format = format
        self.date = date
    
    def new_doc(self, name, date, type):
        with open(self.name, "a") as f:
            f.write(self.type1)
            
            if f.closed == False:
                f.close
        

    class List(object):
        def __init__(self, format):
            self.format = format
        
        def structure(self):
            format = None

new1 = Document("My_List.txt", "10/12/22", None)
new1.new_doc("fdafdsf", "3", "fdsdf")


class AppMenu(ttkk.CTkToplevel, ttkk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Launcher")
        self.geometry("280x150")
        self.configure(bg="#292929")

        self.btn = ttkk.CTkButton(master=self, text="Press", command=new) 

    def new(self):
        


if __name__ == "__main__":
    app = AppMenu()
    app.mainloop()