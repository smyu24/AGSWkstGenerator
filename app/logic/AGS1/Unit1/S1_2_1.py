# absolute path of the parent directory to the sys.path
import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from loader import ExpFunc, getInt, GeoSeq, ArithSeq, latexify, signify, tableGenerator, makeWordProb
from random import randint

def Fill_In_The_Sequence_1(difficulty=1 ,expr='latex'):
    header = ['Term',	'1st','2nd','3rd','4th','5th','6th','7th','8th']
    values = ['Value']
    numterms = len(header) - 1

    if difficulty == 1: # easy
        if randint(0,1):
            start = getInt(-10, 10)
            ratio = getInt(2, 4)
            seq = GeoSeq(ratio, [1,start])
        else:
            start = getInt(-10, 10)
            diff = getInt(-4, 4)
            seq = ArithSeq(diff, [1,start])
    if difficulty == 2: # medium
        if randint(0,1):
            start = getInt(-10, 20)
            ratio = getInt(-4, 4, exclude=[-1,0,1])
            seq = GeoSeq(ratio, [1,start])
        else:
            start = getInt(-20, 20)
            diff = getInt(-15, 15)
            seq = ArithSeq(diff, [1,start])
    if difficulty == 3: # hard
        if randint(0,1):
            start = getInt(-20, 20)
            ratio = getInt(-6, 6, exclude=[-3,-2,-1,0,1,2,3])
            seq = GeoSeq(ratio, [1,start])
        else:
            start = getInt(-50, 50)
            diff = getInt(-30, 30)
            seq = ArithSeq(diff, [1,start])

    terms = latexify(seq.getTerms(numterms))
    for jj in range(1,numterms+1):
        if jj <= 4:
            values.append(signify(terms[jj]))
        else:
            values.append(r'\phantom{$'+ terms[jj] + '$}')
    problem = tableGenerator(header, [values], table_env=False)

    if expr == "latex":
        for jj in range(5,numterms+1):
            values[jj] = signify(terms[jj])
        answer = tableGenerator(header, [values], table_env=False)
    else:
        answer = terms

    return problem, answer

### section2:
#### Use the given values in the table to determine a pattern and complete the table.

#type to not have easy,medium, hard (no option for that)
#pass down rand arraycontaining string of either ["lin", "exp", "neither"]

def Fill_In_The_Sequence_2(kind='lin', expr='latex'):
    problem, solns, labels = makeWordProb(kind, expr)
    
    if kind in ['lin','exp']:
        if type(solns[0]) != list:
            seq = ArithSeq(solns[0],solns[1]) if kind=='lin' else GeoSeq(solns[0],solns[1])
        else:
            seq = ArithSeq.fromPts(solns[0],solns[1]) if kind=='lin' else GeoSeq.fromPts(solns[0],solns[1])
        
        problem += seq.getTable(range(1,7), vals=False, vertical=False, labels=labels)
        
        answer = seq.getTable(range(1,7), vertical=False, labels=labels) if expr=='latex' else seq
    else:
        answer = 'Neither.'

    return problem, answer


### Section 3:
#### instruction Evaluate	the	following	equations	when	x	=	{	1,	2,	3,	4,	5	}.		Organize	your	inputs	and	outputs	into	a	table	of	values	for	each	equation. Let	x	be	the	input	and	y	be	the	output.

def Fill_In_The_Sequence_3(difficulty=1, expr='latex'):
    labels = [r'$x$ input', r'$y$ output']

    if difficulty == 1: # easy
        ratio = getInt(2, 6)
        func = ExpFunc(ratio, 1)
    if difficulty == 2: # medium
        ratio = getInt(2, 6)
        if randint(0,1):
            ratio *= -1
            func = ExpFunc(ratio, 1)
        else:
            func = ExpFunc(ratio, -1)
    if difficulty == 3: # hard
        ratio = getInt(2, 6)
        start = getInt(-6, 6, exclude=[-1,0,1])
        if randint(0,1):
            ratio *= -1
        func = ExpFunc(ratio, start)

    problem = '$' + func.getBaseInt(notation='y') + r'$ \newline '
    problem += func.getTable(range(1,6),vals=False,labels=labels)
    if expr == "latex":
        answer = func.getTable(range(1,6),labels=labels)
    else:
        answer = func.subSet(range(1,6))

    return problem, answer