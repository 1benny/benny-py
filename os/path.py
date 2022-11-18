import os
from time import sleep


# def openthis():
#     f = open(answer, "r")
#     readit = f.read()
#     print(readit)
#     return


# answer = input("Enter file name: ")


# try:
#     openthis()
# except FileNotFoundError:
#     print("Sorry mate, File not found")
#     sleep(2)
# else:
#     print("Heres this instead")

i = input(">> ")
if i == "1":
    f = open("writeout.txt", "r")
    try:
        print(5 // 0)
    except ZeroDivisionError:
        print("hello World")
    else:
        pass

elif i == "2":
    try:
        print(5*1)
    except TypeError:
        print("wtf? not even close")
else:
    pass



