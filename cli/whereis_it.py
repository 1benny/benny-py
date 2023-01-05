import glob
import os

#inp = input("whereis what?: ")
i = input(">> ")

macos_glob = "/Users/admin/**/*"
windows_glob = "C:\\Users\\Ben\\**\\*"

root = glob.glob(macos_glob, recursive=True)

for file in root:
    if i in file:
        print(os.path.join())