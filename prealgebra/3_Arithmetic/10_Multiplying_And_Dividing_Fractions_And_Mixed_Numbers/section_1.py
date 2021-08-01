# First Section

import math
import random
import fractions
from fractions import Fraction

def Multiplying_And_Dividing_Fractions_And_Mixed_Numbers_1(option_difficulty, option_random):
    problemsets = []
    answerset = []
    temp = 0
    list_temp = []
    one = 0
    two = 0
    temp = 0
    value = 0
    holder = ''
    negative = ['-', '']

    if option_difficulty == "easy": 
        one = float("0." + str(random.randint(1, 9)))
        two = float("0." + str(random.randint(1, 9)))
        
    elif option_difficulty == "medium": 
        one = float(random.choice(negative) + str(random.randint(1, 3)) + "." + str(random.randint(1, 9)))
        two = float(random.choice(negative) + str(random.randint(1, 3)) + "." + str(random.randint(1, 9)))

    elif option_difficulty == "hard":
        one = float(random.choice(negative) + str(random.randint(1, 9)) + "." + str(random.randint(1, 9)))
        two = float(random.choice(negative) + str(random.randint(1, 9)) + "." + str(random.randint(1, 9)))

    one = fractions.Fraction(str(one))
    two = fractions.Fraction(str(two))

    temp = str(one * two)
    temp.replace("Fraction(",'')
    temp.replace(")",'')

    list_temp = list(temp)
    value = temp.find("/")
    if len(list_temp) > 1:
        if abs(int(''.join(list_temp[:value]))) >= int(''.join(list_temp[value + 1:])):
            answerset.append(int(int(''.join(list_temp[:value])) / int(''.join(list_temp[value + 1:]))))
            holder = Fraction(int(''.join(list_temp[:value])) % int(''.join(list_temp[value + 1:])), int(''.join(list_temp[value + 1:])))
            holder = str(holder)
            holder.replace('Fraction(','')
            holder.replace(')','')
            answerset.append(holder)
        else:
            answerset.append(temp)
    elif len(list_temp) <= 1:
      answerset.append(temp)
    problemsets.append("$ "+ str(one) + " \times " + str(two) + " $")
    return(problemsets, answerset)

a,b = Multiplying_And_Dividing_Fractions_And_Mixed_Numbers_1("easy", False)
print(a,b)
a,b = Multiplying_And_Dividing_Fractions_And_Mixed_Numbers_1("medium", False)
print(a,b)
a,b = Multiplying_And_Dividing_Fractions_And_Mixed_Numbers_1("hard", False)
print(a,b)