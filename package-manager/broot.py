import customtkinter
from elevate import elevate
from time import sleep
import subprocess as sub
import threading

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")




class Winget(object):

    def __init__(self, cmd):
        self.cmd = cmd
        self.process = None

    def run(self, timeout):
        def target():
#           print('Thread Started')
            self.process = sub.Popen(self.cmd, shell=True)
            self.process.communicate()
#           print("Thread Finished")
        
        thread = threading.Thread(target=target)
        thread.start()
#       sleep(1)
        
        #print(self.process.returncode)
        thread.join(timeout)
        if thread.is_alive():
            print("Terminating Process")
            self.process.terminate()
            thread.join()

#       App.after(timeout)
        #print(self.process.returncode)
#       sleep(0.5)


class App(customtkinter.CTk):
    
    cmd_dict = {
        "i": "install",
        "ii": "search", 
        "iii": "list"    
    }
    
    gwidth=490
    gheight=280

    def __init__(self):
        super().__init__()
#       |
        self.title("Installer")
        self.geometry(f"{App.gwidth}x{App.gheight}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        #threading.Thread(target=self.wsearch).start()

        self.frame1 = customtkinter.CTkFrame(master=self)
        self.frame1.pack(padx=15, pady=10, fill="both", expand=True)
#       |
        self.seperator = customtkinter.CTkLabel(master=self.frame1, 
                                                text="_________________________________________________________________________", 
                                                fg_color="#292929", 
                                                text_color="#FFFFFF")
        self.seperator.place(x=10, y=10)
#       |
        self.label_title = customtkinter.CTkLabel(master=self.frame1, 
                                                  text="Search for a package and install", 
                                                  text_font=("Consolas", 10), 
                                                  fg_color="#292929")
        self.label_title.place(x=110, y=0)
#       |
        self.searchbox = customtkinter.CTkEntry(master=self.frame1, 
                                                width=245, 
                                                height=0, 
                                                border_color="#292929")
        self.searchbox.place(x=3, y=32)
#       |
        self.search_button = customtkinter.CTkButton(master=self.frame1, 
                                                     height=0, 
                                                     width=10,
                                                     border_width=0,
                                                     text="Search", 
                                                     text_font=("Consolas", 9),
                                                     fg_color = "#292929", 
                                                     command=self.run_cmd) #lambda: self.run_cmd("winget search ", self.searchbox.get()))
        self.search_button.place(x=247, y=33)
#       |
        self.install_button = customtkinter.CTkButton(master=self.frame1, 
                                                      height=0, 
                                                      width=10, 
                                                      border_width=0, 
                                                      text="Install", 
                                                      text_font=("Consolas", 9),
                                                      fg_color="#292929",
                                                      command=None)                 
        self.install_button.place(x=312, y=33)
#       |
        self.list_button = customtkinter.CTkButton(master=self.frame1, 
                                                   height=0, 
                                                   width=60, 
                                                   border_width=0, 
                                                   text="List",
                                                   text_font=("Consolas", 9),
                                                   fg_color="#292929",
                                                   command=None)
        self.list_button.place(x=383, y=33)
#       |
        self.h_scroll = customtkinter.CTkScrollbar(self.frame1, 
                                                   orientation='horizontal', 
                                                   fg_color="#292929")
        self.h_scroll.pack(side='bottom', fill='x', padx=10, pady=2)
#       |
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
        
    def on_closing(self, event=0):
        self.destroy()


    def run_cmd(self):
        inpt = Winget("winget list")
        inpt.run(timeout=20)
        #self.output.insert(1.0, inpt)
        


#done = False
#daemon = Winget(f"start /B winget {winget_cmd} {p_name}")

if __name__ == "__main__":
    app = App()
    app.mainloop()