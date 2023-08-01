import os
import time

UP = "\033[1A"
ERASE = "\x1b[2k"

str1 = "Line 1"
str2 = "line 2"
str3 = "line 3"
str4 = "line 4"


print(str1)
print(str2)
print(str3)
print(str4)
    
i = 1
while i < 7:
    print(UP, end=ERASE)
    print("      \b", end=ERASE)
    i += 1