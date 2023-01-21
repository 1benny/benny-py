import os
import argparse as arg
from argparse import *

def list_dir():
    for i in os.listdir(pwd):
        print(i)




def long(pwd):
    contents = []
    for i in os.listdir(pwd):
        if os.path.exists(i in range(len(i)) == True):
            print(i)
#       print(f"{i}    ~>   {}")
#       contents.append(i)
#       for name in contents:
#           each = os.path.join(pwd, name)
#           print(each)





ls = ArgumentParser(prog="ls for windows", description="Linux/Unix-style listing program except its for windows because i created it and we all love windows")
ls.add_argument("dir", type=str, default=False, help="Required positional argument for name of directory to list")
ls.add_argument("-l", metavar="--long", default=False, help="Present list in longer format with extra details")
args = ls.parse_args()

pwd = os.getcwd()

if args.l:
    long(pwd=pwd)