import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from loader import ArithSeq, getInt, GeoSeq, latexify, signify, tableGenerator
from sympy import *
from random import randint

# 1.5.3. Geometric Sequence To Explicit & Recurssive (REPEAT OF 1.5.1?)

# section 1
# instruction : In the next problems, you are given various types of information. Write the recursive and explicit functions for each geometric sequence. Finally, graph each sequence, making sure you clearly label the axes.

# NOT DOEN YET?



