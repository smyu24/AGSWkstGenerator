import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

#makeWordProb is broken because of lack of access to csv
from loader import makeWordProb, LinFunc, ExpFunc, latexify, signify, getInt, startGraph, drawCurve, drawScatter, endGraph, x, y
from sympy import *
from random import randint

# AGS1.2.3.2 - Details Of Linear And Geometric Sequences
# introduction : Based on each of the word problems, determine the following.

def LinOrExp_2_3_2(case=1, expr='latex'):       #TODO: discrete vs. continuous
    if case in [1,2]:               # Linear, discrete and continuous
        kind = 'lin'
    elif case in [3,4]:             # Exponential, discrete and continuous
        kind = 'exp'
    else:
        kind = 'neither'
    problem, solns, _ = makeWordProb(kind, expr)
    
    if case == 5:
        answer = '(a) Neither'
    else:                           # Linear or exponential
        if type(solns[0]) != list:
            func = LinFunc(solns[0],solns[1]) if kind=='lin' else ExpFunc(solns[0],solns[1])
        else:
            func = LinFunc.fromPts(solns[0],solns[1]) if kind=='lin' else ExpFunc.fromPts(solns[0],solns[1])

        answer = r'(a) Linear \newline ' if kind=='lin' else r'(a) Exponential \newline '
        answer += r'(b) Discrete \newline ' if case in [1,3] else r'(b) Continuous \newline '
        answer += fr'(c) $d={latexify(func.slope)}$ \newline ' if kind=='lin' else fr'(c) $r={latexify(func.base)}$ \newline'
        answer += fr'(d) ${func.getSlopeInt()}$ \newline ' if kind=='lin' else fr'(d) ${func.getBaseInt()}$ \newline '

    return problem, answer

for jj in range(10):
    problem, answer = LinOrExp_2_3_2(case=3)
    print(problem, r'\\')
    print(answer)


# Instrcutiont : Based on each of the linear equations, determine the following.

def LinOrExpEq_2_3_2(case=1, expr='latex'):                 # TODO: transcental equations     
    if case <= 3:               # Linear
        if case == 1:
            aa, bb, cc = randint(-10,10), getInt(-10,10), randint(-10,10)
        elif case == 2:
            aa, bb, cc = randint(-10,10), Rational(getInt(-9,9),randint(2,7)), randint(-10,10)
        elif case == 3:
            aa, bb, cc = randint(-10,10), Rational(getInt(-9,9),randint(2,7)), Rational(getInt(-9,9),randint(2,7))
        func = LinFunc(-aa/bb, cc/bb)

        problem = f'${latex(aa*x)}' if aa!=0 else '$'
        problem += f'{latex(bb*y)}' if (aa==0 or bb<0) else f'+{latex(bb*y)}'
        problem += f'={latex(cc)}$'
        
        answer = r'(a) Linear \newline (b) Continuous \newline '
        answer += fr'(c) slope, $d={latexify(func.slope)}$ \newline'
        answer += fr'(d) ${func.getSlopeInt("y")}$'
    
    elif case in [4,5,6,7,8]:             # Exponential
        if case == 4:
            base, shift = randint(2,20), getInt(-10,10)
            intercept = 1 + shift
        elif case == 5:
            base, intercept, shift = randint(2,20), getInt(-10,10), 0
        elif case == 6:
            base, intercept, shift = randint(2,20), Rational(getInt(-9,9),randint(2,7)), 0
        elif case == 7:
            base, intercept, shift = Rational(getInt(-9,9),randint(2,7)),Rational(getInt(-9,9),randint(2,7)), 0
        elif case == 8:
            base, intercept, shift = Rational(getInt(-9,9),randint(2,7)), getInt(-10,10), 0
        func = ExpFunc(base, intercept, shift)

        problem = signify(func.getBaseInt('y')) if case!=4 else signify(latex(base**x) + f'-y={latex(-shift)}')
        
        answer = r'(a) Exponential \newline (b) ' 
        answer += r'Continuous \newline ' if base>0 else r'Discrete \newline '
        answer += fr'(c) growth factor/base, $r={latexify(func.base)}$ \newline'
        answer += fr'(d) ${func.getStdForm("y")}$'

    return problem, answer

for jj in range(10):
    problem, answer = LinOrExpEq_2_3_2(case=randint(4,8))
    print(problem, r'\\')
    print(answer, r'\\ \\')

# Instrcutiont : Based on each of the graphs, determine the following.

def LinOrExpGraph_2_3_2(case=1, expr='latex'):
    if case in [1,2]:               # Linear
        func = LinFunc(getInt(-10,10),randint(-10,10))

        answer = r'(a) Linear \newline (b) '
        answer += r'Continuous \newline ' if case==1 else r'Discrete \newline '
        answer += fr'(c) slope, $d={latexify(func.slope)}$ \newline '
        answer += fr'(d) ${func.getSlopeInt()}$'
    elif case in [3,4]:             # Exponential
        func = ExpFunc(Rational(getInt(-3,3),getInt(-3,3)), getInt(-5,5))

        answer = r'(a) Exponential \newline (b) '
        answer += r'Continuous \newline ' if case==3 else r'Discrete \newline '
        answer += fr'(c) growth factor/base, $r={latexify(func.base)}$ \newline '
        answer += fr'(d) ${func.getBaseInt()}$'
    
    problem = startGraph()
    problem += drawCurve(func.expr,-10,10) if case in [1,3] else drawScatter([[jj,func.subs(jj)] for jj in range(-10,11)])
    problem += endGraph()

    return problem, answer

for jj in range(10):
    problem, answer = LinOrExpGraph_2_3_2(case=randint(1,4))
    print(problem, r'\\')
    print(answer)


# Instrcutiont : Based on each of the tables, determine the following.

