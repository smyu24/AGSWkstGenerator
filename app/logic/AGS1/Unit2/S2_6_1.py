import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from sympy import *
from random import randint

# AGS1.2.6.1 - Percent Increase / Decrease
# instruction : Find the percent increase or decrease in each of the functions.

import pandas as pd

def perequation():
  fname = ["f", "k", "z", "g", "d", "t"]
  fnum = randint(0, 5)
 
  frontnum = randint(15, 54)
  pm = randint(0, 1)
  if(pm == 0):
    ans = randint(1, 100)
    answer = str(ans) + "\\% decrease"
  elif(pm == 1):
    ans = randint(1, 100) + 100
    answer = str(ans - 100) + "\\% increase"

  pro = ans / 100
  problem = "$" + fname[fnum] + "(x) = " + str(frontnum) + "(" + str(pro) + ")^x$"

  return problem, answer

def pertable():
  fname = ["f", "k", "z", "g", "d", "t"]
  fnum = randint(0, 5)

  frontnum = randint(30, 200)
  pm = randint(0, 1)
  if(pm == 0):
    ans = randint(1, 100)
    answer = str(ans) + "\\% decrease"
  elif(pm == 1):
    ans = randint(1, 100) + 100
    answer = str(ans - 100) + "\\% increase"

  tablenum = []
  tablenum.append(frontnum)
  for i in range(1, 5):
    frontnum = (frontnum * (ans/100))
    tablenum.append( "{:.2f}".format(frontnum) )

  problem = "\\begin{tabular}{| C | C |}\n \\hline"
  problem = problem + "\hline x & " + fname[fnum] + "(x)\\ "
  for i in range(5):
    problem = problem + str(i) + "&" + str(tablenum[i]) + "\\\\ \n \\hline"
  problem = problem + "\n\end{tabular}"

  return problem, answer

#??