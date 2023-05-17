import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from loader import LinFunc, Rational, startGraph, drawLinear, endGraph, ExpFunc, x, latex, sympify, emptyGraph, drawCurve
import sympy as sp; import random
"""
AGS1.4.2.3 - Solve For The Variable.
Option 1: Easy
instruction : Solve for the indicated variable. Show your work!
"""

"""
This section generates equations and solves them. 
  Return Parameters: 
      Question Prompt e.g "Solve for x"
      Problem question(in latex friendly format) e.g "\frac{x}{5} = 6" 
      Answer(also in latex friendly format) e.g "x = 30"

Some of the cases could be optimized using reduce or map
This applies to all easy, medium, hard (1.4.2.3)
"""
def equation_packager(output, other, x):
    equation= sp.Eq(sp.sympify(output), sp.sympify(other))
    return sp.latex(equation), sp.solve(equation, x)
def answer_packager(x, answerset):
    return sp.latex(sp.Eq(sp.sympify(x), sp.sympify(answerset[0])))
def q_prompt(x):
    return fr"Solve for ${x}$"

def One_step_Equations_With_Integers_1(option_difficulty):
    problemsets = ""
    answerset = ""
    choices = ['x', 'y', 'a', 'b', 'z', 'p', 't', 'q', 'k', 'u', 'r', 'd', 'w', 's', 'h', 'v']
    addition_expression = ['+', '-']
    negative = ['-', '']
    temp = random.choice([1, 2, 3])
    variables = []
    variable_values = []
    numerals = []
    pass_loop = False
    unique = []
    if temp == 1: 
        variables.append(random.choice(choices))
        sym_1 = random.choice(addition_expression)
        numerals.append(str(random.randint(2, 10))) if option_difficulty=="easy" else (numerals.append(str(random.randint(2, 30))) if option_difficulty=="medium" else numerals.append(str(random.randint(20, 50))))
        numerals.append(str(random.choice(negative))+str(random.randint(1, 10))) if option_difficulty=="easy" else (numerals.append(str(random.choice(negative))+str(random.randint(1, 60))) if option_difficulty=="medium" else numerals.append(str(random.choice(negative))+str(random.randint(20, 90))))
        x = sp.symbols(str(variables[0]))
        output = '{} {} {}'.format(str(variables[0]), sym_1, str(numerals[0])) if random.randint(1,2) == 1 else '{} {} {}'.format(str(numerals[0]), sym_1, str(variables[0]))
        other = '{}'.format(str(numerals[1]))
        problemsets, answerset = equation_packager(output, other, x)

    elif temp == 2:
        while pass_loop == False:
            variables.clear()
            variable_values.clear()
            numerals.clear()
            variables.append(random.choice(choices))
            variable_values.append(str(random.choice(negative)) + str(random.randint(2,10))) if option_difficulty=="easy" or option_difficulty=="medium" else variable_values.append(str(random.choice(negative)) + str(random.randint(5,15)))
            for i in range(1, int(abs(int(variable_values[0])) / 2) + 1):
                if int(abs(int(variable_values[0]))) % i == 0:
                    if i not in unique:
                        unique.append(i)
                    if int(abs(int(variable_values[0]))/i) not in unique:
                        unique.append(int(abs(int(variable_values[0])) / i))
            holder = random.choice(unique[1:])
            randomized = holder * random.randint(5, 10) if option_difficulty=="easy" else (holder * random.randint(5, 15) if option_difficulty=="medium" else holder * random.randint(10, 20))
            if randomized % int(variable_values[0]) != 0:
                randomized = randomized + (randomized % int(variable_values[0]))
            numerals.append(str(random.choice(negative)) + str(randomized))
            x = sp.symbols(str(variables[0]))
            output, other = '{}*{}'.format(str(variable_values[0]), str(variables[0])), '{}'.format(str(numerals[0]))
            problemsets, answerset = equation_packager(output, other, x)
            output = str(answerset)
            output = output.replace('[', ''); output = output.replace(']', '')
            pass_loop = sp.sympify(output).is_integer

    elif temp == 3:
        variables.append(random.choice(choices))
        variable_values.append(str(random.choice(negative))+str(random.randint(2,10))) if option_difficulty=="easy" or option_difficulty=="medium" else variable_values.append(str(random.choice(negative))+str(random.randint(5,15)))
        numerals.append(str(random.choice(negative))+str(random.randint(2,15))) if option_difficulty=="easy" else (numerals.append(str(random.choice(negative))+str(random.randint(2,60))) if option_difficulty=="medium" else numerals.append(str(random.choice(negative))+str(random.randint(20,90))))
        x = sp.symbols(str(variables[0]))
        output, other = '{} / {}'.format(str(variables[0]), str(variable_values[0])), '{}'.format(str(numerals[0]))
        problemsets, answerset = equation_packager(output, other, x)
    
    return(q_prompt(x), problemsets, answer_packager(x, answerset))

def Two_step_Equations_With_Integers_1(option_difficulty = 'easy'):
    problemsets = ""
    answerset = ""
    choices = ['x', 'y', 'a', 'b', 'z', 'p', 't', 'q', 'k', 'u', 'r', 'd', 'w', 's', 'h', 'v']
    addition_expression = ['+', '-']
    negative = ['-', '']
    temp = random.choice([1, 2])
    variables = []
    variable_values = []
    numerals = []
    pass_loop = False
    if option_difficulty == "easy":
        if temp == 1:
            while pass_loop == False:
                variables.clear()
                variable_values.clear()
                numerals.clear()
                variables.append(random.choice(choices))
                sym_1 = random.choice(addition_expression)
                numerals.append(str(random.randint(2, 10)))
                numerals.append(str(random.choice(negative)) + str(random.randint(1, 10)))
                numerals.append(str(random.choice(negative)) + str(random.randint(2, 10)))
                x = sp.symbols(str(variables[0]))
                output = '{}*{} {} {}'.format(str(numerals[2]), str(variables[0]), sym_1, str(numerals[0])) if random.randint(1,2) == 1 else '{} {} {}*{}'.format(str(numerals[0]), sym_1, str(numerals[2]), str(variables[0]))
                other = '{}'.format(str(numerals[1]))
                equation = sp.Eq(sp.sympify(output), sp.sympify(other))
                problemsets= sp.latex(equation)
                answerset= sp.solve(equation, x)
                pass_loop = sp.sympify(sp.solve(equation, x).pop(0)).is_integer

        elif temp == 2:
            variables.append(random.choice(choices))
            variable_values.append(str(random.choice(negative)) + str(random.randint(2,10)))
            numerals.append(str(random.choice(negative)) + str(random.randint(2,15)))
            numerals.append(str(random.randint(2,15)))
            sym_1 = random.choice(addition_expression)
            x = sp.symbols(str(variables[0]))
            output, other = '{} / {} {} {}'.format(str(variables[0]), str(variable_values[0]), sym_1, str(numerals[1])), '{}'.format(str(numerals[0]))
            problemsets, answerset = equation_packager(output, other, x)

    elif option_difficulty == "medium":
        if temp == 1:
            variables.clear()
            variable_values.clear()
            numerals.clear()
            variables.append(random.choice(choices))
            numerals.append(str(random.randint(2, 20)))
            numerals.append(str(random.randint(2, 20)))
            numerals.append(str(random.choice(negative)) +  str(random.randint(1, 40)))
            x = sp.symbols(str(variables[0]))
            output, other = '({} / {}) * {}'.format(str(numerals[0]), str(numerals[1]), str(variables[0])), '{}'.format(str(numerals[2]))
            problemsets, answerset = equation_packager(output, other, x)

        elif temp == 2:
            variables.clear()
            variable_values.clear()
            numerals.clear()
            variables.append(random.choice(choices))
            numerals.append(str(random.randint(2, 20)))
            numerals.append(str(random.randint(2, 20)))
            numerals.append(str(random.randint(1, 30)))
            numerals.append( str(random.randint(2, 30)))
            x = sp.symbols(str(variables[0]))
            output, other = '({} / {}) * {}'.format(str(numerals[0]), str(numerals[1]), str(variables[0])), '{} / {}'.format(str(numerals[2]), str(numerals[3]))
            problemsets, answerset = equation_packager(output, other, x)


    elif option_difficulty == "hard":
        if temp == 1:
            variables.clear()
            variable_values.clear()
            numerals.clear()
            variables.append(random.choice(choices))
            numerals.append(str(random.randint(15, 30)))
            numerals.append(str(random.randint(15, 30)))
            numerals.append(str(random.choice(negative)) + str(random.randint(30, 60)))
            x = sp.symbols(str(variables[0]))
            output, other = '({} / {}) * {}'.format(str(numerals[0]), str(numerals[1]), str(variables[0])), '{}'.format(str(numerals[2]))
            problemsets, answerset = equation_packager(output, other, x)

        elif temp == 2:
            variables.clear()
            variable_values.clear()
            numerals.clear()
            variables.append(random.choice(choices))
            numerals.append(str(random.randint(15, 30)))
            numerals.append(str(random.randint(15, 30)))
            numerals.append(str(random.randint(15, 30)))
            numerals.append(str(random.randint(15, 30)))
            x = sp.symbols(str(variables[0]))
            output, other = '({} / {}) * {}'.format(str(numerals[0]), str(numerals[1]), str(variables[0])), '{} / {}'.format(str(numerals[2]), str(numerals[3]))
            problemsets, answerset = equation_packager(output, other, x)
    return(q_prompt(x), problemsets, answer_packager(x, answerset))

def additional_eq():
    case= random.randint(1,4)
    choices = ['x', 'y', 'a', 'b', 'z', 'p', 't', 'q', 'k', 'u', 'r', 'd', 'w', 's', 'h', 'v']
    addition_expression = ['+', '-']
    negative = ['-', '']
    problemsets = ""
    answerset = ""
    numerals = []
    if case == 1:
        var1= random.choice(choices)
        var2= random.choice(choices)
        while var2 in var1:
            var2= random.choice(choices)
        sym_1= random.choice(addition_expression)
        x= sp.symbols(str(var2))
        numerals.append(random.choice(negative)+str(random.randint(1, 15)))
        numerals.append(str(random.randint(0, 15)))
        output= "{}".format(var1)
        other= "{}*{} {} {}".format(numerals[0], var2, sym_1, numerals[1]) if numerals[1] != 0 else "{}*{}".format(numerals[0], var2)
        problemsets, answerset = equation_packager(output, other, x)

    elif case == 2:
        var1= random.choice(choices)
        var2= random.choice(choices)
        while var2 in var1:
            var2= random.choice(choices)
        var3= random.choice(choices)
        while var3 in var1 or var3 in var2:
            var3= random.choice(choices)
        sym_1= random.choice(addition_expression)
        x= sp.symbols(str(var2))
        numerals.append(str(random.randint(0, 15)))
        output= "{}".format(var1)
        other= "{}*{} {} {}".format(var2, var3, sym_1, numerals[0]) if numerals[0] != 0 else "{}*{}".format(var2, var3)
        problemsets, answerset = equation_packager(output, other, x)

    elif case == 3:
        var1= random.choice(choices)
        sym_1= random.choice(addition_expression)
        x= sp.symbols(str(var1))
        numerals.append(str(random.randint(0, 15)))
        numerals.append(random.choice(negative)+str(random.randint(1, 15)))
        numerals.append(random.choice(negative)+str(random.randint(0, 15)))
        output= '({} {} {}) / ({})'.format(var1, sym_1, numerals[0], numerals[1]) if numerals[0] != 0 else '({}) / ({})'.format(var1, numerals[1])
        other= "{}".format(numerals[2])
        problemsets, answerset = equation_packager(output, other, x)

    elif case == 4:
        var1= random.choice(choices)
        var2= random.choice(choices)
        while var2 in var1:
            var2= random.choice(choices)
        sym_1= random.choice(addition_expression)
        x= sp.symbols(str(var1))
        numerals.append(str(random.randint(1, 15)))
        numerals.append(random.choice(negative)+str(random.randint(1, 15)))
        numerals.append(random.choice(negative)+str(random.randint(0, 15)))
        output= '({} {} {}*{}) / ({})'.format(var1, sym_1, numerals[0], var2, numerals[1])
        other= "{}".format(numerals[2])
        problemsets, answerset = equation_packager(output, other, x)

    return q_prompt(x), problemsets, answer_packager(x, answerset)

# for i in range(10):
#     prompt, problem, answer = random.choice([additional_eq(),One_step_Equations_With_Integers_1(random.choice(["easy", "medium", "hard"])), Two_step_Equations_With_Integers_1(random.choice(["easy", "medium", "hard"]))])
#     print(prompt, " - - - - - ", problem, " - - - - - ",answer)



"""
Option 2: Medium
instruction : Solve for the indicated variable. Show your work!
"""

import sympy as sp; import random

def equation_packager(output, other, x):
    equation= sp.Eq(sp.sympify(output), sp.sympify(other))
    return sp.latex(equation), sp.solve(equation, x)
def answer_packager(x, answerset):
    return sp.latex(sp.Eq(sp.sympify(x), sp.sympify(answerset[0])))
def q_prompt(x):
    return fr"Solve for ${x}$"

def additional_eq_medium():
    case= random.randint(1,4)
    choices = ['x', 'y', 'a', 'b', 'z', 'p', 't', 'q', 'k', 'u', 'r', 'd', 'w', 's', 'h', 'v']
    addition_expression = ['+', '-']
    negative = ['-', '']
    problemsets = ""
    answerset = ""
    numerals = []
    if case == 1:
        var1= random.choice(choices)
        var2= random.choice(choices)
        while var2 in var1:
            var2= random.choice(choices)
        var3= random.choice(choices)
        while var3 in var1 or var3 in var2:
            var3= random.choice(choices)
        var4= random.choice(choices)
        while var4 in var1 or var4 in var2 or var4 in var3:
            var4= random.choice(choices)
        sym_1= random.choice(addition_expression)
        x= sp.symbols(str(var1))
        numerals.append(random.choice(negative)+str(random.randint(1, 15)))
        output= "{} * ({} {} {})".format(var1, var2, sym_1, var3)
        other= "({}*{}) / ({})".format(numerals[0], var4, var2)
        problemsets, answerset = equation_packager(output, other, x)

    elif case == 2:
        var1= random.choice(choices)
        var2= random.choice(choices)
        while var2 in var1:
            var2= random.choice(choices)
        var3= random.choice(choices)
        while var3 in var1 or var3 in var2:
            var3= random.choice(choices)
        var4= random.choice(choices)
        while var4 in var1 or var4 in var2 or var4 in var3:
            var4= random.choice(choices)
        sym_1= random.choice(addition_expression)
        x= sp.symbols(str(var3))
        numerals.append(str(random.randint(1, 15)))
        output= "{} * ({} {} {} * {})".format(var1, var2, sym_1, numerals[0], var3)
        other= "({}) / ({})".format(var4, var2)
        problemsets, answerset = equation_packager(output, other, x)        

    elif case == 3:
        var1= random.choice(choices)
        var2= random.choice(choices)
        while var2 in var1:
            var2= random.choice(choices)
        sym_1= random.choice(addition_expression)
        x= sp.symbols(str(var1))
        numerals.append(random.choice(negative)+str(random.randint(1, 15)))
        numerals.append(str(random.randint(1, 15)))
        numerals.append(str(random.randint(0, 15)))
        numerals.append(str(random.randint(0, 15)))
        output= "({} * {}) / ({}) {} {}".format(numerals[0], var1, numerals[1], sym_1, numerals[2])
        other= "{}".format(numerals[3])
        problemsets, answerset = equation_packager(output, other, x)  

    elif case == 4:
        var1= random.choice(choices)
        var2= random.choice(choices)
        while var2 in var1:
            var2= random.choice(choices)
        sym_1= random.choice(addition_expression)
        x= sp.symbols(str(var1))
        numerals.append(random.choice(negative)+str(random.randint(1, 15)))
        numerals.append(str(random.randint(1, 15)))
        numerals.append(str(random.randint(0, 15)))
        numerals.append(str(random.randint(1, 15)))
        output= "({} * {}) / ({}) {} {} * {}".format(numerals[0], var1, numerals[1], sym_1, numerals[2], var2)
        other= "{}".format(numerals[3])
        problemsets, answerset = equation_packager(output, other, x)  

    return q_prompt(x), problemsets, answer_packager(x, answerset)

# for i in range(20):
#     prompt, problem, solution= additional_eq_medium()
#     print(prompt, " - - - - - ", problem, " - - - - - ", solution)


"""
Option 3: Hard
instruction : Solve for the indicated variable. Show your work!
"""

import sympy as sp; import random

def equation_packager(output, other, x):
    equation= sp.Eq(sp.sympify(output), sp.sympify(other))
    return sp.latex(equation), sp.solve(equation, x)
def answer_packager(x, answerset):
    return sp.latex(sp.Eq(sp.sympify(x), sp.sympify(answerset[0])))
def q_prompt(x):
    return fr"Solve for ${x}$"

def additional_eq_hard():
    case= random.randint(1,3)
    choices = ['x', 'y', 'a', 'b', 'z', 'p', 't', 'q', 'k', 'u', 'r', 'd', 'w', 's', 'h', 'v']
    addition_expression = ['+', '-']
    negative = ['-', '']
    problemsets = ""
    answerset = ""
    numerals = []
    if case == 1:
        var1= random.choice(choices)
        sym_1= random.choice(addition_expression)
        x= sp.symbols(str(var1))
        numerals.append(random.choice(negative)+str(random.randint(1, 15)))
        numerals.append(str(random.randint(1, 15)))
        numerals.append(random.choice(negative)+str(random.randint(1, 15)))
        numerals.append(str(random.randint(1, 15)))
        numerals.append(str(random.randint(1, 15)))
        numerals.append(str(random.randint(0, 15)))
        output= "({})/({}) * (({}*{})/({}) {} {})".format(numerals[0], numerals[1], numerals[2], var1, numerals[3], sym_1, numerals[4])
        other= "{}".format(numerals[5])
        problemsets, answerset = equation_packager(output, other, x)

    elif case == 2 or case == 3:
        var1= random.choice(choices)
        var2= random.choice(choices)
        while var2 in var1:
            var2= random.choice(choices)
        sym_1= random.choice(addition_expression)
        x= sp.symbols(str(var2)) if case == 2 else sp.symbols(str(var1))
        numerals.append(random.choice(negative)+str(random.randint(1, 15)))
        numerals.append(str(random.randint(1, 15)))
        numerals.append(random.choice(negative)+str(random.randint(1, 15)))
        numerals.append(str(random.randint(1, 15)))
        numerals.append(str(random.randint(0, 15)))
        output= "({})/({}) * (({}*{})/({}) {} {})".format(numerals[0], numerals[1], numerals[2], var1, numerals[3], sym_1, var2)
        other= "{}".format(numerals[4])
        problemsets, answerset = equation_packager(output, other, x)        
    
    return q_prompt(x), problemsets, answer_packager(x, answerset)

# for i in range(20):
#     prompt, problem, solution= additional_eq_hard()
#     print(prompt, " - - - - - ", problem, " - - - - - ", solution)