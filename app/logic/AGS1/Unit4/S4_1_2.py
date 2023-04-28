import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from loader import LinFunc, emptyGraph, drawPt, endGraph, startGraph, drawLinear
from sympy import *
import random

# AGS1.4.1.2 - Solve Each Equation And Check Steps.
# Option 1: Graph
# instruction : Graph the following equations on the coordinate grid. Determine if the given point is a solution to the equation.


def generate_point(graph_domain):
    return int(random.randint(graph_domain[0] + 1, graph_domain[1] - 1))

def checkBoundary(pointx,pointy,graph_domain,lineq):
    inDomain=False
    while inDomain == False:
        if pointy <= 0:
            while pointy < graph_domain[0]:
                pointx = generate_point(graph_domain); pointy = lineq.subs(pointx)
        else:
            while pointy > graph_domain[1]:
                pointx = generate_point(graph_domain); pointy = lineq.subs(pointx)
        if pointy > graph_domain[0] and pointy < graph_domain[1]: inDomain=True 

    return pointx,pointy


def Solve_Each_Equation_And_Check_Steps_PT1_4_1_2():
    graph_domain = [-10, 10]
    slope = random.randint(-6, 6) # add fraction funcionality
    yint = random.randint(-6, 6)
    lineq = LinFunc(slope, yint)
    on_line = random.choice([False, True])

    if random.randint(0,1) == 0:
        if on_line == True:
            pointx = generate_point(graph_domain); pointy = lineq.subs(pointx)
            pointx, pointy = checkBoundary(pointx,pointy,graph_domain,lineq)
        else:
            pointx = generate_point(graph_domain); pointy = generate_point(graph_domain)

        # A way to check if the dot really isnt on the graph
        while(on_line == False and (lineq.subs(pointx) == pointy)):
            pointx = generate_point(graph_domain); pointy = generate_point(graph_domain)
            pointx, pointy = checkBoundary(pointx,pointy,graph_domain,lineq)                

        header_graph = r'\newline '+fr'${lineq.getStdForm()}$'+startGraph(*graph_domain, *graph_domain)+drawLinear(
            lineq.expr, graph_domain[0], graph_domain[1])+drawPt([pointx, pointy])+endGraph()+r'\newline'

        problem = lineq.getStdForm(), emptyGraph(*graph_domain, *graph_domain)
        answer = "Yes" if on_line else "No"

    else:
        if on_line == True:
            pointx = generate_point(graph_domain); pointy = lineq.subs(pointx)
            pointx, pointy = checkBoundary(pointx,pointy,graph_domain,lineq)
        else:
            pointx = generate_point(graph_domain); pointy = generate_point(graph_domain)

        # A way to check if the dot really isnt on the graph
        while(on_line == False and (lineq.subs(pointx) == pointy)):
            pointx = generate_point(graph_domain); pointy = generate_point(graph_domain)
            pointx, pointy = checkBoundary(pointx,pointy,graph_domain,lineq)    

        header_graph = r'\newline '+fr'${lineq.getStdForm()}$'+startGraph(*graph_domain, *graph_domain)+drawLinear(
            lineq.expr, graph_domain[0], graph_domain[1])+drawPt([pointx, pointy])+endGraph()+fr'$ Point: ({pointx},{pointy}) $'+r'\newline'

        problem = lineq.getStdForm(), emptyGraph(*graph_domain, *graph_domain)
        answer = "Yes " + \
            fr"$ Point: ({pointx},{pointy}) $" if on_line else "No " + \
            fr"$ Point: ({pointx},{pointy}) $"

    return header_graph, problem[0], problem[1], answer


for i in range(20):
    a = Solve_Each_Equation_And_Check_Steps_PT1_4_1_2()
    print(*a)
# something broke in the middle ofthe run