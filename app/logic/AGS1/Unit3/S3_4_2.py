import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from loader import startGraph, drawLinear, endGraph, drawPt, Rational, drawCurve, lambdify
import random
import sympy

# add new code that truncates running numbers to the ten thousandths value before pushing code; NEED FUNCTION TO TRUNCATE FOR GRAPHICAL
# AGS1.3.4.2 - Graph The New Equation
# Instruction : Two functions are graphed. Graph a new function on the same grid by adding the two given functions.

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


import sympy
def Find_The_Indicated_Values_3_4_2(expr='sympy',option=1):
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
    x = sympy.Symbol('x')
    funcVar = ['a','b','c','d','e','f','g','q','z','k','l','m','m','o','p']
    funcLabel = random.sample(funcVar,3)
    xmin,xmax = -10 , 10

    if option == 1:
      # generate equations & solutions
      eq1lhs,eq1rhs,eq2lhs,eq2rhs,sol = Systems_of_Equation('sympy','point_slope',3,3,3)
      eq3rhs = sympy.sympify(eq1rhs + eq2rhs,rational = True)
      #generate solution_graph
      problem_graph = startGraph() + drawLinear(eq1rhs,xmin,xmax,'black',funcLabel[0])+ drawLinear(eq2rhs,xmin,xmax,'black',funcLabel[1])+ endGraph()
      answer_graph = startGraph() + drawPt(sol) + drawLinear(eq1rhs,xmin,xmax,'black',funcLabel[0])+ drawLinear(eq2rhs,xmin,xmax,'black',funcLabel[1])+drawLinear(eq3rhs,xmin,xmax,'black',funcLabel[2])

    else:
      ratio = random.choice([Rational(1,2),Rational(1,3),2,3])
      yint = random.choice([-4,-3,-2,2,3,4])
      eq1rhs = f'{yint} * ({ratio}) ** x'
      problem_graph = startGraph()+drawCurve(eq1rhs,-10,10,funcLabel[0])
      
      #generate empty grids
      case = random.randint(1,3)
      if case == 1:
        eq2rhs = linearEQgenerator(False,False,False,False,-10,10,-5,5,1,6)
      elif case == 2:
        eq2rhs = linearEQgenerator(False,False,True,False,-10,10,-5,5,1,6)
      elif case == 3:
        eq2rhs = linearEQgenerator(False,False,True,True,-10,10,-5,5,1,6)
      
      problem_graph += drawLinear(eq2rhs,-10,10,'black',funcLabel[1])
      #sol = sympy.linsolve([Eq(eq1rhs,0),Eq(eq2rhs)])
      eq3rhs = sympy.sympify(eq1rhs+eq2rhs,rational=True)
      #print('sol-----!@#!@#!@#',sol)
      answer_graph = problem_graph + drawCurve(eq3rhs,-10,10,funcLabel[2])

    xlistmax = [i for i in range(-10,11)]
    xlist = [-4,-2,-1,1,2,4]
    ylist = []
    
    for i in range(len(xlist)):
      f1 = lambdify(x,eq1rhs)
      f2 = lambdify(x,eq2rhs)
      ylist.append([f1(i),f2(i)])
      answer_graph += drawPt([i,f1(i)])
      answer_graph += drawPt([i,f2(i)])
        
    answer_graph += r'\addplot[color=blue,mark=square,]coordinates {'
    for i in range(len(xlistmax)):
      f1 = lambdify(x,eq1rhs)
      f2 = lambdify(x,eq2rhs)
      answer_graph += f'({f1(i)},{f2(i)})'
      answer_graph += drawPt([i,f2(i)])
    
    answer_graph =answer_graph+'};'+endGraph()

    header = fr'${funcLabel[2]}(x)= {funcLabel[0]}(x) + {funcLabel[1]}(x)$'
    '''
    header = problem display
    problem graph = TIKZ RETURN graph
    answer graph = TIKZ return,  f(x) + g(x) = k(x)
    '''
    print('eq1',eq1rhs,'eq2',eq2rhs,'eq3',eq3rhs,'xlist',xlist,'ylist',ylist)
    return header , problem_graph+endGraph() , answer_graph
    
for i in range(1):
  header,prob,ans = Find_The_Indicated_Values_3_4_2(expr='sympy',option=1)
  print(header)
  print(prob)
  print(ans)
for i in range(1):
  header,prob,ans = Find_The_Indicated_Values_3_4_2(expr='sympy',option=2)
  print(header)
  print(prob)
  print(ans)