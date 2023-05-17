import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from loader import GeoSeq, getInt, ArithSeq, signify
from sympy import *
import random

def Finding_Explicit_And_Recursive_Equations_3_3_3(expr='latex',case=1,lin_or_geo='lin'):
    '''
    expr = latex or sympy
    case = 1 easy 2 medium 3 hard
    lin_or_geo = force to generate lin or geo 
    '''
    if lin_or_geo == 'geo' or random.randint(0,1) == 1:
        seq = GeoSeq(getInt(-4,4), [1,getInt(-5,5)])
    else:
        seq = ArithSeq(getInt(-10,10), [1,getInt(-10,10)])
    
    if case == 1:
        start = 1
        problem = seq.getTable(range(1,4), vals=[1,1,1,1], vertical=True, labels=[fr'$n$',fr'$f(n)$'])
    elif case == 2:
        start = random.randint(2,6)
        finish = start + 4
        problem = seq.getTable(range(start,finish), vals=[1,1,1,1], vertical=True, labels=[fr'$n$',fr'$f(n)$'])
    else:
        start = random.randint(4,12)
        if lin_or_geo == 'geo' or random.randint(0,1) == 1:
            seq = GeoSeq(getInt(-3,3), [start,getInt(-3,3)])
        terms = seq.getTerms(12,start)
        keys = sorted(random.sample(list(terms),4))
        vals = [terms[i] for i in keys]
        problem = seq.getTable(keys, vals, vertical=True, labels=[fr'$n$',fr'$f(n)$'])
      
    if expr == 'latex':
        answer='Explicit ' + signify(seq.getExplicit(start)) + r'\newline'+' Recursive '+signify(seq.getRecursive(start))
    else:
        answer='Explicit ' + signify(seq.getExplicit(start)) + r'\newline'+' Recursive '+signify(seq.getRecursive(start))
  
    return problem, answer
'''
for i in range(1):
  prob , ans = Finding_Explicit_And_Recursive_Equations_3_3_3('latex',1,'lin')
  prob , ans = Finding_Explicit_And_Recursive_Equations_3_3_3('latex',2,'lin')
  prob , ans = Finding_Explicit_And_Recursive_Equations_3_3_3('latex',3,'lin')
'''
for i in range(3):
  prob , ans = Finding_Explicit_And_Recursive_Equations_3_3_3('latex',3,'geo')
  print(prob)
  print(ans)