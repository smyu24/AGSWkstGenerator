#1.3.4 So, Should We Use Recursive Or Explicit?

# absolute path of the parent directory to the sys.path

import os; import sys; import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from loader import ArithSeq, getInt, GeoSeq, latexify, signify, tableGenerator
from sympy import *
from random import randint


def getSequenceDescription(seq, given=4):
    ratioDescrips = {2: 'doubled', 3: 'tripled', 4: 'quadrupled', Rational(1,2): 'halved'}
    
    description = r'The value of the \nth{' + str(given) + '} term is $' + latex(seq.findTerm(given)) + '$.  '
    if type(seq)==ArithSeq:
        changing = 'increasing' if seq.common>=0 else 'decreasing'
        description += fr'The sequence is {changing} by ${latex(abs(seq.common))}$ at each step.'
    elif type(seq)==GeoSeq:
        if seq.common in ratioDescrips.keys():
            change = ratioDescrips[seq.common]
        else:
            change = fr'multiplied by ${latex(seq.common)}$'
        description += f'The sequence is being {change} at each step.'

    return description

def Recursive_vs_Explicit(difficulty=1, expr='latex'):

    if difficulty == 1: # easy
        common = randint(2, 5)
        start = randint(1, 10)
    elif difficulty == 2: # medium
        common = getInt(-5, 5, exclude=[-1,0,1])
        start = getInt(-5, 5)
    elif difficulty == 3: # hard
        common = Rational(getInt(-5,5), randint(2,5))
        start = Rational(getInt(-5,5), randint(2,5))

    if randint(0,1):
        seq = ArithSeq(common, [1,start])
    else:
        seq = GeoSeq(common, [1,start])
    
    useExplicit = randint(0,1)

    problem = r'Explicit equation: $' + seq.getExplicit(0) + r'$ \newline '
    problem += r'Recursive equation: $\text{now} = \text{previous}'
    change = latexify(seq.common, seq.precision)
    if type(seq) == ArithSeq:
        problem += r' + ' if seq.common>0 else ''
    else:
        problem += r' \cdot '
        change = '(' + change +')'if seq.common<0 else change
    problem += change + r'$ \newline '

    if randint(0,1):
        if useExplicit:
            termNum = randint(30,80) if type(seq)==ArithSeq else randint(5,9)
            header = [r'term \#', 1, 2, r'$\ldots$', termNum]
            row = ['value', signify(latexify(seq.terms[1])), signify(latexify(seq.terms[2])), r'$\ldots$', '']
        else:
            termNum = 4
            header = [r'term \#', 1, 2, 3, 4]
            row = ['value', signify(latexify(seq.terms[1])), signify(latexify(seq.terms[2])), signify(latexify(seq.terms[3])), '']
        problem += tableGenerator(header, [row])
    else:
        givenNum = randint(2,4)
        if useExplicit:
            termNum = randint(30,80) if type(seq)==ArithSeq else randint(6,10)
        else:
            termNum = givenNum+randint(1,2)
        problem += getSequenceDescription(seq, given=givenNum) + r' \newline '
    
    problem += r'Find the value of the \nth{' + str(termNum) + '} term.'

    answer = seq.findTerm(termNum)
    answer = signify(latexify(answer, seq.precision)) if expr=='latex' else answer

    return problem, answer

for jj in range(10):
    problem, answer = Recursive_vs_Explicit(2)
    print(problem, r'\\')
    print(answer, r'\\ \\')