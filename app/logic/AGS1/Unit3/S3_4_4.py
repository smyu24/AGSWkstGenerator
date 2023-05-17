import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from loader import LinFunc, getInt, ExpFunc, PWFunc, graphPW
from sympy import *
from random import randint, choice

def graphChars_3_4_4(expr='latex'):
    case = randint(1,2)

    start = randint(-8,2) if randint(0,9) else -oo
    if randint(0,9):
        end = (start+randint(4,10)) if start!=-oo else randint(4,10)
    else:
        end = choice([start+randint(4,10), oo]) if start!=-oo else choice([randint(4,10), oo])
    domain = choice(['(','[']) + f'{start},{end}' + choice([')',']'])
    
    if case == 1:           # Linear
        func = LinFunc(getInt(-3,3),randint(-3,3))
    elif case == 2:         # Exponential
        base = randint(2,4) if randint(0,1) else Rational(1,randint(2,4))
        func = ExpFunc(base, [randint(-3,3),randint(-3,3)], randint(-3,3))

    func = PWFunc([func.expr,domain])
    problem = graphPW(func)

    answer = func.printFeats(['domain','range'])
    feats = func.getFeats(['change'])
    answer += 'Decreasing' if feats['dec']!=EmptySet else 'Increasing'

    return problem, answer

# for jj in range(5):
#     problem, answer = graphChars_3_4_4()
#     print(problem)
#     print(answer)