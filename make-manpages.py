import os
import subprocess as sub

def tee():
    page = input("prog name >> ")
    file = input("writeout name >> ")
    cmd = f"man {page} | tee ~/Desktop/Python/bdives-main/{page}.txt"
    
    with open(f"{file}.txt", "a") as f:
        sub.getoutput(cmd)
        f.write(sub.getoutput(cmd))
        os.system("clear")
        f.close

while True:
    try:
        tee()
        continue
    except KeyboardInterrupt:
        break