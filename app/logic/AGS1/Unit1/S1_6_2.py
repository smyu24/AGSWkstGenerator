# 1.6.2 Is It Arithmetic Or Geometric Sequence
# section1:
# instruction: Find the missing values for each arithmetic or geometric sequence. Select whether it has a constant difference or a constant ratio. State the value of the constant difference or ratio. Indicate if the sequence is arithmetic or geometric by selecting the correct answer.
import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from loader import ArithSeq, getInt, GeoSeq, latexify, signify, makeWordProb
from sympy import *
from random import randint

def Is_It_Arithmetic_Or_Geometric_Sequence(case=1, expr="latex"):
    if case == 1:           # arithmetic list
        seq = ArithSeq(getInt(-10,10), [1,getInt(-10,10)])
        problem = signify(seq.getSeqStr([1,2,3,'',5,6,'']))
    elif case == 2:         # geometric list
        mult = getInt(-5,5,exclude=[-1,0,1])
        ratio, startnum = [mult, 1] if randint(0,1) else [Rational(1,mult), 5]
        seq = GeoSeq(ratio, [startnum,getInt(-5,5)])
        problem = signify(seq.getSeqStr([1,2,'',4,'']))
    else:         # word problems (case 3=arithmetic, case 4=geometric)
        problem, solns, _ = makeWordProb('lin', expr) if case==3 else makeWordProb('exp', expr)
        if type(solns[0]) != list:
            seq = ArithSeq(solns[0],solns[1]) if case==3 else GeoSeq(solns[0],solns[1])
        else:
            seq = ArithSeq.fromPts(solns[0],solns[1]) if case==3 else GeoSeq.fromPts(solns[0],solns[1])

    answer = '(a) ' + signify(seq.getSeqStr(range(1,8))) + r' \newline (b) '
    answer += 'Arithmetic' if case in [1,3] else 'Geometric'
    answer += r' \newline (c) Common '
    answer += 'difference' if case in [1,3] else 'ratio'
    answer += fr' $={latexify(seq.common,seq.precision)}$' + r'\newline (d) ' + signify(seq.getExplicit())
    answer += r' \newline (e) ' + signify(seq.getRecursive())

    return problem, answer