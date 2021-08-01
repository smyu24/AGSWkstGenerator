#Fourth Section

import fractions
import math
import random
from fractions import Fraction

def Percents_Fractions_Decimal_Conversion_4(option_difficulty, option_random):
    problemsets_1 = []
    problemsets_2 = []
    answerset = []
    temp = 0
    list_temp = []
    percent = 0
    replace = ""
    holder = 0

    if(option_difficulty == "easy"):
        problemsets_2.append("0." + str(random.randint(1, 99)))
    
    elif(option_difficulty == "medium"):
        problemsets_2.append("0." + str(random.randint(1, 999)))

    elif(option_difficulty == "hard"):
        problemsets_2.append("0." + str(random.randint(1, 9999)))
    
    temp = round(float(str(problemsets_2[0])) * 100, 2)
    
    list_temp = list(str(temp))
    if int(list_temp[-1]) == 0:
        temp = int(temp)
    problemsets_1.append(str(temp) + "%")
    
    percent = Fraction(problemsets_2[0])
    print("here",percent, problemsets_2)
    percent = str(percent)
    percent.replace("Fraction(",'')
    percent.replace(")",'')

    
    answerset.append(percent)

    return(answerset, problemsets_1)


a,b = Percents_Fractions_Decimal_Conversion_4("easy", False)
print(a,b)

