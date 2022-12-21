# def RGBToHex(r, g, b):
#     r, g, b = x, y, z
#     return '#%02X%02X%02X' % (int(r), int(g), int(b))
#   
# x, y, z = input("enter: ").split()
# print(RGBToHex(int(x), int(y), int(z)))
# 
# 
# def convert_to_hex(r, g, b):
#     return ("{:X}{:X}{:X}").format(r, g, b)
# r, g, b,=input("enter value(s): ")
# print(convert_to_hex(r, g, b))



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