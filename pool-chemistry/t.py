from dataclasses import dataclass

@dataclass
class SaltPool:
    chlorine: tuple = (3.0, 5.0)
    ph: tuple = (7.2, 7.6)
    alkalinity: tuple = (80, 120)

@dataclass
class MineralPool:
    chlorine: tuple = (1.0, 3.0)
    ph: tuple = (7.0, 7.5)
    alkalinity: tuple = (100, 150)



class PoolAnalyzer:
    def __init__(self, pool_data):
        # store the dataclass instance
        self.pool_data = pool_data

    def print_ranges(self):
        # loop through all attributes of the dataclass
        for field_name, value in self.pool_data.__dict__.items():
            print(f"{field_name.capitalize()} range: {value}")


# User input decides which pool
pool_type = input("Enter pool type (salt/mineral): ").strip().lower()

if pool_type == "salt":
    selected_pool = SaltPool()
elif pool_type == "mineral":
    selected_pool = MineralPool()
else:
    print("Unknown pool type")
    exit()

# Initialize analyzer with chosen dataclass
analyzer = PoolAnalyzer(selected_pool)

# Use the method to print values
analyzer.print_ranges()



# -------------------------------------------
# Salt + Mineral Pool
# -------------------------------------------
# Test factor                     Ideal range
# -------------------------------------------
# Total Chlorine:                  0.5 - 3   
# pH:                              7.2 - 7.6 
# Adjusted Alkalinity:             80  - 120 
# Calcium Hardness:                200 - 275 
# Cyanuric Acid:                   30  - 50  
# Magnesium Hardness:              450 - 800 
# -------------------------------------------