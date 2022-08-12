import math
import random

def Adding_And_Subtracting_Integers_1(option_difficulty, option_random, localmin, localmax):
    problemsets = []
    answerset = []
    temp = 0
    list_temp = []
    one = 0
    two = 0

    if(localmin == localmax):
        if option_difficulty == 1:
            one = random.randint(-99, 99)
            two = random.randint(-99, 99)
            
        elif option_difficulty == 2:
            one = random.randint(-999, 999)
            two = random.randint(-999, 999)

        elif option_difficulty == 3:
            one = random.randint(-9999, 9999)
            two = random.randint(-9999, 9999)
    else:
        one = random.randint(localmin, localmax)
        two = random.randint(localmin, localmax)

    answerset.append(one + two)
    if one < 0:
        one = '(' + str(one) +')'
    if two < 0:
        two = '(' + str(two) +')'

    problemsets.append(str(one) + "+" + str(two))

    return(problemsets, answerset)

def Adding_And_Subtracting_Integers_2(option_difficulty, option_random, localmin, localmax):
    problemsets = []
    answerset = []
    temp = 0
    list_temp = []
    one = 0
    two = 0

    if(localmin == localmax):
        if option_difficulty == 1:
            one = random.randint(-99, 99)
            two = random.randint(-99, 99)
            
        elif option_difficulty == 2:
            one = random.randint(-999, 999)
            two = random.randint(-999, 999)

        elif option_difficulty == 3:
            one = random.randint(-9999, 9999)
            two = random.randint(-9999, 9999)
    else:
        one = random.randint(localmin, localmax)
        two = random.randint(localmin, localmax)

    answerset.append(one - two)
    if one < 0:
        one = '(' + str(one) +')'
    if two < 0:
        two = '(' + str(two) +')'

    problemsets.append(str(one) + "-" + str(two))

    return(str(problemsets), str(answerset))