# import os, sys, inspect
# currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# parentdir = os.path.dirname(currentdir)
# sys.path.insert(0, parentdir)

# from loader import startGraph, drawLinear, drawPt, endGraph, drawCurve
# from sympy import *
# import random

# #option 1: linear + linear
# #option 2: linear + geometric

# import sympy
# def Find_The_Indicated_Values_3_4_2(expr='sympy',option=1):
#     '''
#     expr = latex , sympy
#     option = 1 : linear + linear
#              2  : geometric + linear
#     returns -------------------------------------------
#     problem = tikz code for the graph
#     expr = sympy expression
#     xlist = list of x coordinate for each problem sets
#     ylist = list of x coordinate for each problem sets
#     '''

#     #random_boolean = bool(random.getrandbits(1))
#     x = sympy.Symbol('x')
#     funcVar = ['a','b','c','d','e','f','g','q','z','k','l','m','m','o','p']
#     funcLabel = random.sample(funcVar,3)
#     xmin,xmax = -10 , 10

#     if option == 1:
#       # generate equations & solutions
#       eq1lhs,eq1rhs,eq2lhs,eq2rhs,sol = Systems_of_Equation('sympy','point_slope',3,3,3)
#       eq3rhs = sympy.sympify(eq1rhs + eq2rhs,rational = True)
#       #generate solution_graph
#       problem_graph = startGraph() + drawLinear(eq1rhs,xmin,xmax,'black',funcLabel[0])+ drawLinear(eq2rhs,xmin,xmax,'black',funcLabel[1])+ endGraph()
#       answer_graph = startGraph() + drawPt(sol) + drawLinear(eq1rhs,xmin,xmax,'black',funcLabel[0])+ drawLinear(eq2rhs,xmin,xmax,'black',funcLabel[1])+drawLinear(eq3rhs,xmin,xmax,'black',funcLabel[2])

#     else:
#       ratio = random.choice([Rational(1,2),Rational(1,3),2,3])
#       yint = random.choice([-4,-3,-2,2,3,4])
#       eq1rhs = f'{yint} * ({ratio}) ** x'
#       problem_graph = startGraph()+drawCurve(eq1rhs,-10,10,funcLabel[0])
      
#       #generate empty grids
#       case = random.randint(1,3)
#       if case == 1:
#         eq2rhs = linearEQgenerator(False,False,False,False,-10,10,-5,5,1,6)
#       elif case == 2:
#         eq2rhs = linearEQgenerator(False,False,True,False,-10,10,-5,5,1,6)
#       elif case == 3:
#         eq2rhs = linearEQgenerator(False,False,True,True,-10,10,-5,5,1,6)
      
#       problem_graph += drawLinear(eq2rhs,-10,10,'black',funcLabel[1])
#       #sol = sympy.linsolve([Eq(eq1rhs,0),Eq(eq2rhs)])
#       eq3rhs = sympy.sympify(eq1rhs+eq2rhs,rational=True)
#       #print('sol-----!@#!@#!@#',sol)
#       answer_graph = problem_graph + drawCurve(eq3rhs,-10,10,funcLabel[2])

#     xlistmax = [i for i in range(-10,11)]
#     xlist = [-4,-2,-1,1,2,4]
#     ylist = []
    
#     for i in range(len(xlist)):
#       f1 = lambdify(x,eq1rhs)
#       f2 = lambdify(x,eq2rhs)
#       ylist.append([f1(i),f2(i)])
#       answer_graph += drawPt([i,f1(i)])
#       answer_graph += drawPt([i,f2(i)])
        
#     answer_graph += r'\addplot[color=blue,mark=square,]coordinates {'
#     for i in range(len(xlistmax)):
#       f1 = lambdify(x,eq1rhs)
#       f2 = lambdify(x,eq2rhs)
#       answer_graph += f'({f1(i)},{f2(i)})'
#       answer_graph += drawPt([i,f2(i)])
    
#     answer_graph =answer_graph+'};'+endGraph()

#     header = fr'${funcLabel[2]}(x)= {funcLabel[0]}(x) + {funcLabel[1]}(x)$'
#     '''
#     header = problem display
#     problem graph = TIKZ RETURN graph
#     answer graph = TIKZ return,  f(x) + g(x) = k(x)
#     '''
#     print('eq1',eq1rhs,'eq2',eq2rhs,'eq3',eq3rhs,'xlist',xlist,'ylist',ylist)
#     return header , problem_graph+endGraph() , answer_graph

# for i in range(1):
#   header,prob,ans = Find_The_Indicated_Values_3_4_2(expr='sympy',option=1)
#   print(header)
#   print(prob)
#   print(ans)
# for i in range(1):
#   header,prob,ans = Find_The_Indicated_Values_3_4_2(expr='sympy',option=2)
#   print(header)
#   print(prob)
#   print(ans)