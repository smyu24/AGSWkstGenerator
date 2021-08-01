#Second Section

import math
import random


def Percents_Fractions_Decimal_Conversion_2(option_difficulty, option_random):
    problemsets = []
    answerset = []
    temp = 0
    list_temp = []

    if(option_difficulty == "easy"):
        problemsets.append("0." + str(random.randint(1, 99)))
    
    elif(option_difficulty == "medium"):
        problemsets.append(str(random.randint(1, 20)) + "." + str(random.randint(1, 99)))

    elif(option_difficulty == "hard"):
        problemsets.append(str(random.randint(1, 999)) + "." + str(random.randint(1, 999)))


    temp = round(float(str(problemsets[0])) * 100, 2)
    list_temp = list(str(temp))
    if int(list_temp[-1]) == 0:
        temp = int(temp)
    answerset.append(str(temp) + "%")


    return(problemsets, answerset)


a,b = Percents_Fractions_Decimal_Conversion_2("hard", False)
print(a,b)

