from multiprocessing.sharedctypes import Value
from typing import final


# def funky(r, g, b):
#     global x, y, z
#     hex = x, y, z
#     return hex 
#
# x, y, z = input("enter numbers: ").split(" ")
#
# value = funky(r=x, g=y, b=z)
#
# final = (eval(value, ('{:X}{:X}{:X}').format(x, y, z)))
#
# print(final)

def RGBToHex(r, g, b):
    r, g, b = x, y, z
    return '#%02X%02X%02X' % (int(r), int(g), int(b))
  
x, y, z = input("enter: ").split()
print(RGBToHex(int(x), int(y), int(z)))