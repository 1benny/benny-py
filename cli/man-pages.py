import os
import argparse
import time

man = argparse.ArgumentParser(description="Read manual pages for a specified program")
man.add_argument("m", type=str, default=False, help="Name of the program")
args = man.parse_args()


mans = "C:/Users/Ben/Man/"
search = f"{mans}{args.m}.txt"

        
if os.path.exists(search.replace("/", "\\")) == True:
    try:
        with open(search.replace("/", "\\"), "r", encoding="utf-8") as f:
            content = f.read()
            print(content)
            f.close
    except UnicodeDecodeError:
        print('Having trouble with this one...')
        time.sleep(2)
        print('Try again later...')
    except UnicodeError:
        print('Having trouble with this one...')
        time.sleep(2)
        print('Try again later...')
else:
    print(f"Couldn't find man page for '{args.m}'")
    with open("C:\\Users\\Ben\\Desktop\\shit\\Python\\missing-manpages.txt", "a") as f:
        f.write(f"{args.m}.txt\n")
        f.close()