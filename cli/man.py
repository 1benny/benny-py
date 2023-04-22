import platform
import os
import argparse
import time
from colorama import just_fix_windows_console

just_fix_windows_console()
local_os = platform.system()

match local_os:
    case "Windows":
        usr = os.getenv("USERPROFILE")
    case "Darwin":
        usr = os.getenv("HOME")
    case _:
        pass

missing = (f"{usr}\\manpages\\missing.txt")
page_path = (f"{usr}\\manpages\\man-pages\\")

def colour(text, etype):
    if etype == "red":
        out = ('\x1b[1;31;40m' + f'{text}' + '\x1b[0m')
    if etype == "green":
        out = ('\x1b[1;32;40m' + f'{text}' + '\x1b[0m')
    if etype == "blue":
        out = ('\x1b[1;36;40m' + f'{text}' + '\x1b[0m')
    if etype == "yellow":
        out = ('\x1b[1;33;40m' + f'{text}' + '\x1b[0m')
    return out


man = argparse.ArgumentParser(description="Read manual pages for a specified program")
man.add_argument("m", type=str, default=False, help="Name of the program")
args = man.parse_args()

search = f"{page_path}{args.m}.txt"

red_error = colour("Error:", "red")
yes_or_no = colour("[y/n]", "blue")

if os.path.exists(search.replace("/", "\\")) == True:
    try:
        with open(search.replace("/", "\\"), "r", encoding="utf-8") as f:
            content = f.read()
            print(content)
            f.close
    except FileNotFoundError:
        except1 = colour("FileNotFoundError", "green")
        print(f"{red_error} There's a problem with the directory of man-pages' program files.")
        exit(code=1)
    except UnicodeDecodeError:
        except2 = colour("UnicodeDecodeError", "green")
        print(f'Program threw a {except2}. Exiting with 1')
        exit(code=1)
    except UnicodeError:
        except3 = colour("UnicodeError", "green")
        print(f'Program threw a {except3}. Exiting with 1')
        exit(code=1)

else:
    print(colour(f"Couldn't find man page for '{args.m}'...", "red"))
    time.sleep(1)
    
    try: 
        add_missing = input(f"Add entry to missing pages? {yes_or_no}: ")
        if add_missing == "y" or add_missing == "Y":
            with open(missing, "a") as f:
                f.write(f"\n{args.m}.txt")
                f.close()
            print("...")
            with open(missing, "r") as f:
                latest = f.readlines()[-1]
                if (f"{args.m}.txt") in latest:
                    print(colour(f"Successfully added '{args.m}' to missing pages list.", "green") + "\n...")
                    time.sleep(2)
                else:
                    print(f"{red_error} Something went wrong. Entry not added to list.")   
                f.close()

        elif add_missing == "n" or add_missing == "N":
            print(f"No worries.")
            print(colour("Goodbye", "red"))
        
        else:
            print(colour("Input not recognised as answer. Exiting.", "red"))
        
    except FileNotFoundError:
        error = colour("FileNotFoundError", "green")
        print(f"The program threw a {error} error. Exiting with 1.\n")
    except KeyboardInterrupt:
        print(colour("\nGoodbye.", "red"))