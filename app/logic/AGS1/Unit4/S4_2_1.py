import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from loader import LinFunc, getInt, x, QuadFunc, ExpFunc, PWFunc, graphPW
from sympy import *
from random import randint

# AGS1.4.2.1 - Find The Domain And Range.
# Option 1: Simple
# instruction : Find the domain and range for each function graphed below. Use interval notation to write your answer.

def PWDomRange_4_2_1(pieces=randint(1,3), cont=True, expr='latex'):
    endPts, pairs = [randint(-8,-3)], []

    for jj in range(pieces):
        if jj == 0:
            start = randint(-8,8)
        else:
            if cont or randint(0,1):
                start = pairs[-1][0].subs(x,endPts[jj])
            else:
                start = randint(-8,8)
        
        kind = randint(1,2)         # No exponential pieces yet
        if kind == 1:               # Linear
            slope = Rational(getInt(-6,6),randint(1,3))
            func = LinFunc(slope, [endPts[jj],start])
            step = randint(3,6) if slope.q==1 else randint(1,3)*slope.q
        elif kind == 2:             # Quadratic
            step = randint(2,4)
            func = QuadFunc.from2Pts(1, [endPts[jj],start], [endPts[jj]+step,start+randint(-4,4)])
        else:                       # Exponential           TODO: Fix exponential pieces
            step = randint(2,4)
            func = ExpFunc(Rational(1,randint(2,5)), [endPts[jj],start])
        
        endPts.append(endPts[jj] + step)
        interval = f'{endPts[jj]},{endPts[jj+1]}'
        if jj == 0:
            interval = ('(' + interval) if randint(0,1) else ('[' + interval)
        else:                       # Make sure intervals don't overlap
            if cont:
                interval = '[' + interval
            else:
                interval = ('(' + interval) if (pairs[-1][1][-1]==']' or randint(0,1)) else ('[' + interval)
        interval += ')' if (cont or randint(0,1)) else ']'

        expression = func.expr if type(func)!=ExpFunc else func.subs(func.variable-endPts[jj])*func.base**endPts[jj]
        pairs.append([expression, interval])
    
    func = PWFunc(*pairs)

    problem = graphPW(func, contDot=False)
    answer = func.printFeats(['domain','range'])

    return problem, answer

# for jj in range(8):
#     problem, answer = PWDomRange_4_2_1(randint(1,3), cont=True)
#     print(problem)
#     print(answer)