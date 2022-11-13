import os
from time import sleep


#def openit():
#    text_file = open("sample.txt", 'r')
#    text_file.read()
#
#    text_file.close()



def readit():
    tfile = open("new.txt", 'r')
    tfile.read()
    store_info = tfile
    tfile.close()
    sleep(3)
    print(store_info)




def writeit():
    data = input(">> ")
    with open("new.txt", 'w') as file:
        var = file.write(str(data))
        print(var)
        file.close()
        keyfile = file
        print(keyfile)
        pass



readit()








