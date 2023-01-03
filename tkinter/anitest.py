from time import sleep
from tkinter import StringVar
import tkinter as tk
import itertools
import threading
import time
import sys


def animation():
    while True:
        for rod in r'\|/—\|/—':
            print(rod, end='\r')
            
            sleep(0.2)


def animation2(rod):
    text = r'-\|/-\|/-'
    while True:
        for rod in r'-\|/-\|/-':
            text += rod + '\r'
            sleep(0.25)
        return text




done = False

def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rDownloading... ' + c)
        sys.stdout.flush()
        time.sleep(0.2)
    sys.stdout.write('\rSuccess...     ')

t = threading.Thread(target=animate)
t.start()

time.sleep(4)
done = True