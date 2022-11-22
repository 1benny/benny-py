import tkinter as tk
from tkinter import *
import cryptography
import requests
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# Create something to store my passwords and credentials:
#   Utility will store credentials by taking 3 key values:
#       ~ Username  ~>  Username for the login
#       ~ Password  ~>  Password for the login
#       ~ Keyword   ~>  Keyword for describing login/purpose and for searching and retrieving login via Utility
#
# Create the Utility by building a class that utilizes methods in order to manipulate/store the credentials 
#   Class will be called "Manager"
#   Class will need methods ::  Which kind??
#       Will class need variables declared within?
#           ~ If so, will there need to be @classmethods to manipulate them?
#           
# 
class Manager:
    def __init__(self, user, passwd, keywd):
        self.user = user
        self.passwd = passwd
        self.keywd = keywd
    
    def printit(self):
        print("Hello: ", self.keywd)


it = Manager("1", "2", "3")

it.printit()