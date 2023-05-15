import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from loader import ArithSeq, getInt, GeoSeq, signify
from sympy import *
from random import randint

# AGS1.2.3.3 - Fill in the blanks
# Instruction : For each arithmetic sequence below, find the missing terms in the sequence. Then write an explicit rule for the sequence.

def Fill_In_The_Blanks(kind='lin', expr='latex'):
    if kind == 'lin':
        seq = ArithSeq(getInt(-10,10), [1,getInt(-10,10)])
    else:
        seq = GeoSeq(getInt(-10,10), [1,getInt(-10,10)])

    case = randint(1,3)
    if case == 1:
        problem = seq.getTable(range(1,8), vals=[1,0,1,0,1,0,1], vertical=False, labels=['Term','Value'])
    elif case == 2:
        problem = seq.getTable(range(1,8), vals=[1,0,0,1,0,0,1], vertical=False, labels=['Term','Value'])
    else:
        problem = seq.getTable(range(1,8), vals=[1,0,0,0,0,0,1], vertical=False, labels=['Term','Value'])

    if expr == 'latex':
        answer = seq.getTable(range(1,8), vertical=False, labels=['Term','Value'])
        answer += signify(seq.getExplicit())

        if kind=='geo' and case!=2:
            seq = GeoSeq(-1*seq.base, [1,seq.start])
            answer += seq.getTable(range(1,8), vertical=False, labels=['Term','Value'])
            answer += signify(seq.getExplicit())
    else:
        answer = seq

    return problem, answer
