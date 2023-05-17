import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from loader import LinFunc, getInt, latexify, getVar, startGraph, drawLinear, endGraph, drawCurve, x,ExpFunc, PWFunc, graphPW
from sympy import *
from random import randint, sample
import random

#option 1: linear
import sympy
def Find_The_Indicated_Values_PT2_3_5_1(option):
  functionvar= getVar(['a','b','c','d','e','f','g'])
  if option == 1:
    slope = random.randint(-6,6)
    yint = random.randint(-6,6)
    lineq= LinFunc(slope,yint)
    xlist = random.sample(range(-10, 10), 4)
    ylist=[]
    for i in range(len(xlist)):
      ylist.append(lineq.expr.subs(x,xlist[i]))

    header_graph = r'\newline '+fr'${functionvar}(x)$'+startGraph()+drawLinear(lineq,-10,10)+endGraph()+r'\newline'
    answer = ''
    problem =''
    option = ['a','b','c','d']
    for i in range(4):
      if i%2 != 0:
        problem += fr'{option[i]}) ${functionvar}({sympy.latex(xlist[i])})= $ \\'
        answer += fr'{option[i]}) ${functionvar}({sympy.latex(xlist[i])})= {sympy.latex(ylist[i])}$ '
      else:
        problem += fr'{option[i]}) ${functionvar}(x)={sympy.latex(ylist[i])}, x = $ \\'
        answer += fr'{option[i]}) ${functionvar}({sympy.latex(xlist[i])})= {sympy.latex(ylist[i])}$ '

  elif option == 2:
    ratio = random.choice([Rational(1,2),Rational(1,3),2,3,4])
    xpt = getInt(-2,3)
    ypt = getInt(-3,2)
    expeq = ExpFunc(ratio,[xpt,ypt],functionvar)
    xlist = random.sample(range(-10, 10), 4)
    ylist=[]
    for i in range(len(xlist)):
      ylist.append(expeq.expr.subs(x,xlist[i]))

    header_graph = r'\newline $'+fr'{functionvar}(x)$'+startGraph()+drawCurve(expeq.expr,-10,10)+endGraph()+r'\newline'
    answer = ''
    problem =''
    option = ['a','b','c','d']
    for i in range(4):
      if i%2 != 0:
        problem += fr'{option[i]}) ${functionvar}({sympy.latex(xlist[i])})= $ \\'
        answer += fr'{option[i]}) ${functionvar}({sympy.latex(xlist[i])})= {sympy.latex(ylist[i])}$ '
      else:
        problem += fr'{option[i]}) ${functionvar}(x)={sympy.latex(ylist[i])}, x = $ \\'
        answer += fr'{option[i]}) ${functionvar}({sympy.latex(xlist[i])})= {sympy.latex(ylist[i])}$ '
    
  else:
    temp=''

  return header_graph, problem, answer

# for i in range(1):
#   a , b ,c = Find_The_Indicated_Values_PT2_3_5_1(1)
#   print(a)
#   print(b)
#   print(c)


# #option 2: Geometric
# for i in range(1):
#   a , b ,c = Find_The_Indicated_Values_PT2_3_5_1(2)
#   print(a)
#   print(b)
#   print(c)

#Option3: Complex
def PWLinearVals_3_5_1(expr='latex'):
    endPts, pairs = [randint(-9,-5)], []

    for jj in range(randint(3,5)):
        slope, start = Rational(getInt(-6,6),randint(1,3)), randint(-6,6)
        func = LinFunc(slope, [endPts[-1],start])
        
        step = randint(3,6) if slope.q==1 else randint(1,3)*slope.q
        endPts.append(endPts[-1] + step)
        endPts.append(endPts[-1] + randint(1,2))
        pairs.append([func.expr, fr'[{endPts[-3]},{endPts[-2]}]'])
    
    func = PWFunc(*pairs)

    rangeset = func.getRange()
    mnm, mxm = floor(rangeset.inf), ceiling(rangeset.sup)
    start, end = floor(func.domain.inf), ceiling(func.domain.sup)
    inputs = sample(list(range(start,end+1)), 2)
    outputs = sample(list(range(mnm,mxm+1)), 2)

    solns = [func.subs(inputs[0]), func.subs(inputs[1])]
    solns = [jj if jj!=nan else r'\text{Undefined}' for jj in solns]
    solns += [func.solve(outputs[0]), func.solve(outputs[1])]
    solns = [latexify(jj) if jj!=[] else [r'\text{None}'] for jj in solns]

    problem = graphPW(func, contDot=True) + r'\newline '
    problem += fr'(a) ${func.label}({inputs[0]})=$ \newline '
    problem += fr'(b) ${func.label}({inputs[1]})=$ \newline '
    problem += fr'(c) ${func.label}({func.variable})={outputs[0]}, {func.variable}=$ \newline '
    problem += fr'(d) ${func.label}({func.variable})={outputs[1]}, {func.variable}=$'

    answer = fr'(a) ${func.label}({inputs[0]})={solns[0]}$ \newline '
    answer += fr'(b) ${func.label}({inputs[1]})={solns[1]}$ \newline '
    answer += fr'(c) $x={", ".join(solns[2])}$ \newline '
    answer += fr'(d) $x={", ".join(solns[3])}$ \newline '

    return problem, answer

# for jj in range(5):
#     problem, answer = PWLinearVals_3_5_1()
#     print(problem)
#     print(answer)