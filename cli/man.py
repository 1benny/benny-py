import platform
import sys
import os
import argparse
import time
from colorama import just_fix_windows_console


ROOT_DIR = f"{os.environ['userprofile']}\\manpages\\"
MISSING_DIR = os.path.join(ROOT_DIR, "missing.txt")
MANPAGES_DIR = os.path.join(ROOT_DIR, "man-pages")


just_fix_windows_console()
#local_os = platform.system()

#match local_os:
#    case "Windows":
#        usr = os.getenv("USERPROFILE")
#    case "Darwin":
#        usr = os.getenv("HOME")
#    case _:
#        pass

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

red_error = colour("Error:", "red")
yes_or_no = colour("[y/n]", "blue")

man = argparse.ArgumentParser(usage="""man [PROGRAM]
Prints a program's man-pages to stdout""",
                              description=f"""
If the program's man-page is missing or is not readable, you will be prompted to either add the 
name of the missing page to missing.txt, or disregard and exit""")

man.add_argument(f"x", 
                 metavar="[PROGRAM]",
                 nargs="?",
                 help="Name of the program")
man.add_argument("-p",
                 "--path",
                 action="store_true",
                 default=False,
                 help="Print the path in which the man-pages are locally stored and exit.")

args = man.parse_args()
#args.PROGRAM = args.x

search = f"{MANPAGES_DIR}\\{args.x}.txt"

if args.path:
    print(MANPAGES_DIR)
    sys.exit(0)

elif args.x:
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
    elif not args.x:
        print("Hello world")
    else:
        print(colour(f"Couldn't find man page for '{args.x}'...", "red"))
        time.sleep(1)

        try:
            add_missing = input(f"Add entry to missing pages? {yes_or_no}: ")
            if add_missing == "y" or add_missing == "Y":
                with open(MISSING_DIR, "a") as f:
                    f.write(f"\n{args.x}.txt")
                    f.close()
                print("...")
                with open(MISSING_DIR, "r") as f:
                    latest = f.readlines()[-1]
                    if (f"{args.x}.txt") in latest:
                        print(colour(f"Successfully added '{args.x}' to missing pages list.", "green") + "\n...")
                        time.sleep(2)
                    else:
                        print(f"{red_error} Something went wrong. Entry not added to list.")
                    f.close()

            elif add_missing == "n" or add_missing == "N":
                print(colour("All good", "red"))

            else:
                print(colour("Input not recognised as answer. Exiting.", "red"))

        except FileNotFoundError:
            error = colour("FileNotFoundError", "green")
            print(f"The program threw a {error} error. Exiting with 1.\n")
        except KeyboardInterrupt:
            print(colour("\nExiting.", "red"))