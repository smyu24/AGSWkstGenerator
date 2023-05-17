import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from loader import LinFunc, getInt, QuadFunc, ExpFunc, PWFunc, graphPW, ArithSeq, GeoSeq, x
from sympy import *
from random import randint

#section 1 : mix of functions

def PWChars(pieces=randint(3,5), cont=True, expr='latex'):
    endPts, pairs = [0], []

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

    problem = graphPW(func, contDot=True)
    answer = func.printFeats()

    return problem, answer

# for jj in range(5):
#     problem, answer = PWChars(randint(3,5), cont=False)
#     print(problem)
#     print(answer)


#section 2 : recursive
def SeqFeats(kind='lin'):                   # TODO: Answer
    if kind == 'lin':
        seq = ArithSeq(randint(-7,7), [1,randint(-50,50)])
    elif kind == 'exp':
        base = randint(2,5) if randint(0,1) else Rational(1,randint(2,5))
        seq = GeoSeq(base, [1,getInt(-7,7)])

    problem = seq.getRecursive() + r' \newline '
    problem += r'First five terms of the sequence: \newline '
    problem += r'Domain: \newline Range: \newline Maximum: \newline Minimum \newline '
    problem += r'Intercept(s): \newline Interval(s) of increase: \newline Interval(s) of decrease: \newline '
    problem += r'Discrete/Continuous/Discontinuous:'

    answer = fr'First five terms of the sequence: ${seq.getSeqStr(range(1,6))}$ \newline '
    answer += fr'Domain: \newline Range: \newline '
    answer += fr'Maximum: \newline Minimum \newline '
    answer += fr'Intercept(s): \newline '
    answer += fr'Interval(s) of increase: \newline '
    answer += fr'Interval(s) of decrease: \newline '
    answer += fr'Discrete/Continuous/Discontinuous: Discrete'

    return problem, answer

# for jj in range(5):
#     problem, answer = SeqFeats()
#     print(problem)
#     print(answer)