import argparse
import time
import subprocess as sub

def descript(page):
    with open(page, "r", encoding="utf-8") as f:
        desc = f.readlines()[3]
        print(f"\n{desc[6:-1]}")
        f.close()
    return

def missing_page(page):
    with open(page, "a") as f:
        f.write(f"{args.a}\n")
        f.close()
        print(f"Appended '{args.a}' to man-page download helper")
    return

cli = argparse.ArgumentParser(prog="whatis for windows", description="general what is that program")
cli.add_argument("a", type=str, help="Required positional argument for query")
args = cli.parse_args()

database = f"C:\\Users\\Ben\\manpages\\man-pages\\{args.a}.txt"
missing_dir = "C:\\Users\\Ben\\manpages\\missing.txt"

try:
    descript(page=database)
except FileNotFoundError:
    try:
        time.sleep(2)
        print("Nothing found in man-pages")
        time.sleep(1)
        missing = input("Make an entry for missing manpage? y/n: ")
        if missing == "y" or missing == "Y":
            missing_page(page=missing_dir)
        elif missing == "n" or missing == "N":
            print(colour_print.printc("\nNo worries.", "red"))
        elif KeyboardInterrupt:
            print(f"\nWhatever fuckwit")
    except KeyboardInterrupt:
        print(f"\nWhatever fuckwit")