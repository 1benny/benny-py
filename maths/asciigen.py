import string
import random

charList = ""

password = []

for i in range(10):
    randchar = random.choice(string.ascii_letters)
    password.append(randchar)

print("".join(password))