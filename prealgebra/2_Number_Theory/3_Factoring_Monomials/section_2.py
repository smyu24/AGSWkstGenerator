# First Section 

import math
import random

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
max_num_variable = 3

def Factoring_Monomials(option_difficulty, option_random,max_num_variable):
    problemsets = []
    answerset = []
    number = 0
    variable = []
    choices = ['x','y', 'a', 'b', 'z', 'p', 't', 'q', 'k', 'u', 'r', 'd', 'w']
    temp = []
    unique_1 = []
    unique_2 = []
    place_holder = []
    answer = []
    switch = False

    if option_difficulty == "easy":
        number = random.randint(10, 40)
        for i in range(2, number):
            if(number % i) == 0:
                switch = True
        if switch != True:
            number = random.randint(10, 40)
        variable = random.choice(choices)
        for i in range(random.randint(1, 2)):
            place_holder.append(variable)

    elif option_difficulty == "medium":
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

    elif option_difficulty == "hard":
        number = random.randint(70, 100)
        for i in range(2, number):
            if(number % i) == 0:
                switch = True
        if switch != True:
            number = random.randint(10, 40)
        for i in range(random.randint(1, 3)):
          variable = random.choice(choices)
          for i in range(random.randint(1, 7)):
            place_holder.append(variable)

    print(place_holder)
    #answer generation...
    temp = prime_factors(number)
    print("temp", temp)
    answer = str(temp) + str(place_holder)
    for i in temp:
        if i not in unique_1:
            unique_1.append(i)
    
    for i in place_holder:
        if i not in unique_2:
            unique_2.append(i)

    print("unique", unique_1)
    print("unique", unique_2)

    for i in unique_1: # for the numbers
        answerset.append(i)
        answerset.append(temp.count(i))
        answerset.insert(i + 2, ",") # DELETE THIS WHEN USING (FORMAT FOR THIS IS num THEN count OF num)
    
    for i in unique_2: # for the variables
        answerset.append(i)
        answerset.append(place_holder.count(i))
    print(answerset)

    return(number, answerset)

a,b = Factoring_Monomials("hard", False, 3)
print(a,"\n", b,"\n")