# First Section (NOT DONE YETT)

import math
import random
import sympy as sp
import fractions

def decimal_generator(option_difficulty):
    problem = ""
    integer_only = 0
    decimal = 0.0
    decimal_2 = 0.0
    if option_difficulty == "easy": # get rid of 74.90 <--- problem!!! (EDGE 0)
        integer_only = random.randint(1, 9)
        decimal = random.random()
        if integer_only % 2 == 0: 
            problem = "{:.1f}".format(integer_only + decimal)
        else:
            problem = "{:.2f}".format(integer_only + decimal)

    elif option_difficulty == "medium":
        integer_only = random.randint(1, 99)
        decimal = random.random()
        decimal_2 = "{:.2f}".format(decimal)
        if integer_only % 2 == 0:
            if (float(decimal_2) * 100) % 2 == 0:
                problem  = "{:.1f}".format(integer_only + float(decimal))
            elif int(str(decimal_2 * 100)[:1]) % 3 == 0:
                problem  = "{:.4f}".format(integer_only + float(decimal))
            else:
                problem = "{:.2f}".format(integer_only + float(decimal))
        else: #add one more (ten thousandth place) if the front is divisible by 2
            problem = "{:.3f}".format(integer_only + float(decimal))

    elif option_difficulty == "hard":
        integer_only = random.randint(10, 100)
        decimal = random.random()
        if integer_only % 2 == 0:
            problem = "{:.8f}".format(integer_only + decimal)
        else:
            problem = "{:.7f}".format(integer_only + decimal)
            #will have two cutt off points
    
    if str(problem)[-2] == "." and str(problem)[-1] == "0":
        problem = problem[:-2]

    return(problem)

def truncate(n):
    return int(n * 10000000000000) / 10000000000000

def Two_step_Equations_With_Decimals_1(option_difficulty = 'easy', expr = 'latex'):
    problemsets = ''
    answerset = ''
    choices = ['x', 'y', 'a', 'b', 'z', 'p', 't', 'q', 'k', 'u', 'r', 'd', 'w', 's', 'h', 'v']
    all_expressions = ['+', '-', '*', '/']
    addition_expression = ['+', '-']
    mult_expression = ['*', '/']
    case = [1, 2]#
    negative = ['-', '']
    temp = random.choice(case)
    sym_1 = ''
    variables = []
    variable_values = []
    numerals = []
    output = ''
    other = ''
    equation = ''
    pass_loop = False
    holder = ''
    sample = ""

    hip= ''

    if option_difficulty == 1:
        if temp == 1: # generate divisible number first, then add/subtract
            while pass_loop == False:
                variables.clear()
                variable_values.clear()
                numerals.clear()
                variables.append(random.choice(choices))
                variable_values.append(str(decimal_generator("easy")))
                sym_1 = random.choice(addition_expression)
                numerals.append(str(decimal_generator("easy")))
                numerals.append(str(random.choice(negative)) + str(decimal_generator("easy")))

                if sym_1 == "-":
                    sample = float(numerals[1]) + float(numerals[0])
                else:
                    sample = float(numerals[1]) - float(numerals[0])

                holder = float(sample) / float(variable_values[0])
                if len(str(holder)) <= 7: 
                    #print(True, len(str(holder)))
                    #print(holder, sample, numerals[1], numerals[0], variable_values[0])
                    pass_loop = True
            if random.randint(1,2) == 1:
                output = '{} * {} {} {}'.format(str(variable_values[0]), str(variables[0]), sym_1, str(numerals[0]))
            else:
                output = '{} {} {} * {}'.format( str(numerals[0]),  sym_1, str(variable_values[0]), str(variables[0]))
            other = '{}'.format(str(numerals[1]))
            equation = sp.Eq(sp.sympify(output), sp.sympify(other))
            problemsets = sp.latex(equation)
            answerset = holder

        elif temp == 2:
            while pass_loop == False:
                variables.clear()
                variable_values.clear()
                numerals.clear()
                variables.append(random.choice(choices))
                sym_1 = random.choice(addition_expression)
                variable_values.append(str(decimal_generator("easy")))
                numerals.append(str(decimal_generator("easy")))
                numerals.append(str(random.choice(negative)) + str(decimal_generator("easy")))
                
                x = sp.symbols(str(variables[0]))
                    
                output = '({} / {}) {} {}'.format(str(variables[0]), str(variable_values[0]), sym_1, numerals[0])
                other = '{}'.format(str(numerals[1]))
                equation  = sp.Eq(sp.sympify(output), sp.sympify(other))

                hip = sp.solve(equation, x)
                hip = str(hip)
                hip = hip.replace('[', '')
                hip = hip.replace(']', '')
                problemsets = r'\frac{' + str(variables[0]) + '}{' + str(variable_values[0]) + '} ' + sym_1 + ' ' + numerals[0] + ' = ' + numerals[1]
                answerset = truncate(sp.N(hip, chop=True))

                pass_loop = sp.sympify(hip).is_rational


    elif option_difficulty == 2:
        if temp == 1:
            while pass_loop == False:
                variables.clear()
                variable_values.clear()
                numerals.clear()
                variables.append(random.choice(choices))
                variable_values.append(str(decimal_generator("medium")))
                sym_1 = random.choice(addition_expression)
                numerals.append(str(decimal_generator("medium")))
                numerals.append(str(random.choice(negative)) + str(decimal_generator("medium")))

                if sym_1 == "-":
                    sample = float(numerals[1]) + float(numerals[0])
                else:
                    sample = float(numerals[1]) - float(numerals[0])

                holder = float(sample) / float(variable_values[0])
                if len(str(holder)) <= 7: 
                    #print(True, len(str(holder)))
                    #print(holder, sample, numerals[1], numerals[0], variable_values[0])
                    pass_loop = True
            if random.randint(1,2) == 1:
                output = '{} * {} {} {}'.format(str(variable_values[0]), str(variables[0]), sym_1, str(numerals[0]))
            else:
                output = '{} {} {} * {}'.format( str(numerals[0]),  sym_1, str(variable_values[0]), str(variables[0]))
            other = '{}'.format(str(numerals[1]))
            equation = sp.Eq(sp.sympify(output), sp.sympify(other))
            problemsets = sp.latex(equation)
            answerset = holder

        elif temp == 2:
            while pass_loop == False:
                variables.clear()
                variable_values.clear()
                numerals.clear()
                variables.append(random.choice(choices))
                sym_1 = random.choice(addition_expression)
                variable_values.append(str(decimal_generator("medium")))
                numerals.append(str(decimal_generator("medium")))
                numerals.append(str(random.choice(negative)) + str(decimal_generator("medium")))
                
                x = sp.symbols(str(variables[0]))
                    
                output = '({} {} {})'.format(str(variables[0]), sym_1, str(numerals[0]))
                other = '{}'.format(str(float(numerals[1]) * float(variable_values[0])))
                equation  = sp.Eq(sp.sympify(output), sp.sympify(other))
                hip = sp.solve(equation, x)
                hip = str(hip)
                hip = hip.replace('[', '')
                hip = hip.replace(']', '')
                problemsets = r'\frac{' + str(variables[0]) + ' ' + sym_1 + ' ' + str(numerals[0]) + '}{' + str(variable_values[0]) + '}' + ' = ' + numerals[1]
                answerset = sp.N(hip, chop=True)
                print(hip, truncate(answerset))
                answerset = truncate(answerset)
                if len(str(answerset)) <= 20:
                    pass_loop = True

    
    elif option_difficulty == 3:
        if temp == 1:
            variables.append(random.choice(choices))
            sym_1 = random.choice(addition_expression)
            numerals.append(str(decimal_generator("hard")))
            numerals.append(str(random.choice(negative)) +  str(decimal_generator("hard")))
            
            x = sp.symbols(str(variables[0]))
            
            if random.randint(1,2) == 1:
                output = '{} {} {}'.format(str(variables[0]), sym_1, str(numerals[0]))
            else: 
                output = '{} {} {}'.format(str(numerals[0]), sym_1, str(variables[0]))
            other = '{}'.format(str(numerals[1]))
            equation  = sp.Eq(sp.sympify(output), sp.sympify(other))
            hip = sp.solve(equation, x)
            hip = str(hip)
            hip = hip.replace('[', '')
            hip = hip.replace(']', '')
            problemsets = sp.latex(equation)
            answerset = sp.N(hip, chop=True)

        elif temp == 2:
            while pass_loop == False:
                variables.clear()
                variable_values.clear()
                numerals.clear()
                variables.append(random.choice(choices))
                variable_values.append(str(random.choice(negative)) + str(decimal_generator("hard")))
                numerals.append(str(random.choice(negative)) + str(decimal_generator("hard")))
                
                x = sp.symbols(str(variables[0]))
                    
                output = '{}*{}'.format(str(variable_values[0]), str(variables[0]))
                other = '{}'.format(str(numerals[0]))
                equation  = sp.Eq(sp.sympify(output), sp.sympify(other))
                
                hip = sp.solve(equation, x)
                hip = str(hip)
                hip = hip.replace('[', '')
                hip = hip.replace(']', '')

                problemsets = sp.latex(equation)
                answerset = sp.N(hip, chop=True)

                pass_loop = sp.sympify(hip).is_rational
        
        elif temp == 3:
            while pass_loop == False:
                variables.clear()
                variable_values.clear()
                numerals.clear()
                variables.append(random.choice(choices))
                variable_values.append(str(random.choice(negative)) + str(decimal_generator("hard")))
                numerals.append(str(random.choice(negative)) + str(decimal_generator("hard")))
                
                x = sp.symbols(str(variables[0]))
                    
                output = '{} / {}'.format(str(variables[0]), str(variable_values[0]))
                other = '{}'.format(str(numerals[0]))
                equation  = sp.Eq(sp.sympify(output), sp.sympify(other))

                hip = sp.solve(equation, x)
                hip = str(hip)
                hip = hip.replace('[', '')
                hip = hip.replace(']', '')
                answerset = sp.N(hip, chop=True)

                pass_loop = sp.sympify(hip).is_rational

    answerset = str(answerset)
    return(problemsets, answerset)