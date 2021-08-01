# First Section

import math
import random

def Adding_And_Subtracting_Integers_1(option_difficulty, option_random):
    problemsets = []
    answerset = []
    temp = 0
    list_temp = []
    one = 0
    two = 0

    if option_difficulty == "easy":
        one = random.randint(-99, 99)
        two = random.randint(-99, 99)
        
    elif option_difficulty == "medium":
        one = random.randint(-999, 999)
        two = random.randint(-999, 999)

    elif option_difficulty == "hard":
        one = random.randint(-9999, 9999)
        two = random.randint(-9999, 9999)

    answerset.append(one + two)
    if one < 0:
        one = '(' + str(one) +')'
    if two < 0:
        two = '(' + str(two) +')'

    problemsets.append(str(one) + "+" + str(two))

    return(problemsets, answerset)
a,b = Adding_And_Subtracting_Integers_1("easy", False)
print(a,b)