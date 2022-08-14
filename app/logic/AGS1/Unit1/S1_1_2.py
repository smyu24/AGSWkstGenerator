# absolute path of the parent directory to the sys.path

import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from loader import ExpFunc, emptyGraph, LinFunc, drawPt, startGraph, endGraph
from sympy import *
from random import randint,sample


def Graph_The_Ordered_Pairs(difficulty=1):
    if difficulty == 1: # easy
        vals = True
        if randint(0,1):
            func = LinFunc(randint(1,4), randint(1,4))
        else:
            func = LinFunc(randint(-4,-1), randint(10,14))
    elif difficulty == 2: # medium
        vals = True
        if randint(0,1):
            func = ExpFunc(randint(2,4), randint(1,4))
        else:
            denom = randint(2,4)
            start = randint(1,4)*denom**3
            func = ExpFunc(Rational(1,denom), start)
    elif difficulty == 3: # hard
        vals = False
        if randint(0,1):
            func = LinFunc(randint(1,4), randint(1,4))
        else:
            func = ExpFunc(randint(2,4), randint(1,4))

    ymax = 15 if type(func)==LinFunc else 30
    nums = sample(list(range(0,11)),4)
    nums.sort()
    problem = func.getTable(nums,vals,labels=['$x$','$y$'])

    if difficulty == 3:
        problem = '$y = ' + str(func) + r'$ \newline ' + problem
    problem += emptyGraph(ymax=ymax)

    answer = startGraph(ymax=ymax)
    pts = [drawPt([jj,func.subs(jj)]) for jj in nums]
    answer += ' '.join(pts) + endGraph()

    if difficulty == 3:
        answer = func.getTable(nums,labels=['$x$','$y$']) + answer

    return problem, answer
