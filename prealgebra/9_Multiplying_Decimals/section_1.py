# First Section

import math
import random

def Multiplying_Decimals_1(option_difficulty, option_random): # Two numbers (Rounded to the nearest ten thousandth place)
    problemsets = []
    answerset = []
    negative = [1, -1]
    list_holder = []
    one = 0
    two = 0

    if option_difficulty == "easy":
        one = random.choice(negative) * float(str(random.randint(1, 9)) + "." + str(random.randint(1, 9)))
        two = random.choice(negative) * float(str(random.randint(1, 9)) + "." + str(random.randint(1, 9)))
        
    elif option_difficulty == "medium":
        one = random.choice(negative) * float(str(random.randint(1, 9)) + "." + str(random.randint(1, 99)))
        two = random.choice(negative) * float(str(random.randint(1, 9)) + "." + str(random.randint(1, 99)))

    elif option_difficulty == "hard":
        one = random.choice(negative) * float(str(random.randint(1, 99)) + "." + str(random.randint(1, 999)))
        two = random.choice(negative) * float(str(random.randint(1, 99)) + "." + str(random.randint(1, 999)))
    
    
    # answer generation...

    answerset.append(round(one * two, 5)) # about

    problemsets.append("$ " + str(one) + " \times " + str(two) + " $") # "latexified"


    return(problemsets, answerset)

a,b = Multiplying_Decimals_1("easy", False)
print(a,b)
a,b = Multiplying_Decimals_1("medium", False)
print(a,b)
a,b = Multiplying_Decimals_1("hard", False)
print(a,b)