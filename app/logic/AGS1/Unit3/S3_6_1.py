import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from loader import LinFunc, startGraph, drawLinear, endGraph, Rational, ExpFunc, latex, sympify, emptyGraph, drawCurve, x
import sympy
from random import sample, choice

# invalid syntax and incomplete/ borkwn code within the function
# AGS1.3.6.1 - Function Transformations (vertical)
# Instruction : Graph the equations.

def Function_Transformations_3_6_1(option=1,case=1):
  functionvars= sample(['a','b','c','d','e','f','g','h','j','k','p'],3)
  if option == 1:
    if case == 1:
      # generate linear for option 1
      lineqs = []
      slope = choice([Rational(1,2),Rational(-1,2),Rational(1,3),Rational(-1,3),Rational(1,4),Rational(1,4),2,3,4,-2,-3,-4])
      yint = sample(range(-9, 9), 3)
      for i in range(3):
        lineqs.append(LinFunc(slope,yint[i]))
      xlist = sample(range(-10, 10), 4)
      
      problem_graph = startGraph()+drawLinear(lineqs[1].expr,-10,10,functionvars[1])+endGraph()+r'\newline' 
      answer_graph = startGraph()+drawLinear(lineqs[0].expr,-10,10,functionvars[0])+drawLinear(lineqs[1].expr,-10,10,functionvars[1])+drawLinear(lineqs[2].expr,-10,10,functionvars[2])+endGraph()+r'\newline'
      problem = fr'a. Explain how ${functionvars[0]}(x)$ can be translated to be the same as ${functionvars[2]}(x)?$ \\'
      answer = ''
      temp = sympy.sympify(lineqs[2].expr - lineqs[0].expr)
      if int(temp) > 0:
        answer += fr'a. if ${functionvars[2]}(x)$ is translated down ${temp}$ it is the same as ${functionvars[0]}(x)$ \\'
      else:
        answer += fr'a. if ${functionvars[2]}(x)$ is translated up ${abs(temp)}$ it is the same as ${functionvars[0]}(x)$ \\'
      problem += fr'b. Explain how ${functionvars[1]}(x)$ can be translated to be the same as ${functionvars[2]}(x)$? \\'

      temp = sympy.sympify(expeqs[2].expr - expeqs[1].expr)
      if int(temp) > 0:
        answer += fr' b. if {functionvars[2]}(x) is translated down {temp} it is the same as {functionvars[1]}(x)'
      else:
        answer += fr'b. if {functionvars[2]}(x) is translated up {abs(temp)} it is the same as {functionvars[1]}(x)'

    else:     
    # generate geometry for option 1
      expeqs = []
      ratio = choice([Rational(1,2),Rational(1,3),2,3,4])
      xlist = sample(range(-10, 10), 4)
      start = sample(range(-9, 9), 3)
      for i in range(3):
        expeqs.append(ExpFunc(ratio,[0,start[i]],x,functionvars[i]))
      header = r'\newline \begin{cases}'
      for i in range(3):
        header += fr'$ {functionvars[i]}(x) = '+ latex(sympify(expeqs[i].expr , evaluate=False))+r'$ \\'
      header += r'\end{cases}'
      problem_graph =emptyGraph(-10,10,-10,10) + r'\\'
      answer_graph = r'\newline '+startGraph()+drawCurve(expeqs[0].expr,-10,10,functionvars[0])+drawCurve(expeqs[1].expr,-10,10,functionvars[1])+drawCurve(expeqs[2].expr,-10,10,functionvars[2])+endGraph()+r'\newline'
      problem = fr'a. Explain how ${functionvars[0]}(x)$ can be translated to be the same as ${functionvars[2]}(x)?$ \\'
      answer = ''
      temp = start[2]-start[1]

      if int(temp) > 0:
        answer += fr'a. if ${functionvars[2]}(x)$ is translated down ${temp}$ it is the same as ${functionvars[0]}(x)$ \\'
      else:
        answer += fr'a. if ${functionvars[2]}(x)$ is translated up ${abs(temp)}$ it is the same as ${functionvars[0]}(x)$ \\'
      problem += fr'b. Explain how ${functionvars[1]}(x)$ can be translated to be the same as ${functionvars[2]}(x)$? \\'

      temp = start[2]-start[0]

      if int(temp) > 0:
        answer += fr' b. if {functionvars[2]}(x) is translated down {temp} it is the same as {functionvars[1]}(x)'
      else:
        answer += fr'b. if {functionvars[2]}(x) is translated up {abs(temp)} it is the same as {functionvars[1]}(x)'
    # generate section 2 - graph 1 of them and follow other ones 
    # print(header,problem_graph, problem, answer_graph , answer)
    comp_prob = header + r'\newline' + problem_graph + r'\newline' + problem
    comp_problem = header + r'\newline' + answer_graph + r'\newline' + answer
  
  elif option == 2: # generate option 2 problem first and generate second
    if case == 1:   # generate linear
      lineqs = []
      slope = choice([Rational(1,2),Rational(-1,2),Rational(1,3),Rational(-1,3),Rational(1,4),Rational(1,4),2,3,4,-2,-3,-4])
      yint = sample(range(-9, 9), 3)
      for i in range(3):
        lineqs.append(LinFunc(slope,yint[i]))
      xlist = sample(range(-10, 10), 4)
      header = r'\newline \begin{cases}'
      for i in range(3):
        header += fr'$ {functionvars[i]}(x) = '+ sympy.latex(sympy.sympify(lineqs[i].expr , evaluate=False))+r'$ \\'
      header += r'\end{cases}'
      problem = 
      answer_graph = r'\newline '+startGraph()+drawLinear(lineqs[0].expr,-10,10,functionvars[0])+drawLinear(lineqs[1].expr,-10,10,functionvars[1])+drawLinear(lineqs[2].expr,-10,10,functionvars[2])+endGraph()+r'\newline'
      problem = fr'a. Explain how ${functionvars[0]}(x)$ can be translated to be the same as ${functionvars[2]}(x)?$ \\'
      answer = ''
      temp = sympy.sympify(lineqs[2].expr - lineqs[0].expr)
      if int(temp) > 0:
        answer += fr'a. if ${functionvars[2]}(x)$ is translated down ${temp}$ it is the same as ${functionvars[0]}(x)$ \\'
      else:
        answer += fr'a. if ${functionvars[2]}(x)$ is translated up ${abs(temp)}$ it is the same as ${functionvars[0]}(x)$ \\'
      problem += fr'b. Explain how ${functionvars[1]}(x)$ can be translated to be the same as ${functionvars[2]}(x)$? \\'

      temp = sympy.sympify(expeqs[2].expr - expeqs[1].expr)
      if int(temp) > 0:
        answer += fr' b. if {functionvars[2]}(x) is translated down {temp} it is the same as {functionvars[1]}(x)'
      else:
        answer += fr'b. if {functionvars[2]}(x) is translated up {abs(temp)} it is the same as {functionvars[1]}(x)'
  
    else:  # generate geo option 2
      expeqs = []
      ratio = choice([Rational(1,2),Rational(1,3),2,3,4])
      xlist = sample(range(-10, 10), 4)
      start = sample(range(-9, 9), 3)
      for i in range(3):
        expeqs.append(ExpFunc(ratio,[0,start[i]],x,functionvars[i]))
      header = r'\newline \begin{cases}'
      for i in range(3):
        header += fr'$ {functionvars[i]}(x) = '+ latex(sympify(expeqs[i].expr , evaluate=False))+r'$ \\'
      header += r'\end{cases}'
      problem_graph =emptyGraph(-10,10,-10,10) + r'\\'
      answer_graph = r'\newline '+startGraph()+drawCurve(expeqs[0].expr,-10,10,functionvars[0])+drawCurve(expeqs[1].expr,-10,10,functionvars[1])+drawCurve(expeqs[2].expr,-10,10,functionvars[2])+endGraph()+r'\newline'
      problem = fr'a. Explain how ${functionvars[0]}(x)$ can be translated to be the same as ${functionvars[2]}(x)?$ \\'
      answer = ''
      temp = start[2]-start[1]

      if int(temp) > 0:
        answer += fr'a. if ${functionvars[2]}(x)$ is translated down ${temp}$ it is the same as ${functionvars[0]}(x)$ \\'
      else:
        answer += fr'a. if ${functionvars[2]}(x)$ is translated up ${abs(temp)}$ it is the same as ${functionvars[0]}(x)$ \\'
      problem += fr'b. Explain how ${functionvars[1]}(x)$ can be translated to be the same as ${functionvars[2]}(x)$? \\'

      temp = start[2]-start[0]

      if int(temp) > 0:
        answer += fr' b. if {functionvars[2]}(x) is translated down {temp} it is the same as {functionvars[1]}(x)'
      else:
        answer += fr'b. if {functionvars[2]}(x) is translated up {abs(temp)} it is the same as {functionvars[1]}(x)'
    # generate section 2 - graph 1 of them and follow other ones 
    # print(header,problem_graph, problem, answer_graph , answer)
    comp_prob = header + r'\newline' + problem_graph + r'\newline' + problem
    comp_problem = header + r'\newline' + answer_graph + r'\newline' + answer

  return comp_prob , comp_problem


for i in range(1):
    prob , ans = Function_Transformations_3_6_1(1,2)
    print(prob) 
    print(ans)
    print('----------------------------')

#Section 2: Transfrom the graph from the given grap
for i in range(1):
  prob , ans = Function_Transformations_3_6_1(2,2)
  print(prob)
  print(ans)
  print('----------------------------')