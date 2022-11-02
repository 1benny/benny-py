import os
from pytube import YouTube
from time import sleep
import tkinter as tk
from tkinter import filedialog

tk.Tk().withdraw()

chosen_vid = YouTube("https://www.youtube.com/watch?v=umxtU6wmXJg&ab_channel=bdives")

title = chosen_vid.title
thumb = chosen_vid.thumbnail_url

print("Video title: " + title)

sleep(1)

print("Downloading...")



folderx = input("Make new directory? [Y/N]")
if folderx == "Y":
    download_path = filedialog.askdirectory()
    sleep(2)
    print("Saved video to " + download_path)
else:
    download_path = "C:\\Users\\Ben\\Desktop\\"

chosen_vid = chosen_vid.streams.get_highest_resolution()

chosen_vid.download(download_path)

sleep(2)

print("Done!")

wanna_open = input("Open video in explorer? [Y/N]: ")

if wanna_open == "Y" or wanna_open == "y":
    sleep(3)
    os.system(start=final_path)
else:
    pass