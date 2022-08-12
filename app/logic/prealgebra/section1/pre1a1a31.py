import math
import random


def latexify(input, option="inline"):
    if option == "inline":
        return input 
    else:
        return '\[' + input + '\]'


def insert_comma(num):
    num = int(num)
    return (f"{num:,}")


def insert_overline(problemsets):
    ticker = True
    while ticker == True:
        problemsets = str(problemsets)
        a = random.randint(0, len(problemsets) - 2)
        list(problemsets)
        if problemsets[a] != "." and problemsets[a] != ",":
            ticker = False
    
    problemsets = str(problemsets)
    problemsets = problemsets[:a] + r"\overline" + problemsets[a:]

    a = (((problemsets.rfind('e')) - len(problemsets)) * -1) - 1
    return(problemsets , a)

def rounding(problemsets, underscores):
    inversed_under = underscores * -1
    skipper = (inversed_under) + 1
    pass_through = False
    accepted = 0
    empty = ''
    while pass_through == False:
        if problemsets[skipper] == ',' or problemsets[skipper] == '.':
            skipper += 1
        elif int(problemsets[skipper]) >= 5:
            cut = problemsets[inversed_under + 1:]
            for i in range(len(cut)):
                if cut[i] == ',':
                    empty = empty + ','
                else:
                    empty = empty + '0'
            other_half = problemsets[:inversed_under + 1]
            other_half = list(''.join(other_half))
            if int(str(other_half[-1])) != 9:
                other_half[-1] = str(int(str(other_half[-1])) + 1)
            else:
                other_half[-1] = str(0)
                # check for commas next
                if other_half[other_half.index('o') - 2] == 9 or other_half[other_half.index('o') - 2] == ',':
                    if other_half[other_half.index('o') - 3] == 9 or other_half[other_half.index('o') - 2] == ',':
                        if other_half[other_half.index('o') - 4] == 9 or other_half[other_half.index('o') - 2] == ',':
                            other_half[other_half.index('o') - 5] = str(int(other_half[other_half.index('o') - 4]) + 1)
                        else: 
                            other_half[other_half.index('o') - 4] = str(int(other_half[other_half.index('o') - 4]) + 1)
                    else:
                        other_half[other_half.index('o') - 3] = str(int(other_half[other_half.index('o')- 3]) + 1)
                else:
                    other_half[other_half.index('o') - 2] = str(int(other_half[other_half.index('o') - 2]) + 1)


            problemsets = ''.join(other_half) + empty
            pass_through = True
        else:
            cut = problemsets[inversed_under + 1:]
            for i in range(len(cut)):
                if cut[i] == ',':
                    empty = empty + ','
                else:
                    empty = empty + '0'
            other_half = problemsets[:inversed_under + 1]
            problemsets = other_half + ''.join(empty)
            pass_through = True
    return(problemsets)


def Rounding_Number_Section_1(option_difficulty='easy',expr='latex', localmin=0, localmax=0):
    problemsets = ""
    temp_problem = []
    temp = ""
    if(localmin == localmax):
        if(option_difficulty == 1):
            problemsets = random.randint(100, 99999)
        elif(option_difficulty == 2):
            problemsets = random.randint(1000, 999999)
        elif(option_difficulty == 3):
            problemsets = random.randint(10000, 89999999)
    else:
        problemsets = random.randint(localmin, localmax)
    problemsets = list(str(problemsets))
    temp_problem = insert_comma(''.join(problemsets))
    temp_problem, temp = insert_overline(temp_problem)
    problemsets = temp_problem
    temp_problem = rounding(temp_problem, temp)
    if expr == 'latex':
        return(latexify(problemsets), latexify(temp_problem))
    else:
        return(insert_comma(''.join(problemsets)), temp_problem) 