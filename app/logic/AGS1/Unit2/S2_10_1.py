import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from loader import ArithSeq, brackify, GeoSeq, latexify, signify, tableGenerator
from sympy import *
from random import randint

# AGS1.2.10.1 - Slope-Intercept / Point-Slope Form
# instruction : Use the given information to create an explicit equation. Your explicit equation should be in either slope-intercept ( y=mx+b ) or point-slope form ( y=m(x−x1)+y1 ). Use the form that is most efficient based on the given information.

def LinearForms_2_10_1(case=1, expr='latex'):
    func = LinFunc(getInt(-9,9), getInt(-9,9))
    if case == 1: # slope and point
        problem = fr'$m = {latexify(func.slope)},\quad '
        if randint(0,1): # from intercept
            problem += fr'b = {latexify(func.intercept)}$'
            answer = signify(func.getSlopeInt())
        else: # from point
            pt = getInt(-9,9)
            answer = signify(func.getPtSlope(pt))

            pt = [latexify(pt), latexify(func.subs(pt))]
            problem += fr'({pt[0]},{pt[1]})$'
    else: # from table
        problem = func.getTable([32,33,34,35],labels=['$x$','$y$'])
        answer = signify(func.getSlopeInt() + r',\quad ' + func.getPtSlope(33))

    return problem, answer

for jj in range(10):
    problem, answer = LinearForms_2_10_1()
    print(problem, r'\\')
    print(answer, r'\\')


# instruction : For each table of values, write two different explicit equations in point-slope form and slope-intercept form.

for jj in range(10):
    problem, answer = LinearForms_2_10_1(case=2)
    print(problem, r'\\')
    print(answer, r'\\')