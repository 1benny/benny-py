weight = input("Enter your weight>> ")
measure = input("is that [K]g or [L]bs ")
if measure == 'K' or measure == "k":
    ktop = int(weight) * float(2.20462262185)
    print(str(ktop) + "Lbs")
else:
    pass

if measure == 'L' or measure == "l":
    ptok = int(weight) / float(2.20462262185)
    print(str(ptok) + "Kgs")
else:
    pass