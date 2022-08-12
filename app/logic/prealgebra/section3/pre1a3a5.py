# First Section

import math
import random

def Adding_And_Subtracting_Decimals_1(option_difficulty, option_random, localmin, localmax):
    problemsets = []
    answerset = []
    one = 0
    two = 0
    place = 0

    if(localmin == localmax):
        if option_difficulty == 1:
            one = float(str(random.randint(-9, 9)) + "." + str(random.randint(1, 9)))
            two = float(str(random.randint(-9, 9)) + "." + str(random.randint(1, 9)))
            place = 1
            
        elif option_difficulty == 2:
            one = float(str(random.randint(-99, 99)) + "." + str(random.randint(1, 99)))
            two = float(str(random.randint(-99, 99)) + "." + str(random.randint(1, 99)))
            place = 2

        elif option_difficulty == 3:
            one = float(str(random.randint(-999, 999)) + "." + str(random.randint(1, 999)))
            two = float(str(random.randint(-999, 999)) + "." + str(random.randint(1, 999)))
            place = 3
    else:
        one = float(str(random.randint((int(localmin)), localmax)) + "." + str(random.randint(1, localmax)))
        two = float(str(random.randint((int(localmin)), localmax)) + "." + str(random.randint(1, localmax)))
        if option_difficulty == 1:
            place = 1
            
        elif option_difficulty == 2:
            place = 2

        elif option_difficulty == 3:
            place = 3
        
    answerset.append(round(one + two, place))
    if one < 0:
        one = '(' + str(one) +')'
    if two < 0:
        two = '(' + str(two) +')'

    problemsets.append(str(one) + "+" + str(two))

    return(problemsets, answerset)

def Adding_And_Subtracting_Decimals_2(option_difficulty, option_random, localmin, localmax):
    problemsets = []
    answerset = []
    one = 0
    two = 0
    place = 0

    if(localmin == localmax):
        if option_difficulty == 1:
            one = float(str(random.randint(-9, 9)) + "." + str(random.randint(1, 9)))
            two = float(str(random.randint(-9, 9)) + "." + str(random.randint(1, 9)))
            place = 1
            
        elif option_difficulty == 2:
            one = float(str(random.randint(-99, 99)) + "." + str(random.randint(1, 99)))
            two = float(str(random.randint(-99, 99)) + "." + str(random.randint(1, 99)))
            place = 2

        elif option_difficulty == 3:
            one = float(str(random.randint(-999, 999)) + "." + str(random.randint(1, 999)))
            two = float(str(random.randint(-999, 999)) + "." + str(random.randint(1, 999)))
            place = 3
    else:
        one = float(str(random.randint((int(localmin)), localmax)) + "." + str(random.randint(1, localmax)))
        two = float(str(random.randint((int(localmin)), localmax)) + "." + str(random.randint(1, localmax)))
        if option_difficulty == 1:
            place = 1
            
        elif option_difficulty == 2:
            place = 2

        elif option_difficulty == 3:
            place = 3
        
    answerset.append(round(one - two, place))
    if one < 0:
        one = '(' + str(one) +')'
    if two < 0:
        two = '(' + str(two) +')'

    problemsets.append(str(one) + "-" + str(two))

    return(problemsets, answerset)