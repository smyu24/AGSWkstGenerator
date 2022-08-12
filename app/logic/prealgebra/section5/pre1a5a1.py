# First Section

import math
import random
import sympy as sp

def One_step_Equations_With_Integers_1(option_difficulty, option_random):
    problemsets = ""
    answerset = []
    choices = ['x', 'y', 'a', 'b', 'z', 'p', 't', 'q', 'k', 'u', 'r', 'd', 'w', 's', 'h', 'v']
    addition_expression = ['+', '-']
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
    unique = []
    holder = 0
    randomized = 0
    if option_difficulty == 1:
        if temp == 1:
            variables.append(random.choice(choices))
            sym_1 = random.choice(addition_expression)
            numerals.append(str(random.randint(2, 10)))
            numerals.append(str(random.choice(negative)) +  str(random.randint(1, 10)))

            x = sp.symbols(str(variables[0]))
            if random.randint(1,2) == 1:
                output = '{} {} {}'.format(str(variables[0]), sym_1, str(numerals[0]))
            else:
                output = '{} {} {}'.format(str(numerals[0]), sym_1, str(variables[0]))
            other = '{}'.format(str(numerals[1]))
            equation  = sp.Eq(sp.sympify(output), sp.sympify(other))

            problemsets = (sp.latex(equation))
            answerset.append(sp.solve(equation, x))

        elif temp == 2:
            while pass_loop == False:
                variables.clear()
                variable_values.clear()
                numerals.clear()
                #problemsets.clear()
                answerset.clear()
                variables.append(random.choice(choices))
                variable_values.append(str(random.choice(negative)) + str(random.randint(2,10)))
                for i in range(1, int(abs(int(variable_values[0])) / 2) + 1):
                    if int(abs(int(variable_values[0]))) % i == 0:
                        if i not in unique:
                            unique.append(i)
                        if int(abs(int(variable_values[0]))/i) not in unique:
                            unique.append(int(abs(int(variable_values[0])) / i))
                holder = random.choice(unique[1:])

                randomized = holder * random.randint(5, 10)
                if randomized % int(variable_values[0]) != 0:
                    randomized = randomized + (randomized % int(variable_values[0]))
                numerals.append(str(random.choice(negative)) + str(randomized))
                x = sp.symbols(str(variables[0]))

                output = '{}*{}'.format(str(variable_values[0]), str(variables[0]))
                other = '{}'.format(str(numerals[0]))
                equation  = sp.Eq(sp.sympify(output), sp.sympify(other))

                problemsets=(sp.latex(equation))
                answerset.append(sp.solve(equation, x))

                output = str(answerset[0])
                output = output.replace('[', '')
                output = output.replace(']', '')

                pass_loop = sp.sympify(output).is_integer

        elif temp == 3:
            variables.append(random.choice(choices))
            variable_values.append(str(random.choice(negative)) + str(random.randint(2,10)))
            numerals.append(str(random.choice(negative)) + str(random.randint(2,15)))
            x = sp.symbols(str(variables[0]))

            output = '{} / {}'.format(str(variables[0]), str(variable_values[0]))
            other = '{}'.format(str(numerals[0]))
            equation  = sp.Eq(sp.sympify(output), sp.sympify(other))

            problemsets=(sp.latex(equation))
            answerset.append(sp.solve(equation, x))

    elif option_difficulty == 2:
        if temp == 1:
            variables.append(random.choice(choices))
            sym_1 = random.choice(addition_expression)
            numerals.append(str(random.randint(2, 30)))
            numerals.append(str(random.choice(negative)) +  str(random.randint(1, 60)))

            x = sp.symbols(str(variables[0]))

            if random.randint(1,2) == 1:
                output = '{} {} {}'.format(str(variables[0]), sym_1, str(numerals[0]))
            else:
                output = '{} {} {}'.format(str(numerals[0]), sym_1, str(variables[0]))
            other = '{}'.format(str(numerals[1]))
            equation  = sp.Eq(sp.sympify(output), sp.sympify(other))

            problemsets=(sp.latex(equation))
            answerset.append(sp.solve(equation, x))

        elif temp == 2:
            while pass_loop == False:
                variables.clear()
                variable_values.clear()
                numerals.clear()
                #problemsets.clear()
                answerset.clear()
                variables.append(random.choice(choices))
                variable_values.append(str(random.choice(negative)) + str(random.randint(2,10)))
                for i in range(1, int(abs(int(variable_values[0])) / 2) + 1):
                    if int(abs(int(variable_values[0]))) % i == 0:
                        if i not in unique:
                            unique.append(i)
                        if int(abs(int(variable_values[0]))/i) not in unique:
                            unique.append(int(abs(int(variable_values[0])) / i))
                holder = random.choice(unique[1:])

                randomized = holder * random.randint(5, 15)
                if randomized % int(variable_values[0]) != 0:
                    randomized = randomized + (randomized % int(variable_values[0]))
                numerals.append(str(random.choice(negative)) + str(randomized))
                x = sp.symbols(str(variables[0]))

                output = '{}*{}'.format(str(variable_values[0]), str(variables[0]))
                other = '{}'.format(str(numerals[0]))
                equation  = sp.Eq(sp.sympify(output), sp.sympify(other))

                problemsets=(sp.latex(equation))
                answerset.append(sp.solve(equation, x))

                output = str(answerset[0])
                output = output.replace('[', '')
                output = output.replace(']', '')

                pass_loop = sp.sympify(output).is_integer

        elif temp == 3:
            variables.append(random.choice(choices))
            variable_values.append(str(random.choice(negative)) + str(random.randint(2,10)))
            numerals.append(str(random.choice(negative)) + str(random.randint(2,60)))
            x = sp.symbols(str(variables[0]))

            output = '{} / {}'.format(str(variables[0]), str(variable_values[0]))
            other = '{}'.format(str(numerals[0]))
            equation  = sp.Eq(sp.sympify(output), sp.sympify(other))

            problemsets=(sp.latex(equation))
            answerset.append(sp.solve(equation, x))

    elif option_difficulty == 3:
        if temp == 1:
            variables.append(random.choice(choices))
            sym_1 = random.choice(addition_expression)
            numerals.append(str(random.randint(2, 50)))
            numerals.append(str(random.choice(negative)) +  str(random.randint(1, 90)))

            x = sp.symbols(str(variables[0]))

            if random.randint(1,2) == 1:
                output = '{} {} {}'.format(str(variables[0]), sym_1, str(numerals[0]))
            else:
                output = '{} {} {}'.format(str(numerals[0]), sym_1, str(variables[0]))
            other = '{}'.format(str(numerals[1]))
            equation  = sp.Eq(sp.sympify(output), sp.sympify(other))

            problemsets=(sp.latex(equation))
            answerset.append(sp.solve(equation, x))

        elif temp == 2:
            while pass_loop == False:
                variables.clear()
                variable_values.clear()
                numerals.clear()
                #problemsets.clear()
                answerset.clear()
                variables.append(random.choice(choices))
                variable_values.append(str(random.choice(negative)) + str(random.randint(2,15)))
                for i in range(1, int(abs(int(variable_values[0])) / 2) + 1):
                    if int(abs(int(variable_values[0]))) % i == 0:
                        if i not in unique:
                            unique.append(i)
                        if int(abs(int(variable_values[0]))/i) not in unique:
                            unique.append(int(abs(int(variable_values[0])) / i))
                holder = random.choice(unique[1:])

                randomized = holder * random.randint(5, 20)
                if randomized % int(variable_values[0]) != 0:
                    randomized = randomized + (randomized % int(variable_values[0]))
                numerals.append(str(random.choice(negative)) + str(randomized))
                x = sp.symbols(str(variables[0]))

                output = '{}*{}'.format(str(variable_values[0]), str(variables[0]))
                other = '{}'.format(str(numerals[0]))
                equation  = sp.Eq(sp.sympify(output), sp.sympify(other))

                problemsets=(sp.latex(equation))
                answerset.append(sp.solve(equation, x))

                output = str(answerset[0])
                output = output.replace('[', '')
                output = output.replace(']', '')

                pass_loop = sp.sympify(output).is_integer

        elif temp == 3:
            variables.append(random.choice(choices))
            variable_values.append(str(random.choice(negative)) + str(random.randint(2,15)))
            numerals.append(str(random.choice(negative)) + str(random.randint(2,90)))
            x = sp.symbols(str(variables[0]))

            output = '{} / {}'.format(str(variables[0]), str(variable_values[0]))
            other = '{}'.format(str(numerals[0]))
            equation  = sp.Eq(sp.sympify(output), sp.sympify(other))

            problemsets=(sp.latex(equation))
            answerset.append(sp.solve(equation, x))

    return(problemsets, answerset)