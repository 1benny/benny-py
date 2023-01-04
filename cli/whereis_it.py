import glob

#inp = input("whereis what?: ")
i = input(">> ")

root = glob.glob(f"C:\\Users\\Ben\\**\\*.exe", recursive=True)

for file in root:
    if i in file:
        print(file)

