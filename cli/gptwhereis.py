import argparse
import glob
import os
import sys

# Paths to search
SYSTEM_ROOT = "C:\\**\\*"
USER_HOME = os.path.expanduser("~") + "\\**\\*"

def search(root_folder, target_name):
    found = False
    for path in glob.iglob(root_folder, recursive=True):
        if os.path.basename(path).lower() == target_name.lower():
            print(path)
            found = True
    if not found:
        print(f"No matches found for: {target_name}")

def main():
    parser = argparse.ArgumentParser(description="whereis-style file search for Windows")
    parser.add_argument("target", type=str, help="Filename or directory to search for")
    parser.add_argument("-x", "--system", action="store_true", help="Search entire system instead of user directory")
    args = parser.parse_args()

    try:
        root = SYSTEM_ROOT if args.system else USER_HOME
        search(root, args.target)
    except KeyboardInterrupt:
        print("\nSearch cancelled by user.")
        sys.exit(1)

if __name__ == "__main__":
    main()