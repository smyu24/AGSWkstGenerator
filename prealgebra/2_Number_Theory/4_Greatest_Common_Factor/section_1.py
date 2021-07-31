# First Section
import math
import random


def Greatest_Common_Factor_1(option_difficulty, option_random):
    problemsets = []
    answerset = []
    holder = []
    temp = []
    gcf = 0

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
    gcf = math.gcd(answerset[0], answerset[1])
    print(gcf)
    return(gcf, answerset)


a, b = Greatest_Common_Factor_1("medium", False)
print(a,b)
