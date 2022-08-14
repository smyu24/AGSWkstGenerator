import random
from random import randint, choice, sample

import latextable
from texttable import Texttable

from sympy import *

variables = 'a b c d m n p q r s t w x y'
variables = symbols(variables, real=True)
variables += (Symbol('z'),)
a,b,c,d,m,n,p,q,r,s,t,w,x,y,z = variables

# import sympy
# from sympy import latex,simplify,nsimplify,sympify,Symbol,symbols
# from sympy import Rational,Integer,Float,S,oo
# from sympy import log,Pow,powsimp,powdenest,sqrt,real_root,lcm
# from sympy import ImageSet,Interval,Lambda,Contains,Union,Piecewise,EmptySet

from scipy import stats
import numpy as np