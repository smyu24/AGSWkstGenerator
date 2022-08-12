import fractions
import math
import random
from fractions import Fraction

def Percents_Fractions_Decimal_Conversion_1(option_difficulty, option_random, localmin, localmax):
    problemsets = []
    answerset = []
    temp = 0
    list_temp = []

    if(localmin == localmax):
        if(option_difficulty == 1):
            problemsets.append("0." + str(random.randint(1, 99)))
        elif(option_difficulty == 2):
            problemsets.append(str(random.randint(1, 99)) + "." + str(random.randint(1, 99)))
        elif(option_difficulty == 3):
            problemsets.append(str(random.randint(-999, 999)) + "." + str(random.randint(1, 999)))
    else:
        if(option_difficulty == 1):
            problemsets.append("0." + str(random.randint(localmin, localmax)))
        elif(option_difficulty == 2):
            problemsets.append(str(random.randint(1, 99)) + "." + str(random.randint(localmin, localmax)))
        elif(option_difficulty == 3):
            problemsets.append(str(random.randint(-999, 999)) + "." + str(random.randint(localmin, localmax)))


    temp = round(float(str(problemsets[0])) * 100, 2)
    list_temp = list(str(temp))
    if int(list_temp[-1]) == 0:
        temp = int(temp)
    answerset.append(str(temp))


    return(str(answerset), str(problemsets))

def Percents_Fractions_Decimal_Conversion_2(option_difficulty, option_random, localmin, localmax):
    problemsets = []
    answerset = []
    temp = 0
    list_temp = []

    if(localmin == localmax):
        if(option_difficulty == 1):
            problemsets.append("0." + str(random.randint(1, 99)))
        elif(option_difficulty == 2):
            problemsets.append(str(random.randint(1, 20)) + "." + str(random.randint(1, 99)))
        elif(option_difficulty == 3):
            problemsets.append(str(random.randint(1, 999)) + "." + str(random.randint(1, 999)))
    else:
        if(option_difficulty == 1):
            problemsets.append("0." + str(random.randint(localmin, localmax)))
        elif(option_difficulty == 2):
            problemsets.append(str(random.randint(1, 20)) + "." + str(random.randint(localmin, localmax)))
        elif(option_difficulty == 3):
            problemsets.append(str(random.randint(1, 999)) + "." + str(random.randint(localmin, localmax)))


    temp = round(float(str(problemsets[0])) * 100, 2)
    list_temp = list(str(temp))
    if int(list_temp[-1]) == 0:
        temp = int(temp)
    answerset.append(str(temp))


    return(str(problemsets), str(answerset))

def Percents_Fractions_Decimal_Conversion_3(option_difficulty, option_random, localmin, localmax):
    problemsets_1 = []
    problemsets_2 = []
    answerset = []
    temp = 0
    list_temp = []
    percent = 0
    replace = ""
    holder = 0

    if(localmin == localmax):
        if(option_difficulty == 1):
            problemsets_2.append("0." + str(random.randint(1, 99)))
        
        elif(option_difficulty == 2):
            problemsets_2.append("0." + str(random.randint(1, 999)))

        elif(option_difficulty == 3):
            problemsets_2.append("0." + str(random.randint(1, 9999)))
    else:
        problemsets_2.append("0." + str(random.randint(localmin, localmax)))

    
    temp = round(float(str(problemsets_2[0])) * 100, 2)
    
    list_temp = list(str(temp))
    if int(list_temp[-1]) == 0:
        temp = int(temp)
    problemsets_1.append(str(temp))
    
    percent = Fraction(problemsets_2[0])
    percent = str(percent)
    percent.replace("Fraction(",'')
    percent.replace(")",'')

    
    answerset.append(percent)

    return(str(problemsets_1), str(answerset))

def Percents_Fractions_Decimal_Conversion_4(option_difficulty, option_random, localmin, localmax):
    problemsets_1 = []
    problemsets_2 = []
    answerset = ""
    temp = 0
    list_temp = []
    percent = 0
    replace = ""
    holder = 0

    if(localmin == localmax):
        if(option_difficulty == 1):
            problemsets_2.append("0." + str(random.randint(1, 99)))
        
        elif(option_difficulty == 2):
            problemsets_2.append("0." + str(random.randint(1, 999)))

        elif(option_difficulty == 3):
            problemsets_2.append("0." + str(random.randint(1, 9999)))
    else:
        problemsets_2.append("0." + str(random.randint(localmin, localmax)))
    
    temp = round(float(str(problemsets_2[0])) * 100, 2)
    
    list_temp = list(str(temp))
    if int(list_temp[-1]) == 0:
        temp = int(temp)
    problemsets_1.append(str(temp))
    
    percent = Fraction(problemsets_2[0])
    percent = str(percent)
    percent.replace("Fraction(",'')
    percent.replace(")",'')

    
    answerset = percent

    a_list = []
    a_list = str(answerset).split("/")
    frac = "\\frac{" + a_list[0] + "}" + "{" + a_list[1] + "}"
    return(frac, str(problemsets_1))