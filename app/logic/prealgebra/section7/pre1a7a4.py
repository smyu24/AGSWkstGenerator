import random

def insert_comma(num):
    num = int(num)
    return (f"{num:,}")

def insert_comma2(num):
    num = float(num)
    return (f"{num:,}")

def truncate(number):
    number = float(number)
    return((number * 100) / 100)

def decimal_generator(option_difficulty):
    problem = ""
    integer_only = 0
    decimal = 0.0
    decimal_2 = 0.0
    if option_difficulty == 1: # get rid of 74.90 <--- problem!!! (EDGE 0)
        integer_only = random.randint(1, 9)
        decimal = random.random()
        if integer_only % 2 == 0: 
            problem = "{:.1f}".format(decimal)
        else:
            problem = "{:.2f}".format(decimal)

    elif option_difficulty == 2:
        integer_only = random.randint(1, 99)
        decimal = random.random()
        decimal_2 = "{:.2f}".format(decimal)
        if integer_only % 2 == 0:
            if (float(decimal_2) * 100) % 2 == 0:
                problem  = "{:.1f}".format(float(decimal))
            elif int(str(decimal_2 * 100)[:1]) % 3 == 0:
                problem  = "{:.4f}".format(float(decimal))
            else:
                problem = "{:.2f}".format(float(decimal))
        else: #add one more (ten thousandth place) if the front is divisible by 2
            problem = "{:.3f}".format(float(decimal))

    elif option_difficulty == 3:
        integer_only = random.randint(10, 100)
        decimal = random.random()
        if integer_only % 2 == 0:
            problem = "{:.8f}".format(decimal)
        else:
            problem = "{:.7f}".format(decimal)
            #will have two cutt off points
    
    if str(problem)[-2] == "." and str(problem)[-1] == "0":
        problem = problem[:-2]

    return(problem)

def decimal_only_generator(option_difficulty):
    problem = ""
    integer_only = 0
    decimal = 0.0
    decimal_2 = 0.0
    if option_difficulty == 1: # get rid of 74.90 <--- problem!!! (EDGE 0)
        integer_only = random.randint(1, 9)
        decimal = random.random()
        if integer_only % 2 == 0: 
            problem = "{:.1f}".format(decimal)
        else:
            problem = "{:.2f}".format(decimal)

    elif option_difficulty == 2:
        integer_only = random.randint(1, 99)
        decimal = random.random()
        decimal_2 = "{:.2f}".format(decimal)
        if integer_only % 2 == 0:
            if (float(decimal_2) * 100) % 2 == 0:
                problem  = "{:.1f}".format(float(decimal))
            elif int(str(decimal_2 * 100)[:1]) % 3 == 0:
                problem  = "{:.4f}".format(float(decimal))
            else:
                problem = "{:.2f}".format(float(decimal))
        else: #add one more (ten thousandth place) if the front is divisible by 2
            problem = "{:.3f}".format(float(decimal))

    elif option_difficulty == 3:
        integer_only = random.randint(10, 100)
        decimal = random.random()
        if integer_only % 2 == 0:
            problem = "{:.8f}".format(decimal)
        else:
            problem = "{:.7f}".format(decimal)
            #will have two cutt off points
    
    if str(problem)[-2] == "." and str(problem)[-1] == "0":
        problem = problem[:-2]
    elif float(problem) == 0.0:
        decimal_only_generator(option_difficulty)
    return(problem)

def Scientific_Notation_Section_1(option_difficulty = 'easy', expr= 'latex'):
    one = ""
    answer = ""
    squared = ""
    if option_difficulty == 1:
        one = random.randint(100,10000)

        answer = str(f'{one: .10E}')
        answer = str(str(round(float(truncate(answer[:answer.find("E")])), 9)) + str(answer[answer.find("E"):]))

        squared = answer[answer.find("+"):]
        squared = int(squared)
        answer = answer[:answer.find("+") + 1]
        answer = answer.replace("E+", r" \times 10^{"+ str(squared) +"}")

        return(insert_comma(one), answer)

    elif option_difficulty == 2:
        squared = ""
        one = float(decimal_generator(option_difficulty))

        answer = str(f'{one: .10E}')
        answer = str(str(round(float(truncate(answer[:answer.find("E")])), 9)) + str(answer[answer.find("E"):]))


        squared = answer[answer.find("-"):]
        squared = int(str(squared))
        answer = answer[:answer.find("-") + 1]
        answer = answer.replace("E-", r" \times 10^{"+ str(squared)+"}")

        return(one, answer)
    
    elif option_difficulty == 3:
        number = ""
        decimal = ""
        number = random.randint(0, 999999)
        decimal = float(decimal_only_generator(option_difficulty))
        one = float(number + decimal)

        answer = str(f'{one: .10E}')
        answer = str(str(round(float(truncate(answer[:answer.find("E")])), 9)) + str(answer[answer.find("E"):]))

        if answer.find("+") != -1:
            squared = answer[answer.find("+"):]
            squared = int(squared)
            answer = answer[:answer.find("+") + 1]
            answer = answer.replace("E+", r" \times 10^{"+ str(squared)+"}")
        else:
            squared = answer[answer.find("-"):]
            squared = int(str(squared))
            answer = answer[:answer.find("-") + 1]
            answer = answer.replace("E-", r" \times 10^{"+ str(squared)+"}")

        return(insert_comma2(one), answer)

def Scientific_Notation_Section_2(option_difficulty = 'easy', expr= 'latex'):
    one = ""
    answer = ""
    squared = ""
    if option_difficulty == 1:
        one = random.randint(100,10000)

        answer = str(f'{one: .10E}')
        answer = str(str(round(float(truncate(answer[:answer.find("E")])), 9)) + str(answer[answer.find("E"):]))
        
        squared = answer[answer.find("+"):]
        squared = int(squared)
        answer = answer[:answer.find("+") + 1]
        answer = answer.replace("E+", r" \times 10^{"+ str(squared)+"}")

        return(answer, insert_comma(one))

    elif option_difficulty == 2:
        squared = ""
        one = float(decimal_generator(option_difficulty))

        answer = str(f'{one: .10E}')
        answer = str(str(round(float(truncate(answer[:answer.find("E")])), 9)) + str(answer[answer.find("E"):]))

        squared = answer[answer.find("-"):]
        squared = int(str(squared))
        answer = answer[:answer.find("-") + 1]
        answer = answer.replace("E-", r" \times 10^{"+ str(squared)+"}")

        return(answer, one)
    
    elif option_difficulty == 3:
        number = ""
        decimal = ""
        number = random.randint(0, 999999)
        decimal = float(decimal_only_generator(option_difficulty))
        one = float(number + decimal)

        answer = str(f'{one: .10E}')
        answer = str(str(round(float(truncate(answer[:answer.find("E")])), 9)) + str(answer[answer.find("E"):]))

        if answer.find("+") != -1:
            squared = answer[answer.find("+"):]
            squared = int(squared)
            answer = answer[:answer.find("+") + 1]
            answer = answer.replace("E+", r" \times 10^{"+ str(squared)+"}")
        else:
            squared = answer[answer.find("-"):]
            squared = int(str(squared))
            answer = answer[:answer.find("-") + 1]
            answer = answer.replace("E-", r" \times 10^{"+ str(squared)+"}")

        return(answer, insert_comma2(one))

def Scientific_Notation_Section_3(option_difficulty = 'easy', expr= 'latex'):
    one = ""
    problem = ""
    answer = ""
    squared = ""
    squared_2 = ""
    negative = ["-", ""]

    if option_difficulty == 1: 
        one = random.randint(5, 100)
        squared = str(random.choice(negative)) + str(random.randint(2,5))

        problem = str(one) + r" \times 10^{"+ str(squared)+"}"

        answer = str(f'{one: .10E}')
        answer = str(str(round(float(truncate(answer[:answer.find("E")])), 9)) + str(answer[answer.find("E"):]))

        if answer.find("+") != -1:
            squared_2 = answer[answer.find("+"):]
            squared_2 = int(squared_2) + int(squared)
            answer = answer[:answer.find("+") + 1]
            answer = answer.replace("E+", r" \times 10^{"+ str(squared_2)+"}")
        else:
            squared_2 = answer[answer.find("-"):]
            squared_2 = int(squared_2) + int(squared)
            answer = answer[:answer.find("-") + 1]
            answer = answer.replace("E-", r" \times 10^{"+ str(squared_2)+"}")

        return(problem, answer)

    elif option_difficulty == 2:
        one = float(decimal_generator(option_difficulty))
        squared = str(random.choice(negative)) + str(random.randint(2,5))

        problem = str(one) + r" \times 10^{"+ str(squared)+"}"

        answer = str(f'{one: .10E}') 
        answer = str(str(round(float(truncate(answer[:answer.find("E")])), 9)) + str(answer[answer.find("E"):]))

        squared_2 = answer[answer.find("-"):]
        squared_2 = int(squared_2) + int(squared)
        answer = answer[:answer.find("-") + 1]
        answer = answer.replace("E-", r" \times 10^{"+ str(squared_2)+"}")

        return(problem, answer)
    
    elif option_difficulty == 3: 
        number = ""
        decimal = ""
        number = random.randint(0, 9999)
        decimal = float(decimal_only_generator("medium"))
        squared = str(random.choice(negative)) + str(random.randint(2,10))
        one = float(float(number) + float(decimal))

        problem = str(one) + r" \times 10^{"+ str(squared)+"}"

        answer = str(f'{one: .10E}')
        answer = str(str(round(float(truncate(answer[:answer.find("E")])), 9)) + str(answer[answer.find("E"):]))

        if answer.find("+") != -1:
            squared_2 = answer[answer.find("+"):]
            squared_2 = int(squared_2) + int(squared)
            answer = answer[:answer.find("+") + 1]
            answer = answer.replace("E+", r" \times 10^{"+ str(squared_2)+"}")
        else:
            squared_2 = answer[answer.find("-"):]
            squared_2 = int(squared_2) + int(squared)
            answer = answer[:answer.find("-") + 1]
            answer = answer.replace("E-", r" \times 10^{"+ str(squared_2)+"}")

        return(problem, answer)

def sci_formatter(answer, squared):
    squared_2 = ""
    if answer.find("+") != -1:
        squared_2 = answer[answer.find("+"):]
        squared_2 = int(squared_2) + int(squared)
        answer = answer[:answer.find("+") + 1]
        answer = answer.replace("E+", r" \times 10^{"+ str(squared_2)+"}")
    else:
        squared_2 = answer[answer.find("-"):]
        squared_2 = int(squared_2) + int(squared)
        answer = answer[:answer.find("-") + 1]
        answer = answer.replace("E-", r" \times 10^{"+ str(squared_2)+"}")
    return(answer, float(answer[:answer.find("t") - 2]), answer[answer.find("{") +1:-1])

def sciformatter(answer, squared):
    squared_2 = ""
    if answer.find("+") != -1:
        squared_2 = int(squared)
        answer = answer[:answer.find("+") + 1]
        answer = answer.replace("E+", r" \times 10^{"+ str(squared_2)+"}")
    else:
        squared_2 = int(squared)
        answer = answer[:answer.find("-") + 1]
        answer = answer.replace("E-", r" \times 10^{"+ str(squared_2)+"}")
    return(answer, float(answer[:answer.find("t") - 2]))

def Scientific_Notation_Section_4(option_difficulty = 'easy', expr= 'latex'):
    one = ""
    two = ""
    problem = ""
    answer = ""
    answer_1 = ""
    answer_2 = ""
    squared = ""
    squared_two = ""
    squared_2 = ""
    negative = ["-", ""]
    filler = ""

    if option_difficulty == 1: # (7 × 10^2)(9 × 10^6) solve then scientific
        first_para = ""
        second_para = ""
        one = random.randint(5, 100)
        two = random.randint(5, 100)
        squared = str(random.choice(negative)) + str(random.randint(2,5))
        squared_two = str(random.choice(negative)) + str(random.randint(2,5))

        answer_1 = str(f'{one: .10E}')
        answer_1 = str(round(truncate(float(answer_1[:answer_1.find("E")])), 9)) + str(answer_1[answer_1.find("E"):])

        answer_2 = str(f'{two: .10E}')
        answer_2 = str(round(truncate(float(answer_2[:answer_2.find("E")])), 9)) + str(answer_2[answer_2.find("E"):])

        first_para, one, squared = sci_formatter(answer_1, squared)
        second_para, two, squared_two = sci_formatter(answer_2, squared_two)

        problem = fr'({first_para})({second_para})'

        answer = (one) * (two)

        answer = str(f'{answer: .10E}')
        answer = str(str(round(float(truncate(answer[:answer.find("E")])), 9)) + str(answer[answer.find("E"):]))

        answer = sciformatter(answer, int(squared) + int(squared_two) + 1)[0]
        return(problem, answer)


    elif option_difficulty == 2:
        first_para = ""
        second_para = ""
        one = float(decimal_generator(option_difficulty))
        two = float(decimal_generator(option_difficulty))
        squared = str(random.choice(negative)) + str(random.randint(2,5))
        squared_two = str(random.choice(negative)) + str(random.randint(2,5))

        answer_1 = str(f'{one: .10E}')
        answer_1 = str(round(truncate(float(answer_1[:answer_1.find("E")])), 9)) + str(answer_1[answer_1.find("E"):])

        answer_2 = str(f'{two: .10E}')
        answer_2 = str(round(truncate(float(answer_2[:answer_2.find("E")])), 9)) + str(answer_2[answer_2.find("E"):])

        first_para, one, squared = sci_formatter(answer_1, squared)
        second_para, two, squared_two = sci_formatter(answer_2, squared_two)

        problem = fr'({first_para})({second_para})'

        answer = (one) * (two)

        answer = str(f'{answer: .10E}')
        answer = str(str(round(float(truncate(answer[:answer.find("E")])), 9)) + str(answer[answer.find("E"):]))

        answer = sciformatter(answer, int(squared) + int(squared_two) + 1)[0]
        return(problem, answer)

    elif option_difficulty == 3:
        first_para = ""
        second_para = ""

        one = float(str(random.randint(5, 99)) + str(decimal_generator("medium")))
        two = float(str(random.randint(5, 99)) + str(decimal_generator("medium")))

        squared = str(random.choice(negative)) + str(random.randint(2,10))
        squared_two = str(random.choice(negative)) + str(random.randint(2,10))

        answer_1 = str(f'{one: .10E}')
        answer_1 = str(round(truncate(float(answer_1[:answer_1.find("E")])), 9)) + str(answer_1[answer_1.find("E"):])

        answer_2 = str(f'{two: .10E}')
        answer_2 = str(round(truncate(float(answer_2[:answer_2.find("E")])), 9)) + str(answer_2[answer_2.find("E"):])

        first_para, one, squared = sci_formatter(answer_1, squared)
        second_para, two, squared_two = sci_formatter(answer_2, squared_two)

        problem = fr'({first_para})({second_para})'

        answer = (one) * (two)

        answer = str(f'{answer: .10E}')
        answer = str(str(round(float(truncate(answer[:answer.find("E")])), 9)) + str(answer[answer.find("E"):]))

        answer = sciformatter(answer, int(squared) + int(squared_two) + 1)[0]
        return(problem, answer)
