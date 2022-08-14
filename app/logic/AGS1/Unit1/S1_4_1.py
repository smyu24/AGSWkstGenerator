import os; import sys; import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from loader import ArithSeq, getInt, GeoSeq, latexify, signify, tableGenerator
import sympy, random

# 1.4.1 Arithmetic - Explicit & Recursive
# section 1
# instruction : Find the next three terms in each sequence. Identify the common difference. Write a recursive function and an explicit function for each sequence.

## REDO THIS ONE!!!!