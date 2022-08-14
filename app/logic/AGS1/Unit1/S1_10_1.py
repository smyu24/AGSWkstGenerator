import os; import sys; import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from loader import ArithSeq, getInt, GeoSeq, latexify, signify, tableGenerator
from sympy import *
from random import randint

# 1.10.1 Information to Arithmetic(?) Sequence.
# instruction: write the explicit equation for each geometric sequence.

"""for jj in range(10):
    problem, answer = infoToSeq(case=randint(1,4),kind='lin')
    print(problem)
    print(answer)"""