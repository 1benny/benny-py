import os
from pytube import YouTube


folder = input("Choose name for new directory: ")
os.mkdir(f"./{folder}")

vid = YouTube(input("Enter URL: "))

title = vid.title
thumb = vid.thumbnail_url

print(thumb)

vid = vid.streams.get_highest_resolution()

print(title)

vid.download(f"C:\\Users\\Ben\\Desktop\\{folder}")