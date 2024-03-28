# Wed Aug 23 13:45:29 2023
# bdxves
#
# stopwatch.py
#
#
import time
import customtkinter as ttkk
import os

ttkk.set_default_color_theme("dark-blue")
ttkk.set_appearance_mode("dark")

class Stopwatch(ttkk.CTk):
    global pwd
    global assets
    pwd = os.getcwd()

    def __init__(self):
        super().__init__()
        assets = (f"{os.getenv('programdata')}\\Stopwatch\\")
        icon = f"{assets}stopwatch_icon.ico"

#        self.iconbitmap(icon)
        self.title("Stopwatch")
        self.geometry("250x100")
        #self.resizable(False, False)
        self.start_time = None
        self.running = False
        self.timeVar = ttkk.StringVar()
        self.mstimeVar = ttkk.StringVar()

        self.frame = ttkk.CTkFrame(master=self,
                                   fg_color="#3c3c3c")
        self.frame.pack(expand=True, fill="both", padx=5, pady=5)
        self.inner_frame = ttkk.CTkFrame(self.frame,
                                         width=220)
        self.inner_frame.pack(pady=(5,35), padx=7, fill="both", expand=True)
        #
        self.x_label = ttkk.CTkLabel(master=self.inner_frame,
                                     font=("Fira Code SemiBold", 24),
                                     text=".",
                                     fg_color="transparent",
                                     width=0)
        self.ms_label = ttkk.CTkLabel(master=self.inner_frame,
                                      font=("Fira Code SemiBold", 24),
                                      text="00",
                                      textvariable=self.mstimeVar)
        self.ms_label.pack(side="right", pady=(4, 6), padx=(0,40))
        self.time_label = ttkk.CTkLabel(master=self.inner_frame,
                                        font=("Fira Code SemiBold", 24),
                                        text="00:00:00",
                                        textvariable=self.timeVar)
        self.time_label.pack(pady=(5, 0), padx=(35, 0), anchor="w")
        #
        self.startstop_button = ttkk.CTkButton(self.frame,
                                           text="start",
                                           width=110,
                                           height=24,
                                           border_width=0,
                                           command=self.initbutton)
        self.startstop_button.place(x=7, y=60)
#        self.pause_button = ttkk.CTkButton(self.frame,
#                                           text="stop",
#                                           width=70,
#                                           height=24,
#                                           border_width=0,
#                                           command=self.pause)
#        self.pause_button.place(x=85, y=60)
        self.reset_button = ttkk.CTkButton(self.frame,
                                           text="reset",
                                           width=110,
                                           height=24,
                                           border_width=0,
                                           command=self.reset)
        self.reset_button.place(x=123, y=60)

        self.mainloop()

    def initbutton(self):
        if not self.running:
            self.start()
        else:
            self.pause()


    def start(self):
        self.x_label.place(x=145, y=4.7)
        self.startstop_button.configure(text="stop")
#           if preserve:
# ->            self.start_time = time.time() - self.new_time
# ->            print(time.time() - self.start_time)
# ->        else:
        self.start_time = time.time()

        self.timer()
        self.running = True


    def timer(self):
        self.timeVar.set(self.format(time.time() - self.start_time))
        self.mstimeVar.set(self.add_ms(time.time() - self.start_time))
        self.after_loop = self.after(50, self.timer)

    def pause(self):
        if self.running:
            self.startstop_button.configure(text="start") 
            self.after_cancel(self.after_loop)
            self.running = False
            self.time_paused = time.time()
#            self.pause_loop()                                  // Redundant as pause button no longer pauses, just stops
#        elif not self.running:
#            self.pause_button.configure(text="pause")          // ~104
#            self.after_cancel(self.preserve_loop)              // No need for wait-cancel as the time is no longer preserved when stop button is pressed
#            self.start()
#            self.running = True

#    def pause_loop(self):                                      //
#        self.new_time = time.time() - self.time_paused         // Redundant function for pause loop
#        self.preserve_loop = self.after(50, self.pause_loop)   //


    def reset(self):
        self.after_cancel(self.after_loop)
        self.running = False
        self.timeVar.set("00:00:00")
        self.mstimeVar.set("00")


    @staticmethod
    def format(elapse):
        hour = int(elapse/3600)
        min = int(elapse/60 - hour * 60.0)
        sec = int(elapse - hour * 3600.00 - min * 60.0)
#       hsec = int((elapse - hour * 3600.0 - min * 60.0 - sec) * 100.0)
        return '%02d:%02d:%02d' % (hour, min, sec)

    @staticmethod
    def add_ms(elapse):
        hour = int(elapse/3600)
        min = int(elapse/60 - hour * 60.0)
        sec = int(elapse - hour * 3600.00 - min * 60.0)
        hsec = int((elapse - hour * 3600.0 - min * 60.0 - sec) * 100.0)
        return '%d' % (hsec)

Stopwatch()