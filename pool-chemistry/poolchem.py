#enter pool liters
#   -> work with per 10,000
#enter chemical
#   -> store and parse to use with const ideal ppm values 
#enter result ppm
#   -> work with const ppm values per chemical
#
#
class Pool:
    def __init__(self, volume, calcium):
        self.volume = volume
        self.calcium = calcium

    def showMe(self):
        print(f"Pool volume: {self.volume}L")
        print(f"Total hardness: {self.calcium}")


    def findRequiredCal(self):
        result = (((calUpper - calLower)/2) + calLower)
        print(result)

        needs = self.volume * (result - self.calcium)
        dose = needs/1000000
        print(f"{dose}kg")



calLower, calUpper = (200, 400)

poolVol = input("volume: ")
testResults = input("current calcium: ")

letzGo = Pool(poolVol, testResults)
letzGo.findRequiredCal()

#idealBuffer = 90



#resultCalcium = int(input("calcium (ppm): "))
#poolVol = int(input("pool volume (L): "))
#resultBuffer = int(input("buffer (ppm): "))


#print(resultCalcium)
#print(resultBuffer)

#findRequiredCal(poolVol, resultCalcium)