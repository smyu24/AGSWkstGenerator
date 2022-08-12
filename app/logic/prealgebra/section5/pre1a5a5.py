# First Section

import math
import random
import sympy as sp

def checker(a, b):
    a = int(a)
    b = int(b)
    if a == b or a % b == 0 or b % a == 0:
        print("------------")
        return False
    return True

def Two_step_Equations_With_Integers_1(option_difficulty = 'easy', expr = 'latex'):
    problemsets = ""
    answerset = []
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
    unique = []
    holder = 0
    randomized = 0

    if option_difficulty == 1:
        if temp == 1:
            while pass_loop == False:
                variables.clear()
                variable_values.clear()
                numerals.clear()
                #problemsets.clear()
                answerset.clear()
                variables.append(random.choice(choices))
                sym_1 = random.choice(addition_expression)
                numerals.append(str(random.randint(2, 10)))
                numerals.append(str(random.choice(negative)) +  str(random.randint(1, 10)))
                numerals.append(str(random.choice(negative)) +  str(random.randint(2, 10)))
                x = sp.symbols(str(variables[0]))
                if random.randint(1,2) == 1:
                    output = '{}*{} {} {}'.format(str(numerals[2]), str(variables[0]), sym_1, str(numerals[0]))
                else: 
                    output = '{} {} {}*{}'.format(str(numerals[0]), sym_1, str(numerals[2]), str(variables[0]))
                other = '{}'.format(str(numerals[1]))
                equation  = sp.Eq(sp.sympify(output), sp.sympify(other))
                    
                problemsets=(sp.latex(equation))
                answerset.append(sp.solve(equation, x))
                pass_loop = sp.sympify(sp.solve(equation, x).pop(0)).is_integer
        
        elif temp == 2:
            variables.append(random.choice(choices))
            variable_values.append(str(random.choice(negative)) + str(random.randint(2,10)))
            numerals.append(str(random.choice(negative)) + str(random.randint(2,15)))
            numerals.append(str(random.randint(2,15)))
            sym_1 = random.choice(addition_expression)
            x = sp.symbols(str(variables[0]))
                
            output = '{} / {} {} {}'.format(str(variables[0]), str(variable_values[0]), sym_1, str(numerals[1]))
            other = '{}'.format(str(numerals[0]))
            equation  = sp.Eq(sp.sympify(output), sp.sympify(other))

            problemsets=(sp.latex(equation))
            answerset.append(sp.solve(equation, x))

    elif option_difficulty == 2:
        if temp == 1:
            variables.clear()
            variable_values.clear()
            numerals.clear()
            #problemsets.clear()
            answerset.clear()
            variables.append(random.choice(choices))
            numerals.append(str(random.randint(2, 20)))
            numerals.append(str(random.randint(2, 20)))
            numerals.append(str(random.choice(negative)) +  str(random.randint(1, 40)))
                
            x = sp.symbols(str(variables[0]))
            
            output = '({} / {}) * {}'.format(str(numerals[0]), str(numerals[1]), str(variables[0]))
            other = '{}'.format(str(numerals[2]))
            equation  = sp.Eq(sp.sympify(output), sp.sympify(other))
            problemsets=(sp.latex(equation))
            answerset.append(sp.solve(equation, x))

        elif temp == 2:
            variables.clear()
            variable_values.clear()
            numerals.clear()
            #problemsets.clear()
            answerset.clear()
            variables.append(random.choice(choices))
            numerals.append(str(random.randint(2, 20)))
            numerals.append(str(random.randint(2, 20)))
            numerals.append(str(random.randint(1, 30)))
            numerals.append( str(random.randint(2, 30)))
                
            x = sp.symbols(str(variables[0]))
            
            output = '({} / {}) * {}'.format(str(numerals[0]), str(numerals[1]), str(variables[0]))
            other = '{} / {}'.format(str(numerals[2]), str(numerals[3]))
            equation  = sp.Eq(sp.sympify(output), sp.sympify(other))
            problemsets=(sp.latex(equation))
            answerset.append(sp.solve(equation, x))


    elif option_difficulty == 3:
        if temp == 1:
            variables.clear()
            variable_values.clear()
            numerals.clear()
            #problemsets.clear()
            answerset.clear()
            variables.append(random.choice(choices))
            numerals.append(str(random.randint(15, 30)))
            numerals.append(str(random.randint(15, 30)))
            numerals.append(str(random.choice(negative)) +  str(random.randint(30, 60)))
                
            x = sp.symbols(str(variables[0]))
            
            output = '({} / {}) * {}'.format(str(numerals[0]), str(numerals[1]), str(variables[0]))
            other = '{}'.format(str(numerals[2]))
            equation  = sp.Eq(sp.sympify(output), sp.sympify(other))
            problemsets=(sp.latex(equation))
            answerset.append(sp.solve(equation, x))

        elif temp == 2:
            variables.clear()
            variable_values.clear()
            numerals.clear()
            #problemsets.clear()
            answerset.clear()
            variables.append(random.choice(choices))
            numerals.append(str(random.randint(15, 30)))
            numerals.append(str(random.randint(15, 30)))
            numerals.append(str(random.randint(15, 30)))
            numerals.append( str(random.randint(15, 30)))
                
            x = sp.symbols(str(variables[0]))
            
            output = '({} / {}) * {}'.format(str(numerals[0]), str(numerals[1]), str(variables[0]))
            other = '{} / {}'.format(str(numerals[2]), str(numerals[3]))
            equation  = sp.Eq(sp.sympify(output), sp.sympify(other))
            problemsets=(sp.latex(equation))
            answerset.append(sp.solve(equation, x))

    return(problemsets, answerset)