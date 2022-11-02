import tkinter as tk
from math import *

def rgb_to_hex(r, g, b):
    return ("{:X} {:X} {:X}").format(r, g, b)
    
print(rgb_to_hex(57, 242, 168))