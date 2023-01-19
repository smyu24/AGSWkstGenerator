import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from loader import LinFunc, getInt, sample, startGraph, drawLinear, endGraph, ExpFunc, drawCurve, y
from sympy import *
from random import randint, choice

# CODE NOT USABLE; ADJUST THEN APPROPRIATE INTO FUNCTION THAT US USABLE
# AGS1.3.4.3- Compare Two Functions
# Instruction : Use the graph to answer the following questions.

import sympy, random
import numpy as np
import scipy.optimize as opt


def linearEQgenerator(zeroSlope=False,zeroYint=False,fractionSlope=False,fractionYint=False,minM=-10,maxM=10,minB=-10,maxB=10,minDenominator=1,maxDenominator=6):
  """
  Generates an equation given the slope and intercept.
  It handles cases where m is fractional.
  -----
  minM = minimum slope
  returns sympy notation
  """
  if zeroSlope == True:
      m = 0
  elif fractionSlope == True:
      m = sympy.Rational(random.randint(minM,maxM),random.randint(minDenominator, maxDenominator))
      while m == 0:
        m = sympy.Rational(random.randint(minM,maxM),random.randint(minDenominator, maxDenominator))
  else:
      m = random.randint(minM,maxM)
      while m == 0:
          m = random.randint(minM,maxM)

  if zeroYint == True:
      b = 0
  elif fractionYint == True:
      b = sympy.Rational(random.randint(minB,maxB),random.randint(minDenominator, maxDenominator))
      while b == 0:
        b = sympy.Rational(random.randint(minB,maxB),random.randint(minDenominator, maxDenominator))
  else:
      b = random.randint(minB,maxB)
      while b == 0:
          b = random.randint(minB,maxB)

  rhs = ""

  if m != 0:
      if m == 1:
          rhs = f"x"
      elif m == -1:
          rhs = f"-x"
      else:
          rhs = f"{m}*x"
      if b > 0:
          rhs +=  f"+{b}"
      elif b < 0:
          rhs += f"{b}"
  else:
      if b > 0 or b < 0:
          rhs =  f"{b}"
      else:
          rhs = ""

  return rhs
  
def Systems_of_Equation(expr='sympy',option='standard',range_x=3,range_y=3,coeff_mult_range=5):
    '''
    expr = latex , sympy
    option = standard : ax + by = c
          point_slope : y=mx+b 
    range_x = location of solution for x-coordination(evenly distributed -3 to 3 or -10 to 10)
    range_y = location of solution for y-coordination(evenly distributed -3 to 3 or -10 to 10)
    coeff_mult_range= controller for dynamic range shift for the coeff of eqs
    '''
    x, y = sympy.symbols('x y')
    # Generate solution point first
    x = random.randint(-range_x, range_x)
    y = random.randint(-range_y, range_y)
    # Start from reduced echelon form (coeffs 1)
    c1 = [1, 0, x]
    c2 = [0, 1, y]
    def randNonZero():
        return random.choice([i for i in range(-coeff_mult_range, coeff_mult_range) if i != 0])
    # Add random (non-zero) multiple of equations (rows) to each other
    c1_mult = randNonZero()
    c2_mult = randNonZero()
    new_c1 = [c1[i] + c1_mult * c2[i] for i in range(len(c1))]
    new_c2 = [c2[i] + c2_mult * c1[i] for i in range(len(c2))]

    # construct Standard Form
    def standard_form_construct(coeffs): 
        # lots of edge cases for perfect formatting
        x_sign = '-' if coeffs[0] < 0 else ''
        # No redundant 1s
        x_coeff = str(abs(coeffs[0])) #if abs(coeffs[0]) != 1 else ''
        # If x coeff is 0, dont include x
        x_str = f'{x_sign}{x_coeff}*x' if coeffs[0] != 0 else ''
        # if x isn't included and y is positive, dont include operator
        op = ' - ' if coeffs[1] < 0 else (' + ' if x_str != '' else '')
        # No redundant 1s
        y_coeff = abs(coeffs[1]) #if abs(coeffs[1]) != 1 else ''
        # Don't include if 0, unless x is also 0 (probably never happens)
        y_str = f'{y_coeff}*y' #if coeffs[1] != 0 else ('' if x_str != '' else '0')
        lhs = f'{x_str}{op}{y_str}'
        rhs = f'{coeffs[2]}'
        return lhs , rhs
    
    # construct point slope form
    def pointslope_form_construct(coeffs):
        slope = sympy.Rational(-coeffs[0],coeffs[1])
        yint = sympy.Rational(coeffs[2],coeffs[1])
        lhs = 'y'
        rhs = f'{slope}*x + {yint}' if slope != 0 else (f' {yint}')
        return lhs , rhs
    
    if option == 'standard':
      eq1lhs , eq1rhs = standard_form_construct(new_c1)
      eq2lhs , eq2rhs = standard_form_construct(new_c2)

    elif option == 'point_slope':
      eq1lhs , eq1rhs = pointslope_form_construct(new_c1)
      eq2lhs , eq2rhs = pointslope_form_construct(new_c2)

    solution = [x,y]

    if expr == 'sympy':  
      return sympy.sympify(eq1lhs), sympy.sympify(eq1rhs), sympy.sympify(eq2lhs), sympy.sympify(eq2rhs), solution
    elif expr == 'latex':
      return sympy.latex(sympy.sympify(eq1lhs)) , sympy.latex(sympy.sympify(eq1rhs)),sympy.latex(sympy.sympify(eq2lhs)),sympy.latex(sympy.sympify(eq2rhs)) , solution


def Compare_Two_Functions_3_4_3(expr='sympy',option=1):
    '''
    expr = latex , sympy
    option = 1 : linear + linear
             2  : geometric + linear
    returns -------------------------------------------
    problem = tikz code for the graph
    expr = sympy expression
    xlist = list of x coordinate for each problem sets
    ylist = list of x coordinate for each problem sets
    '''
    #random_boolean = bool(random.getrandbits(1))
    x = Symbol('x')
    funcVar = ['a','b','c','d','e','f','g','q','z','k','l','m','m','o','p']
    funcLabel = sample(funcVar,2)
    xmin,xmax = -10 , 10
    xlist = [-3,-2,-1,0,1,2,3]

    if option == 1:
      xlistmax = [i for i in range(xmin,xmax)]
      # generate equations & solutions
      eq1lhs,eq1rhs,eq2lhs,eq2rhs,sol = Systems_of_Equation('sympy','point_slope',3,3,3)
      #generate solution_graph
      problem_graph = r'\newline'+startGraph() + drawLinear(eq1rhs,xmin,xmax,'black',funcLabel[0])+ drawLinear(eq2rhs,xmin,xmax,'black',funcLabel[1])+ endGraph()
      eq1rhs = sympify(eq1rhs,rational = True)
      eq2rhs = sympify(eq2rhs,rational = True)
      
      question = fr'\newline a) Where does ${funcLabel[0]}(x)= {funcLabel[1]}(x) $ ? \\'
      answer_text = question + f'({sol[0],sol[1]})'

      y1list = []
      y2list = []
      f1 = lambdify(x,eq1rhs)
      f2 = lambdify(x,eq2rhs)
      b = sample(xlist,2)
      for i in range(len(xlistmax)):
        y1list.append(f1(i))
        y2list.append(f2(i))

      '''
      print(b)
      print('xlist',xlist)
      print('y1ist',y1list)
      print('y2ist',y2list)
'''
      question_b = fr'b) What is ${funcLabel[0]}({b[0]}) + {funcLabel[1]}({b[0]}) $ ? \\'
      question += question_b 
      answer_text = answer_text + question_b + fr'Approximately {y1list[b[0]] + y2list[b[0]] }'
      
      question += fr'c) What is ${funcLabel[1]}({b[1]}) - {funcLabel[0]}({b[1]}) $ ? \\'
      answer_text += fr'Approximately { y1list[b[1]] - y2list[b[1]]}'
      
      question += 'd) '+fr'State the interval where ${funcLabel[0]}(x) > {funcLabel[1]}(x) $ \\' 
      answer_text += r'$'+ sympy.latex(sympy.solveset(eq1rhs > eq2rhs, x, S.Reals)) + r'$'

      question += 'e) '+fr'State the interval where ${funcLabel[0]}(x) \leq {funcLabel[1]}(x) $ \\' 
      answer_text += r'$'+ sympy.latex(sympy.solveset(eq1rhs <= eq2rhs, x, S.Reals)) + r'$'

    else:
      xlistmax = [i for i in np.arange(xmin,xmax,0.1)]
      xlist = [-3,-2,-1,0,1,2,3]
      #generate expo func
      ratio = choice([Rational(1,2),Rational(1,3),2,3])
      eq1rhs=ExpFunc(ratio,[getInt(),getInt()])
      problem_graph = r'\newline'+startGraph()+drawCurve(eq1rhs.expr,-10,10,funcLabel[0])
      #generate lin func reduce overlaping cases or generate more logical "fitting" type of problems
      if ratio < 0:
        slope = getInt(-5,-1)
      else:
        slope = getInt(1,5)
      yint = getInt()
      eq2rhs = LinFunc(slope,yint)
      problem_graph += drawLinear(eq2rhs.expr,-10,10,'black',funcLabel[1]) + endGraph()
      eq1rhs = sympify(eq1rhs.expr,rational = True)
      eq2rhs = sympify(eq2rhs.expr,rational = True)
      '''
      print('x,y',x,y)
      print(eq1rhs,eq2rhs)

      '''
      print(xlistmax)
      #storage
      y1list = []
      y2list = []
      result = []
      intersect = []
      # pick 2 random x values for the prob
      b = random.sample(xlist,2)
      # start comparision instead of using inequality needs to be updated later
      f1 = lambdify(x,eq1rhs)
      f2 = lambdify(x,eq2rhs)
      for i in xlistmax:
        temp1 = round(f1(i),1)
        temp2 = round(f2(i),1)
        y1list.append(temp1)
        y2list.append(temp2)
        result.append(1 if temp1 > temp2 else 0)
#        print("temp1:", temp1," temp2: ",temp2)
      
      for i in range(len(result) -1):
        if result[i] != result[i+1]:
          intersect.append(i)
      
      print('xlist',xlist)
      print('y1list',y1list)
      print('y2list',y2list)
      print(result)
      print(intersect)
      
      '''
      # if first > second all the way
      if len(set(result)) == 1:
        answer_d = r"(-\infty , \infty)"
        answer_e = "None"
      elif len(set(result)) == 0:
        answer_d = "None"
        answer_e = r"(-\infty , \infty)"
      # figuring out interval notation
      else:
        for temp in len(intersect):
          if intersect(temp) >
      '''   
      question_a= fr'\newline a) Where does ${funcLabel[0]}(x)= {funcLabel[1]}(x) $ ? \\'
      answer_text = question_a + fr'{x},{y} \newline'

      question_b = fr'b) What is ${funcLabel[0]}({b[0]}) + {funcLabel[1]}({b[0]}) $ ? \\'
      answer_text = answer_text + question_b + fr'Approximately {y1list[b[0]] + y2list[b[0]] } \\'
      
      question_c = fr'c) What is ${funcLabel[1]}({b[1]}) - {funcLabel[0]}({b[1]}) $ ? \\'
      answer_text = answer_text + question_c + fr'Approximately { y1list[b[1]] - y2list[b[1]]} \\'

      question = question_a+question_b+question_c
      '''
      question_d= fr'd) State the interval where ${funcLabel[0]}(x) > {funcLabel[1]}(x) $ \\' 
      answer_text = answer_text + question_d + r'$'+ sympy.latex(sympy.solveset(eq1rhs > eq2rhs, x, S.Reals)) + r'$'

      question_e = fr'e) State the interval where ${funcLabel[0]}(x) \leq {funcLabel[1]}(x) $ \\' 
      answer_text = answer_text + question_e+ r'$'+ sympy.latex(sympy.solveset(eq1rhs <= eq2rhs, x, S.Reals)) + r'$'
      '''

    '''
    problem graph = TIKZ problem graph
    answer graph = TIKZ answer graph,  f(x) + g(x)
    '''
  #  print('eq1',eq1rhs,'eq2',eq2rhs,'xlist',xlist,'y1list',y1list,'y2list',y2list)
    return problem_graph, question , answer_text


for i in range(1):
  problem_graph , question , answer_text = Compare_Two_Functions_3_4_3('sympy',2)
  print(problem_graph)
  print(question)
  print(answer_text)