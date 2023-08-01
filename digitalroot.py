def digital_root(n):    
    print(n)
    
    if n <= 9:
        return n
    else:
        sum([int(i) for i in str(n)])

digital_root(14554)