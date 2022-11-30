from time import sleep
import os


class test:
    x = os.getcwd()
    
    print("The PWD is currently " + x)
    
    change_dir = input("Would you like to change? Y/N: ")
    
    if change_dir == "Y" or change_dir == "y" or change_dir == "yes":
        pwd = os.getcwd()
        if 'Desktop' in pwd:
            pwd = pwd
        else:
            pwd = os.path.join(pwd, 'Desktop')
    else:
        print("wow how pointless")
    
    sleep(3)
    
    os.chdir(pwd)
    
    sleep(2)
    
    print(pwd)


print("hello world")