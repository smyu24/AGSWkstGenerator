import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from loader import ArithSeq, brackify, GeoSeq, latexify, signify, tableGenerator
from sympy import *
from random import randint

# AGS 2.2.2 - Indicate The Relationship? (SKIP?)
# instruction : Create a graphical model based on the context. Indicate if the relationship is linear or exponential and if the context is best modeled as discrete or continuous.

# missing code...

## Indicate_The_Relationship

