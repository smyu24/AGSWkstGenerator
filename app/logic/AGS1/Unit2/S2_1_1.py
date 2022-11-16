import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from loader import ArithSeq, brackify, GeoSeq, latexify, signify, tableGenerator
from sympy import *
from random import randint

# 
# TO DO W/ Word Prob alg completion (need to find CSV files again) or just use /Prealg-1-5-4

# ags.2.1.1 - Ratio ( don't work on this yet )
# instruction : Set up the equation and find the designated ratio.
# section1
# Apples are on sale at the market at 4pounds for $2.00. What is the price for 1pounds.

# problem:
# equation : 
# ratio : 
# answer
# equation : 4x=200
# ratio : $0.50
# Apples are on sale at the market at 4pounds for $2.00. Three apples weigh about a pound. About how much would 1apple cost? (Round to the nearest cent.)

# problem:
# equation : 
# ratio : 
# answer
# equation : 3x=100
# ratio : $0.50
# One dozen eggs cost $1.98. How much does cost? (Round to the nearest cent.)

# problem:
# equation : 
# ratio : 
# answer
# equation : 3x=100
# ratio : $0.50