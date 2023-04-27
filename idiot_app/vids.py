import cv2
import numpy
import playsound
from time import sleep
import multiprocessing

def playaudio():
    playsound.playsound("idiot.wav")

def playvid():
    cap = cv2.VideoCapture('idiot.mp4')

    if (cap.isOpened()== False):
        print("Error opening video file")

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            cv2.imshow('Frame', frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                audio_thread.kill()
                break

            elif cv2.getWindowProperty('Frame', cv2.WND_PROP_VISIBLE) < 1:
                playsound.playsound("fart.wav")
    cap.release()
    cv2.destroyAllWindows()

audio_thread = multiprocessing.Process(target=playaudio)
video_thread = multiprocessing.Process(target=playvid)

if __name__ == "__main__":
    audio_thread.start()
    video_thread.start()