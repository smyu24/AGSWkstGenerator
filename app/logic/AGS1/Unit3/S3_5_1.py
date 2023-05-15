import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from loader import LinFunc, getInt, getVar, startGraph, drawLinear, endGraph, x, ExpFunc, Rational, drawCurve, PWFunc, latexify, graphPW
import random
from random import randint, sample
import sympy
from sympy import nan
from math import floor, ceiling

# THIRD SECTION IS INCOMPLETE
# AGS1.3.5.1 - Find The Indicated Values - PT2
# Instruction : Use the graph of each function to find the indicated values.

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

# option 1: linear
for i in range(1):
  a , b ,c = Find_The_Indicated_Values_PT2_3_5_1(1)
  print(a)
  print(b)
  print(c)


# option 2: Geometric
for i in range(1):
  a , b ,c = Find_The_Indicated_Values_PT2_3_5_1(2)
  print(a)
  print(b)
  print(c)

# option 3: complex

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

for jj in range(5):
    problem, answer = PWLinearVals_3_5_1()
    print(problem)
    print(answer)


r""" SEEMS INCOMPLETE; FINSIH TO GET ALGGORITHM WORKING
# right now can graph functions. After, in order to get values for specific points, use sympy to solve

#linear, geometric, complex (discontinuous, piece)
def FindTheIndicatedValues(equation, dimentions_of_graph=[-10, 10], inequal=""):
    # [Function, [point_1,point_2, points_3]]
    # Current prerequisite: https://www.overleaf.com/project/615e6c5476af58171469bd7d

    #\drawgraph{-10}{10}{x-3}{}{}

    # if inequality:
        #\drawle
        #\drawge

    #find the y value from x value; find the x value from y value
    out = []
    inputted = ""
    out.append(r'\drawgraph') # \drawgraph{doamin negative}{domain positive}{function input}{inequality selector (leave blank if not inequal)}{}
    inputted = fr"`{dimentions_of_graph[0]}~`{dimentions_of_graph[1]}~`{equation}~`{inequal}~`~"
    inputted = inputted.replace("`", "{")
    inputted = inputted.replace("~", "}")
    out.append(inputted)

    return ''.join(out)
print(FindTheIndicatedValues("2(3)^x"))


def plotGraph(equation, dimentions_of_graph=[-10, 10, -10, 10]):
    # dimentions_of_graph  - [xmin, xmax, ymin, ymax]
    # number of plots, if separate graphs, dimentions of the graph (x axis, y axis)
    out = []
    inputted = ""
    out.append(r'\begin{tikzpicture}\begin{axis}')
    out.append(fr'[xmin={dimentions_of_graph[0]}, xmax={dimentions_of_graph[1]}, ymin={dimentions_of_graph[2]}, ymax={dimentions_of_graph[3]}, xtick distance=2, ytick distance=2, axis x line=center, axis y line=center]')
    inputted = fr'\addplot[domain= {dimentions_of_graph[0]}:{dimentions_of_graph[1]}] `({equation})~;'
    inputted = inputted.replace('`', '{')
    inputted = inputted.replace('~', '}')
    out.append(inputted)
    out.append(r'\end{axis}')
    out.append(r'\end{tikzpicture}')

    return ''.join(out)
print(plotGraph("2(3)^x"))



# \documentclass{article}
# \usepackage{pgfplots}
# \usetikzlibrary{intersections}
# \usetikzlibrary{patterns}

# \begin{document}
# \begin{tikzpicture}

# \begin{axis}[xmin=-10, xmax=10, ymin=-10, ymax=10, xtick distance=2, ytick distance=2, axis x line=center, axis y line=center]
# \addplot[domain=-10:-1.1622776601683795] {(x^2-4*x-6)};
# \addplot[domain= 5.16227766016838:10] {(x^2-4*x-6)};
# \addplot[domain= -10:10] {(2(3)^x)};
# \end{axis}

# \end{tikzpicture}
# \end{document}

# \documentclass{article}
# \usepackage{tikz}
# \begin{document}
# \begin{tikzpicture}[scale=2, domain=-3:3]
# \draw[->] (-3.1,0) -- (3.1,0) node[right] {$x$};
# \draw[->] (0,-2.1) -- (0,2.1) node[above] {$y$};
# \draw[dotted] (-3.1,-2.1) grid (3.1,2.1);
# \draw[very thick, color=blue] plot[id=logistic] function{1/(1+exp(-x))} node[right=0.15cm] {$f_1(x) = \frac{1}{1+e^{-x}}$};
# \draw[very thick, color=red] plot[id=hypertan] function{tanh(x)} node[above right=0.15cm] {$f_2(x) = tanh(x)$};
# \draw[very thick, color=orange] plot[id=algebraic] function{x/sqrt(1+x*x)} node[below right=0.15cm] {$f_3(x) = \frac{x}{\sqrt{1+x^2}}$};
# \draw[very thick, color=brown] plot[id=arctangent] function{atan(x)} node[above right=0.15cm] {$f_4(x) = arctan(x)$};
# \node[align=center, font=\bfseries, yshift=2em, xshift=-4.5em] (title) at (current bounding box.north) {Sigmoidal functions};
# \end{tikzpicture}
# \end{document}
"""