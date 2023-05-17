import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from loader import LinFunc, getInt, minipagify, signify
from sympy import *
from random import randint

def LinSysTable_3_3_1(expr='latex'):
    pt = [randint(0,4),randint(-10,10)]
    func1 = LinFunc(getInt(-4,4), pt)
    func2 = LinFunc(getInt(-4,4, exclude=[0,func1.slope]), pt, label='g')

    left = signify(func1.getSlopeInt()) + func1.getTable(range(5),vals=False)
    right = signify(func2.getSlopeInt()) + func2.getTable(range(5),vals=False)
    problem = minipagify(left, right)
    problem += 'Point of intersection:'

    left = signify(func1.getSlopeInt()) + func1.getTable(range(5))
    right = signify(func2.getSlopeInt()) + func2.getTable(range(5))
    answer = minipagify(left, right)
    answer += fr'Point of intersection: $({pt[0]},{pt[1]})$'

    return problem, answer

# for jj in range(5):
#     problem, answer = LinSysTable_3_3_1()
#     print(problem, r'\\')
#     print(answer, r'\\')