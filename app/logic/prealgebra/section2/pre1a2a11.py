import math
import random

def latexify(input, option="inline"):
    if option == "inline":
        return input
    else:
        return '\[' + input + '\]'

def Divisibility_And_Factors_Section_1(option_difficulty='easy', expr='latex', localmin = 0, localmax = 0):
    problemsets = ""
    temp_problem = []
    answerset = []
    temp = ""

    if (localmin == localmax):
        if option_difficulty == 1:
            dividing_number = random.randint(2,10)
            problemsets = random.randint(10, 25)
        elif option_difficulty == 2:
            dividing_number = random.randint(2,15)
            problemsets = random.randint(25, 100)
        elif option_difficulty == 3:
            dividing_number = random.randint(2,23)
            problemsets = random.randint(90, 999)
    else:
        if option_difficulty == 1:
            dividing_number = random.randint(localmin, localmax)
            problemsets = random.randint(10, 25)
        elif option_difficulty == 2:
            dividing_number = random.randint(localmin, localmax)
            problemsets = random.randint(25, 100)
        elif option_difficulty == 3:
            dividing_number = random.randint(localmin, localmax)
            problemsets = random.randint(90, 999)

    if expr == 'latex':
        temp_problem = latexify(str(problemsets)), " \\text{ by } ", latexify(str(dividing_number))
    else:
        temp_problem = str(problemsets), "  \\text{ by }  ", str(dividing_number)

    temp_problem = ''.join(temp_problem)
    temp = problemsets/dividing_number
    if temp % 1 != 0:
        answerset = "No"
    else:
        answerset = "Yes"
  
    return(temp_problem, answerset)