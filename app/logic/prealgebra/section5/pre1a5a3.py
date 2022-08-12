# First Section

import math
import numbers
import random
import sympy as sp
import fractions

def fraction_generator(option_difficulty):
    problem = ""
    numerator = 4
    denominator = 4
    while float(numerator / denominator) == 1:
        if option_difficulty == "easy": # get rid of 74.90 <--- problem!!! (EDGE 0)
            numerator = random.randint(1, 4)
            denominator = random.randint(2, 5)
            problem = fractions.Fraction(numerator, denominator)

        elif option_difficulty == "medium":
            numerator = random.randint(2, 7)
            denominator = random.randint(2, 9)
            problem = fractions.Fraction(numerator, denominator)

        elif option_difficulty == "hard":
            numerator = random.randint(2, 25)
            denominator = random.randint(2, 12)
            problem = fractions.Fraction(numerator, denominator)
    return(problem)

def truncate(n):
    return int(round(n,4) * 1000) / 1000

def One_step_Equations_With_Fractions_1(option_difficulty, option_random):
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

    hip= ''

    if option_difficulty == 1:
        if temp == 1:
            variables.append(random.choice(choices))
            variable_values.append(str(fraction_generator("easy")))
            numerals.append(str(random.choice(negative)) +  str(random.randint(2,5)))
            
            x = sp.symbols(str(variables[0]))
            
            output = '{} * {}'.format(str(variable_values[0]), str(variables[0]))
            other = '{}'.format(str(numerals[0]))
            equation  = sp.Eq(sp.sympify(output), sp.sympify(other))
            hip = sp.solve(equation, x)
            hip = str(hip)
            hip = hip.replace('[', '')
            hip = hip.replace(']', '')
            problemsets = sp.latex(equation)
            answerset = sp.N(hip, chop=True)

        elif temp == 2:
            variables.append(random.choice(choices))
            sym_1 = random.choice(addition_expression)
            variable_values.append(str(random.choice(negative)) + str(fraction_generator("easy")))
            numerals.append(str(random.choice(negative)) + str(random.randint(1,5)))
            
            x = sp.symbols(str(variables[0]))
            if random.randint(1,2) == 1:
                output = '{} {} {}'.format(str(variables[0]), sym_1, str(variable_values[0]))
            else:
                output = '{} {} {}'.format(str(variable_values[0]), sym_1, str(variables[0]))
            other = '{}'.format(str(numerals[0]))
            equation  = sp.Eq(sp.sympify(output), sp.sympify(other))
            holder = output + ' = ' + other

            hip = sp.solve(equation, x)
            hip = str(hip)
            hip = hip.replace('[', '')
            hip = hip.replace(']', '')
            problemsets = sp.latex(equation)
            answerset = sp.N(hip, chop=True)

            pass_loop = sp.sympify(hip).is_rational

    elif option_difficulty == 2:
        if temp == 1:
            variables.append(random.choice(choices))
            variable_values.append(str(fraction_generator("medium")))
            numerals.append(str(random.choice(negative)) +  str(fraction_generator("medium")))
            
            x = sp.symbols(str(variables[0]))
            
            output = '{} * {}'.format(str(variable_values[0]), str(variables[0]))
            other = '{}'.format(str(numerals[0]))
            equation  = sp.Eq(sp.sympify(output), sp.sympify(other))
            hip = sp.solve(equation, x)
            hip = str(hip)
            hip = hip.replace('[', '')
            hip = hip.replace(']', '')
            problemsets = sp.latex(equation)
            answerset = sp.N(hip, chop=True)

        elif temp == 2:
            variables.append(random.choice(choices))
            sym_1 = random.choice(addition_expression)
            numerals.append(str(fraction_generator("medium")))
            numerals.append(str(random.choice(negative)) + str(fraction_generator("medium")))
            
            x = sp.symbols(str(variables[0]))
            if random.randint(1,2) == 1:
                output = '{} {} {}'.format(str(variables[0]), sym_1, str(numerals[0]))
            else:
                output = '{} {} {}'.format(str(numerals[0]), sym_1, str(variables[0]))
            other = '{}'.format(str(numerals[1]))
            equation  = sp.Eq(sp.sympify(output), sp.sympify(other))
            holder = output + ' = ' + other

            hip = sp.solve(equation, x)
            hip = str(hip)
            hip = hip.replace('[', '')
            hip = hip.replace(']', '')
            problemsets = sp.latex(equation)
            answerset = sp.N(hip, chop=True)
        
    elif option_difficulty == 3:
        if temp == 1:
            variables.append(random.choice(choices))
            variable_values.append(str(fraction_generator("hard")))
            numerals.append(str(random.choice(negative)) +  str(fraction_generator("hard")))
            
            x = sp.symbols(str(variables[0]))
            
            output = '{} * {}'.format(str(variable_values[0]), str(variables[0]))
            other = '{}'.format(str(numerals[0]))
            equation  = sp.Eq(sp.sympify(output), sp.sympify(other))
            hip = sp.solve(equation, x)
            hip = str(hip)
            hip = hip.replace('[', '')
            hip = hip.replace(']', '')
            problemsets = sp.latex(equation)
            answerset = sp.N(hip, chop=True)

        elif temp == 2:
            variables.append(random.choice(choices))
            sym_1 = random.choice(addition_expression)
            numerals.append(str(fraction_generator("hard")))
            numerals.append(str(random.choice(negative)) + str(fraction_generator("hard")))
            
            x = sp.symbols(str(variables[0]))
            if random.randint(1,2) == 1:
                output = '{} {} {}'.format(str(variables[0]), sym_1, str(numerals[0]))
            else:
                output = '{} {} {}'.format(str(numerals[0]), sym_1, str(variables[0]))
            other = '{}'.format(str(numerals[1]))
            equation  = sp.Eq(sp.sympify(output), sp.sympify(other))
            holder = output + ' = ' + other

            hip = sp.solve(equation, x)
            hip = str(hip)
            hip = hip.replace('[', '')
            hip = hip.replace(']', '')
            problemsets = sp.latex(equation)
            answerset = sp.N(hip, chop=True)
    answerset = str(truncate(answerset))
    answerset = sp.latex(sp.sympify(fractions.Fraction(answerset)))
    return(problemsets, answerset)