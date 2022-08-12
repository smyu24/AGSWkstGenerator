import random

def latexify(input, option="inline"):
    if option == "inline":
        return input
    else:
        return '\[' + input + '\]'

def Factoring_Num_Section_1(option_difficulty = 1, expr = 'latex', option_min = 10, option_max = 50):
    problemsets = ""
    temp = []

    if(option_min == option_max):
        if option_difficulty == 1:
            problemsets = random.randint(10, 50)
        elif option_difficulty == 2 or option_difficulty == 3:
            problemsets = random.randint(50, 99)
    else:
        problemsets = random.randint(option_min, option_max)

    #answer generation...
    for i in range(1, int(problemsets / 2) + 1):
        if problemsets % i == 0:
            if i not in temp:
                temp.append(i)
            if int(problemsets/i) not in temp:
                temp.append(int(problemsets/i))
    temp.sort()
    if expr == 'latex':
        for i in range(len(temp)):
            temp[i] = latexify(temp[i])
        problemsets = latexify(problemsets)
    return(problemsets, ', '.join(str(i) for i in temp)) # nothing yet

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def Factoring_Num(option_difficulty = 'easy', expr = 'latex', localmin = 0, localmax = 0):
    problemsets = ""
    answerset = []
    temp = []
    unique = []

    if(localmin == localmax):
        if option_difficulty == 1:
            problemsets = random.randint(10, 50)
        elif option_difficulty == 2 or option_difficulty == 3:
            problemsets = random.randint(50, 99)
    else:
        problemsets = random.randint(localmin, localmax)

    #answer generation...
    temp = prime_factors(problemsets)

    for i in temp:
        if i not in unique:
            unique.append(i)

    for i in unique:
        if temp.count(i) != 1:
            answerset.append(str(i) + "^" + str(temp.count(i)))
        else:
            answerset.append(str(i))
    if expr == 'latex':
        return(latexify(problemsets), ', '.join(latexify(i) for i in answerset))
    else:
        return(problemsets, ', '.join(str(i) for i in answerset))