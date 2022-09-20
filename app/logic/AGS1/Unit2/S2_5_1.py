import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from loader import sample
from sympy import *
from random import randint

# AGS1.2.5.1 - Higher Order Roots 
# instruction : Rewrite each of the radical expressions to remove perfect square factors from inside the radical.

def RadicalSimplify(expr='latex'):
    primes = sample([2,3,5,7],3)
    primes.sort()

    root = randint(2,5)
    if root == 2:
        if randint(0,1):
            problem = sqrt(primes[1]*primes[0]**2, evaluate=False)
        else:
            problem = sqrt(primes[0]*primes[1]*primes[2])
    else:
        case = randint(1,6)
        if case <= 4:
            base = (primes[1]**(case-1)) * (primes[0]**root)
        elif case == 5:
            base = primes[2] * (primes[1]**(root-1)) * (primes[0]**root)
        elif case == 6:
            base = (primes[2]**2) * (primes[0]*primes[1])**root
        problem = real_root(base, root, evaluate=False)

    answer = simplify(problem)

    if expr == 'latex':
        problem = '$' + latex(problem) + '$'
        answer = '$' + latex(answer) + '$'

    return problem, answer

for jj in range(10):
    problem, answer = RadicalSimplify()
    print(problem, r'\\ ')
    print(answer, r'\\ \\')