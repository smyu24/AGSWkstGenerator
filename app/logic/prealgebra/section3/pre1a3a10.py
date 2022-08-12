# First Section

import math
import random
import fractions
from fractions import Fraction

def Multiplying_And_Dividing_Fractions_And_Mixed_Numbers_1(option_difficulty, option_random, localmin, localmax):
    problemsets = ""
    answerset = []
    temp = 0
    list_temp = []
    one = 0
    two = 0
    temp = 0
    value = 0
    holder = ''
    negative = ['-', '']

    if(localmin == localmax):
        if option_difficulty == 1: 
            one = float("0." + str(random.randint(1, 9)))
            two = float("0." + str(random.randint(1, 9)))
            
        elif option_difficulty == 2: 
            one = float(random.choice(negative) + str(random.randint(1, 3)) + "." + str(random.randint(1, 9)))
            two = float(random.choice(negative) + str(random.randint(1, 3)) + "." + str(random.randint(1, 9)))

        elif option_difficulty == 3:
            one = float(random.choice(negative) + str(random.randint(1, 9)) + "." + str(random.randint(1, 9)))
            two = float(random.choice(negative) + str(random.randint(1, 9)) + "." + str(random.randint(1, 9)))
    else:
        if option_difficulty == 1: 
            one = float("0." + str(random.randint(localmin, localmax)))
            two = float("0." + str(random.randint(localmin, localmax)))
            
        elif option_difficulty == 2: 
            one = float(random.choice(negative) + str(random.randint(1, 3)) + "." + str(random.randint(localmin, localmax)))
            two = float(random.choice(negative) + str(random.randint(1, 3)) + "." + str(random.randint(localmin, localmax)))

        elif option_difficulty == 3:
            one = float(random.choice(negative) + str(random.randint(1, 9)) + "." + str(random.randint(localmin, localmax)))
            two = float(random.choice(negative) + str(random.randint(1, 9)) + "." + str(random.randint(localmin, localmax)))
        

    one = fractions.Fraction(str(one))
    two = fractions.Fraction(str(two))

    temp = str(one * two)
    temp.replace("Fraction(",'')
    temp.replace(")",'')

    list_temp = list(temp)
    value = temp.find("/")
    
    frac3 = ""
    if(value > 0):
        if abs(int(''.join(list_temp[:value]))) >= int(''.join(list_temp[value + 1:])):
            answerset.append(int(int(''.join(list_temp[:value])) / int(''.join(list_temp[value + 1:]))))
            holder = Fraction(int(''.join(list_temp[:value])) % int(''.join(list_temp[value + 1:])), int(''.join(list_temp[value + 1:])))
            holder = str(holder)
            holder.replace('Fraction(','')
            holder.replace(')','')
            answerset.append(holder)
        else:
            answerset.append(temp)
        
        c_list = []
        if(len(answerset) > 1):
            c_list = str(answerset[1]).split("/")
            frac3 = str(answerset[0]) + r"\frac{" + c_list[0] + "}" + "{" + c_list[1] + "}"
        else:
            c_list = str(answerset[0]).split("/")
            frac3 = r"\frac{" + c_list[0] + "}" + "{" + c_list[1] + "}"            
    else:
        answerset = (temp)
        frac3 = answerset


    a_list = []
    a_list = str(one).split("/")
    frac = r"\frac{" + a_list[0] + "}" + "{" + a_list[1] + "}"

    b_list = []
    b_list = str(two).split("/")
    frac2 = r"\frac{" + b_list[0] + "}" + "{" + b_list[1] + "}"
    problemsets = frac + r" \times " + frac2

    return(problemsets, frac3)

def Multiplying_And_Dividing_Fractions_And_Mixed_Numbers_2(option_difficulty, option_random, localmin, localmax):
    problemsets = ""
    answerset = []
    temp = 0
    list_temp = []
    one = 0
    two = 0
    temp = 0
    value = 0
    holder = ''
    negative = ['-', '']

    if(localmin == localmax):
        if option_difficulty == 1:
            one = float("0." + str(random.randint(1, 9)))
            two = float("0." + str(random.randint(1, 9)))

        elif option_difficulty == 2:
            one = float(random.choice(negative) +
                        str(random.randint(1, 3)) + "." + str(random.randint(1, 9)))
            two = float(random.choice(negative) +
                        str(random.randint(1, 3)) + "." + str(random.randint(1, 9)))

        elif option_difficulty == 3:
            one = float(random.choice(negative) +
                        str(random.randint(1, 9)) + "." + str(random.randint(1, 9)))
            two = float(random.choice(negative) +
                        str(random.randint(1, 9)) + "." + str(random.randint(1, 9)))
    else:
        if option_difficulty == 1:
            one = float("0." + str(random.randint(localmin, localmax)))
            two = float("0." + str(random.randint(localmin, localmax)))

        elif option_difficulty == 2:
            one = float(random.choice(negative) +
                        str(random.randint(1, 3)) + "." + str(random.randint(localmin, localmax)))
            two = float(random.choice(negative) +
                        str(random.randint(1, 3)) + "." + str(random.randint(localmin, localmax)))

        elif option_difficulty == 3:
            one = float(random.choice(negative) +
                        str(random.randint(1, 9)) + "." + str(random.randint(localmin, localmax)))
            two = float(random.choice(negative) +
                        str(random.randint(1, 9)) + "." + str(random.randint(localmin, localmax)))

    one = fractions.Fraction(str(one))
    two = fractions.Fraction(str(two))

    temp = str(one / two)
    temp.replace("Fraction(", '')
    temp.replace(")", '')

    list_temp = list(temp)

    value = temp.find("/")
    if len(list_temp) > 1:
        if(value > 0):
            if abs(int(''.join(list_temp[:value]))) >= int(''.join(list_temp[value + 1:])):
                answerset.append(
                    int(int(''.join(list_temp[:value])) / int(''.join(list_temp[value + 1:]))))
                holder = Fraction(int(''.join(list_temp[:value])) % int(
                    ''.join(list_temp[value + 1:])), int(''.join(list_temp[value + 1:])))
                holder = str(holder)
                holder.replace('Fraction(', '')
                holder.replace(')', '')
                answerset.append(holder)
            else:
                answerset.append(temp)
        
            c_list = []
            if(len(answerset) > 1):
                c_list = str(answerset[1]).split("/")
                frac3 = str(answerset[0]) + r"\frac{" + c_list[0] + "}" + "{" + c_list[1] + "}"
            else:
                c_list = str(answerset[0]).split("/")
                frac3 = r"\frac{" + c_list[0] + "}" + "{" + c_list[1] + "}"     
        else:
            frac3 = temp
    elif len(list_temp) <= 1:
      answerset=temp
      frac3 = answerset

    a_list = []
    a_list = str(one).split("/")
    frac = r"\frac{" + a_list[0] + "}" + "{" + a_list[1] + "}"

    b_list = []
    b_list = str(two).split("/")
    frac2 = r"\frac{" + b_list[0] + "}" + "{" + b_list[1] + "}"
    problemsets = frac + r" \div " + frac2

    return(problemsets, frac3)