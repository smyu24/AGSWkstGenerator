import math
import random

def Multiplying_Decimals_1(option_difficulty, option_random, localmin, localmax): # Two numbers (Rounded to the nearest ten thousandth place)
    problemsets = []
    answerset = []
    negative = [1, -1]
    list_holder = []
    one = 0
    two = 0

    if(localmin == localmax):
        if option_difficulty == 1:
            one = random.choice(negative) * float(str(random.randint(1, 9)) + "." + str(random.randint(1, 9)))
            two = random.choice(negative) * float(str(random.randint(1, 9)) + "." + str(random.randint(1, 9)))
            
        elif option_difficulty == 2:
            one = random.choice(negative) * float(str(random.randint(1, 9)) + "." + str(random.randint(1, 99)))
            two = random.choice(negative) * float(str(random.randint(1, 9)) + "." + str(random.randint(1, 99)))

        elif option_difficulty == 3:
            one = random.choice(negative) * float(str(random.randint(1, 99)) + "." + str(random.randint(1, 999)))
            two = random.choice(negative) * float(str(random.randint(1, 99)) + "." + str(random.randint(1, 999)))
    else:
        if option_difficulty == 1:
            one = random.choice(negative) * float(str(random.randint(1, 9)) + "." + str(random.randint(localmin, localmax)))
            two = random.choice(negative) * float(str(random.randint(1, 9)) + "." + str(random.randint(localmin, localmax)))
            
        elif option_difficulty == 2:
            one = random.choice(negative) * float(str(random.randint(1, 9)) + "." + str(random.randint(localmin, localmax)))
            two = random.choice(negative) * float(str(random.randint(1, 9)) + "." + str(random.randint(localmin, localmax)))

        elif option_difficulty == 3:
            one = random.choice(negative) * float(str(random.randint(1, 99)) + "." + str(random.randint(localmin, localmax)))
            two = random.choice(negative) * float(str(random.randint(1, 99)) + "." + str(random.randint(localmin, localmax)))
    
    
    # answer generation...

    answerset.append(round(one * two, 5)) # about

    problemsets.append(str(one) + " \times " + str(two)) # "latexified"


    return(problemsets, answerset)

def Multiplying_Decimals_2(option_difficulty, option_random, localmin, localmax): # Three numbers (Rounded to the nearest ten thousandth place)
    problemsets = []
    answerset = []
    negative = [1, -1]
    list_holder = []
    one = 0
    two = 0
    three = 0

    if(localmin == localmax):
        if option_difficulty == 1:
            one = random.choice(negative) * float(str(random.randint(1, 9)) + "." + str(random.randint(1, 9)))
            two = random.choice(negative) * float(str(random.randint(1, 9)) + "." + str(random.randint(1, 9)))
            three = random.choice(negative) * float(str(random.randint(1, 9)) + "." + str(random.randint(1, 9)))
            
        elif option_difficulty == 2:
            one = random.choice(negative) * float(str(random.randint(1, 9)) + "." + str(random.randint(1, 99)))
            two = random.choice(negative) * float(str(random.randint(1, 9)) + "." + str(random.randint(1, 99)))
            three = random.choice(negative) * float(str(random.randint(1, 9)) + "." + str(random.randint(1, 99)))

        elif option_difficulty == 3:
            one = random.choice(negative) * float(str(random.randint(1, 99)) + "." + str(random.randint(1, 999)))
            two = random.choice(negative) * float(str(random.randint(1, 99)) + "." + str(random.randint(1, 999)))
            three = random.choice(negative) * float(str(random.randint(1, 99)) + "." + str(random.randint(1, 999)))
    else:
        if option_difficulty == 1:
            one = random.choice(negative) * float(str(random.randint(1, 9)) + "." + str(random.randint(localmin, localmax)))
            two = random.choice(negative) * float(str(random.randint(1, 9)) + "." + str(random.randint(localmin, localmax)))
            three = random.choice(negative) * float(str(random.randint(1, 9)) + "." + str(random.randint(localmin, localmax)))
            
        elif option_difficulty == 2:
            one = random.choice(negative) * float(str(random.randint(1, 9)) + "." + str(random.randint(localmin, localmax)))
            two = random.choice(negative) * float(str(random.randint(1, 9)) + "." + str(random.randint(localmin, localmax)))
            three = random.choice(negative) * float(str(random.randint(1, 9)) + "." + str(random.randint(localmin, localmax)))

        elif option_difficulty == 3:
            one = random.choice(negative) * float(str(random.randint(1, 99)) + "." + str(random.randint(localmin, localmax)))
            two = random.choice(negative) * float(str(random.randint(1, 99)) + "." + str(random.randint(localmin, localmax)))
            three = random.choice(negative) * float(str(random.randint(1, 99)) + "." + str(random.randint(localmin, localmax)))
    
    # answer generation...

    answerset.append(round(one * two * three, 5)) # about

    problemsets.append(str(one) + " \times " + str(two) + " \times " + str(three)) # "latexified"


    return(problemsets, answerset)