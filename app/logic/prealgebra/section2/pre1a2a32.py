import math
import random

def latexify(input, option="inline"):
    if option == "inline":
        return input
    else:
        return '\[' + input + '\]'

def Greatest_Common_Factor_Section_1(option_difficulty = 'easy', expr = 'latex', localmin = 0, localmax = 0):
    problemsets = []
    answerset = []
    holder = []
    temp = []
    gcf = 0

    if(localmax == localmin):
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
    gcf = math.gcd(answerset[0], answerset[1])

    answerset = str(answerset[0]) + ", " + str(answerset[1])
    return(answerset , str(gcf))

def count_var_f(variable, format):
    unique = []
    answerset = []
    for i in variable:
        if i not in unique:
            unique.append(i)
    for i in unique:
        if variable.count(i) != 1:
            answerset.append(str(i) + "^" + str(variable.count(i)))
        else:
            answerset.append(str(i))
    if format == True:
        return(answerset)
    else:
        return(''.join((str(b) for b in answerset)))


def generate_variables(option_difficulty):
    variable = []
    choices = ['x', 'y', 'z', 't', 'u', 'r']
    one = random.randint(1, len(choices) - 2)
    two = random.randint(0, one - 1)
    three = random.randint(one + 1, len(choices) - 1)

    if option_difficulty == 1:
        for i in range(2):
            mult = [True, False]
            picked = random.randint(1, 2)
            if i == 0 and random.choice(mult) == True:
                variable.append(choices[one] * picked)
            elif i == 1 and random.choice(mult) == True:
                variable.append(choices[two] * picked)

    elif option_difficulty == 2:
        for i in range(3):
            mult = [True, False]
            picked = random.randint(1, 3)
            if i == 0 and random.choice(mult) == True:
                variable.append(choices[one] * picked)
            elif i == 1 and random.choice(mult) == True:
                variable.append(choices[two] * picked)
            elif i == 2:
                variable.append(choices[three] * picked)

    elif option_difficulty == 3:
        for i in range(3):
            picked = random.randint(1, 7)
            if i == 0:
                variable.append(choices[one] * picked)
            elif i == 1:
                variable.append(choices[two] * picked)
            elif i == 2:
                variable.append(choices[three] * picked)

    return(variable)

def overlapping_var(first, second):
    answer = ""
    taken_1 = ""
    taken_2 = ""
    for i in range(len(first)):
        for t in range(len(second)):
            taken_1 = first[i]
            taken_2 = second[t]
            if taken_1[:1] == taken_2[:1]:
                if taken_1[1:2] == '^' and taken_2[1:2] == '^':
                    if taken_1[2:] >= taken_2[2:]:
                        answer = answer + str(taken_2)
                    else:
                        answer = answer + str(taken_1)
                else:
                    answer = answer + str(taken_1[:1])
    if answer != 'None':
        return(answer)
    else:
        return('')

def Greatest_Common_Factor_Section_2(option_difficulty = 'easy', expr = 'latex', localmin = 0, localmax = 0):
    problemsets = []
    answerset = []
    holder = []
    temp = []
    gcf = 0

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
    gcf = math.gcd(answerset[0], answerset[1])

    generated_1 = ''.join(generate_variables(option_difficulty))
    generated_2 = ''.join(generate_variables(option_difficulty))
    list(generated_1)
    list(generated_2)
    first = str(count_var_f(generated_1, False))
    second = str(count_var_f(generated_2, False))
    gcf = str(gcf) + str(overlapping_var(count_var_f(generated_1, True), count_var_f(generated_2, True)))
    answerset[0] = '{}{}'.format(str(answerset[0]), first)
    answerset[1] = '{}{}'.format(str(answerset[1]), second)
    # manipulate the answerset here [0], [1] (add variabels)


    answerset = str(answerset[0]) + ", " + str(answerset[1])
    return(answerset , gcf)