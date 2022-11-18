taps_passed = "All Taps/Mixers resulted compliant for water saving efficiency."


date = input("Date as ../.. /..  : ")
anyensuite = input("ensuite present? [Y/N]: ")
if anyensuite == "Y" or anyensuite == "y":
    ensuite = "en suite"
else:
    ensuite = ""

complies = input("All taps flow rate passed? [Y/N]: ")
if complies == "Y" or complies == "y":
    final_compliance = taps_passed
else:
    final_compliance = "The remaining fixtures on the property resulted compliant for water saving efficiency."

anyproblems = input("Problems with fixtures? [Y/N]: ")
if anyproblems == "Y" or anyproblems == "y":
    present_problems = ("the " + input("Fixtures with problems: "))
    problem1 = input("Problem 1: ")
    solution1 = input("Replaced or Repaired?: ")
    append = input("Append additional problems? [Y/N]: ")
    if append == "Y" or append == "y":
        problem2 = input("Problem 2: ")
        solution2 = input("replaced or repaired?: ")
    else:
        pass
else:
    present_problems = "none of the fixtures."

print(f"Attended Property on {date} for Water Efficiency Complaince Test. Tested fixtures in Kitchen, Main Bathroom, Laundry and {ensuite} for water efficiency, in which we discovered issues with {present_problems}")