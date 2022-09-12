import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from loader import ArithSeq, brackify, GeoSeq, latexify, signify, tableGenerator
from sympy import *
from random import randint

# AGS1.2.4.2 - Fill In The Table - Fractional Exponent
# instruction : Fill in the missing values of the table based on the growth that is described, then create the explicit equation for the table.

def FillInTheTable_2_4_2(case=1, expr='latex'):
    primes = [2,3,5,7]
    ratioDescrips = {2: 'doubled', 3: 'tripled', 4: 'quadrupled'}
    labels = ['Years','Bacteria']

    if case == 1: # 1/3 case
        func = ExpFunc(choice(primes), getInt(-7,7,exclude=[-1,0,1]), variable=t)

        nums = [Rational(jj,3) for jj in range(10)]
        vals = [1] + 3*[0,0,1]
    else: # 1/2 cases (prime ratio and perfect square ratio)
        base = choice(primes) if case==2 else choice(primes)**2
        func = ExpFunc(base, getInt(-7,7,exclude=[-1,0,1]), variable=t)

        nums = [Rational(jj,2) for jj in range(9)]
        vals = [1] + 4*[0,1]
    
    if (func.base in [2,3,4]) and randint(0,1):
        problem = fr'The growth in the table is {ratioDescrips[func.base]} at each whole year. \newline '
    else:
        problem = fr'The values in the table grow by a factor of ${func.base}$ at each whole year. \newline '
    problem += func.getTable(nums, vals, vertical=False, labels=labels)
    
    answer = func.getTable(nums, vertical=False, labels=labels)
    answer += signify(func.getBaseInt(notation='b'))

    return problem, answer

for jj in range(10):
    problem, answer = FillInTheTable_2_4_2(randint(1,3))
    print(problem)
    print(answer, r'\\')