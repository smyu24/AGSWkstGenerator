## 1.2.3 Finding Patterns In Geometric Shapes

#Growing, growing Dots
# LOOK AT THE GOOGLE COLAB MODULE 1

# parameter will be a random selection from a static array
#of ["lin", "exp"]

# absolute path of the parent directory to the sys.path

import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from loader import ArithSeq, brackify, GeoSeq
from random import randint

def Finding_Patterns_In_Geometric_Shapes(kind='lin'):
    if kind == 'lin':
        case = randint(1,6)
        growth, intercept = [randint(1,4),randint(-1,3)]
        if case == 1: # line of dots
            diff = growth
            problem, answer = [r'\dotPattern']*2
        elif case in [2,3]: # wide  or tall L
            diff = 2*growth
            problem, answer = [r'\wideLdotPattern']*2 if case==2 else [r'\tallLdotPattern']*2
        elif case in [4,5]: # wide or tall T
            diff = 3*growth
            problem, answer = [r'\wideTdotPattern']*2 if case==4 else [r'\tallTdotPattern']*2
        elif case == 6: # rectangle
            diff = intercept*growth
            problem, answer = [r'\polyRectanglePattern{0}']*2

        seq = ArithSeq(diff, intercept)
        problem += brackify(growth) + brackify(intercept) + '{1}{3}{2}'
        answer += brackify(growth) + brackify(intercept) + '{4}{5}{2}'
    elif kind == 'exp':
        growth1, growth2 = randint(2,3), randint(1,2)
        seq = GeoSeq(growth1*growth2, randint(2,3))
        problem, answer = [r'\expRectanglePattern']*2
        problem += brackify(growth1) + brackify(growth2) + brackify(seq.intercept) + '{1}{3}{2}'
        answer += brackify(growth1) + brackify(growth2) + brackify(seq.intercept) + '{4}{5}{2}'

    return problem, answer