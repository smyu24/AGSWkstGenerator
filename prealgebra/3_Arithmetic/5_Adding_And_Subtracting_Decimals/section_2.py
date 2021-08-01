# Second Section

import math
import random

def Adding_And_Subtracting_Decimals_2(option_difficulty, option_random):
    problemsets = []
    answerset = []
    one = 0
    two = 0
    place = 0

    if option_difficulty == "easy":
        one = float(str(random.randint(-9, 9)) + "." + str(random.randint(1, 9)))
        two = float(str(random.randint(-9, 9)) + "." + str(random.randint(1, 9)))
        place = 1
        
    elif option_difficulty == "medium":
        one = float(str(random.randint(-99, 99)) + "." + str(random.randint(1, 99)))
        two = float(str(random.randint(-99, 99)) + "." + str(random.randint(1, 99)))
        place = 2

    elif option_difficulty == "hard":
        one = float(str(random.randint(-999, 999)) + "." + str(random.randint(1, 999)))
        two = float(str(random.randint(-999, 999)) + "." + str(random.randint(1, 999)))
        place = 3
        
    answerset.append(round(one - two, place))
    if one < 0:
        one = '(' + str(one) +')'
    if two < 0:
        two = '(' + str(two) +')'

    problemsets.append(str(one) + "-" + str(two))

    return(problemsets, answerset)
a,b = Adding_And_Subtracting_Decimals_2("easy", False)
print(a,b)
a,b = Adding_And_Subtracting_Decimals_2("medium", False)
print(a,b)
a,b = Adding_And_Subtracting_Decimals_2("hard", False)
print(a,b)