import time
import os
from dataclasses import dataclass

@dataclass
class SaltPool:
    name = "Salt Pool"
    chlorL, chlorU = (2, 4)
    phL, phU = (7.2, 7.8)
    alkL, alkU = (80, 120)
    calL, calU = (200, 400)
    cyaL, cyaU = (30, 100)
    saltL, saltU = (2500, 3500)

@dataclass
class MineralPool:
    name = "Salt + Mineral Pool"
    chlorL, chlorU = (0.5, 3)
    phL, phU = (7.2, 7.6)
    alkL, alkU = (80, 120)
    calL, calU = (200, 275)
    cyaL, cyaU = (30, 50)
    saltL, saltU = (2500, 3500)
    magL, magU = (450, 800)



class pool_watertest:
    def __init__(self, profile, volume, result):
        self.profile = profile
        self.volume = volume
        self.result = result
    
    def compare_results(self):
        try:
            print(f"""
{self.profile.name}\t\t\t vol. {self.volume:,d}L\n----------------------------------------------
Test factor\t\tIdeal range\tResult\n----------------------------------------------
Total Chlorine:\t\t{self.profile.chlorL} - {self.profile.chlorU}\t\t{self.result[0]:>5}
pH:\t\t\t{self.profile.phL} - {self.profile.phU}\t{self.result[1]:>5}
Adjusted Alkalinity:\t{self.profile.alkL} - {self.profile.alkU}\t{self.result[2]:>5}
Calcium Hardness:\t{self.profile.calU} - {self.profile.calU}\t{self.result[3]:>5}""")
            if isinstance(self.profile, MineralPool):
                print(f"""Cyanuric Acid:\t\t{self.profile.cyaL} - {self.profile.cyaU}\t\t{self.result[4]:>5}
Magnesium Hardness:\t{self.profile.magL} - {self.profile.magU}\t{self.result[5]:>5}""")
            elif isinstance(self.profile, SaltPool):
                print(f"Cyanuric Acid:\t\t{self.profile.cyaL} - {self.profile.cyaU}\t{self.result[4]:>5}")
        except AttributeError:
            print("Attribute error.")
            exit(0)
        

    def chlorDose(self):
        try:
            float_list = [float(i) for i in self.result if i is not None]
        except ValueError:
            print("ValueError")
            exit(0)
        else:
            mediumIdeal = (((self.profile.chlorU - self.profile.chlorL)/2) + self.profile.chlorL)
            ppm_increase = (mediumIdeal - float_list[0])
            grams_needed = (ppm_increase * self.volume) /1000
            chlorineDose = grams_needed / 125
        
        return chlorineDose * 1000


    def explainDose(self):
        print(self.chlorDose())
        dose_ml = self.chlorDose()
        print("\n----------------------------------------------\n")
        print(f"Needs {dose_ml:.2f} mL HyChlor.")


try:
    user_result = input("Pool profile: ")
    user_volume = int(input("Pool volume in litres: "))
    factors = input("Results: ").split()
except KeyboardInterrupt:
    print("Operation cancelled by user.")
    exit(1)

except ValueError:
    print("Invalid literal. Don't use so many args.")
    exit(1)

else:
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

time.sleep(0.5)
print("...")
time.sleep(0.5)

doTestWithResults = pool_watertest(profile=pool, volume=user_volume, result=results)
doTestWithResults.compare_results()
doTestWithResults.explainDose()