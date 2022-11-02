from tkinter import *
import tkinter as tk
from math import *


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# For Ace and ensuring organisation of Rinnai contracted installs                                                                                                                       # 
# Ultimately the goal if writing this program will be to ensure that future subcontracted works/ possibly any works in general will have a backup proofreader                           #
# to work as a double-checker of sorts, which will assist in my job and will assist Dustin in organising correct parts delivery as well as help cooperation with Builders who can't     #
# manage the site good enough to make sure the other trades are forming the prerequisites correctly                                                                                     #                                                                                                                                                                                        #
#                                                                                                                                                                                       #
#                                                                                                                                                                                       #
# < Will act like a database that will eventually have a UI for ease of use by all members of staff --                                                                                  #       
#  -- The UI will utilize drop-down boxes for lists as well as checkboxes for double checking [work with ideas later]                                                                   #
#  -- A search box for units that will pass keywords and tags such inventory numbers, order numbers and retail names                                                                    #
#                                                                                                                                                                                       #
# ***For now the program will be raw coded and will operate in the Visual Studio or a command prompt**                                                                                  #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #



# Parts List + Unit for 750 Flame Fire

log_750 = ...

if log_750 is {1, 4}:
    print("cool")
else:
    print("not cool")




import requests
from tkinter import *


#def post1():
#    req = requests.post("https://textbelt.com/text", {
#            "phone": inp_phone, 
#            "message": inp_msg,
#            "key": "324123213413423142134213432141324132423"
#        })
#    return req

#inp_phone = input("phone: ")
#inp_msg = input("message: ")

#print(post1().json())


options = print("""
# # # # # # # # # # # # # # # # # 
#   Choose an option [1] [2]    #
#                               #
# [1] ~ Send SMS through POST   #
#                               #
# [2] ~ Check quota status      #
#                               #
# # # # # # # # # # # # # # # # #   
    """)

opt_input = input(">> ")

if opt_input == "1":
    print("*insert function here*")
elif opt_input == "2":
    print("*insert other function here")
elif opt_input == "9":
    print("you found a secret. cool.")
else:
    print("Invalid option") 
