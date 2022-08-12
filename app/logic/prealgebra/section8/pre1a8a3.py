import random
import sympy

def percentify(num):
    if str(float(num))[-2:] == ".0":
        num = int(num)
    return(str(num) + "\\%")

def inc_dec_formatter(num, choice):
    num = str(num)
    if choice == True:
        return(num + " Increase")
    elif choice == False:
        return(num + " Decrease")

measurements = ["miles", "grams", "ft", "minutes", "seconds", "meters", "kilos", "dollars", "liters", "tons"]
pick = [True, False]

def Finding_Percent_Change_Section_1(option_difficulty = 'easy', expr = 'latex'):
    problem = ""
    answer = 0
    type = ""

    intA = random.randint(1,100)
    intB = random.randint(1,200)
    floatA = float(str(random.randint(1,99)) + "." + str(random.randint(1,9)))
    floatB = float(str(random.randint(1,199)) + "." + str(random.randint(1,9)))

    chosen = random.choice(pick)
    if option_difficulty == 1: #From 82 to 38
        type = False
        problem = "From $" + str(intA) + "$ to $" + str(intB) +"$" 
        answer = ( intB - intA ) / intA
        if intB >= intA:
            answer = answer + 1
            type = True
        else:
            answer = float(answer) * -1
        return(problem, inc_dec_formatter(percentify(round(100 * round(answer, 4), 2)), type))


    elif option_difficulty == 2: #What percent of  81.88  is  122 ? 
        if chosen == True:
            type = False
            problem = "From $" + str(intA) + "$ to $" + str(floatB) +"$" 
            answer = ( floatB - intA ) / intA
            if floatB >= intA:
                answer = answer + 1
                type = True
            else:
                answer = float(answer) * -1
            return(problem, inc_dec_formatter(percentify(round(100 * round(answer, 4), 2)), type))
        else:
            type = False
            problem = "From $" + str(floatB) + "$ to $" + str(intB) +"$" 
            answer = ( intB - floatB ) / floatB
            if intB >= floatB:
                answer = answer + 1
                type = True
            else:
                answer = float(answer) * -1
            return(problem, inc_dec_formatter(percentify(round(100 * round(answer, 4), 2)), type))


    elif option_difficulty == 3: # 76% of what is 188.12 ? || 144.26  is  23%  of what? 
        if chosen == True:
            type = False
            problem = "From $" + str(floatA) + "$ to $" + str(floatB) +"$"
            answer = ( floatB - floatA ) / floatA
            if floatB >= floatA:
                answer = answer + 1
                type = True
            else:
                answer = float(answer) * -1
            return(problem, inc_dec_formatter(percentify(round(100 * round(answer, 4), 2)), type))
        else:
            type = False
            problem = "From $" + str(floatB) + "$ to $" + str(floatA) +"$"
            answer = ( floatA - floatB ) / floatB
            if floatA >= floatB:
                answer = answer + 1
                type = True
            else:
                answer = float(answer) * -1
            return(problem, inc_dec_formatter(percentify(round(100 * round(answer, 4), 2)), type))

def Finding_Percent_Change_Section_2(option_difficulty = 'easy', expr = 'latex'):
    problem = ""
    answer = 0
    type = ""
    measure = random.choice(measurements)

    intA = random.randint(1,100)
    intB = random.randint(1,200)
    floatA = float(str(random.randint(1,99)) + "." + str(random.randint(1,9)))
    floatB = float(str(random.randint(1,199)) + "." + str(random.randint(1,9)))

    chosen = random.choice(pick)
    if option_difficulty == 1: #From 82 to 38
        type = False
        problem = "From " + str(intA) + " " + str(measure) + " to " + str(intB) + " " + str(measure)
        answer = ( intB - intA ) / intA
        if intB >= intA:
            answer = answer + 1
            type = True
        else:
            answer = float(answer) * -1
        return(problem, inc_dec_formatter(percentify(round(100 * round(answer, 4), 2)), type))


    elif option_difficulty == 2: #What percent of  81.88  is  122 ? 
        if chosen == True:
            type = False
            problem = "From " + str(intA) + " " + str(measure) + " to " + str(floatB) + " " + str(measure)
            answer = ( floatB - intA ) / intA
            if floatB >= intA:
                answer = answer + 1
                type = True
            else:
                answer = float(answer) * -1
            return(problem, inc_dec_formatter(percentify(round(100 * round(answer, 4), 2)), type))
        else:
            type = False
            problem = "From " + str(floatB) + " " + str(measure) + " to " + str(intB) + " " + str(measure)
            answer = ( intB - floatB ) / floatB
            if intB >= floatB:
                answer = answer + 1
                type = True
            else:
                answer = float(answer) * -1
            return(problem, inc_dec_formatter(percentify(round(100 * round(answer, 4), 2)), type))


    elif option_difficulty == 3: # 76% of what is 188.12 ? || 144.26  is  23%  of what? 
        if chosen == True:
            type = False
            problem = "From " + str(floatA) + " " + str(measure) + " to " + str(floatB) + " " + str(measure)
            answer = ( floatB - floatA ) / floatA
            if floatB >= floatA:
                answer = answer + 1
                type = True
            else:
                answer = float(answer) * -1
            return(problem, inc_dec_formatter(percentify(round(100 * round(answer, 4), 2)), type))
        else:
            type = False
            problem = "From " + str(floatB) + " " + str(measure) + " to " + str(floatA) + " " + str(measure)
            answer = ( floatA - floatB ) / floatB
            if floatA >= floatB:
                answer = answer + 1
                type = True
            else:
                answer = float(answer) * -1
            return(problem, inc_dec_formatter(percentify(round(100 * round(answer, 4), 2)), type))