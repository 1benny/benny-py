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
        self.resizable(False, True)

        self.frame1 = ttkk.CTkFrame(self, fg_color="#3d3d3d")
        self.frame1.pack(fill="both", expand=True, padx=15, pady=15)

        self.label1 = ttkk.CTkLabel(self, 
                                    text="Enter a search query in the search bar below",
                                    text_font=("Montserrat Medium", 11), 
                                    text_color="#ffffff", 
                                    fg_color="#3d3d3d",
                                    bg_color="#3d3d3d")
        self.label1.place(x=50, y=25)

        self.entry1 = ttkk.CTkEntry(self,
                                    width=340,
                                    height=25,
                                    fg_color="#292929",
                                    bg_color="#3d3d3d",
                                    border_color="#3f3f3f",
                                    border_width=0,
                                    text_font=("Montserrat Medium", 8))
        self.entry1.place(x=50, y=60)

        self.button_search = ttkk.CTkButton(self,
                                            text="Search",
                                            text_font=("Montserrat Medium", 10),
                                            bg_color="#3f3f3f",
                                            width=340,
                                            height=25,
                                            command=None)
        self.button_search.place(x=50, y=95)

    class Dork:

        def __init__(self, method, query, ):
            self.query = query
            self.method = method

        def search(self, method, query):
            req = requests.get()




if __name__ == "__main__":
    app = UI()
    app.mainloop()


##  intitle, inurl, intext, define, site


f'site:facebook.com intext:"{query}" OR intext:"{query}" OR intext:"{query}"'
site:instagram.com intext:"61411144247" OR intext:"+61411144247" OR intext:"0411144247"

"intext:"61411144247" OR intext:"+61411144247" OR intext:"0411144247" OR intext:"0411 144 247""
"(ext:doc OR ext:docx OR ext:odt OR ext:pdf OR ext:rtf OR ext:sxw OR ext:psw OR ext:ppt OR ext:pptx OR ext:pps OR ext:csv OR ext:txt OR ext:xls) intext:"61411144247" OR intext:"+61411144247" OR intext:"0411144247""