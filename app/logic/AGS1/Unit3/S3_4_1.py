# import os, sys, inspect
# currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# parentdir = os.path.dirname(currentdir)
# sys.path.insert(0, parentdir)

# from loader import startGraph, drawLinear, endGraph, drawCurve, emptyGraph
# from sympy import *
# from random import randint

# #---AGS1.3.4.1-------generator
# import sympy
# import random
# def Find_The_Indicated_Values_3_4_1(expr='sympy',option=1):
#     '''
#     expr = latex , sympy
#     option = 1 : linear
#              2  : geometric
#     returns -------------------------------------------
#     problem = tikz code for the graph
#     expr = sympy expression
#     xlist = list of x coordinate for each problem sets
#     ylist = list of x coordinate for each problem sets
#     '''

#     #random_boolean = bool(random.getrandbits(1))
#     x = sympy.Symbol('x')
#     if option == 1:
#       case = random.randint(1,3)
#       if case == 1:
#         eq = linearEQgenerator(False,False,False,False,-10,10,-10,10,1,6)
#       elif case == 2:
#         eq = linearEQgenerator(False,False,True,False,-10,10,-10,10,1,6)
#       elif case == 3:
#         eq = linearEQgenerator(False,False,True,True,-10,10,-10,10,1,6)
#       answergraph = startGraph()+drawLinear(eq,-8,8)+endGraph()
#       eq = sympy.sympify(eq,rational = True)
#       xlist = random.sample(range(-30, 30), 4)
#     else:
#       ratio = random.choice([Rational(1,2),Rational(1,3),2,3,4])
#       yint = random.choice([-4,-3,-2,2,3,4])
#       eq = f'{yint} * ({ratio}) ** x'
#       answergraph = startGraph()+drawCurve(eq,-8,8)+endGraph()
#       eq = sympy.sympify(eq,rational = True)
#       xlist = random.sample(range(-5, 5),4)

#     ylist=[]
#     for i in range(len(xlist)):
#       ylist.append(eq.subs(x,xlist[i]))

#     if option == 1:
#       question = r'Graph the explicit function $f(x)= '+sympy.latex(sympy.sympify(eq))+r'$ and find the indicated values. \\ a) '
#       answer ='a) '+ answergraph +r'\\'
#       question += emptyGraph(-10,10,-10,10)
#       question += r'\\ '
#       option = ['b','c','d','e']
#       for i in range(4):
#         if i%2 != 0:
#           question += fr'{option[i]}) $f({sympy.latex(xlist[i])})= $ \\'
#           answer += fr'{option[i]}) $f({sympy.latex(xlist[i])})= {sympy.latex(ylist[i])}$ '
#         else:
#           question += fr'{option[i]}) $f(x)={sympy.latex(ylist[i])}, x = $ \\'
#           answer += fr'{option[i]}) $f({sympy.latex(xlist[i])})= {sympy.latex(ylist[i])}$ '
#     else: # option 2
#       answer = 'a) '+ answergraph+r'\\'
#       question = r'Graph the explicit function $f(x)= '+sympy.latex(eq)+r'$ and find the indicated values. \\ a) '
#       question += emptyGraph(-10,10,-10,10)
#       question += r'\\ '
#       option = ['b','c','d','e']
#       for i in range(4):
#         if i%2 != 0:
#           question += fr'{option[i]}) $f({sympy.latex(xlist[i])})= $ \\'
#           answer += fr'{option[i]}) $f({sympy.latex(xlist[i])})= {sympy.latex(ylist[i])}$ '
#         else:
#           question += fr'{option[i]}) $f(x)={sympy.latex(ylist[i])}, x = $ \\'
#           answer += fr'{option[i]}) $f({sympy.latex(xlist[i])})= {sympy.latex(ylist[i])}$ '
    
#     answer += r'\\'
#     return question, answer

# #---AGS1.3.4.1-------Caller
# #option 1: equation
# for i in range(10):
#   print('Arith-------------------------------')
#   question , answer = Find_The_Indicated_Values_3_4_1(expr='sympy',option=1)
#   print('question: ',question)
#   print(' ')
#   print('answer: ',answer)
#   print(' ')


# #option 2: graph
# for i in range(4):
#   print('GEO-------------------------------')
#   question , answer = Find_The_Indicated_Values_3_4_1(expr='sympy',option=1)
#   print('question ------')
#   print(question)
#   print(answer)