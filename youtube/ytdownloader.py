from pytube import YouTube
from time import sleep
import os
import tkinter
from tkinter import filedialog

tkinter.Tk().withdraw()

print("""

# # # # # # # # # # # # # # # # # # # # # # #
#  The Dawg's YouTube downloader            #
#   ~ Version-0.0.1                         #
#   ~ Only for use by bald people           #
# # # # # # # # # # # # # # # # # # # # # # # 
""")

url = input("// Enter URL >>  ")

vid = YouTube(url)

title = vid.title
thumb = vid.thumbnail_url
vid = vid.streams.get_highest_resolution()

print(f"Downloading '{title}'")

sleep(1)


# // Absolutely obnoxious looking while loop with try block that will annoy you until you use the right option //
# // Tries for if yes (Y, y), then pick, but if no (N, n) do nothing which results in using current working directory as download path //   
while True:
    try:
        choose_dir = input("""
Would you like to choose a custom directory? [Y/N]: """)
        if choose_dir == "Y" or choose_dir == "y":
            final_dir = filedialog.askdirectory()
            vid.download(final_dir)
            break
        elif choose_dir == 'N' or choose_dir == 'n':
            pwd = os.getcwd()
            if 'Desktop' in pwd:
                final_dir = pwd
            vid.download(final_dir)
            break
    except TypeError:
            print("Invalid option")
            continue

sleep(1)

print(f"""
Successfully downloaded '{title}' into {final_dir}
""")

open_sesame = input("""Open in explorer? [Y/N]: """)
if open_sesame == "Y" or open_sesame == "y":
    os.system(f'start {final_dir}')
else:
    pass