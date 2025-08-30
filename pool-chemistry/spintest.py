from dataclasses import dataclass
from os import system
import time

##  Add calculate w/ forumla per chemical
##  format
##  make less ugly/clunky


@dataclass
class SaltPool:
    name = "Salt Pool"
    #chlorine: tuple = (2, 4)
    chlorLower, chlorUpper = (2, 4)
    #ph: tuple = (7.2, 7.8)
    phLower, phUpper = (7.2, 7.8)
    #alk: tuple = (80, 120)
    alkLower, alkUpper = (80, 120)
    #calc: tuple = (200, 400)
    calcLower, calcUpper = (200, 400)
    #cya: tuple = (30, 100)
    cyaLower, cyaUpper = (30, 100)
    saltLower, saltUpper = (2500, 3500)

@dataclass
class MineralPool:
    name = "Salt + Mineral Pool"
    chlorLower, chlorUpper = (0.5, 3)
    phLower, phUpper = (7.2, 7.6)
    alkLower, alkUpper = (80, 120)
    calcLower, calcUpper = (200, 275)
    cyaLower, cyaUpper = (30, 50)
    saltLower, saltUpper = (2500, 3500)
    magLower, magUpper = (450, 800)


class SpinTest:
    def __init__(self, profile, result):
        self.profile = profile
        self.result = result
    
    def compare_results(self):
        
        system("cls")
        print(self.result)
        
        try:
            print(f"----------------------------------------------\n{self.profile.name}\n----------------------------------------------")
            print("Test factor\t\tIdeal range\tResult\n----------------------------------------------")
            print(f"Total Chlorine:\t\t{self.profile.chlorLower} - {self.profile.chlorUpper}\t\t{self.result[0]}")
            print(f"pH:\t\t\t{self.profile.phLower} - {self.profile.phUpper}\t{self.result[1]}")
            print(f"Adjusted Alkalinity:\t{self.profile.alkLower} - {self.profile.alkUpper}\t{self.result[2]}")
            print(f"Calcium Hardness:\t{self.profile.calcLower} - {self.profile.calcUpper}\t{self.result[3]}")
#            print(f"Cyanuric Acid:\t\t{self.profile.cyaLower} - {self.profile.cyaUpper}\t{self.result[4]}")
            if len(self.result) > 4:
                print(f"Cyanuric Acid:\t\t{self.profile.cyaLower} - {self.profile.cyaUpper} \t{self.result[4]}")
                print(f"Magnesium Hardness:\t{self.profile.magLower} - {self.profile.magUpper}\t{self.result[5]}")
            else:
                print(f"Cyanuric Acid:\t\t{self.profile.cyaLower} - {self.profile.cyaUpper}\t{self.result[4]}")
        except AttributeError:
            exit(0)
    

    def chlorDose(self):
        try:
            float_list = [float(i) for i in self.result if i is not None]
        except ValueError:
            print("ValueError")
            return 0

#        if self.result[0] > self.profile.chlorUpper:
        chlorineDose = 0
#        else:
        gramsChlor = ((self.profile.chlorUpper - float_list[0]) / 1000)
        chlorineDose = gramsChlor / 125
        return chlorineDose
    
    def explainDose(self):
        dose_ml = self.chlorDose()
        print("\n----------------------------------------------\n")
        print(f"Needs {dose_ml:.1f} mL HyChlor.")



user_result = (input("Pool profile: "))

user_volume = input("Pool volume in litres: ")

factors = input("Results: ").split()

#chlorineResult, phResult, alkResult, calcResult, cyaResult, magResult = input("Results: ").split()


#chlorineResult, phResult, alkResult, calcResult, cyaResult, magResult = (factors + [None]*6)[:6]

if user_result == "salt":
    if len(factors) != 5:
        print("Salt profile expects only 5 test factors.")
        exit(0)
    else:
        pool = SaltPool()
        profileName = "Salt Pool"
        results = factors

elif user_result == "mineral":
    if len(factors) != 6:
        print("Salt + Mineral profile expects only 6 test factors.")
        exit(0)
    else:
        pool = MineralPool()
        profileName = "Salt + Mineral Pool"
        results = factors
    




system("cls")
time.sleep(1)
print("...")
time.sleep(1)

# showTestResults = SpinTest(profile=pool, result=(chlorineResult, phResult, alkResult, calcResult, cyaResult, magResult))
showTestResults = SpinTest(profile=pool, result=results)
showTestResults.compare_results()
showTestResults.explainDose()