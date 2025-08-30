#
#
#
# class saltpool
#     initialize volume, ph, calcium, sunblock alkalinity...
#         initializing class compares data entered with preset class specific data (2-of)
#             self.x
#             self.y
#             self.z
#                 ->    if not ==
# 
# 
# 
# 
# 


#enter pool liters
#   -> work with per 10,000
#enter chemical
#   -> store and parse to use with const ideal ppm values 
#enter result ppm
#   -> work with const ppm values per chemical
#
#

# class salt...
#   ph                  = 7.2 - 7.8
#   adjusted alkalinity = 80 - 120
#   total hardness      = 200 - 400
#   cyanuric acid       = 30 - 100
#   salt                = 2500 - 3500

#class theralux mineral...
#   total chlorine      = 0.5 - 3
#   ph                  = 7.2 - 7.8
#   adjusted alkalinity = 80 - 120
#   total hardness      = 200 - 275
#   cyanuric acid       = 30 - 50
#   salt                = 2500 - 3500
#   magnesium hardness  = 450 - 800

class SaltPool:
    def __init__(self, volume, ph, alk, calcium, sunblock, salt):
        self.volume = volume
        self.ph = ph
        self.alk = alk
        self.calcium = calcium
        self.sunblock = sunblock
        self.salt = salt
