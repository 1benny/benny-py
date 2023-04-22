import cv2
import numpy as np
from playsound import playsound
from ffpyplayer.player import MediaPlayer
from time import sleep


def idiot(path):
    vid = cv2.VideoCapture("idiot.mp4")
    player = MediaPlayer
    

cap = cv2.VideoCapture("idiot.mp4")

if (cap.isOpened()== False):
    print("Error opening video file")

playsound("C:\\Users\\Ben\\Projects\\bdives-py\\idiot_app\\idiot.wav")

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow('Frame', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break
    
cap.release()

cv2.destroyAllWindows()

