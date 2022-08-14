import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from loader import ArithSeq, getInt, GeoSeq, makeWordProb, signify, startGraph, endGraph, drawPt, emptyGraph
from sympy import *

# 1.5.1 Information To Geometric sequence.

# section 1
# instruction : In the next problems, you are given various types of information. Write the recursive and explicit functions for each geometric sequence. Finally, graph each sequence, making sure you clearly label the axes.

def infoToSeq(case=1, kind='lin', expr='latex'):
    if case == 1: # word problem
        problem, solns, labels = makeWordProb(kind, expr)
        problem += r' \newline '

        if type(solns[0]) != list:
            seq = ArithSeq(solns[0],solns[1]) if kind=='lin' else GeoSeq(solns[0],solns[1])
        else:
            seq = ArithSeq.fromPts(solns[0],solns[1]) if kind=='lin' else GeoSeq.fromPts(solns[0],solns[1])
    else:
        common = getInt(-7,7) if kind=='lin' else getInt(-5,5,exclude=[-1,0,1])
        start = getInt(-5,5)
        seq = ArithSeq(common, [1,start]) if kind=='lin' else GeoSeq(common, [1,start])
        labels = ['$n$', '$f(n)$']

        if case == 2: # list
            problem = seq.getSeqStr() + r' \newline '
        elif case == 3: # table
            problem = seq.getTable([1,2,3,4]) #+ r' \newline '
        elif case == 4: # graph
            problem = startGraph(-1,10,-10,10)
            for jj in range(1,5):
                problem += drawPt([jj,seq.findTerm(jj)])
            problem += endGraph() + r' \newline '

    answer = 'a) ' + signify(seq.getRecursive()) + r' \newline '
    answer += 'b) ' + signify(seq.getExplicit()) + r' \newline '
    if case != 3:
        problem += seq.getTable(range(1,6), vals=False, labels=labels) #+ r' \newline '
        answer += seq.getTable(range(1,6), labels=labels) #+ r' \newline '
    if case != 4:
        problem += emptyGraph(-1,10,-10,10)
        answer += startGraph(-1,10,-10,10)
        for jj in range(1,5):
            answer += drawPt([jj,seq.findTerm(jj)])
        answer += endGraph() + r' \newline '

    if expr != 'latex':   
        answer = seq

    return problem, answer

for jj in range(10):
    problem, answer = infoToSeq(case=1,kind='exp')
    print(problem)
    print(answer)