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
        temp_problem = latexify(str(problemsets)), " by ", latexify(str(dividing_number))
    else:
        temp_problem = str(problemsets), " by ", str(dividing_number)

    temp_problem = ''.join(temp_problem)
    temp = problemsets/dividing_number
    if temp % 1 != 0:
        answerset = "No"
    else:
        answerset = "Yes"
  
    return(temp_problem, answerset)
################################################################################################
def Divisibility_And_Factors_Section_2(option_difficulty = 1, expr ='latex', localmin = 0, localmax = 0):
    problemsets = ""
    answerset = []
    temp = []
    header_numbers = []

    if(localmin == localmax):   
        if option_difficulty == 1:
            problemsets = random.randint(1, 99)
            for i in range(3):
                header_numbers.insert(i, random.randint(1,10))

        elif option_difficulty == 2:
            problemsets = random.randint(50, 500)
            for i in range(5):
                header_numbers.insert(i, random.randint(1,10))

        elif option_difficulty == 3:
            problemsets = random.randint(500, 9999)
            for i in range(7):
                header_numbers.insert(i, random.randint(1,10))
    else:
        if option_difficulty == 1:
            problemsets = random.randint(localmin, localmax)
            for i in range(3):
                header_numbers.insert(i, random.randint(1,10))

        elif option_difficulty == 2:
            problemsets = random.randint(localmin, localmax)
            for i in range(5):
                header_numbers.insert(i, random.randint(1,10))

        elif option_difficulty == 3:
            problemsets = random.randint(localmin, localmax)
            for i in range(7):
                header_numbers.insert(i, random.randint(1,10))       
    
    for i in header_numbers:
        if i not in temp:
            temp.append(i)

    header_numbers = temp
    header_numbers.sort()
    #answer generation...
    for i in range(len(header_numbers)):
        if problemsets/header_numbers[i] % 1 == 0:
            if expr == 'latex':
                answerset.append(latexify(str(header_numbers[i])))
            else: 
                answerset.append((str(header_numbers[i])))

    if len(answerset) == 0:
        answerset.append("None")
    if expr == 'latex':
        for i in range(len(header_numbers)):
            header_numbers[i] = latexify(header_numbers[i])   
        problemsets = latexify(problemsets)
    
    lst = (', '.join(str(v) for v in header_numbers))
    return(lst, problemsets, ', '.join(str(v) for v in answerset))
#############################################################################################
def Factoring_Num_Section_1(option_difficulty = 1, expr = 'latex', option_min = 10, option_max = 50):
    problemsets = ""
    answerset = []
    temp = []

    if(option_min == option_max):
        if option_difficulty == 1:
            problemsets = random.randint(10, 50)
        elif option_difficulty == 2:
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
        if option_difficulty == "easy":
            problemsets = random.randint(10, 50)
        elif option_difficulty == "medium" or option_difficulty == "hard":
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
###############################################################################################################
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
    add = []
    mult = 0
    temp = []
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
    temp = []
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
##########################################################################################
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
    filler = ""
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
####################################################################################################
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