import threading
import subprocess as sub
from subprocess import *
from time import sleep
import os
import re

class Winget(object):

    def __init__(self, cmd):
        self.cmd = cmd
        self.process = None

    def run(self, timeout):
        def target():
            print('Thread Started')
            self.process = sub.Popen(self.cmd, shell=True)
            self.process.communicate()
            print("Thread Finished")
        
        thread = threading.Thread(target=target)
        thread.start()

        thread.join(timeout)
        if thread.is_alive():
            print("Terminating Process")
            self.process.terminate()
            thread.join()
        print(self.process.returncode)


myList = ["install", "search", "list"]
#  x = input(">> ")
#  if any(i in myList for i in x.split()):
#      print(x)
#  else:
#      print("Invalid statement! Get a life!")

inp = input(">> ")



if any(i in myList for i in inp.split()):
    command = Winget(inp)
    command.run(timeout=20)