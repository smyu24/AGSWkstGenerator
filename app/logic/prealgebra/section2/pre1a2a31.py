import random

def latexify(input, option="inline"):
    if option == "inline":
        return input
    else:
        return '\[' + input + '\]'

def count_var(variable):
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
    return(''.join(str(i) for i in answerset))

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

def count_var2(variable, format):
    unique = []
    answerset = []
    a = ""
    for i in variable:
        if i not in unique:
            unique.append(i)
    for i in unique:
        if variable.count(i) != 1:
            answerset.append(str(i) + "^" + str(variable.count(i)))
        else:
            answerset.append(str(i))
    if format == True:
        for i in range(len(answerset)):
            if i == 0:
                a = a + answerset[i]
            else:
                a = a + ", " + answerset[i]
        return(a)
    else:
        return(''.join((str(b) for b in answerset)))

def Factoring_Monomials_Section_1(option_difficulty = 'easy', expr = 'latex', localmin = 0, localmax = 0):
    problemsets = ""
    answerset = []
    number = 0
    variable = []
    choices = ['x','y', 'a', 'b', 'z', 'p', 't', 'q', 'k', 'u', 'r', 'd', 'w']
    place_holder = []
    switch = False

    if(localmin == localmax):
        if option_difficulty == 1:
            number = random.randint(10, 40)
            for i in range(2, number):
                if(number % i) == 0:
                    switch = True
            if switch != True:
                number = random.randint(10, 40)
            variable = random.choice(choices)
            for i in range(random.randint(1, 2)):
                place_holder.append(variable)

        elif option_difficulty == 2:
            number = random.randint(40, 70)
            for i in range(2, number):
                if(number % i) == 0:
                    switch = True
            if switch != True:
                number = random.randint(10, 40)
            for i in range(random.randint(1, 2)):
                variable = random.choice(choices)
            for i in range(random.randint(1, 4)):
                place_holder.append(variable)

        elif option_difficulty == 3:
            number = random.randint(70, 100)
            for i in range(2, number):
                if(number % i) == 0:
                    switch = True
            if switch != True:
                number = random.randint(10, 40)
            for i in range(random.randint(2, 3)):
                variable = random.choice(choices)
            for i in range(random.randint(1, 7)):
                place_holder.append(variable)
    else:
        number = random.randint(localmin, localmax)
        if option_difficulty == 1:
            for i in range(2, number):
                if(number % i) == 0:
                    switch = True
            if switch != True:
                number = random.randint(10, 40)
            variable = random.choice(choices)
            for i in range(random.randint(1, 2)):
                place_holder.append(variable)

        elif option_difficulty == 2:
            for i in range(2, number):
                if(number % i) == 0:
                    switch = True
            if switch != True:
                number = random.randint(10, 40)
            for i in range(random.randint(1, 2)):
                variable = random.choice(choices)
            for i in range(random.randint(1, 4)):
                place_holder.append(variable)

        elif option_difficulty == 3:
            for i in range(2, number):
                if(number % i) == 0:
                    switch = True
            if switch != True:
                number = random.randint(10, 40)
            for i in range(random.randint(2, 3)):
                variable = random.choice(choices)
            for i in range(random.randint(1, 7)):
                place_holder.append(variable)

    #answer generation...
    problemsets = prime_factors(number)
    problemsets = problemsets + place_holder
    answerset = ', '.join(str(i) for i in problemsets)
    number = str(number) + count_var(place_holder)

    return(number, answerset)

def Factoring_Monomials_Section_2(option_difficulty = 'easy', expr = 'latex', localmin = 0, localmax = 0):
    problemsets = ""
    answerset = ""
    number = 0
    variable = []
    choices = ['x','y', 'a', 'b', 'z', 'p', 't', 'q', 'k', 'u', 'r', 'd', 'w']
    place_holder = []
    switch = False

    if(localmin == localmax):
        if option_difficulty == 1:
            number = random.randint(10, 40)
            for i in range(2, number):
                if(number % i) == 0:
                    switch = True
            if switch != True:
                number = random.randint(10, 40)
            variable = random.choice(choices)
            for i in range(random.randint(1, 2)):
                place_holder.append(variable)

        elif option_difficulty == 2:
            number = random.randint(40, 70)
            for i in range(2, number):
                if(number % i) == 0:
                    switch = True
            if switch != True:
                number = random.randint(10, 40)
            for i in range(random.randint(1, 2)):
                variable = random.choice(choices)
            for i in range(random.randint(1, 4)):
                place_holder.append(variable)

        elif option_difficulty == 3:
            number = random.randint(70, 100)
            for i in range(2, number):
                if(number % i) == 0:
                    switch = True
            if switch != True:
                number = random.randint(10, 40)
            for i in range(random.randint(2, 3)):
                variable = random.choice(choices)
            for i in range(random.randint(1, 7)):
                place_holder.append(variable)
    else:
        number = random.randint(localmin, localmax)
        if option_difficulty == 1:
            for i in range(2, number):
                if(number % i) == 0:
                    switch = True
            if switch != True:
                number = random.randint(10, 40)
            variable = random.choice(choices)
            for i in range(random.randint(1, 2)):
                place_holder.append(variable)

        elif option_difficulty == 2:
            for i in range(2, number):
                if(number % i) == 0:
                    switch = True
            if switch != True:
                number = random.randint(10, 40)
            for i in range(random.randint(1, 2)):
                variable = random.choice(choices)
            for i in range(random.randint(1, 4)):
                place_holder.append(variable)

        elif option_difficulty == 3:
            for i in range(2, number):
                if(number % i) == 0:
                    switch = True
            if switch != True:
                number = random.randint(10, 40)
            for i in range(random.randint(2, 3)):
                variable = random.choice(choices)
            for i in range(random.randint(1, 7)):
                place_holder.append(variable)

    #answer generation...
    problemsets = prime_factors(number)
    answerset = count_var2(problemsets, True)
    answerset = answerset + ", " + count_var2(place_holder, True)
    if expr == 'latex':
        answerset = latexify(answerset)
    number = str(number) + count_var2(place_holder, False)
    if expr == 'latex':
        return(latexify(number), answerset)
    else:
        return(number, answerset)