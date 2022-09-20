import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from sympy import *
from random import randint

# AGS1.2.7.2 - Radical And Fraction Exponent
# instruction : Each of the expressions can be written using either radical notation,  ^{n}\sqrt{a ^ {m}}  , or rational exponents,  a ^ {\frac{m/n}} . Rewrite each of the given expressions in the form that is missing. Do not simplify.

def notequal(inta, intb):
  while inta == intb:
      inta = randint(1, 25)
  return inta

def singlefraction(inta, intb, intc):
  return "$" + str(inta) + "^{\\frac{" + str(intc) + "}{" + str(intb) + "}}$"

def singlesqrt(inta, intb, intc):
  if intb == 2:
    return "$ \\sqrt{" +  str(inta) + "^{" + str(intc) +"}}$"
  else:
    return "$ \\sqrt[" + str(intb) + "]{" +  str(inta) + "^{" + str(intc) +"}}$"

def dualsqrt(inta, intb, intc, intd, inte):
  if inta == intb:
    if intc == 2:
      return "$ \\sqrt{" +  str(inta) + "^{" + str(intd + inte) +"}}$"
    else:
      return "$ \\sqrt[" + str(intc) + "]{" +  str(inta) + "^{" + str(intd + inte) +"}}$"
  else:
    if intc == 2:
      return "$ \\sqrt{" +  str(inta) + "^{" + str(intd) +"}*" +  str(intb) + "^{" + str(inte) +"}}$"
    else:
      return "$ \\sqrt[" + str(intc) + "]{" +  str(inta) + "^{" + str(intd) +"}*" +  str(intb) + "^{" + str(inte) +"}}$"

def trisqrt(inta, intb, intc, intd, inte, intf, intg):
  if inta == intb:
    if intd == 2:
      return "$ \\sqrt{" +  str(inta) + "^{" + str(intf + inte) +"}*" + str(intc) + "^{" + str(intg) +"}" + "}$"
    else:
      return "$ \\sqrt[" + str(intd) + "]{" +  str(inta) + "^{" + str(intf + inte) +"}*" + str(intc) + "^{" + str(intg) +"}" + "}$"
  else:
    if intd == 2:
      return "$ \\sqrt{" +  str(inta) + "^{" + str(inte) +"}*" +  str(intb) + "^{" + str(intf) +"}*" + str(intc) + "^{" + str(intg) +"}" + "}$"
    else:
      return "$ \\sqrt[" + str(intd) + "]{" +  str(inta) + "^{" + str(inte) +"}*" +  str(intb) + "^{" + str(intf) +"}*" + str(intc) + "^{" + str(intg) +"}" + "}$"
    
def radicalandfractionexponent(diff = 1, expr = "latex", form = "r"):
  if diff == 1: #single
    inta = randint(5, 250)
    intb = randint(2, 5)
    intc = intb
    intc = notequal(intc, intb)
    if form == "r":    
      problem = "Radical form " + singlesqrt(inta, intb, intc)
      answer = singlefraction(inta, intb, intc)
    else:
      problem = "Exponential form " + singlefraction(inta, intb, intc)
      answer = singlesqrt(inta, intb, intc)

  elif diff == 2: #dual
    inta = randint(3, 9)
    intb = randint(3, 9)
    intc = randint(2, 5)
    intd = intc
    intd = notequal(intd, intc)
    inte = intc
    inte = notequal(inte, intc)

    if form == "r":    
      problem = "Radical form " + dualsqrt(inta, intb, intc, intd, inte)
      answer = singlefraction(inta, intc, intd) + " * " + singlefraction(intb, intc, inte)
    else:
      problem = "Exponential form " + singlefraction(inta, intc, intd) + " * " + singlefraction(intb, intc, inte)
      answer = dualsqrt(inta, intb, intc, intd, inte)

  elif diff == 3: #tri
    fs = ["a", "b", "c", "d"]
    inta = randint(3, 9)
    intb = randint(3, 9)
    intc = fs[randint(0, 3)]
    intd = randint(2, 5)
    inte = intd
    intfe= notequal(inte, intd)
    intf = intd
    intf = notequal(intf, intd)
    intg = intd
    intg = notequal(intg, intd)

    if form == "r":    
      problem = "Radical form " + trisqrt(inta, intb, intc, intd, inte, intf, intg)
      answer = singlefraction(inta, intd, inte) + " * " + singlefraction(intb, intd, intf) + " * " + singlefraction(intc, intd, intg)
    else:
      problem = "Exponential form " + singlefraction(inta, intd, inte) + " * " + singlefraction(intb, intd, intf) + " * " + singlefraction(intc, intd, intg)
      answer = trisqrt(inta, intb, intc, intd, inte, intf, intg)

  return problem, answer

print(radicalandfractionexponent(3, "latex", "r"))