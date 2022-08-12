# First Section

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
            problem = "{:.6f}".format(integer_only + decimal)
        else:
            problem = "{:.5f}".format(integer_only + decimal)
            #will have two cutt off points
    return(problem)

def truncate(n):
    return int(round(n,4) * 1000) / 1000

def find_replace(sent, replace, var, var_val):
    return sent.replace(replace, r'\frac{' + var + '}{' + var_val + '}')


def One_step_Equations_With_Decimals_1(option_difficulty, option_random):
    problemsets = ''
    answerset = ''
    choices = ['x', 'y', 'a', 'b', 'z', 'p', 't', 'q', 'k', 'u', 'r', 'd', 'w', 's', 'h', 'v']
    all_expressions = ['+', '-', '*', '/']
    addition_expression = ['+', '-']
    mult_expression = ['*', '/']
    case = [1, 2, 3]#
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
            sym_1 = random.choice(addition_expression)
            numerals.append(str(decimal_generator("easy")))
            numerals.append(str(random.choice(negative)) +  str(decimal_generator("easy")))
            
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
                variable_values.append(str(random.choice(negative)) + str(decimal_generator("easy")))
                numerals.append(str(random.choice(negative)) + str(decimal_generator("easy")))
                
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
                variable_values.append(str(random.choice(negative)) + str(decimal_generator("easy")))
                numerals.append(str(random.choice(negative)) + str(decimal_generator("easy")))
                
                x = sp.symbols(str(variables[0]))
                    
                output = '{} / {}'.format(str(variables[0]), str(variable_values[0]))
                other = '{}'.format(str(numerals[0]))
                equation  = sp.Eq(sp.sympify(output), sp.sympify(other))
                holder = output + ' = ' + other

                hip = sp.solve(equation, x)
                hip = str(hip)
                hip = hip.replace('[', '')
                hip = hip.replace(']', '')
                problemsets = find_replace(holder, output, str(variables[0]), str(variable_values[0]))
                answerset = sp.N(hip, chop=True)

                pass_loop = sp.sympify(hip).is_rational

    elif option_difficulty == 2:
        if temp == 1:
            variables.append(random.choice(choices))
            sym_1 = random.choice(addition_expression)
            numerals.append(str(decimal_generator("medium")))
            numerals.append(str(random.choice(negative)) +  str(decimal_generator("medium")))
            
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
                variable_values.append(str(random.choice(negative)) + str(decimal_generator("medium")))
                numerals.append(str(random.choice(negative)) + str(decimal_generator("medium")))
                
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
                variable_values.append(str(random.choice(negative)) + str(decimal_generator("medium")))
                numerals.append(str(random.choice(negative)) + str(decimal_generator("medium")))
                
                x = sp.symbols(str(variables[0]))
                    
                output = '{} / {}'.format(str(variables[0]), str(variable_values[0]))
                other = '{}'.format(str(numerals[0]))
                equation  = sp.Eq(sp.sympify(output), sp.sympify(other))
                holder = output + ' = ' + other

                hip = sp.solve(equation, x)
                hip = str(hip)
                hip = hip.replace('[', '')
                hip = hip.replace(']', '')
                problemsets = find_replace(holder, output, str(variables[0]), str(variable_values[0]))
                answerset = sp.N(hip, chop=True)

                pass_loop = sp.sympify(hip).is_rational
    
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
                holder = output + ' = ' + other

                hip = sp.solve(equation, x)
                hip = str(hip)
                hip = hip.replace('[', '')
                hip = hip.replace(']', '')
                problemsets = find_replace(holder, output, str(variables[0]), str(variable_values[0]))
                answerset = sp.N(hip, chop=True)

                pass_loop = sp.sympify(hip).is_rational

    answerset = str(truncate(answerset))
    return(problemsets, answerset)