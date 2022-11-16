import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from sympy import *
from random import randint

# AGS1.2.6.2 - Monthly / Exponential
# instruction : Rewrite each of the expressions containing an annual interest rate to reveal a monthly, quarterly, or daily interest rate. Find the rate and provide the time period it would represent.

def Monthly_Exponential(diff = 1, expr = "latex"):
  ndict = [1, 4, 6, 12, 52, 365]
  sdict = ["annually", "quarterly", "semi-annually", "monthly", "weekly", "daily"]
  num = randint(0, 6)

  if diff == 1: #natural number
    inta = randint(1, 150)
    ans = "{:.4f}".format(inta ** (1 / ndict[num]))
  elif diff == 2: #decimal
    inta = randint(1, 100) / 100 + 1
    ans = "{:.4f}".format(inta ** (1 / ndict[num]))
  
  problem = "$(" + str(inta) + "^{\\frac{1}{" + str(ndict[num]) + "}})^{" + str(ndict[num]) +"t}$"
  answer = "$" + str(ans) + "^t$, " + sdict[num] + " rate of " + str(ans) 

  return problem, answer

"""
  File "c:\Users\smyu2\OneDrive\GitHub\AGS_Worksheet_Generator\app\logic\AGS1\Unit2\S2_6_2.py", line 29, in <module>
    print(monthlyexp(2))
  File "c:\Users\smyu2\OneDrive\GitHub\AGS_Worksheet_Generator\app\logic\AGS1\Unit2\S2_6_2.py", line 22, in monthlyexp
    ans = "{:.4f}".format(inta ** (1 / ndict[num]))
IndexError: list index out of range

"""