import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from loader import ArithSeq, brackify, GeoSeq, latexify, signify, tableGenerator
from sympy import *
from random import randint

# AGS1.2.5.2 - Evaluate The Function
# Instruction : Find the indicated values for each of the problems.

def evaluatethefunction(diff=1, expr="latex"):
  fname = ["f", "k", "z"]
  fnum = randint(0, 2)
  arr = []
  if(diff == 1): #linear
    arr.append(randint(-100,200))
    arr.append(randint(-40,50))

    arr.append(randint(-20, 20))
    arr.append((arr[0] * arr[2]) - (arr[1]))

    arr.append(randint(1, 20))
    arr.append((arr[0] * arr[4]) - (arr[1]))

    arr.append(arr[0] * (0.5) - (arr[1]))

    problem = "Given equation is $" + fname[fnum] + "(x) = " + str(arr[0]) + "*x"
    if(arr[1] < 0):
      problem = problem + " + " + str(arr[1]) + "$"
    else:
      problem = problem + " - " + str(arr[1]) + "$"

  elif (diff == 2): #exp
    arr.append(randint(-9,9))
    arr.append(randint(-9,9))

    arr.append(randint(-3, 3))
    arr.append((arr[0] ** arr[2]) * (arr[1]))

    arr.append(randint(-3, 3))
    arr.append((arr[0] ** arr[2]) * (arr[1]))

    arr.append(arr[0] * (0.5) - (arr[1]))

    problem = "Given equation is $" + fname[fnum] + "(x) = " + str(arr[0]) + "^x * " + str(arr[1]) + "$"
  
  elif (diff == 3): #exp equation
    arr.append(0) 
    arr.append(0) 

    while arr[0] == 0:
      arr[0] = randint(-9,9) #0
    while arr[1] == 0:
      arr[1] = randint(-9,9) #1


    arr.append(randint(1, 3)) #2
    arr.append(arr[0]* (arr[1] ** arr[2]))

    arr.append(randint(1, 3)) #4
    arr.append(arr[0]* (arr[1] ** arr[2]))

    arr.append("{:.2f}".format(arr[0]* (arr[1] ** 0.5)))

  elif (diff == 4): #Quadratic
    arr.append(0) 
    arr.append(0) 
    arr.append(0) 
    arr.append(0) 

    while arr[0] == 0:
      arr[0] = randint(-10,10) #0 intA
    while arr[1] == 0:
      arr[1] = randint(-10,10) #1 intB
    while arr[2] == 0:
      arr[2] = randint(-60,60) #2 intC

    while arr[3] == 0:
      arr[3] = randint(-5,5) #3 x for a
    arr.append( arr[0] * (arr[3] ** 2) + (arr[1] * arr[3]) + arr[2] ) #aa 4

    arr.append(0) 
    while arr[5] == 0:
      arr[5] = randint(-5,5) #5 x for b
    arr.append( arr[0] * (arr[5] ** 2) + (arr[1] * arr[5]) + arr[2] ) #ab 6

    arr.append("{:.2f}".format( arr[0] * ( 0.5 ** 2) + (arr[1] * 0.5) + arr[2] )) #ac 7

    problem = "Given equation is $" + fname[fnum] + "(x) = " + str(arr[0]) + " * x^2 + " + str(arr[1]) + " * x + " + str(arr[2]) + "$"

  elif (diff == 5): #Mix
    arr.append(0) 
    arr.append(0) 

    while arr[0] == 0:
      arr[0] = randint(-5,5) #0 intA
    while arr[1] == 0:
      arr[1] = randint(-10,10) #1 intB

    arr.append(0) 
    while arr[2] == 0:
      arr[2] = randint(1,5) #2 x for a
    arr.append( (arr[0] * (arr[2] ** 2)) + (arr[1] ** arr[2])  )#aa 3

    arr.append(0) 
    while arr[4] == 0:
      arr[4] = randint(1,5) #4 x for b
    arr.append(arr[0] * (arr[4] ** 2) + (arr[1] ** arr[4] )) #ab 5

    arr.append( "{:.2f}".format( arr[0] * (0.5 ** 2) + (arr[1] ** 0.5) ) ) #ac 6

    problem = "Given equation is $" + fname[fnum] + "(x) = " + str(arr[0]) + "* x^2 + " + str(arr[1]) + "^x $"

  if diff == 1 or diff == 2 or diff == 3:
    pa = " a). Find $" + fname[fnum] + "(" + str(arr[2]) + ")"+ "$"
    pb = " b). Find x if $" + fname[fnum] + "(x) = " + str(arr[5]) + "$"
    pc = " c). Find $" + fname[fnum] + "(0.5)$"

    fa = "Answer " + "a. " + str(arr[3]) + " b. " + str(arr[4]) + " c. " + str(arr[6])
  elif diff == 4:
    pa = " a). Find $" + fname[fnum] + "(" + str(arr[3]) + ")"+ "$"
    pb = " b). Find x if $" + fname[fnum] + "(x) = " + str(arr[5]) + "$"
    pc = " c). Find $" + fname[fnum] + "(0.5)$"

    fa = "Answer " + "a. " + str(arr[4]) + " b. " + str(arr[6]) + " c. " + str(arr[7])
  elif diff == 5:
    pa = " a). Find $" + fname[fnum] + "(" + str(arr[2]) + ")"+ "$"
    pb = " b). Find x if $" + fname[fnum] + "(x) = " + str(arr[4]) + "$"
    pc = " c). Find $" + fname[fnum] + "(0.5)$"

    fa = "Answer " + "a. " + str(arr[3]) + " b. " + str(arr[5]) + " c. " + str(arr[6])

  return problem + "\newline" + pa + "\newline" + pb + "\newline" + pc, fa

    