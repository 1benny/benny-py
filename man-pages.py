import os
import subprocess as sub
import argparse


man = argparse.ArgumentParser(description="Read manual pages for a specified program")
man.add_argument("m", metavar="Only required positional argument, used to specify man-page for program", type=str, default=False, help="Name of the program")
args = man.parse_args()


mans = "C:/Users/Ben/Man/"
search = f"{mans}{args.m}.txt"


### Test to see if function works by printing yes if the directory exists
        
if os.path.exists(search.replace("/", "\\")) == True:
    #print(os.listdir(mans))
    with open(search.replace("/", "\\"), "r") as f:
        content = f.read()
        print(content)
        f.close

else:
    print(f"Couldn't find man page for '{args.m}'")