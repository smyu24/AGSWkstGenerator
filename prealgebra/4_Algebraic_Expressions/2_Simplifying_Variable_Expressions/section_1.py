# First Section (ANSWER GENERATION NEED WORK)
from math import *
import random

from sympy import sympify
import sympy as sp

def valid(input, variable):
    print(input[:input.find(variable)])
    if int(input[:input.find(variable)]) == 0:
        return(0)
    
    elif int(input[:input.find(variable)]) == 1:
        return(variable)
    elif int(input[:input.find(variable)]) == -1:
        return("-" + variable)
    else:
        print(input)
        input = input[:input.find(variable)] +  "*" + input[input.find(variable):]
        print(input)
        return(input)

def Simplifying_Variable_Expressions_1(option_difficulty, option_random):
    problemsets = []
    answerset = []
    temp = 0
    choices = ['x', 'y', 'a', 'b', 'z', 'p', 't', 'q', 'k', 'u', 'r', 'd', 'w', 's', 'h', 'v']
    all_expressions = ['+', '-', '*', '/']
    addition_expression = ['+', '-']
    mult_expression = ['*', '/']
    case = [1, 2, 3]#
    negative = ['-', '']
    temp = random.choice(case)
    sym_1 = ''
    sym_2 = ''
    sym_3 = ''
    sym_4 = ''
    variables = []
    variable_values = []
    numerals = []
    output = ''
    print('temp:',temp)

    if option_difficulty == "easy":
        if temp == 1:
            variables.append(random.choice(choices))
            
            variable_values.append(str(random.randint(2, 10)))
            variable_values.append(str(random.randint(2, 10)))

            sym_1 = random.choice(addition_expression)
            #one = valid(str(variable_values[0]) + str(variables[0]), variables[0])
            #two = valid(str(variable_values[1]) + str(variables[0]), variables[0])
            
            str_expr = '{}*{} {} {}*{}'.format(str(variable_values[0]), str(variables[0]), sym_1, str(variable_values[1]), str(variables[0]))
            expr = sympify(str_expr, evaluate=False)
            print(expr)
            problemsets.append(sp.latex(expr))
            answerset.append(sp.latex(sp.sympify(str_expr, evaluate=True)))
        
        elif temp == 2:
            variables.append(random.choice(choices)) # num2-10 variable  ±  variable  ±  num
            
            variable_values.append(str(random.randint(2, 10)))

            numerals.append(str(random.randint(1, 10)))

            sym_1 = random.choice(addition_expression)
            sym_2 = random.choice(addition_expression)

            str_expr = '{}*{} {} {} {} {}'.format(str(variable_values[0]), str(variables[0]), sym_1, str(variables[0]), sym_2, str(numerals[0]))
            expr = sympify(str_expr, evaluate=False)
            print(expr)
            problemsets.append(sp.latex(expr))
            answerset.append(sp.latex(sp.sympify(str_expr, evaluate=True)))
            

        elif temp == 3: # num2-10 variable  ±  num2-10variable  ±  num2-10variable
            variables.append(random.choice(choices))
            
            variable_values.append(str(random.randint(2, 10)))
            variable_values.append(str(random.randint(2, 10)))
            variable_values.append(str(random.randint(2, 10)))

            sym_1 = random.choice(addition_expression)
            sym_2 = random.choice(addition_expression)

            str_expr = '{}*{} {} {}*{} {} {}*{}'.format(str(variable_values[0]), str(variables[0]), sym_1, str(variable_values[1]), str(variables[0]), sym_2, str(variable_values[2]), str(variables[0]))
            expr = sympify(str_expr, evaluate=False)
            print(expr)
            problemsets.append(sp.latex(expr))
            answerset.append(sp.latex(sp.sympify(str_expr, evaluate=True)))
        
#---------------------------------------------------------------------------------------------------------
    elif option_difficulty == "medium": # TEMP ONE, TWO, AND THREE HAS ISSUE WITH PARA (SOLUTION IS EITHER ADD $$ OR SOMETHING ELSE)
        if temp == 1:
            variables.append(random.choice(choices)) #(num -10 to 10 variable  ±  num2-10variable ) + num2-10
            
            variable_values.append(str(random.choice(negative)) + str(random.randint(2, 10)))
            variable_values.append(str(random.randint(2, 10)))

            numerals.append(str(random.randint(1, 10)))

            sym_1 = random.choice(addition_expression)
            sym_2 = random.choice(addition_expression)

            str_expr = '({}*{} {} {}*{}) {} {}'.format(str(variable_values[0]), str(variables[0]), sym_1, str(variable_values[1]), str(variables[0]), sym_2, numerals[0])
            print(str_expr)
            expr = sympify(str_expr, evaluate=False)
            print(expr)
            output = expr
            print(output)
            problemsets.append(sp.latex(expr))
            answerset.append(sp.latex(sp.sympify(str_expr, evaluate=True)))
        
        elif temp == 2:
            variables.append(random.choice(choices)) #num2-10 variable  ±  num 2-10(variable  ±  num2-10)
            
            variable_values.append(str(random.randint(2, 10)))

            numerals.append(str(random.randint(2, 10)))
            numerals.append(str(random.randint(1, 10)))

            sym_1 = random.choice(addition_expression)
            sym_2 = random.choice(addition_expression)

            str_expr = '{}*{} {} {} * ({} {} {})'.format(str(variable_values[0]), str(variables[0]), sym_1, str(numerals[0]), str(variables[0]), sym_2, str(numerals[1]))
            print(str_expr)
            expr = sympify(str_expr, evaluate=False)
            print(expr)
            problemsets.append(sp.latex(expr))
            answerset.append(sp.latex(sp.sympify(str_expr, evaluate=True)))
        
        elif temp == 3:
            variables.append(random.choice(choices)) #num2-10 variable  ±  num 2-10(variable  ±  num)  ±  num2-10
            
            variable_values.append(str(random.randint(2, 10)))

            numerals.append(str(random.randint(2, 10)))
            numerals.append(str(random.randint(1, 10)))
            numerals.append(str(random.randint(1, 10)))

            sym_1 = random.choice(addition_expression)
            sym_2 = random.choice(addition_expression)
            sym_3 = random.choice(addition_expression)

            str_expr = '{}*{} {} {} * ({} {} {}) {} {}'.format(str(variable_values[0]), str(variables[0]), sym_1, str(numerals[0]), str(variables[0]), sym_2, str(numerals[1]), sym_3, str(numerals[2]))
            expr = sympify(str_expr, evaluate=False)
            print(expr)
            problemsets.append(sp.latex(expr))
            answerset.append(sp.latex(sp.sympify(str_expr, evaluate=True)))
            
    elif option_difficulty == "hard":
        if temp == 1: #num(-10 to 10) (variable  ±  variable )  ±  num(2 to 10) (variable  ±  NUM )
            variables.append(random.choice(choices)) # HERERERE

            variable_values.append(str(random.randint(2, 10)))
            variable_values.append(str(random.randint(2, 10)))

            numerals.append(str(random.choice(negative)) + str(random.randint(2, 10)))
            numerals.append(str(random.randint(2, 10)))
            numerals.append(str(random.randint(1, 10)))

            sym_1 = random.choice(addition_expression)
            sym_2 = random.choice(addition_expression)
            sym_3 = random.choice(addition_expression)

            str_expr = '{}*({}*{} {} {}) {} {}*({}*{} {} {})'.format(str(numerals[0]), str(variable_values[0]), str(variables[0]), sym_1, str(variables[0]), sym_2, str(numerals[1]), str(variable_values[1]), str(variables[0]), sym_3,  str(numerals[2]))
            expr = sympify(str_expr, evaluate=False)
            print(expr)
            problemsets.append(sp.latex(expr))
            answerset.append(sp.latex(sp.sympify(str_expr, evaluate=True)))
        elif temp == 2:
            variables.append(random.choice(choices))
            variables.append(random.choice(choices))

            variable_values.append(str(random.randint(2, 10)))
            variable_values.append(str(random.randint(2, 10)))
            variable_values.append(str(random.randint(2, 10)))

            numerals.append(str(random.choice(negative)) + str(random.randint(2, 10)))
            numerals.append(str(random.randint(1, 10)))

            sym_1 = random.choice(addition_expression)
            sym_2 = random.choice(addition_expression)
            sym_3 = random.choice(addition_expression)

            str_expr = '{}*({}*{} {} {}) {} {}*({}*{} {} {}*{})'.format(str(numerals[0]), str(variable_values[0]), str(variables[0]), sym_1, str(variables[1]), sym_2, str(numerals[1]), str(variable_values[1]), str(variables[1]), sym_3,  str(variable_values[2]), str(variables[0]))
            expr = sympify(str_expr, evaluate=False)
            print(expr)
            problemsets.append(sp.latex(expr))
            answerset.append(sp.latex(sp.sympify(str_expr, evaluate=True)))

        elif temp == 3:
            variables.append(random.choice(choices))
            variables.append(random.choice(choices))

            variable_values.append(str(random.randint(2, 10)))
            variable_values.append(str(random.randint(2, 10)))

            numerals.append(str(random.choice(negative)) + str(random.randint(2, 10)))
            numerals.append(str(random.randint(1, 10)))

            sym_1 = random.choice(addition_expression)
            sym_2 = random.choice(addition_expression)
            sym_3 = random.choice(addition_expression)

            str_expr = '{} * {} {} {}*({} {} {})'.format(variable_values[0], variables[0], sym_1, numerals[0], variables[1], sym_2, numerals[1])
            expr = sympify(str_expr, evaluate=False)
            print(expr)
            problemsets.append(sp.latex(expr))
            answerset.append(sp.latex(sp.sympify(str_expr, evaluate=True)))

    return(problemsets, answerset)

print("EASY!!!\n\n")
for i in range(20):
    a, b = Simplifying_Variable_Expressions_1("easy", False)
    print(a, b)

print("MEDIUM!!!\n\n")
for i in range(20):
    a, b = Simplifying_Variable_Expressions_1("medium", False)
    print(a, b)

print("HARD!!!\n\n")
for i in range(20):
    a, b = Simplifying_Variable_Expressions_1("hard", False)
    print(a, b)
