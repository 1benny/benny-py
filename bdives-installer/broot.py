import customtkinter
import subprocess as sub
from elevate import elevate
import threading
from time import sleep

elevate(show_console=False)

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


class App(customtkinter.CTk):
    
    gwidth=490
    gheight=280

    def __init__(self):
        super().__init__()

        self.title("Installer")
        self.geometry(f"{App.gwidth}x{App.gheight}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        #threading.Thread(target=self.wsearch).start()
    
        self.frame1 = customtkinter.CTkFrame(master=self)
        self.frame1.pack(padx=15, pady=10, fill="both", expand=True)

        self.seperator = customtkinter.CTkLabel(master=self.frame1, 
                                                text="_________________________________________________________________________", 
                                                fg_color="#292929", 
                                                text_color="#FFFFFF")
        self.seperator.place(x=10, y=10)

        self.label_title = customtkinter.CTkLabel(master=self.frame1, 
                                                  text="Search for a package and install", 
                                                  text_font=("Consolas", 10), 
                                                  fg_color="#292929")
        self.label_title.place(x=110, y=0)

        self.searchbox = customtkinter.CTkEntry(master=self.frame1, 
                                                width=245, 
                                                height=0, 
                                                border_color="#292929")
        self.searchbox.place(x=3, y=32)

        self.search_button = customtkinter.CTkButton(master=self.frame1, 
                                                     height=0, 
                                                     width=10,
                                                     border_width=0,
                                                     text="Search", 
                                                     text_font=("Consolas", 9),
                                                     fg_color = "#292929", 
                                                     command=App.wsearchD)
        self.search_button.place(x=247, y=33)

        self.install_button = customtkinter.CTkButton(master=self.frame1, 
                                                      height=0, 
                                                      width=10, 
                                                      border_width=0, 
                                                      text="Install", 
                                                      text_font=("Consolas", 9),
                                                      fg_color="#292929",
                                                      command=None)                 
        self.install_button.place(x=312, y=33)

        self.list_button = customtkinter.CTkButton(master=self.frame1, 
                                                   height=0, 
                                                   width=60, 
                                                   border_width=0, 
                                                   text="List",
                                                   text_font=("Consolas", 9),
                                                   fg_color="#292929",
                                                   command=None)
        self.list_button.place(x=383, y=33)

        self.h_scroll = customtkinter.CTkScrollbar(self.frame1, 
                                                   orientation='horizontal', 
                                                   fg_color="#292929")
        self.h_scroll.pack(side='bottom', fill='x', padx=10, pady=2)

        self.output = customtkinter.CTkTextbox(master=self.frame1, 
                                               width=450,
                                               height=180, 
                                               fg_color="#3D3D3D",
                                               text_font=("Consolas", 9),
                                               wrap='none',
                                               corner_radius=6,
                                               xscrollcommand=self.h_scroll.set)
        self.output.place(x=5, y=58)

    ### want this block of functions to inherit the methods of a premade class that includes "winget" class
    
    def wsearch():
        search = app.output.get()
        process = sub.getoutput(f"winget search {search}")
        sleep(3)
        app.output.insert(1.0, process)
        return
    
    def wsearchD():
        print("hello trees")
        y = threading.Thread(target=self.wsearch)
        y.start()

        print(threading.active_count)


    def on_closing(self, event=0):
        self.destroy()


class Winget(threading.Thread, App):
    def __init__(self):
        super().__init__()
        




if __name__ == "__main__":
    app = App()
    app.mainloop()

