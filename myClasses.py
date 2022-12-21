class Human(object):
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob
    
    def newborn(self):
        print(f"Welcome, {name}, born {dob}")

name = input("Name your child: ")
dob = input("Date: ")

baby = Human(name, dob)

baby.newborn()