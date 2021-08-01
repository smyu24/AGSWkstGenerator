#Second Section

import math
import random
from fractions import Fraction

def Fractions_And_Decimals_Conversion_2(option_difficulty, option_random):
    problemsets = []
    answerset = []
    recurring = False
    holder = 0
    
    if(option_difficulty == "easy"):
        problemsets.append(str(random.randint(1, 9) + "0." + str(random.randint(1, 99))))
    
    elif(option_difficulty == "medium"):
        problemsets.append(str(random.randint(1, 9)) + "." + str(random.randint(1, 99)))

    elif(option_difficulty == "hard"):
        problemsets.append(str(random.randint(10, 25)) + "." + str(random.randint(1, 999)))
    
    holder = int(round(float(problemsets[0]),1 )) - float(problemsets[0])
    print(holder)
    print(Fraction(holder, 100))

    return(problemsets, answerset, recurring)


a,b,c = Fractions_And_Decimals_Conversion_2("medium", False)
print(a,b,c)