# global rgb_input
# rgb_input = input("Enter rgb values: ")

# def testfunc(r, g, b):
#    return ("{:X:X:X}").format(r, g, b)
# print(testfunc(str(rgb_input)))

# k = 1
# v = "house"
# c = "yes"

# input ("Do you own {} {}? If so, answer {}".format( k,v,c ))


#def multi_input(*args):
#    return input



#def rgb_to_hex(rgb):
#    return '%02x%02x%02x' % rgb
# result = rgb_to_hex((255, 255, 195))
# print(result)


# car = {"brand": "Ford", "model": "Mustang", "year": 1964}

# x = car.get("model")

# print(x)




####<< Needs a variable that holds the input as 3 comma-separated
####<< value, that can also somehow be plugged into the keyword
####<< arguments for formatting as rgb




#inpt = input().split(",")
#
#print(inpt)
#


#------------------------------------------------------------------------------------------


# Python program showing how to
# multiple input using split
  
# taking two inputs at a time
x, y = input("Enter two values: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)
print()
  
# taking three inputs at a time
x, y, z = input("Enter three values: ").split()
print("Total number of students: ", x)
print("Number of boys is : ", y)
print("Number of girls is : ", z)
print()
  
# taking two inputs at a time
a, b = input("Enter two values: ").split()
print("First number is {} and second number is {}".format(a, b))
print()
  
# taking multiple inputs at a time 
# and type casting using list() function
x = list(map(int, input("Enter multiple values: ").split()))
print("List of students: ", x)