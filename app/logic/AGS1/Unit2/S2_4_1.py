import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from loader import ArithSeq, brackify, GeoSeq, latexify, signify, tableGenerator
from sympy import *
from random import randint

# AGS1.2.4.1 - Square Roots
# instruction : Rewrite each of the square roots below by removing repeated factors from under the square root.

def SqrtSimplify(expr='latex'):
    primes = sample([2,3,5,7],3)
    primes.sort()

    case = randint(1,6)
    if case <= 3:
        base = (primes[0]*primes[1]**2) * (primes[2]**(case-1))
    elif case == 4:
        base = (primes[0]*primes[1]*primes[2])**2
    elif case == 5:
        base = (primes[0]*primes[1]**2) * primes[2]**3
    else:
        base = primes[0]*primes[1]*primes[2]
    
    problem = sqrt(base, evaluate=False)
    answer = simplify(problem)

    if expr == 'latex':
        problem = '$' + latex(problem) + '$'
        answer = '$' + latex(answer) + '$'

    return problem, answer

for jj in range(10):
    problem, answer = SqrtSimplify()
    print(problem, r'\\ ')
    print(answer, r'\\ \\')