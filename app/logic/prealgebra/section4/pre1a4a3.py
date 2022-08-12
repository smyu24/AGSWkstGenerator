# First Section (ANSWER GENERATION NEED WORK)
from math import *
import random

from sympy import sympify
import sympy as sp

def Distributive_Property_1(option_difficulty, option_random, localmin, localmax):
    problemsets = ""
    answerset = []
    temp = 0
    choices = ['x', 'y', 'a', 'b', 'z', 'p', 't', 'q', 'k', 'u', 'r', 'd', 'w', 's', 'h', 'v']
    all_expressions = ['+', '-', '*', '/']
    addition_expression = ['+', '-']
    mult_expression = ['*', '/']
    case = [1, 2, 3]#
    negative = ['-', '']
    #temp = random.choice(case)
    temp = 1
    sym_1 = ''
    sym_2 = ''
    sym_3 = ''
    sym_4 = ''
    variables = []
    variable_values = []
    numerals = []
    output = ''

    if option_difficulty == 1:
        if temp == 1:
            variables.append(random.choice(choices))

            numerals.append(str(random.randint(2,10)))
            numerals.append(str(random.randint(1,10)))

            sym_1 = random.choice(addition_expression)

            str_expr = '{}*({} {} {})'.format(str(numerals[0]), str(variables[0]), sym_1, str(numerals[1]))
            expr = sympify(str_expr, evaluate=False)
            problemsets = sp.latex(expr)
            answerset.append(sp.latex(sp.sympify(str_expr, evaluate=True)))
        
        elif temp == 2:
            variables.append(random.choice(choices)) 
            variables.append(random.choice(choices)) 
            
            variable_values.append(str(random.randint(2, 10)))

            numerals.append(str(random.randint(2,10)))

            sym_1 = random.choice(addition_expression)

            str_expr = '{}*({} {} {}*{})'.format(str(numerals[0]), str(variables[0]), sym_1, str(variable_values[0]), str(variables[1]))
            expr = sympify(str_expr, evaluate=False)
            problemsets = sp.latex(expr)
            answerset.append(sp.latex(sp.sympify(str_expr, evaluate=True)))
            

        elif temp == 3:
            variables.append(random.choice(choices)) 
            variables.append(random.choice(choices)) 
            
            variable_values.append(str(random.randint(2, 10)))
            variable_values.append(str(random.randint(2, 10)))

            numerals.append(str(random.randint(2,10)))

            sym_1 = random.choice(addition_expression)

            str_expr = '{}*({}*{} {} {}*{})'.format(str(numerals[0]), str(variable_values[0]), str(variables[0]), sym_1, str(variable_values[1]), str(variables[1]))
            expr = sympify(str_expr, evaluate=False)
            problemsets = sp.latex(expr)
            answerset.append(sp.latex(sp.sympify(str_expr, evaluate=True)))
        
    elif option_difficulty == 2:
        if temp == 1:
            variables.append(random.choice(choices)) 
            
            variable_values.append(str(random.randint(2, 10)))

            numerals.append(str(random.choice(negative)) + str(random.randint(2,10)))
            numerals.append(str(random.randint(1,10)))

            sym_1 = random.choice(addition_expression)

            str_expr = '{}*({}*{} {} {})'.format(str(numerals[0]), str(variable_values[0]), str(variables[0]), sym_1, str(numerals[1]))
            expr = sympify(str_expr, evaluate=False)
            problemsets = sp.latex(expr)
            answerset.append(sp.latex(sp.sympify(str_expr, evaluate=True)))
        
        elif temp == 2:
            variables.append(random.choice(choices)) 
            variables.append(random.choice(choices)) 
            
            variable_values.append(str(random.randint(2, 10)))
            variable_values.append(str(random.randint(2, 10)))

            numerals.append(str(random.choice(negative)) + str(random.randint(2,10)))

            sym_1 = random.choice(addition_expression)

            str_expr = '{}*({}*{} {} {}*{})'.format(str(numerals[0]), str(variable_values[0]), str(variables[0]), sym_1, str(variable_values[1]), str(variables[1]))
            expr = sympify(str_expr, evaluate=False)
            problemsets = sp.latex(expr)
            answerset.append(sp.latex(sp.sympify(str_expr, evaluate=True)))
        
        elif temp == 3: 
            variables.append(random.choice(choices)) 
            variables.append(random.choice(choices)) 

            numerals.append(str(random.choice(negative)) + str(random.randint(2,10)))

            sym_1 = random.choice(addition_expression)

            str_expr = '{}*({} {} {})'.format(str(numerals[0]), str(variables[0]), sym_1, str(variables[1]))
            expr = sympify(str_expr, evaluate=False)
            problemsets = sp.latex(expr)
            answerset.append(sp.latex(sp.sympify(str_expr, evaluate=True)))
            
    elif option_difficulty == 3:
        if temp == 1:
            variables.append(random.choice(choices)) 
            variables.append(random.choice(choices)) 
            
            variable_values.append(str(random.randint(2, 20)))
            variable_values.append(str(random.randint(2, 20)))

            numerals.append(str(random.choice(negative)) + str(random.randint(10,20)))

            sym_1 = random.choice(addition_expression)

            str_expr = '{}*({}*{} {} {}*{})'.format(str(numerals[0]), str(variable_values[0]), str(variables[0]), sym_1, str(variable_values[1]), str(variables[1]))
            expr = sympify(str_expr, evaluate=False)
            problemsets = sp.latex(expr)
            answerset.append(sp.latex(sp.sympify(str_expr, evaluate=True)))

        elif temp == 2:#var var num
            variables.append(random.choice(choices)) 
            variables.append(random.choice(choices)) 
            
            variable_values.append(str(random.choice(negative)) + str(random.randint(2, 10)))
            variable_values.append(str(random.randint(2, 20)))

            numerals.append(str(random.choice(negative)) + str(random.randint(10,20)))
            numerals.append(str(random.randint(2,20)))

            sym_1 = random.choice(addition_expression)
            sym_2 = random.choice(addition_expression)

            str_expr = '{}*({}*{} {} {}*{} {} {})'.format(str(numerals[0]), str(variable_values[0]), str(variables[0]), sym_1, str(variable_values[1]), str(variables[1]), sym_2, numerals[1])
            expr = sympify(str_expr, evaluate=False)
            problemsets = sp.latex(expr)
            answerset.append(sp.latex(sp.sympify(str_expr, evaluate=True)))

        elif temp == 3:
            variables.append(random.choice(choices)) 
            variables.append(random.choice(choices)) 
            variables.append(random.choice(choices)) 
            
            variable_values.append(str(random.choice(negative)) + str(random.randint(2, 10)))
            variable_values.append(str(random.randint(2, 20)))
            variable_values.append(str(random.randint(2, 20)))

            numerals.append(str(random.choice(negative)) + str(random.randint(10,20)))

            sym_1 = random.choice(addition_expression)
            sym_2 = random.choice(addition_expression)

            str_expr = '{}*({}*{} {} {}*{} {} {}*{})'.format(str(numerals[0]), str(variable_values[0]), str(variables[0]), sym_1, str(variable_values[1]), str(variables[1]), sym_2, str(variable_values[2]), str(variables[2]))
            expr = sympify(str_expr, evaluate=False)
            problemsets = sp.latex(expr)
            answerset.append(sp.latex(sp.sympify(str_expr, evaluate=True)))

    return(problemsets, answerset)