import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from sympy import *
from random import randint

# AGS1.2.11.1 - Compare Different Characteristics
# instruction : Compare different characteristics of each type of function by filling in the cells of each table as completely as possible.

from sympy import *

def notzero(min, max):
  inta = 0
  while inta == 0:
    inta = randint(min, max)
  return inta

def getyval(equation, xtable=[]):
  x = Symbol('x')
  ytable = []
  for i in xtable:
    ytable.append(equation.subs(x, i))
  return ytable

def creategraph(equation=0, point1=[], point2=[], form=0):
  if form == 0: #linear equation
    answer = "\\begin{minipage}[t]{0.5\\textwidth}\n\\begin{tikzpicture}\n\\begin{axis}\n[mmt axis style,xmin=-1,xmax=4,xtick={-5,0,...,11},ymin=-1,ymax=15,ytick={-10,-5,...,15},]\n"
    answer = answer + "\\addplot[red,domain=-5:5] {" + str(equation) + "};\n"

  elif form == 1:
    answer = "\\begin{minipage}[t]{0.5\\textwidth}\n\\begin{tikzpicture}\n\\begin{axis}\n[mmt axis style,xmin=-1,xmax=4,xtick={-5,0,...,11},ymin=-1,ymax=15,ytick={-10,-5,...,15},]\n"
    answer = answer + "\\addplot[red,domain=-5:5] {" + str(equation) + "};\n"

  answer = answer + "\\fill[black] (axis cs:" + str(point1[0]) + "," + str(point1[1]) + ") circle(2pt);\n"
  answer = answer + "\\fill[black] (axis cs:" + str(point2[0]) + "," + str(point2[1]) + ") circle(2pt);\n"
  answer = answer + "\\end{axis} \\end{tikzpicture} \\end{minipage}"
  return answer

def setlinearequation(m, xint, yint):
  if yint >= 0:
    if xint > 0:
      equ = str(m) + "* (x + " + str(xint) + ") + " + str(yint)
    elif xint < 0:
      equ = str(m) + "* (x " + str(xint) + ") + " + str(yint)
    else:
      equ = str(m) + "* x + "  + str(yint)
  else:
    if xint > 0:
      equ = str(m) + "* (x + " + str(xint) + ") " + str(yint)
    elif xint < 0:
      equ = str(m) + "* (x " + str(xint) + ") " + str(yint)
    else:
      equ = str(m) + "* x "  + str(yint)

  return equ
  
def setexpequation(a, m, xint, yint):
  if yint > 0:
    if xint > 0:
      equ = str(a) + "*(" + str(m) + "^{x + " + str(xint) + "}) + " + str(yint)
    elif xint < 0:
      equ = str(a) + "*(" + str(m) + "^{x " + str(xint) + "}) + " + str(yint)
    else:
      equ = str(a) + "*(" + str(m) + "^{x}) + " + str(yint)
  elif yint < 0:
    if xint > 0:
      equ = str(a) + "*(" + str(m) + "^{x + " + str(xint) + "}) " + str(yint)
    elif xint < 0:
      equ = str(a) + "*(" + str(m) + "^{x " + str(xint) + "}) " + str(yint)
    else:
      equ = str(a) + "*(" + str(m) + "^{x}) " + str(yint)
  else:
    if xint > 0:
      equ = str(a) + "*(" + str(m) + "^{x + " + str(xint) + "})"
    elif xint < 0:
      equ = str(a) + "*(" + str(m) + "^{x " + str(xint) + "})"
    else:
      equ = str(a) + "*(" + str(m) + "^{x}) "
  return equ

def createproblem(equation):
  problem = "\\begin{center} \n \\begin{tabular}{|l|c|} \\hline \n"
  problem = problem + "$ $ & $" + str(equation) + "$ \\\\ \\hline" + " \n "
  problem = problem + r"Type of growth & $ $ \\ \hline" + "\n"
  problem = problem + r"\pbox{20cm}{What kind of sequence \\ corresponds to each model?} & $ $ \\ \hline" + "\n"
  problem = problem + r"Make a table of values & \begin{tabular}{c|c} \hline $x$ & $y$\\ \hline -1 & $ $ \\ \hline 0 & $ $ \\ \hline 1 & $ $ \\ \hline 2 & $ $ \\ \hline 3 & $ $ \\ \end{tabular} \\ \hline" + "\n"
  problem = problem + r"Find the rate of change & $ $ \\ \hline" + "\n" 
  problem = problem + r"\pbox{20cm}{Graph each equation. \\ Compare the graphs. \\ What is the same? \\ What is different?} &"
  problem = problem + r"[t]{0.5\textwidth}" + "\n" + r"\begin{tikzpicture}\begin{axis} [mmt axis style,xmin=-1,xmax=5,xtick={-5,0,...,11},ymin=-1,ymax=15,ytick={-10,-5,...,15},]" + "\n" + r"\end{axis} \end{tikzpicture} \\ \hline" + "\n"
  problem = problem + r" Find the y-intercept for each function. & $ $" + r"\\ \hline" + "\n" + r"\end{tabular}\end{center}"

  return problem

def createanswer(equation=0, growth=0, model=0, yint=[], rate=0, graph=0, inty=0):
  problem = "\\begin{center} \n \\begin{tabular}{|l|c|} \\hline \n "
  problem = problem + r"$ $ & $" + str(equation) + r"$ \\ \hline" + " \n "
  problem = problem + r"Type of growth & $ " + growth + " $ \\\\ \hline" + "\n "
  problem = problem + r"\pbox{20cm}{What kind of sequence \\ corresponds to each model?} & $ " + model + r" $ \\ \hline" + "\n "
  problem = problem + r"Make a table of values & \begin{tabular}{c|c} \hline $x$ & $y$\\ \hline -1 & $ " + str(yint[0])
  problem = problem + r" $ \\ \hline 0 & $ " + str(yint[1])
  problem = problem + r" $ \\ \hline 1 & $ " + str(yint[2])
  problem = problem + r" $ \\ \hline 2 & $ " + str(yint[3])
  problem = problem + r" $ \\ \hline 3 & $ " + str(yint[4]) + r" $ \\ \end{tabular} \\ \hline" + "\n "
  problem = problem + r"Find the rate of change & $ " + str(rate) + r" $ \\ \hline" + "\n " 
  problem = problem + r"\pbox{20cm}{Graph each equation. \\ Compare the graphs. \\ What is the same? \\ What is different?} & " + graph + r"\\ \hline " + "\n "
  problem = problem + r"Find the y-intercept for each function. & $ " + str(inty) + r" $ \\ \hline" + "\n" + r"\end{tabular}\end{center}"

  return problem

def comparedifferent(diff = 1, expr="latex"):
  xtable = [-1, 0, 1, 2, 3]
  if diff == 1: #linear
    x = Symbol('x')
    a = notzero(-8, 8)
    b = notzero(-2, 10)
    xint = randint(-3, 5)
    equation = setlinearequation(a, xint, b)
    ytable = getyval(a * (x+xint) + b, xtable)
    graph = creategraph(equation, [ xtable[1], ytable[1] ],[ xtable[3], ytable[3] ], 0)
    yintercept = (a * xint) + b

    return createproblem(equation), createanswer(equation, "Linear", "Arithmetic", ytable, a, graph, yintercept)
  elif diff == 2: #quadratic
    x = Symbol('x')
    a = notzero(-3, 4)
    m = notzero(1, 4)
    xint = notzero(-2, 2)
    yint = randint(-2, 2)
    equation = setexpequation(a, m, xint, yint)
    ytable = getyval((a * (m**(x+xint))+yint), xtable)
    graph = creategraph(str(a)+"*+pow("+str(m)+","+str(x)+"+"+str(xint)+")+"+str(yint), [ xtable[1], ytable[1] ],[ xtable[3], ytable[3] ], 1)

    return createproblem(equation), createanswer(equation, "Exponential", "Geometric", ytable, m, graph, ytable[1])


    #!!!!! minipage, vspace, and textwidth are all on previous versions. must update before pushing onto official build