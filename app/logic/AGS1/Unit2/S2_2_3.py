import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from sympy import *
from random import randint

# AGS 2.2.3 - Solve the following equations.
# Solve for x.

def notzero(min, max):
  inta = 0
  while inta == 0:
    inta = randint(min, max)
  return inta

def notequal(inta, intb, min, max):
  intb = inta
  while inta == intb:
    intb = randint(min, max)
  return intb

def case1(diff=1):
  if diff == 1:
    m = notzero(-20, 20)
    y = randint(-30, 30)
    a = notzero(-5, 5)
  if diff == 2:
    m = notzero(-40, 40)
    y = randint(-100, 100)
    a = notzero(-10, 10)
  if diff == 3:
    m = notzero(-60, 60)
    y = randint(-200, 200)
    a = notzero(-20, 20)

  if y < 0:
    equation = str(a) + "x " + str(y) + " = " + str(a*m+y)
  elif y > 0:
    equation = str(a) + "x + " + str(y) + " = " + str(a*m+y)
  else:
    equation = str(a) + "x = " + str(a*m+y)
  return equation, a

def case2(diff=1):
  if diff == 1:
    ft = notzero(1, 9)
    fb = 0
    fb = notequal(ft, fb, 1, 9)
    a = notzero(-5, 5)
  if diff == 2:
    ft = notzero(-9, 9)
    fb = 0
    fb = notequal(ft, fb, 1, 9)
    a = notzero(-10, 10)
  if diff == 3:
    ft = notzero(1, 60)
    fb = 0
    fb = notequal(ft, fb, -60, 60)
    a = notzero(-30, 30)

  equation = r'$\frac{' + str(ft) + "}{" + str(fb) + "}$x = " + str( "{:.2f}".format((ft/fb)*a) )
  return equation, a

def followingequation(diff=1, expr="latex", lvl=1):
  if lvl == 1:
    return case1(diff)
  else:
    return case2(diff)

"""
param
------
reg seed [0][1]; "latex"; random.randint(0,1)
"""