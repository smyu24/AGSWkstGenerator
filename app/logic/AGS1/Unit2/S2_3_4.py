import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from loader import getInt, LinFunc, startGraph, latexify, sample, endGraph, drawCurve
from sympy import *
from random import randint

# AGS1.2.3.4 - Find the Slope
# Instruction : Find the rate of change (slope) in each of the problems.


def Find_The_Slope_Table(case=1, expr="latex"):
    slope = Rational(getInt(-8,8),2)
    intercept = Rational(getInt(-12,12),2)
    func = LinFunc(slope, intercept)

    if case == 1: # table
        nums = sample(list(range(-15,26)), 4)
        nums.sort()
        problem = func.getTable(nums)
    elif case == 2: # points
        nums = sample(list(range(-15,26)), 2)
        nums.sort()
        problem = f'$({nums[0]},{latexify(func.subs(nums[0]))}), '
        problem += f'({nums[1]},{latexify(func.subs(nums[1]))})$'
    else: # graph
        problem = startGraph(-6,6,-6,6)
        problem += drawCurve(func.expr, -6, 6)
        problem += endGraph()

    answer = '$m =' + latexify(func.slope) + '$'

    return problem, answer