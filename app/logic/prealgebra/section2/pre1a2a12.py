import math
import random

def latexify(input, option="inline"):
    if option == "inline":
        return input
    else:
        return '\[' + input + '\]'
        
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