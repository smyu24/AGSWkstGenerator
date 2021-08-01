# Second Section

import math
import random

def Multiplying_Decimals_2(option_difficulty, option_random): # Three numbers (Rounded to the nearest ten thousandth place)
    problemsets = []
    answerset = []
    negative = [1, -1]
    list_holder = []
    one = 0
    two = 0
    three = 0
    if option_difficulty == "easy":
        one = random.choice(negative) * float(str(random.randint(1, 9)) + "." + str(random.randint(1, 9)))
        two = random.choice(negative) * float(str(random.randint(1, 9)) + "." + str(random.randint(1, 9)))
        three = random.choice(negative) * float(str(random.randint(1, 9)) + "." + str(random.randint(1, 9)))
    
    elif option_difficulty == "medium":
        one = random.choice(negative) * float(str(random.randint(1, 9)) + "." + str(random.randint(1, 99)))
        two = random.choice(negative) * float(str(random.randint(1, 9)) + "." + str(random.randint(1, 99)))
        three = random.choice(negative) * float(str(random.randint(1, 9)) + "." + str(random.randint(1, 99)))    
    
    elif option_difficulty == "hard":
        one = random.choice(negative) * float(str(random.randint(1, 99)) + "." + str(random.randint(1, 999)))
        two = random.choice(negative) * float(str(random.randint(1, 99)) + "." + str(random.randint(1, 999)))
        three = random.choice(negative) * float(str(random.randint(1, 99)) + "." + str(random.randint(1, 999)))
    
    # answer generation...

    answerset.append(round(one * two * three, 5)) # about

    problemsets.append("$ " + str(one) + " \times " + str(two) + " \times " + str(three) + " $") # "latexified"


    return(problemsets, answerset)

a,b = Multiplying_Decimals_2("easy", False)
print(a,b)
a,b = Multiplying_Decimals_2("medium", False)
print(a,b)
a,b = Multiplying_Decimals_2("hard", False)
print(a,b)