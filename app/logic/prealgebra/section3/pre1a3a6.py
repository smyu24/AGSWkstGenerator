# First Section (ADDITION)

import fractions
import math
import random
from fractions import Fraction

def Adding_And_Subtracting_Fractions_And_Mixed_Numbers_1(option_difficulty, option_random, localmin, localmax):
    problemsets = ""
    answerset = ""
    answerset_2 = []
    one = 0
    two = 0
    place = 0
    temp = 0

    if(localmin == localmax):
        if option_difficulty == 1: # Common denomiator
            one = float("0." + str(random.randint(1, 9)))
            two = float("0." + str(random.randint(1, 9)))
            
        elif option_difficulty == 2: # No Common Denominator + chance to be bigger than 1
            one = float(str(random.randint(-3, 3)) + "." + str(random.randint(1, 9)))
            two = float(str(random.randint(-3, 3)) + "." + str(random.randint(1, 9)))

        elif option_difficulty == 3:
            one = float(str(random.randint(-9, 9)) + "." + str(random.randint(1, 9)))
            two = float(str(random.randint(-9, 9)) + "." + str(random.randint(1, 9)))
    else:
        if option_difficulty == 1: # Common denomiator
            one = float("0." + str(random.randint(localmin, localmax)))
            two = float("0." + str(random.randint(localmin, localmax)))
            
        elif option_difficulty == 2: # No Common Denominator + chance to be bigger than 1
            one = float(str(random.randint(-3, 3)) + "." + str(random.randint(localmin, localmax)))
            two = float(str(random.randint(-3, 3)) + "." + str(random.randint(localmin, localmax)))

        elif option_difficulty == 3:
            one = float(str(random.randint(-9, 9)) + "." + str(random.randint(localmin, localmax)))
            two = float(str(random.randint(-9, 9)) + "." + str(random.randint(localmin, localmax)))

    one = fractions.Fraction(str(one))
    two = fractions.Fraction(str(two))

    temp = str(one + two)
    temp.replace("Fraction(",'')
    temp.replace(")",'')
    answerset = temp

    a_list = []
    a_list = str(one).split("/")
    frac = r"\frac{" + a_list[0] + "}" + "{" + a_list[1] + "}"

    b_list = []
    b_list = str(two).split("/")
    frac2 = r"\frac{" + b_list[0] + "}" + "{" + b_list[1] + "}"

    c_list = []
    c_list = str(answerset).split("/")
    
    if(len(c_list) > 1):
        frac3 = r"\frac{" + c_list[0] + "}" + "{" + c_list[1] + "}"
    else:
        frac3 = answerset
    
    if one < 0:
        one = '(' + frac +')'
    else:
        one = frac
    if two < 0:
        two = '(' + frac2 +')'
    else:
        two = frac2

    problemsets = (str(one) + "+" + str(two))
    return(problemsets, frac3)

def Adding_And_Subtracting_Fractions_And_Mixed_Numbers_2(option_difficulty, option_random, localmin, localmax):
    problemsets = ""
    answerset = ""
    one = 0
    two = 0
    temp = 0
    
    if(localmin == localmax):
        if option_difficulty == 1: # Common denomiator
            one = float("0." + str(random.randint(1, 9)))
            two = float("0." + str(random.randint(1, 9)))
            
        elif option_difficulty == 2: # No Common Denominator + chance to be bigger than 1
            one = float(str(random.randint(-3, 3)) + "." + str(random.randint(1, 9)))
            two = float(str(random.randint(-3, 3)) + "." + str(random.randint(1, 9)))

        elif option_difficulty == 3:
            one = float(str(random.randint(-9, 9)) + "." + str(random.randint(1, 9)))
            two = float(str(random.randint(-9, 9)) + "." + str(random.randint(1, 9)))
    else:
        if option_difficulty == 1: # Common denomiator
            one = float("0." + str(random.randint(localmin, localmax)))
            two = float("0." + str(random.randint(localmin, localmax)))
            
        elif option_difficulty == 2: # No Common Denominator + chance to be bigger than 1
            one = float(str(random.randint(-3, 3)) + "." + str(random.randint(localmin, localmax)))
            two = float(str(random.randint(-3, 3)) + "." + str(random.randint(localmin, localmax)))

        elif option_difficulty == 3:
            one = float(str(random.randint(-9, 9)) + "." + str(random.randint(localmin, localmax)))
            two = float(str(random.randint(-9, 9)) + "." + str(random.randint(localmin, localmax)))

    one = fractions.Fraction(str(one))
    two = fractions.Fraction(str(two))

    temp = str(one + two)
    temp.replace("Fraction(",'')
    temp.replace(")",'')
    answerset = temp

    a_list = []
    a_list = str(one).split("/")
    frac = r"\frac{" + a_list[0] + "}" + "{" + a_list[1] + "}"

    b_list = []
    b_list = str(two).split("/")
    frac2 = r"\frac{" + b_list[0] + "}" + "{" + b_list[1] + "}"

    c_list = []
    c_list = str(answerset).split("/")

    if(len(c_list) > 1):
        frac3 = r"\frac{" + c_list[0] + "}" + "{" + c_list[1] + "}"
    else:
        frac3 = answerset
    
    if one < 0:
        one = '(' + frac +')'
    else:
        one = frac
    if two < 0:
        two = '(' + frac2 +')'
    else:
        two = frac2

    problemsets = (str(one) + "-" + str(two))
    return(problemsets, frac3)