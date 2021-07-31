# Second Section

import math
import random


def Find_LCM(one, two):
   lcm = 0
   greater = 0
   if one > two:
       greater = one
   else:
       greater = two

   while(True):
       if ((greater % one == 0) and (greater % two == 0)):
           LCM = greater
           break
       greater += 1

   return LCM

def Least_Common_Multiple_2(option_difficulty, option_random):
    problemsets = []
    answerset = []
    variable = []
    choices = ['x', 'y', 'a', 'b', 'z', 'p', 't',
               'q', 'k', 'u', 'r', 'd', 'w', 's', 'h', 'v']
    filler = ""
    decider = ['more', 'stop']
    holder = []
    temp = []
    lcm = 0

    if option_difficulty == "easy":
        problemsets = random.randint(2, 10)
        variable.append(random.choice(choices))
        filler = random.choice(decider)
        print(filler)
        if filler == "more":
            variable.append(2)
            filler = random.choice(decider)
            if filler == "more":
                variable.append(random.choice(choices))
        else:
            filler = random.choice(decider)
            variable.append(random.choice(choices))
            if filler == "more":
                variable.append(2)

    elif option_difficulty == "medium":
        problemsets = random.randint(10, 20)
        variable.append(random.choice(choices))
        filler = random.choice(decider)
        if filler == "more":
            variable.append(2)
            filler = random.choice(decider)
            if filler == "more":
                variable.append(random.choice(choices))
                filler = random.choice(decider)
                if filler == "more":
                    variable.append(2)
            else:
                variable.pop(1)
                variable.append(3)
        else:
            filler = random.choice(decider)
            if filler == "more":
                variable.append(random.choice(choices))
                if filler == "more":
                    variable.append(2)

    elif option_difficulty == "hard": # THREE NUMBERS 10ba, 20ba, 28ba || 28b, 20ab3, 16b
        problemsets = random.randint(10, 15)
        for i in range(1,4):
            variable.append(random.choice(choices))
            filler = random.choice(decider)
            if filler == "more":
                variable.append(2) # NOT POPPING CORREcTLY
                filler = random.choice(decider)
                if filler == "more":
                    variable.append(random.choice(choices))
                else:
                    variable.pop(-1)
                    variable.append(3)
            else:
                print("else:")
                filler = random.choice(decider)
                if filler != "more":
                    filler = random.choice(decider)
            variable.append("|")
    print(variable)
    # answer generation...
    for i in range(1, int(problemsets / 2) + 1):
        if problemsets % i == 0:
            if i not in temp:
                temp.append(i)
            if int(problemsets/i) not in temp:
                temp.append(int(problemsets / i))
    print(temp)
    holder = random.choice(temp[1:])
    print("holder", holder)
    if option_difficulty == "easy":
        answerset.append(holder * random.randint(2, 10))
        answerset.append(holder * random.randint(2, 10))
        if(answerset[0] == answerset[1]):
            answerset.pop(1)
            answerset.append(holder * random.randint(2, 10))
    elif option_difficulty == "medium":
        answerset.append(holder * random.randint(10, 15))
        answerset.append(holder * random.randint(10, 15))
        if(answerset[0] == answerset[1]):
            answerset.pop(1)
            answerset.append(holder * random.randint(10, 15))
    elif option_difficulty == "hard":
        answerset.append(holder * random.randint(5, 10))
        answerset.append(holder * random.randint(5, 10))
        if(answerset[0] == answerset[1]):
            answerset.pop(1)
            answerset.append(holder * random.randint(5, 10))
        answerset.append(holder * random.randint(5, 10))
    
    print("answerset:", answerset)
    lcm = Find_LCM(answerset[0], answerset[1])
 
    return(lcm, answerset)


a, b = Least_Common_Multiple_2("hard", False)
print(a,b)
