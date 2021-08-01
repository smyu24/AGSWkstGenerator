# First Section (ADDITION)

import fractions
import math
import random
from fractions import Fraction

def Adding_And_Subtracting_Fractions_And_Mixed_Numbers_1(option_difficulty, option_random): # SIMPLIFY!!!
    problemsets = []
    answerset = []
    one = 0
    two = 0
    coeff = 0
    num = 0
    numerator = 0
    denominator = 0
    temp = 0
    if option_difficulty == "easy": # Common denomiator
        one = float("0." + str(random.randint(1, 9)))
        two = float("0." + str(random.randint(1, 9)))
        
    elif option_difficulty == "medium": # No Common Denominator + chance to be bigger than 1
        one = float(str(random.randint(-3, 3)) + "." + str(random.randint(1, 9)))
        two = float(str(random.randint(-3, 3)) + "." + str(random.randint(1, 9)))

    elif option_difficulty == "hard":
        one = float(str(random.randint(-9, 9)) + "." + str(random.randint(1, 9)))
        two = float(str(random.randint(-9, 9)) + "." + str(random.randint(1, 9)))

    print(fractions.Fraction(str(one))) # fractions.Fraction(float)
    print(fractions.Fraction(str(two)))
    one = fractions.Fraction(str(one))
    two = fractions.Fraction(str(two))

    temp = str(one + two)
    temp.replace("Fraction(",'')
    temp.replace(")",'')

    coeff = list(temp)
    print(coeff) # HERE MANIPULATE HERE (FIND THE '/' AND THEN INDEX)
    #numerator = str(coeff[:coeff.index("/")])
    #denominator = str(coeff[coeff.index("/") + 1:])
    #num = int(int(numerator[2]) / int(denominator[2]))
    #print(num)
    #numerator = numerator % denominator
    #coeff = numerator + "/" + denominator
    #answerset.append(num)
    answerset.append(coeff)
    
    if one < 0:
        one = '(' + str(one) +')'
    if two < 0:
        two = '(' + str(two) +')'

    problemsets.append(str(one) + "+" + str(two))
    return(problemsets, answerset)


a,b = Adding_And_Subtracting_Fractions_And_Mixed_Numbers_1("easy", False)
print(a,b)
a,b = Adding_And_Subtracting_Fractions_And_Mixed_Numbers_1("medium", False)
print(a,b)
a,b = Adding_And_Subtracting_Fractions_And_Mixed_Numbers_1("hard", False)
print(a,b)