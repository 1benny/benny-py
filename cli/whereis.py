import argparse as ap
import os
import sys


SYSTEM_DIR = "C:\\"
USER_DIR = os.path.expanduser("~")

def search(root_folder, targetName):
    for root, dirs, files in os.walk(root_folder, topdown=True, onerror=None):
        for file in files:
            if targetName.lower() in file.lower():
                print(os.path.join(root, file))



program = ap.ArgumentParser(usage="""whereis [OPTION]... FILE""", description="Recursively search for files or directories")
program.add_argument("name", metavar="FILE", type=str, help="Name of file to search for")
program.add_argument("-d", "--drive", action="store_true", help="Used for searching thru entire drive")


if len(sys.argv) == 1:
    program.print_usage()
    sys.exit(0)
args = program.parse_args()
try:
    if args.drive:
        search(SYSTEM_DIR, args.name)
    elif args.name:
        search(USER_DIR, args.name)

except KeyboardInterrupt:
    print("\nOperation cancelled by user.")
