#First Section

import math
import random
from fractions import Fraction

def Recurring_Decimal_Finder(numerator, denominator):
    recur = ""
    dict = {}
    remainder = numerator % denominator

    while ((remainder != 0) and (remainder not in dict)):
        dict[remainder] = len(recur)

        remainder = remainder * 10
        res_part = remainder // denominator
        recur += str(res_part)
        remainder = remainder % denominator

    if (remainder == 0):
        return("")
    else:
        return(recur[dict[remainder]:])

def Fractions_And_Decimals_Conversion(option_difficulty, option_random):
    problemsets = []
    answerset = 0
    numerator = 0
    denominator = 0
    coefficient = 0
    trailing = 0
    recurring = False
    temp = ""
    frac = ""
    replacement = ""
    place = 0
    
    if(option_difficulty == "easy"):
        denominator = random.randint(2, 10)
        numerator = random.randint(1, denominator - 1)
        print(numerator, denominator)
        problemsets.append(numerator)
        problemsets.append(denominator)
        answerset = (numerator/denominator)

    elif(option_difficulty == "medium"):
        denominator = random.randint(11, 50)
        numerator = random.randint(1, denominator - 1)
        coefficient = random.randint(1,5)
        print(coefficient, numerator, denominator)
        problemsets.append(coefficient)
        frac = str(Fraction(numerator, denominator))
        frac.replace("Fraction(", '')
        frac.replace(")", '')  
        problemsets.append(frac)
        answerset = (numerator/denominator)
        
    elif(option_difficulty == "hard"):
        denominator = random.randint(20, 999)
        numerator = random.randint(10, denominator - 1)
        coefficient = random.randint(10,25)
        print(coefficient, numerator, denominator)
        problemsets.append(coefficient)
        frac = str(Fraction(numerator, denominator))
        frac.replace("Fraction(", '')
        frac.replace(")", '')  
        problemsets.append(frac)
        answerset = (numerator/denominator)

    if len(str(answerset)) > 6:
        recurring = True
        trailing = Recurring_Decimal_Finder(numerator, denominator)
        temp = str(trailing)
        print("temp",temp)
    
        replacement = str(answerset)
        place = replacement.find(str(trailing)) + len(str(trailing))
        print("replacement",place)
        replacement = list(replacement)
        print(replacement[:int(place)])
        answerset = replacement[:int(place)]
        answerset = "".join(answerset)
        answerset = round(float(answerset), 3)
        
    return(problemsets, float(answerset) + float(coefficient), recurring, trailing)


a,b,c,d = Fractions_And_Decimals_Conversion("hard", False)
print(a,b,c,d)