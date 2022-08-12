# First Section (ANSWER GENERATION NEED WORK)
from math import *
import random

from sympy import sympify, latex, symbols
import sympy as sp

def variable_and_variable_value(min, max, num_of_vars, variables, variable_values, choices):
    var_holder = ''
    while len(variables) != num_of_vars:
        var_holder = random.choice(choices)
        if var_holder not in variables: 
            variables.append(str(var_holder))
            variable_values.append(str(random.randint(min, max)))
    return(random.sample(variables, len(variables)), random.sample(variable_values, len(variable_values)))

def variable_repeat_sorter(variables):
    random_var_pick = []
    for i in range(len(variables)):
        random_var_pick.append(random.choice(variables))
    return(random_var_pick)

def Evaluating_Variable_Expressions_1(option_difficulty = 0, expr = "latex"):
    problemsets = []
    answerset = []
    temp = 0
    choices = ['x', 'y', 'a', 'b', 'z', 'p', 't', 'q', 'k', 'u', 'r', 'd', 'w', 's', 'h', 'v']
    variables = []
    all_expressions = ['+', '-', '*', '/']
    addition_expression = ['+', '-']
    mult_expression = ['*', '/']
    case = [1, 2, 3, 4]#
    negative = ['-', '']
    temp = random.choice(case)
    filler = ''
    sym_1 = ''
    sym_2 = ''
    sym_3 = ''
    sym_4 = ''
    indexes = []
    variable_values = []
    output = ''
    pass_loop = False
    x = "" 

    while pass_loop != True:
      if option_difficulty == 1: #(NUM range from 1~10)
          if temp == 1:
              variable_and_variable_value(1, 10, 2, variables, variable_values, choices)
              variables = variable_repeat_sorter(variables)
              vars_found = []
              equation = ''
         
              indexes.append(variables[0])
              indexes.append(variables[1])
              indexes.append(str(random.randint(2, 10)))
              random.shuffle(indexes)
 

              sym_1 = str(random.choice(addition_expression))
              sym_2 = str(random.choice(mult_expression))
              output = sympify(indexes[0] + sym_1 + indexes[1] + sym_2 + indexes[2])
          
              output = str(output)
              equation = output
              for i in range(len(variables)):
                  if output.find(variables[i]) != -1:
                      output = output.replace(variables[i], variable_values[i])
                      vars_found.append(i)
              random.shuffle(vars_found)
              answerset.append(sympify(output))
              if len(vars_found) == 1:
                  problemsets.append('Given that ' + variables[vars_found[0]] + ' = ' + variable_values[vars_found[0]])
              elif len(vars_found) == 2:
                  problemsets.append('Given that ' + variables[vars_found[0]] + ' = ' + variable_values[vars_found[0]] + ', and ' + variables[vars_found[1]] + ' = '+ variable_values[vars_found[1]])
              problemsets.append(equation)

          elif temp == 2:
              variable_and_variable_value(1, 10, 1, variables, variable_values, choices)
              vars_found = []
              equation = ''
            
              indexes.append(variables[0])
              indexes.append(str(random.randint(2, 10)))
              indexes.append(str(random.randint(2, 10)))
              random.shuffle(indexes)
              
              sym_1 = str(random.choice(addition_expression))
              sym_2 = str(random.choice(mult_expression))
              output = '({} {} {}) {} {}'.format(indexes[0], sym_1, indexes[1], sym_2, indexes[2])
              equation = output
              
              equation = output
              for i in range(len(variables)):
                  if output.find(variables[i]) != -1:
                      output = output.replace(variables[i], variable_values[i])
                      vars_found.append(i)
              random.shuffle(vars_found)
              answerset.append(sympify(output))

              problemsets.append('Given that ' + variables[vars_found[0]] + ' = ' + variable_values[vars_found[0]])
              problemsets.append(equation)

          
          elif temp == 3:
              variable_and_variable_value(1, 10, 2, variables, variable_values, choices)
              variables = variable_repeat_sorter(variables)
              vars_found = []
              equation = ''
              
              indexes.append(variables[0])
              indexes.append(variables[1])
              indexes.append(str(random.randint(2, 10)))
              random.shuffle(indexes)

              sym_1 = str(random.choice(addition_expression))
              sym_2 = str(random.choice(addition_expression))
              output = sympify(indexes[0] + sym_1 + indexes[1] + sym_2 + indexes[2])
            
              output = str(output)
              equation = output
              for i in range(len(variables)):
                  if output.find(variables[i]) != -1:
                      output = output.replace(variables[i], variable_values[i])
                      vars_found.append(i)
              random.shuffle(vars_found)
              answerset.append(sympify(output))
              if len(vars_found) == 1:
                  problemsets.append('Given that ' + variables[vars_found[0]] + ' = ' + variable_values[vars_found[0]])
              elif len(vars_found) == 2:
                  problemsets.append('Given that ' + variables[vars_found[0]] + ' = ' + variable_values[vars_found[0]] + ', and ' + variables[vars_found[1]] + ' = '+ variable_values[vars_found[1]])
              elif len(vars_found) == 3:
                  problemsets.append('Given that ' + variables[vars_found[0]] + ' = ' + variable_values[vars_found[0]] + ', ' + variables[vars_found[1]] + ' = '+ variable_values[vars_found[1]] + ', and ' + variables[vars_found[2]] + ' = '+ variable_values[vars_found[2]])
              problemsets.append(equation)

          elif temp == 4:
              variable_and_variable_value(1, 10, 2, variables, variable_values, choices)
              variables = variable_repeat_sorter(variables)
              vars_found = []
              equation = ''
              
              indexes.append(variables[0])
              indexes.append(variables[1])
              indexes.append(str(random.randint(2, 10)))
              indexes.append(str(random.randint(2, 10)))
              random.shuffle(indexes)

              sym_1 = str(random.choice(addition_expression))
              sym_2 = str(random.choice(addition_expression))
              output = sympify(indexes[0] + "*" + indexes[1] + sym_1 + indexes[2] + sym_2 + indexes[3])
            
              output = str(output)
              equation = output
              for i in range(len(variables)):
                  if output.find(variables[i]) != -1:
                      output = output.replace(variables[i], variable_values[i])
                      vars_found.append(i)
              random.shuffle(vars_found)
              answerset.append(sympify(output))
              if len(vars_found) == 1:
                  problemsets.append('Given that ' + variables[vars_found[0]] + ' = ' + variable_values[vars_found[0]])
              elif len(vars_found) == 2:
                  problemsets.append('Given that ' + variables[vars_found[0]] + ' = ' + variable_values[vars_found[0]] + ', and ' + variables[vars_found[1]] + ' = '+ variable_values[vars_found[1]])
              problemsets.append(equation)
              
  #---------------------------------------------------------------------------------------------------------
      elif option_difficulty == 2: #(NUM range from 1~15)
          if temp == 1:
              variable_and_variable_value(1, 15, 2, variables, variable_values, choices)
              variables = variable_repeat_sorter(variables)
              vars_found = []
              equation = ''
        
              indexes.append(variables[0])
              indexes.append(variables[1])
              indexes.append(str(random.randint(2, 10)))
              random.shuffle(indexes)

              sym_1 = str(random.choice(addition_expression))
              sym_2 = str(random.choice(mult_expression))
              output = '({} {} {}) ** {} {} {}'.format(indexes[0], sym_1, indexes[1], str(2), sym_2, indexes[2])

              filler = sympify(output, evaluate=False)
          
              for i in range(len(variables)):
                  if output.find(variables[i]) != -1:
                      output = output.replace(variables[i], variable_values[i])
                      vars_found.append(i)
              random.shuffle(vars_found)
              answerset.append(sympify(output))
              if len(vars_found) == 1:
                  problemsets.append('Given that ' + variables[vars_found[0]] + ' = ' + variable_values[vars_found[0]])
              elif len(vars_found) == 2:
                  problemsets.append('Given that ' + variables[vars_found[0]] + ' = ' + variable_values[vars_found[0]] + ', and ' + variables[vars_found[1]] + ' = '+ variable_values[vars_found[1]])
              problemsets.append(filler)

          elif temp == 2:
              variable_and_variable_value(1, 15, 3, variables, variable_values, choices)
              variables = variable_repeat_sorter(variables)
              vars_found = []
              equation = ''

              indexes.append(variables[0])
              indexes.append(variables[1])
              indexes.append(variables[2])
              indexes.append(str(random.randint(2, 10)))
              random.shuffle(indexes)

              sym_1 = str(random.choice(mult_expression))
              sym_2 = str(random.choice(addition_expression))
              sym_3 = str(random.choice(all_expressions))
              output = '(({} {} {}) {} {}) {} {}'.format(indexes[0], sym_1, indexes[1], sym_2, indexes[2], sym_3, indexes[3])
              filler = sympify(output, evaluate=False)
            
              for i in range(len(variables)):
                  if output.find(variables[i]) != -1:
                      output = output.replace(variables[i], variable_values[i])
                      vars_found.append(i)
              random.shuffle(vars_found)
              answerset.append(sympify(output))
              if len(vars_found) == 1:
                  problemsets.append('Given that ' + variables[vars_found[0]] + ' = ' + variable_values[vars_found[0]])
              elif len(vars_found) == 2:
                  problemsets.append('Given that ' + variables[vars_found[0]] + ' = ' + variable_values[vars_found[0]] + ', and ' + variables[vars_found[1]] + ' = '+ variable_values[vars_found[1]])
              elif len(vars_found) == 3:
                  problemsets.append('Given that ' + variables[vars_found[0]] + ' = ' + variable_values[vars_found[0]] + ', ' + variables[vars_found[1]] + ' = '+ variable_values[vars_found[1]] + ', and ' + variables[vars_found[2]] + ' = '+ variable_values[vars_found[2]])
              problemsets.append(filler)
          
          elif temp == 3:
              variable_and_variable_value(1, 15, 3, variables, variable_values, choices)
              variables = variable_repeat_sorter(variables)
              vars_found = []
              equation = ''
 
              indexes.append(variables[0])
              indexes.append(variables[1])
              indexes.append(variables[2])
              indexes.append(str(random.randint(2, 10)))
              random.shuffle(indexes)

              sym_1 = str(random.choice(addition_expression))
              sym_2 = str(random.choice(addition_expression))
              sym_3 = str(random.choice(all_expressions))
              output = '(({} ** {} {} {}) {} {}) {} {}'.format(indexes[0], str(random.randint(2, 4)), sym_1, indexes[1], sym_2, indexes[2], sym_3, indexes[3])
              filler = sympify(output, evaluate=False)
      
            
              for i in range(len(variables)):
                  if output.find(variables[i]) != -1:
                      output = output.replace(variables[i], variable_values[i])
                      vars_found.append(i)
              random.shuffle(vars_found)

              answerset.append(sympify(output))
              if len(vars_found) == 1:
                  problemsets.append('Given that ' + variables[vars_found[0]] + ' = ' + variable_values[vars_found[0]])
              elif len(vars_found) == 2:
                  problemsets.append('Given that ' + variables[vars_found[0]] + ' = ' + variable_values[vars_found[0]] + ', and ' + variables[vars_found[1]] + ' = '+ variable_values[vars_found[1]])
              elif len(vars_found) == 3:
                  problemsets.append('Given that ' + variables[vars_found[0]] + ' = ' + variable_values[vars_found[0]] + ', ' + variables[vars_found[1]] + ' = '+ variable_values[vars_found[1]] + ', and ' + variables[vars_found[2]] + ' = '+ variable_values[vars_found[2]])
              problemsets.append(filler)
              
          elif temp == 4:
              variable_and_variable_value(1, 15, 4, variables, variable_values, choices)
              variables = variable_repeat_sorter(variables)
              vars_found = []
              equation = ''

              indexes.append(variables[0])
              indexes.append(variables[1])
              indexes.append(variables[2])
              indexes.append(variables[3])
              random.shuffle(indexes)

              sym_1 = str(random.choice(addition_expression))
              sym_2 = str(random.choice(addition_expression))
              sym_3 = str(random.choice(addition_expression))
              output = '({} {} {}) ** {} {} ({} {} {}) ** {}'.format(indexes[0], sym_1, indexes[1], str(random.randint(2, 4)), sym_2, indexes[2], sym_3, indexes[3], str(random.randint(2, 4)))
              filler = sympify(output, evaluate=False)
         
              for i in range(len(variables)):
                  if output.find(variables[i]) != -1:
                      output = output.replace(variables[i], variable_values[i])
                      vars_found.append(i)
              random.shuffle(vars_found)
              answerset.append(sympify(output))
              if len(vars_found) == 1:
                  problemsets.append('Given that ' + variables[vars_found[0]] + ' = ' + variable_values[vars_found[0]])
              elif len(vars_found) == 2:
                  problemsets.append('Given that ' + variables[vars_found[0]] + ' = ' + variable_values[vars_found[0]] + ', and ' + variables[vars_found[1]] + ' = '+ variable_values[vars_found[1]])         
              elif len(vars_found) == 3:
                  problemsets.append('Given that ' + variables[vars_found[0]] + ' = ' + variable_values[vars_found[0]] + ', ' + variables[vars_found[1]] + ' = '+ variable_values[vars_found[1]] + ', and ' + variables[vars_found[2]] + ' = '+ variable_values[vars_found[2]])
              problemsets.append(filler)


      elif option_difficulty == 3: #(NUM range from 5~15)
          if temp == 1:
              variable_and_variable_value(5, 15, 4, variables, variable_values, choices)
              variables = variable_repeat_sorter(variables)
              vars_found = []
              equation = ''
        
              indexes.append(variables[0])
              indexes.append(variables[1])
              indexes.append(variables[2])
              indexes.append(variables[3])
              random.shuffle(indexes)

              sym_1 = str(random.choice(addition_expression))
              sym_2 = str(random.choice(mult_expression))
              sym_3 = str(random.choice(addition_expression))
              output = '({} {} {}) {} ({} {} {}) ** {}'.format(indexes[0], sym_1, indexes[1], sym_2, indexes[2], sym_3, indexes[3], str(random.randint(2, 4)))
              filler = sympify(output, evaluate=False)
           
              for i in range(len(variables)):
                  if output.find(variables[i]) != -1:
                      output = output.replace(variables[i], variable_values[i])
                      vars_found.append(i)
              random.shuffle(vars_found)
              answerset.append(sympify(output))
              if len(vars_found) == 1:
                  problemsets.append('Given that ' + variables[vars_found[0]] + ' = ' + variable_values[vars_found[0]])
              elif len(vars_found) == 2:
                  problemsets.append('Given that ' + variables[vars_found[0]] + ' = ' + variable_values[vars_found[0]] + ', and ' + variables[vars_found[1]] + ' = '+ variable_values[vars_found[1]])
              elif len(vars_found) == 3:
                  problemsets.append('Given that ' + variables[vars_found[0]] + ' = ' + variable_values[vars_found[0]] + ', ' + variables[vars_found[1]] + ' = '+ variable_values[vars_found[1]] + ', and ' + variables[vars_found[2]] + ' = '+ variable_values[vars_found[2]])
              elif len(vars_found) == 4:
                  problemsets.append('Given that ' + variables[vars_found[0]] + ' = ' + variable_values[vars_found[0]] + ', ' + variables[vars_found[1]] + ' = '+ variable_values[vars_found[1]] + ', ' + variables[vars_found[2]] + ' = '+ variable_values[vars_found[2]] + ', and ' + variables[vars_found[3]] + ' = '+ variable_values[vars_found[3]])
              problemsets.append(filler)
          
          elif temp == 2:
              variable_and_variable_value(5, 15, 3, variables, variable_values, choices)
              variables = variable_repeat_sorter(variables)
              vars_found = []
              equation = ''
             
              indexes.append(variables[0])
              indexes.append(variables[1])
              indexes.append(variables[2])
              indexes.append(str(random.randint(2, 10)))
              random.shuffle(indexes)

              sym_1 = str(random.choice(mult_expression))
              sym_2 = str(random.choice(addition_expression))
              sym_3 = str(random.choice(addition_expression))
              output = '(({} {} {}) ** {} {} {}) {} {}'.format(indexes[0], sym_1, indexes[1], str(random.randint(2, 4)), sym_2, indexes[2], sym_3, indexes[3])
 
              filler = sympify(output, evaluate=False)
              
              for i in range(len(variables)):
                  if output.find(variables[i]) != -1:
                      output = output.replace(variables[i], variable_values[i])
                      vars_found.append(i)
              random.shuffle(vars_found)
              answerset.append(sympify(output))
              if len(vars_found) == 1:
                  problemsets.append('Given that ' + variables[vars_found[0]] + ' = ' + variable_values[vars_found[0]])
              elif len(vars_found) == 2:
                  problemsets.append('Given that ' + variables[vars_found[0]] + ' = ' + variable_values[vars_found[0]] + ', and ' + variables[vars_found[1]] + ' = '+ variable_values[vars_found[1]])
              elif len(vars_found) == 3:
                  problemsets.append('Given that ' + variables[vars_found[0]] + ' = ' + variable_values[vars_found[0]] + ', ' + variables[vars_found[1]] + ' = '+ variable_values[vars_found[1]] + ', and ' + variables[vars_found[2]] + ' = '+ variable_values[vars_found[2]])
              problemsets.append(filler)
              
          
          elif temp == 3: # START HERE
              variable_and_variable_value(5, 15, 4, variables, variable_values, choices)
              variables = variable_repeat_sorter(variables)
              vars_found = []
              equation = ''
             
              indexes.append(variables[0])
              indexes.append(variables[1])
              indexes.append(variables[2])
              indexes.append(variables[3])
              indexes.append(str(random.randint(2, 10)))
              indexes.append(str(random.randint(2, 10)))
              random.shuffle(indexes)

              sym_1 = str(random.choice(addition_expression))
              sym_2 = str(random.choice(addition_expression))
              sym_3 = str(random.choice(mult_expression))
              sym_4 = str(random.choice(mult_expression))
              output = '({} / {}) {} {} {} {} {} {} {} {}'.format(indexes[0], indexes[1], sym_1, indexes[2], sym_2, indexes[3], sym_3, indexes[4], sym_4, indexes[5])

              filler = sympify(output, evaluate=False)
         
              for i in range(len(variables)):
                  if output.find(variables[i]) != -1:
                      output = output.replace(variables[i], variable_values[i])
                      vars_found.append(i)
              random.shuffle(vars_found)
              answerset.append(sympify(output))
              if len(vars_found) == 1:
                  problemsets.append('Given that ' + variables[vars_found[0]] + ' = ' + variable_values[vars_found[0]])
              elif len(vars_found) == 2:
                  problemsets.append('Given that ' + variables[vars_found[0]] + ' = ' + variable_values[vars_found[0]] + ', and ' + variables[vars_found[1]] + ' = '+ variable_values[vars_found[1]])
              elif len(vars_found) == 3:
                  problemsets.append('Given that ' + variables[vars_found[0]] + ' = ' + variable_values[vars_found[0]] + ', ' + variables[vars_found[1]] + ' = '+ variable_values[vars_found[1]] + ', and ' + variables[vars_found[2]] + ' = '+ variable_values[vars_found[2]])
              elif len(vars_found) == 4:
                  problemsets.append('Given that ' + variables[vars_found[0]] + ' = ' + variable_values[vars_found[0]] + ', ' + variables[vars_found[1]] + ' = '+ variable_values[vars_found[1]] + ', ' + variables[vars_found[2]] + ' = '+ variable_values[vars_found[2]] + ', and ' + variables[vars_found[3]] + ' = '+ variable_values[vars_found[3]])
              problemsets.append(filler)

          elif temp == 4:
              variable_and_variable_value(5, 15, 5, variables, variable_values, choices)
              variables = variable_repeat_sorter(variables)
              vars_found = []
              equation = ''
              
              indexes.append(variables[0])
              indexes.append(variables[1])
              indexes.append(variables[2])
              indexes.append(variables[3])
              indexes.append(variables[4])
              indexes.append(str(random.randint(2, 10)))
              indexes.append(str(random.randint(2, 10)))
              random.shuffle(indexes)

              sym_1 = str(random.choice(addition_expression))
              sym_2 = str(random.choice(addition_expression))
              sym_3 = str(random.choice(mult_expression))
              output = '({} / {}) {} ({} * {} / {}) {} {} {} {}'.format(indexes[0], indexes[1], sym_1, indexes[2], indexes[3], indexes[4], sym_2, indexes[5], sym_3, indexes[6])

              filler = sympify(output, evaluate=False)
              
              for i in range(len(variables)):
                  if output.find(variables[i]) != -1:
                      output = output.replace(variables[i], variable_values[i])
                      vars_found.append(i)
              random.shuffle(vars_found)
              answerset.append(sympify(output))
              if len(vars_found) == 1:
                  problemsets.append('Given that ' + variables[vars_found[0]] + ' = ' + variable_values[vars_found[0]])
              elif len(vars_found) == 2:
                  problemsets.append('Given that ' + variables[vars_found[0]] + ' = ' + variable_values[vars_found[0]] + ', and ' + variables[vars_found[1]] + ' = '+ variable_values[vars_found[1]])
              elif len(vars_found) == 3:
                  problemsets.append('Given that ' + variables[vars_found[0]] + ' = ' + variable_values[vars_found[0]] + ', ' + variables[vars_found[1]] + ' = '+ variable_values[vars_found[1]] + ', and ' + variables[vars_found[2]] + ' = '+ variable_values[vars_found[2]])
              elif len(vars_found) == 4:
                  problemsets.append('Given that ' + variables[vars_found[0]] + ' = ' + variable_values[vars_found[0]] + ', ' + variables[vars_found[1]] + ' = '+ variable_values[vars_found[1]] + ', ' + variables[vars_found[2]] + ' = '+ variable_values[vars_found[2]] + ', and ' + variables[vars_found[3]] + ' = '+ variable_values[vars_found[3]])
              elif len(vars_found) == 5:
                  problemsets.append('Given that ' + variables[vars_found[0]] + ' = ' + variable_values[vars_found[0]] + ', ' + variables[vars_found[1]] + ' = '+ variable_values[vars_found[1]] + ', ' + variables[vars_found[2]] + ' = '+ variable_values[vars_found[2]] + ', ' + variables[vars_found[3]] + ' = '+ variable_values[vars_found[3]] + ', and ' + variables[vars_found[4]] + ' = '+ variable_values[vars_found[4]])

              problemsets.append(filler)
      if (len(problemsets) >= 2):
        pass_loop = True
      else:
        answerset.clear()
        problemsets.clear()
    if str(answerset) == "[zoo]":
      answerset[0] = "Undefined"

    if expr == "latex":
      return(latex(problemsets[0], mode="plain") + " \\\\ " + latex(sympify(problemsets[1], evaluate=False), mode='plain'), latex(answerset.pop(0)))
    else:
      return(str(problemsets[0]) + " \\\\ " + str(problemsets[1]), answerset.pop(0))