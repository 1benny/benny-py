from time import sleep
from pytube import YouTube
import os

newfolder = input("Enter name for the new directory at C: -> Users -> Ben -> Desktop -> ... ")

os.mkdir(f"C:\\Users\\Ben\\Desktop\\{newfolder}")

url = YouTube("https://www.youtube.com/watch?v=CNcHPxHX63c&ab_channel=Dercury")
title = url.title
thumb = url.thumbnail_url

print(title)

sleep(3)

print(thumb)

url = url.streams.get_highest_resolution()

url.download(f"C:\\Users\\Ben\\Desktop\\{newfolder}")

input("")