import subprocess as sub
import threading
from time import sleep

def cmd():
    #sub.Popen("cmd.exe /k")
    print("Hello Friend")
    sleep(1)
    print("Goodbye Friend")


x = threading.Thread(target=cmd)
x.start()
print(threading.active_count())

sleep(4)

print("done...")


class wingetit():
    def __init__(self, query, install, list):
        self.query = query
        self.install = install
        self.list = list
