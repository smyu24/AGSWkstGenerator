import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from loader import ArithSeq, brackify, GeoSeq, latexify, signify, tableGenerator
from sympy import *
from random import randint

# AGS1.2.7.1 - Fill In The Table
# instruction : Fill in the table of values for each function.

def FillInTheTable(option='exp', expr='latex'):
    header = ['$x$', '$f(x)$']
    rows = []

    if option == 'lin': # linear
        start = getInt(-5, 5)
        diff = getInt(-5, 5)
        seq = ArithSeq(diff, [1,start])
    if option == 'exp': # exponential
        start = choice([-3,-2,2,3])
        ratio = choice([Rational(1,2), Rational(1,3), 2,3,4])
        seq = GeoSeq(ratio, [1,start])

    terms = latexify(seq.getTerms(num=5, startnum=-2))
    for jj in range(-1, 4):
        rows.append([signify(str(jj)), r'\phantom' + brackify(signify(terms[jj]))])
    emptyTable = tableGenerator(header, rows, table_env=False)
    problems = []
    answers = []
    for case in [0,1,2,-1]:
        if option=='lin':
            func = LinFunc(diff,[case,start])
            func = func.getPtSlope(case) if case!=0 else func.getSlopeInt()
        else:
            func = ExpFunc(ratio,[case,start])
            func = func.getPtBase(case) if case!=0 else func.getBaseInt()
        problems.append([func, emptyTable])

        for jj in range(5):
            rows[jj][1] = signify(terms[jj-case])
        answers.append(tableGenerator(header, rows, table_env=False))

    if expr=='latex':
        problem = ''
        answer = ''
        for jj in range(4):
            if jj%2==0:
                problem += '\\vspace{0.25in}\n'
                answer += '\\vspace{0.25in}\n'
            problem += '\\begin{minipage}[t]{0.5\\textwidth}\n'
            problem += '$' + problems[jj][0] + '$ \n'
            problem += problems[jj][1] + '\n\\end{minipage}\n'
            answer += '\\begin{minipage}[t]{0.5\\textwidth}\n'
            answer += '$' + problems[jj][0] + '$ \n'
            answer += answers[jj] + '\n\\end{minipage}\n'
    else:
        problem = problems
        answer = answers

    return problem, answer
  

for i in range(1):
    problem, answer = FillInTheTable(option='exp')
    print(problem, answer)