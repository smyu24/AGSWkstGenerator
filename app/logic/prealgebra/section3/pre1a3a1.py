#First Section

import math
import random
from fractions import Fraction
import sympy

def Fractions_And_Decimals_Conversion(option_difficulty, option_random, localmin, localmax):
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
    
    if(option_difficulty == 1):
        if(localmin == localmax):
            denominator = random.randint(2, 10)
        else:
            denominator = random.randint(localmin, localmax)
        numerator = random.randint(1, denominator - 1)
        #print(numerator, denominator)
        problemsets.append(str(numerator) + "/" + str(denominator))
        answerset = (numerator/denominator)

    elif(option_difficulty == 2):
        if(localmin == localmax):
            denominator = random.randint(11, 50)
        else:
            denominator = random.randint(localmin, localmax)
        numerator = random.randint(1, denominator - 1)
        coefficient = random.randint(1,5)
        #print(coefficient, numerator, denominator)
        problemsets.append('({a}) / {b}'.format(a= int(coefficient) * int(denominator) + int(numerator), b= str(denominator)))

        answerset = ((int(coefficient) * int(denominator)) + int(numerator)) / int(denominator)
        
    elif(option_difficulty == 3):
        if(localmin == localmax):
            denominator = random.randint(20, 999)
        else:
            denominator = random.randint(localmin, localmax)
        numerator = random.randint(10, denominator - 1)
        coefficient = random.randint(10,25)
        #print(coefficient, numerator, denominator)
        problemsets.append('({a}) / {b}'.format(a= int(coefficient) * int(denominator) + int(numerator), b= str(denominator)))
        answerset = ((int(coefficient) * int(denominator)) + int(numerator)) / int(denominator)

    if len(str(answerset)) > 6:
        answerset = round(float(answerset), 3)
        
    return(sympy.latex(sympy.sympify(str(problemsets[0])),fold_short_frac=False, mode="inline"), str(answerset))