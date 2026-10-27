import tkinter
from tkinter import filedialog
from PIL import Image
from PIL.ExifTags import TAGS
import os

#def getData(ipath):
#    with Image.open(ipath) as img:
#        exif = img.getexif()
#
#        gps_info = exif.get_ifd(0x8825)
#        gps = {}
#
#        for tag_id, value in exif.items():
#            tag = TAGS.get(tag_id, tag_id)
#            print(f"{tag}: {value}")
#    return 

parent = tkinter.Tk()
parent.withdraw()

imagePath = filedialog.askopenfilename(
    title="Select image file",
    filetypes=[("Media files", "*.jpg *.png *.mp4 *.heic")]
)

#parse file path to metadata function

if imagePath:
    image = imagePath.replace("/", "\\")
    with Image.open(image) as img:
        exif = img.getexif()

#        gps_info = exif.get_ifd(0x8825)
#        gps = {}

        for tag_id, value in exif.items():
            tag = TAGS.get(tag_id, tag_id)
            print(f"{tag}: {value}")
else:
    print("Failure.")
