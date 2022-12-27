import os
import elevate

def find(filename):
    result = []

    for root, dir, files in os.walk("C:\\Users\\Ben\\Desktop\\"):
        if filename in files:
            result.append(os.path.join(root, filename))
        return result


print(find("whereis.txt"))