def RGBToHex(r, g, b):
    r, g, b = x, y, z
    return '#%02X%02X%02X' % (int(r), int(g), int(b))
  
x, y, z = input("enter: ").split()
print(RGBToHex(int(x), int(y), int(z)))