# First Section

import math
import random

def Multiplying_Integers_1(option_difficulty, option_random):
    problemsets = []
    answerset = []
    to_be_prime = 0
    holder = []
    negative = [1, -1]
    temp = []
    list_holder = []
    if option_difficulty == "easy": # Pure positive integers
        to_be_prime = random.randint(2, 10)

    elif option_difficulty == "medium": # Mix of positive and negetives
        to_be_prime = random.randint(10, 20)

    elif option_difficulty == "hard": # All previous options + higher number threshold
        to_be_prime = random.randint(15, 30)

    # answer generation...
    for i in range(1, int(to_be_prime / 2) + 1):
        if to_be_prime % i == 0:
            if i not in temp:
                temp.append(i)
            if int(to_be_prime/i) not in temp:
                temp.append(int(to_be_prime / i))

    holder = random.choice(temp[1:])
    print("holder", holder)

    if option_difficulty == "easy":
        list_holder.append(random.choice(negative) * (holder * random.randint(2, 10)))
        list_holder.append(random.choice(negative) * holder)

    elif option_difficulty == "medium":
        list_holder.append(random.choice(negative) * (holder * random.randint(5, 15)))
        list_holder.append(random.choice(negative) * holder)

    elif option_difficulty == "hard":
        list_holder.append(random.choice(negative) * (holder * random.randint(10, 15)))
        list_holder.append(random.choice(negative) * holder)
    
    problemsets.append("$ " + str(list_holder[0]) + " \times " + str(list_holder[1]) + " $") # "latexified"

    answerset.append(int(list_holder[0]*list_holder[1]))

    return(problemsets, answerset) # $6 \times 3 = 28$


a,b = Multiplying_Integers_1("easy", False)
print(a,b)
a,b = Multiplying_Integers_1("medium", False)
print(a,b)
a,b = Multiplying_Integers_1("hard", False)
print(a,b)