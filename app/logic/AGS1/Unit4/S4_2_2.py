import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from loader import makeInterval, oo, signify, graphSet, x, latex
import sympy
from random import randint, choice 

"""
AGS1.4.2.2 - Graph Inequality
Option 1: Simple
instruction : For each of the inequalities, graph the values being described on the numbers lines.
"""

def graphInequal_4_2_2():
    start = randint(-20,10) if randint(0,9) else -oo
    if randint(0,9):
        end = (start+randint(10,30)) if start!=-oo else randint(-10,10)
    else:
        end = choice([start+randint(10,30), oo]) if start!=-oo else randint(-10,10)    
    interval = makeInterval(choice(['(','[']) + f'{start},{end}' + choice([')',']']))

    problem = signify(latex(interval.as_relational(x)))

    answer,_ = graphSet(interval)

    return problem, answer

# for jj in range(10):
#     problem, answer = graphInequal_4_2_2()
#     print(problem, r'\\')
#     print(answer)