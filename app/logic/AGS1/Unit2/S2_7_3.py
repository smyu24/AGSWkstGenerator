import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from loader import ArithSeq, brackify, GeoSeq, latexify, signify, tableGenerator
from sympy import *
from random import randint

# AGS1.2.7.3 - X-intercept & Y-intercept
# instruction : Given the function, find the  x -intercept(s) and  y -intercept if they exist, and then use them to graph the function.

from sympy import Symbol

def notzero(fnum, snum):
  inta = 0
  while inta == 0:
      inta = randint(fnum, snum)
  return inta

def setlinearequation(m, xint, yint):
  if yint >= 0:
    if xint > 0:
      equ = str(m) + "* (x + " + str(xint) + ") + " + str(yint)
    elif xint < 0:
      equ = str(m) + "* (x - " + str(xint) + ") + " + str(yint)
    else:
      equ = str(m) + "* x + "  + str(yint)
  else:
    if xint > 0:
      equ = str(m) + "* (x + " + str(xint) + ") " + str(yint)
    elif xint < 0:
      equ = str(m) + "* (x - " + str(xint) + ") " + str(yint)
    else:
      equ = str(m) + "* x "  + str(yint)

  return equ

def setexpequation(a, m, xint, yint):
  if yint > 0:
    if xint > 0:
      equ = str(a) + "*(" + str(m) + "^{x + " + str(xint) + "} + " + str(yint)
    elif xint < 0:
      equ = str(a) + "*(" + str(m) + "^{x " + str(xint) + "} + " + str(yint)
    else:
      equ = str(a) + "*(" + str(m) + "^{x} + " + str(yint)
  elif yint < 0:
    if xint > 0:
      equ = str(a) + "*(" + str(m) + "^{x + " + str(xint) + "} " + str(yint)
    elif xint < 0:
      equ = str(a) + "*(" + str(m) + "^{x " + str(xint) + "} " + str(yint)
    else:
      equ = str(a) + "*(" + str(m) + "^{x} " + str(yint)
  else:
    if xint > 0:
      equ = str(a) + "*(" + str(m) + "^{x + " + str(xint) + "}"
    elif xint < 0:
      equ = str(a) + "*(" + str(m) + "^{x " + str(xint) + "}"
    else:
      equ = str(a) + "*(" + str(m) + "^{x} "
  return equ

def createequation(equation, xint, yint, xintercept, yintercept, form):
  if xintercept != 0 and yintercept != 0:
    answer = "\\begin{minipage}[t]{0.5\\textwidth}\n\\begin{tikzpicture}\n\\begin{axis}\n[mmt axis style,xmin=-7,xmax=7,xtick={-5,0,...,11},ymin=-6,ymax=6,ytick={-10,-5,...,11},]\n"
    answer = answer + "\\addplot[red,domain=-10:10] {" + equation + "};\n"
    answer = answer + "\\fill[black] (axis cs: 0," + str("{:.2f}".format(yintercept)) + ") circle(2pt);\n"
    if form == 2 and xintercept == 0:
      answer = answer
    else:
      answer = answer + "\\fill[black] (axis cs:" + str("{:.2f}".format(xintercept)) + ", 0) circle(2pt);\n"
    answer = answer + "\\end{axis} \\end{tikzpicture} \\end{minipage}\n"
    answer = answer + "x-intercept: " + str("{:.2f}".format(xintercept)) + ", y-intercept: " + str("{:.2f}".format(yintercept))
  else:
    answer = "There is no x-intercept and y-intercept"
  return answer

def xinterceptyintercept(diff = 1, expr = "latex"):
  list = ["f", "g", "d", "u"]
  letter = list[randint(0, 3)]

  if diff == 1: #liner
    m = notzero(-3, 4)
    xint = randint(0, 5)
    yint = randint(-4, 4)
    equation = setlinearequation(m, xint, yint)
    xintercept = (-(m * xint) - yint) / m
    yintercept = (m * xint) + yint
    answer = createequation(equation, xint, yint, xintercept, yintercept, 1)
  elif diff == 2: #exp
    a = notzero(-3, 4)
    m = notzero(1, 4)
    xint = notzero(-2, 3)
    yint = randint(-2, 2)
    equation = setexpequation(a, m, xint, yint)
    answer = "{:.2f}".format(a * (m**(0-xint)) + yint) #Y-int

  return equation, answer

xinterceptyintercept(2)
 
# Generate the empty grid from -7 to 7
def GraphXintYint_2_7_3(kind='lin', expr='latex'):
    case = randint(1,6)
    if kind == 'lin':
        if case == 1:
            slope, pt = Rational(getInt(-6,6),randint(2,6)), [0, 0]
        elif case == 2:
            slope, pt = Rational(getInt(-6,6),randint(2,6)), [getInt(-6,6), 0]
        elif case == 3:
            slope, pt = Rational(getInt(-6,6),randint(2,6)), [getInt(-6,6), randint(-6,6)]
        elif case == 4:
            slope, pt = getInt(-6,6), [0, getInt(-6,6)]
        elif case == 5:
            slope, pt = getInt(-6,6), [getInt(-6,6), 0]
        elif case == 6:
            slope, pt = getInt(-6,6), [getInt(-6,6), randint(-6,6)]

        func = LinFunc(slope, pt)
    elif kind == 'exp':
        if case == 1:
            base, pt, shift = randint(2,4), [getInt(-6,6), getInt(2,6)], 0
        elif case == 2:
            base, pt, shift = randint(2,4), [getInt(-6,6), getInt(2,6)], getInt(-6,6)
        elif case == 3:
            base, pt, shift = randint(2,4), [getInt(-6,6), getInt(-6,6)], getInt(-6,6)
        elif case == 4:
            base, pt, shift = Rational(1,randint(2,4)), [getInt(-6,6), getInt(2,6)], 0
        elif case == 5:
            base, pt, shift = Rational(1,randint(2,4)), [getInt(-6,6), getInt(2,6)], getInt(-6,6)
        elif case == 6:
            base, pt, shift = Rational(1,randint(2,4)), [getInt(-6,6), getInt(-6,6)], getInt(-6,6)
    
        func = ExpFunc(base, pt, shift=shift)

    problem = signify(func.getPtSlope(pt[0])) if kind=='lin' else signify(func.getPtBase(pt[0]))
    problem += r' \newline $y$-intercept: $(\quad, \quad)$ \newline '
    problem += r'$x$-intercept: $(\quad, \quad)$ \newline '
    problem += emptyGraph()

    xint = func.solve(0)
    xint = xint if type(xint) in [Integer,Rational] else N(xint,3)

    answer = fr'$y$-intercept = $(0,{latexify(func.intercept)})$ \newline $x$-intercept: '
    answer += fr'$({latexify(xint)}, 0)$ \newline ' if xint!=None else r'None \newline '
    answer += startGraph() + drawCurve(func.expr,-10,10) + drawPt([0,N(func.intercept,3)])
    answer += (drawPt([xint,0]) + endGraph()) if xint!=None else endGraph()

    return problem, answer

for jj in range(5):
    problem, answer = GraphXintYint_2_7_3(kind='exp')
    print(problem)
    print(answer)