line = [1]

while len(line) < 100:
    for i in line:
        line.append(i+1)
        print(line[-1])