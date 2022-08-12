import random

def latexify(input, option="inline"):
    if option == "inline":
        return input
    else:
        return '\[' + input + '\]'

def Find_LCM(one, two):
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


def Least_Common_Multiple(option_difficulty = 'easy', expr = 'latex', localmin = 0, localmax = 0):
    problemsets = []
    answerset = []
    holder = []
    temp = []
    lcm = 0

    if(localmin == localmax):
        if option_difficulty == 1:
            problemsets = random.randint(2, 10)

        elif option_difficulty == 2:
            problemsets = random.randint(10, 20)

        elif option_difficulty == 3:
            problemsets = random.randint(15, 25)
    else:
        problemsets = random.randint(localmin, localmax)

    # answer generation...
    for i in range(1, int(problemsets / 2) + 1):
        if problemsets % i == 0:
            if i not in temp:
                temp.append(i)
            if int(problemsets/i) not in temp:
                temp.append(int(problemsets / i))
    holder = random.choice(temp[1:])
    if option_difficulty == 1:
        answerset.append(holder * random.randint(2, 10))
        answerset.append(holder * random.randint(2, 10))
        if(answerset[0] == answerset[1]):
            answerset.pop(1)
            answerset.append(holder * random.randint(2, 10))
    elif option_difficulty == 2:
        answerset.append(holder * random.randint(10, 20))
        answerset.append(holder * random.randint(10, 20))
        if(answerset[0] == answerset[1]):
            answerset.pop(1)
            answerset.append(holder * random.randint(10, 20))
    elif option_difficulty == 3:
        answerset.append(holder * random.randint(15, 25))
        answerset.append(holder * random.randint(15, 25))
        if(answerset[0] == answerset[1]):
            answerset.pop(1)
            answerset.append(holder * random.randint(15, 25))
    lcm = Find_LCM(answerset[0], answerset[1])
    return(str(answerset[0]) + ", " + str(answerset[1]), str(lcm))