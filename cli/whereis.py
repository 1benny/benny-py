import argparse
import glob
import os


sys = "C:\\**\\*"
home = "C:\\Users\\Ben\\**\\*"

def search(root_folder):
    for file in glob.iglob(root_folder, include_hidden=True, recursive=True):
        if args.a in file:
            print(file)
            break
    

cli = argparse.ArgumentParser(description="whereis program for recusively searching directories")
cli.add_argument("a", type=str, default=True, help="Required positional arg for filename/directory to search for")
cli.add_argument("-x", metavar="--system", action="store_const", const=True, default=False, help="Search entire system")
args = cli.parse_args()

try:
    if args.x:
        search(root_folder=sys)
    else:
        search(root_folder=home)

except KeyboardInterrupt:
    print("Detected keyboard interrupt. Exiting")
    