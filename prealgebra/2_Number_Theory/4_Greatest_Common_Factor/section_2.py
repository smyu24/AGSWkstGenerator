# Second Section NOT DONE YET NEED TO DO LAST PART (VARIABLE AND NUMBER COMBINATION)

import math
import random


def Greatest_Common_Factor_2(option_difficulty, option_random):
    problemsets = 0
    answerset = []
    holder = []
    temp = []
    variable = []
    choices = ['x', 'y', 'a', 'b', 'z', 'p', 't',
               'q', 'k', 'u', 'r', 'd', 'w', 's', 'h', 'v']
    filler = ""
    decider = ['more', 'stop']
    gcf = 0
    len_checker = 0
    output = []

    if option_difficulty == "easy":
        problemsets = random.randint(5, 40)
        variable.append(random.choice(choices))
        filler = random.choice(decider)
        if filler == "more":
            variable.append(2)
        else:
            filler = random.choice(decider)
            if filler == "more":
                variable.append(random.choice(choices))
                if filler == "more":
                    variable.append(2)

    elif option_difficulty == "medium":
        problemsets = random.randint(10, 80)
        variable.append(random.choice(choices))
        filler = random.choice(decider)
        if filler == "more":
            variable.append(2)
        else:
            filler = random.choice(decider)
            if filler == "more":
                variable.append(random.choice(choices))
                if filler == "more":
                    variable.append(2)

    elif option_difficulty == "hard":
        problemsets = random.randint(10, 150)
        variable.append(random.choice(choices))
        filler = random.choice(decider)
        if filler == "more":
            variable.append(2)
            filler = random.choice(decider)
            if filler == "more":
                variable.pop(1)
                variable.append(3)
        elif filler == "stop":
            filler = random.choice(decider)
            if filler == "more":
                variable.append(random.choice(choices))

    # answer generation...
    for i in range(1, int(problemsets / 2) + 1):
        if problemsets % i == 0:
            if i not in temp:
                temp.append(i)
            if int(problemsets/i) not in temp:
                temp.append(int(problemsets / i))
    holder = random.choice(temp[1:])
    if option_difficulty == "easy":
        while(len(answerset) != 2):
            len_checker = holder * random.randint(2, 10)
            if answerset.count(len_checker) == 0:
                answerset.append(len_checker)

    elif option_difficulty == "medium":
        while(len(answerset) != 2):
            len_checker = holder * random.randint(10, 20)
            if answerset.count(len_checker) == 0:
                answerset.append(len_checker)

    elif option_difficulty == "hard":
        while(len(answerset) != 2):
            len_checker = holder * random.randint(15, 25)
            if answerset.count(len_checker) == 0:
                answerset.append(len_checker)
    
    print("variable:", variable)
    gcf = math.gcd(answerset[0], answerset[1])
    #try:
    #    if(int(variable[1])):
            #output.append(str(answerset[0]) + variable[0:2])
            #output.append(str(answerset[1]) + variable[2:4])
    #except:
            #output.append(str(answerset[0]) + variable[0])
            #output.append(str(answerset[1]) + variable[0:])
    print(output)
    
    return(gcf, answerset)


a, b = Greatest_Common_Factor_2("medium", False)
print(a, b)