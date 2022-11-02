import math

one = int(input('>> '))
two = int(input('>> '))
divisorfunc = (float(one) / float(two))
modfunc = (int(one) % int(two))
op = input('Operation: ')
modext = int(one) // int(two) or float(one) / float(two)
if op == "+":
    print(int(one) + int(two))
if op == "-":
    print(int(one) - int(two))
if op == "/":
    print(float(one) / float(two))
if op == "*":
    print(int(one) * int(two))
if op == "//":
    print(int(one) // int(two))
if op == "**":
    print(int(one) ** int(two))
if op == "%":
    modchoice = input("return with divisor?[Y/N] ")
    if (modchoice) == "y":
        str(print("divisor:>> " + str(divisorfunc)))
        str(print("modulo:>> " + str(modfunc)))
    else:
        print(modfunc)
if op == "gcd":
    print(math.gcd(int(one), int(two)))
if op == "lcm":
    print(math.lcm(int(one), int(two)))