[post.py]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import requests
from tkinter import *


def post1():
    req = requests.post("https://textbelt.com/text", {
            "phone": inp_phone, 
            "message": inp_msg,
            "key": inp_key
        })
    return req


options = print("""
# # # # # # # # # # # # # # # # # # # 
#     Choose an option [1] [2]      #
#                                   #
#    [1] ~ Send SMS through POST    #
#                                   #
#    [2] ~ Check quota status       #
#                                   #
# # # # # # # # # # # # # # # # # # #  
    """)

opt_input = input(">> ")
if opt_input == "1":
    print("""
# # # # # # # # # # # # # # # # # # #
#    Enter Phone number formatted   #
#     with area code e.g. ~ [61]    #
# # # # # # # # # # # # # # # # # # #
    """)

    inp_phone = input("phone: ")
    print("""
# # # # # # # # # # # # # # # # # # #
#       Enter Message to send:      #
#  [Nothing vulgar it won't send]   #
# # # # # # # # # # # # # # # # # # # 
    """)

    inp_msg = input("message: ")
    print("""
# # # # # # # # # # # # # # # # # # #
#  Enter API Key or use "textbelt"  #
# [Check Key quota using option 2]  #
# # # # # # # # # # # # # # # # # # #
""")

    inp_key = input("API Key: ")
    print(post1().json())
    
elif opt_input == "2":
    print("*insert other function here")

elif opt_input == "9":
    print("you found a secret. cool.")
else:
    print("Invalid option") 

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

[post-animation.py]

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import random

reg = LinearRegression()

x_values = []
y_values = []

for i in range(1000):
    plt.clf()
    x_values.append(random.randint(0,100))
    y_values.append(random.randint(0,100))

    x = np.array(x_values)
    x = x.reshape(-1, 1)

    y = np.array(y_values)
    y = y.reshape(-1, 1)

    if i % 20 == 0:
        reg.fit(x, y)
        plt.xlim(0,100)
        plt.ylim(0,100)
        plt.scatter(x_values, y_values, color="black")
        plt.plot(list(range(100)), reg.predict(np.array([x for x in range(100)]).reshape(-1, 1)))
        plt.pause(0.0001)

plt.show()

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

[var_plots.py]

import matplotlib.pyplot as plt
import random

values = [0] * 50

for i in range(50):
    values[i] = (random.randint(0, 100))
    plt.xlim(0,50)
    plt.ylim(0, 100)
    plt.bar(list(range(50)), values)
    plt.pause(0.0001)
			
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~