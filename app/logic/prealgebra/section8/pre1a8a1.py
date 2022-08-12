import fractions
import math
import random
from fractions import Fraction

def reg_truncate(n, p = False):
    if p:
        n = float(n)
        return(round(((round(n, p + 2) * 1000) / 1000), p + 2))
    else:
        n = float(n)
        return((n * 1000) / 1000)

def min_max_checker(option_min, option_max):
    option_min = int(option_min)
    option_max = int(option_max)
    if option_min == 0 and option_max == 0:
        return(True)
    return(False)

def insert_comma_1(num):
    num = int(num)
    return (f"{num:,}")

def decimals_generator(option_difficulty, option_min, option_max):
    if min_max_checker(option_min, option_max) == True:
        if option_difficulty == 2:
            integer_only = random.randint(9, 9999)
            decimal = random.random()
            decimal_2 = "{:.2f}".format(decimal)
            if integer_only % 2 == 0:
                if (float(decimal_2) * 100) % 2 == 0:
                    problem  = "{:.1f}".format(integer_only + float(decimal))
                    place = 1
                else:
                    problem = "{:.2f}".format(integer_only + float(decimal))
                    place = 2
            else:
                problem = "{:.3f}".format(integer_only + float(decimal))
                place = 3

        elif option_difficulty == 3:
            integer_only = random.randint(99, 99999999)
            decimal = random.random()
            if integer_only % 2 == 0:
                problem = "{:.2f}".format(integer_only + decimal)
                place = 2
            else:
                problem = "{:.3f}".format(integer_only + decimal)
                place = 3
    
    else: 
        option_max = option_max - 1
        if option_difficulty == 1: 
            integer_only = random.randint(option_min, option_max)
            decimal = random.random()
            if integer_only % 2 == 0: 
                problem = "{:.1f}".format(integer_only + decimal)
                place = 3
            else:
                problem = "{:.2f}".format(integer_only + decimal)
                place = 2

        elif option_difficulty == 2:
            integer_only = random.randint(option_min, option_max)
            decimal = random.random()
            decimal_2 = "{:.2f}".format(decimal)
            if integer_only % 2 == 0:
                if (float(decimal_2) * 100) % 2 == 0:
                    problem  = "{:.1f}".format(integer_only + float(decimal))
                    place = 1
                else:
                    problem = "{:.2f}".format(integer_only + float(decimal))
                    place = 2
            else:
                problem = "{:.3f}".format(integer_only + float(decimal))
                place = 3

        elif option_difficulty == 3:
            integer_only = random.randint(option_min, option_max)
            decimal = random.random()
            if integer_only % 2 == 0:
                problem = "{:.2f}".format(integer_only + decimal)
                place = 2
            else:
                problem = "{:.3f}".format(integer_only + decimal)
                place = 3
    return(reg_truncate(problem), place)

def whole_generator(option_difficulty, option_min, option_max):
    after_comma = []
    if min_max_checker(option_min, option_max) == True:
        problemsets = random.randint(1, 200)

    else:
        problemsets = random.randint(option_min, option_max)

    after_comma = insert_comma_1(problemsets)
    return(after_comma)

def percentify(num):
    return(str(num) + "\\%")

def Fractions_Decimals_and_Percents_Section_1(option_difficulty = 'easy', expr = 'latex'):
    number = ""
    answer = 0
    place = 0
    if option_difficulty == 1:
        number = whole_generator(option_difficulty, 1, 200)
        answer = int(number) / 100

    elif option_difficulty == 2:
        number, place = decimals_generator(option_difficulty, 1, 200)
        answer = float(number) / 100

    elif option_difficulty == 3:
        number, place = decimals_generator(option_difficulty, 1, 200)
        answer = float(number) / 100

    return(percentify(number), reg_truncate(answer, place))

#Second Section
def Percents_Fractions_Decimal_Conversion_22(option_difficulty, option_random):
    problemsets = []
    answerset = []
    temp = 0
    list_temp = []

    if(option_difficulty == 1):
        problemsets.append("0." + str(random.randint(1, 99)))
    
    elif(option_difficulty == 2):
        problemsets.append(str(random.randint(1, 20)) + "." + str(random.randint(1, 99)))

    elif(option_difficulty == 3):
        problemsets.append(str(random.randint(1, 999)) + "." + str(random.randint(1, 999)))


    temp = round(float(str(problemsets[0])) * 100, 2)
    list_temp = list(str(temp))
    if int(list_temp[-1]) == 0:
        temp = int(temp)
    answerset.append(str(temp) + "\\%")


    return(problemsets[0], answerset[0])

def Percents_Fractions_Decimal_Conversion_33(option_difficulty, option_random):
    problemsets_1 = []
    problemsets_2 = []
    answerset = []
    temp = 0
    list_temp = []
    percent = 0
    replace = ""
    holder = 0

    if(option_difficulty == 1):
        problemsets_2.append("0." + str(random.randint(1, 99)))
    
    elif(option_difficulty == 2):
        problemsets_2.append("0." + str(random.randint(1, 999)))

    elif(option_difficulty == 3):
        problemsets_2.append("0." + str(random.randint(1, 9999)))
    
    temp = round(float(str(problemsets_2[0])) * 100, 2)
    
    list_temp = list(str(temp))
    if int(list_temp[-1]) == 0:
        temp = int(temp)
    problemsets_1.append(str(temp) + "\\%")
    
    percent = Fraction(problemsets_2[0])
    percent = str(percent)
    percent.replace("Fraction(",'')
    percent.replace(")",'')

    
    answerset.append(percent)

    return(problemsets_1[0], answerset[0])

#Fourth Section
def Percents_Fractions_Decimal_Conversion_44(option_difficulty, option_random):
    problemsets_1 = []
    problemsets_2 = []
    answerset = []
    temp = 0
    list_temp = []
    percent = 0
    replace = ""
    holder = 0

    if(option_difficulty == 1):
        problemsets_2.append("0." + str(random.randint(1, 99)))
    
    elif(option_difficulty == 2):
        problemsets_2.append("0." + str(random.randint(1, 999)))

    elif(option_difficulty == 3):
        problemsets_2.append("0." + str(random.randint(1, 9999)))
    
    temp = round(float(str(problemsets_2[0])) * 100, 2)
    
    list_temp = list(str(temp))
    if int(list_temp[-1]) == 0:
        temp = int(temp)
    problemsets_1.append(str(temp) + "\\%")
    
    percent = Fraction(problemsets_2[0])
    percent = str(percent)
    percent.replace("Fraction(",'')
    percent.replace(")",'')

    
    answerset.append(percent)

    return(answerset[0], problemsets_1[0])