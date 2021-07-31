# First Section

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

def Least_Common_Multiple_1(option_difficulty, option_random):
    problemsets = []
    answerset = []
    holder = []
    temp = []
    lcm = 0

    if option_difficulty == "easy":
        problemsets = random.randint(2, 10)

    elif option_difficulty == "medium":
        problemsets = random.randint(10, 20)

    elif option_difficulty == "hard":
        problemsets = random.randint(15, 25)

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
        answerset.append(holder * random.randint(10, 20))
        answerset.append(holder * random.randint(10, 20))
        if(answerset[0] == answerset[1]):
            answerset.pop(1)
            answerset.append(holder * random.randint(10, 20))
    elif option_difficulty == "hard":
        answerset.append(holder * random.randint(15, 25))
        answerset.append(holder * random.randint(15, 25))
        if(answerset[0] == answerset[1]):
            answerset.pop(1)
            answerset.append(holder * random.randint(15, 25))
    print("answerset:", answerset)
    lcm = Find_LCM(answerset[0], answerset[1])
 
    return(lcm, answerset)


a, b = Least_Common_Multiple_1("easy", False)
print(a,b)
