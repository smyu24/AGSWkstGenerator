import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from loader import ArithSeq, brackify, GeoSeq, latexify, signify, tableGenerator
from sympy import *
from random import randint

# AGS1.2.8.1 - Fill In The Missing Numbers As Arithmetic & Geometric Sequence
# instruction : The first and fifth terms of a sequence are given. Fill in the missing numbers if it is an arithmetic sequence. Then fill in the numbers if it is a geometric sequence. Write the explicit rule for each function.

def FillInTheMeansTable(expr='latex'):
    ratio = randint(2,7)
    start = getInt(-9,9)
    geo = GeoSeq(ratio,[1,start])
    geoterms = latexify(geo.getTerms(5))
    end = geo.findTerm(5)

    row = [signify(geoterms[1]), r'\phantom{$' + geoterms[2] + r'$}', r'\phantom{$' + geoterms[3] + r'$}', r'\phantom{$' + geoterms[4] + r'$}', signify(geoterms[5])]
    header = ['Arithmetic'] + row
    row = ['Geometric'] + row
    
    if randint(0,1):
        problem = tableGenerator(header, [row])
        row[2:5] = [signify(geoterms[2]), signify(geoterms[3]), signify(geoterms[4])]

        arith = ArithSeq.fromPts([1,start],[5,end],variable=n)
    else:
        header[1:] = header[:0:-1]
        row[1:] = row[:0:-1]
        problem = tableGenerator(header, [row])
        row[2:5] = [signify(geoterms[4]), signify(geoterms[3]), signify(geoterms[2])]
        
        geo = GeoSeq.fromPts([1,end],[5,start],variable=n)
        arith = ArithSeq.fromPts([1,end],[5,start],variable=n)

    arithterms = latexify(arith.getTerms(4))
    header[2:5] = [signify(arithterms[2]), signify(arithterms[3]), signify(arithterms[4])]
    answer = tableGenerator(header, [row])
    if expr=='latex':
        answer += r'\newline ' + signify(arith.getExplicit()) + r'\newline '
        answer += signify(geo.getExplicit())
    else:
        answer = [answer, arith, geo]

    return problem, answer

for jj in range(5):
    problem, answer = FillInTheMeansTable()
    print(problem)
    print(answer)