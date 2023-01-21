import argparse
import time
import subprocess as sub

cli = argparse.ArgumentParser(prog="whatis for windows", description="general what is that program")
cli.add_argument("a", type=str, help="Required positional argument for query")
args = cli.parse_args()

database = "C:/Users/Ben/Man/"
search = ((f"{database}{args.a}.txt").replace("/", "\\"))
manpage_installer = "C:\\Users\\Ben\\Man\\python\\missing\\"

try:
    with open(search, "r", encoding="utf-8") as f:
        desc = f.readlines()[3]
        print(f"\n{desc[6:-1]}")
        f.close()
except FileNotFoundError:
    try:
        time.sleep(2)
        print("Nothing found in man-pages")
        time.sleep(1)
        missing = input("Make an entry for missing manpage? y/n: ")
        if missing == "y" or missing == "Y":
            with open(manpage_installer, "a") as f:
                f.write(f"{args.a}\n")
                f.close()
                print(f"\nAppended '{args.a}' to man-page download helper")
        else:
            print("\nNo worries.")
    except KeyboardInterrupt:
        print(f"\nWhatever fuckwit")