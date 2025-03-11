#enter pool liters
#   -> work with per 10,000
#enter chemical
#   -> store and parse to use with const ideal ppm values 
#enter result ppm
#   -> work with const ppm values per chemical
#
#

def findRequiredCal(litres, current):
    target = (((idealCalciumHigh - idealCalciumLow)/2) + idealCalciumLow)
    print(target)
    
    needs = litres * (target - current)
    dose = needs/1000000
    print(f"{dose}kg")

idealCalciumLow = 200
idealCalciumHigh = 400

#idealBuffer = 90

resultCalcium = int(input("calcium (ppm): "))
poolVol = int(input("pool volume (L): "))
#resultBuffer = int(input("buffer (ppm): "))


#print(resultCalcium)
#print(resultBuffer)

findRequiredCal(poolVol, resultCalcium)