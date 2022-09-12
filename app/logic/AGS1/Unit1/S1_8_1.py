import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from loader import ArithSeq, getInt, GeoSeq, signify
from sympy import *
from random import randint

# 1.8.1 Fill the gap
# section 1
# Each of the tables given represents a sequence. Find the missing terms in the sequence, show your method, and create the explicit and recursive equations.

def Fill_The_Gap(kind='lin', expr='latex'):
    if kind == 'lin':
        seq = ArithSeq(getInt(-10,10), [1,getInt(-10,10)])
    else:
        seq = GeoSeq(getInt(-10,10), [1,getInt(-10,10)])

    case = randint(1,3)
    length = case + 3
    if case == 1:
        problem = seq.getTable(range(1,length), vals=[1,0,1], labels=['$x$','$y$'])
    elif case == 2:
        problem = seq.getTable(range(1,length), vals=[1,0,0,1], labels=['$x$','$y$'])
    else:
        problem = seq.getTable(range(1,length), vals=[1,0,0,1,0], labels=['$x$','$y$'])

    answer = seq.getTable(range(1,length), labels=['$x$','$y$'])
    if expr == 'latex':
        answer += signify(seq.getExplicit()) + r' \newline '
        answer += signify(seq.getRecursive())
    else:
        answer = [answer] + [seq]

    return problem, answer

for jj in range(10):
    problem, answer = Fill_The_Gap()
    print(problem)
    print(answer, r'\\ \\')