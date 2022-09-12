import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from loader import startGraph, drawLine, drawSlopeTri, drawPt, endGraph, brackify, latexify, signify, getInt, LinFunc, sample, minipagify
from sympy import Rational
from random import randint

# ags.mod2.2.1 - Find The Slope In Each Representation.
# Instruction : Find the slopes and show whether or not the slopes are the same for the pairs of representations provided.
def getSlopeTriGraph(func, pt1, pt2):
    if type(pt1)!=list:
        pt1 = [pt1] + [func.subs(pt1)]
    if type(pt2)!=list:
        pt2 = [pt2] + [func.subs(pt2)]

    graph = startGraph()
    graph += drawLine(func.expr, -1, 6)
    graph += drawSlopeTri(pt1, pt2)
    graph += drawPt(pt1) + drawPt(pt2)
    graph += endGraph()
    return graph

def MatchTheSlopes(case=1):
    if case == 1: # Graph vs. graph
        slope = Rational(getInt(-7,7),2)
        intercept = randint(-5,0) if slope>0 else randint(0,5)
        func1 = LinFunc(slope, intercept)
        intercept = randint(-5,0) if slope>0 else randint(0,5)
        func2 = LinFunc(slope, intercept)

        nums = sample(list(range(0,6)),4)
        nums.sort()
        pts1 = [[jj, func1.subs(jj)] for jj in nums[::3]]
        pts2 = [[jj, func2.subs(jj)] for jj in nums[1:3]]
        graph1 = getSlopeTriGraph(func1, pts1[0], pts1[1])
        graph2 = getSlopeTriGraph(func2, pts2[0], pts2[1])

        problem = minipagify(graph1, graph2)

        answer1 = r'$\text{Slope}=\frac'
        answer1 += brackify(pts1[1][1]-pts1[0][1]) + brackify(pts1[1][0]-pts1[0][0])
        answer1 += f'={latexify(slope)}$'
        answer2 = r'$\text{Slope}=\frac'
        answer2 += brackify(pts2[1][1]-pts2[0][1]) + brackify(pts2[1][0]-pts2[0][0])
        answer2 += f'={latexify(slope)}$'
        answer = minipagify(answer1, answer2)
    elif case == 2: # Table vs. table
        slope = getInt(-7,7)
        func1 = LinFunc(slope, randint(-9,9))
        func2 = LinFunc(slope, randint(-9,9))

        nums = sample(list(range(1,20)),4)
        nums.sort()
        problem = minipagify(func1.getTable(nums), func2.getTable([1,2,3,4]))
        
        answer1 = r'$\text{Slope}=\frac'
        answer1 += brackify(func1.subs(nums[1])-func1.subs(nums[0])) + brackify(nums[1]-nums[0])
        answer1 += f'={latexify(slope)}$'
        answer2 = r'$\text{Slope}=\frac'
        answer2 += brackify(func2.subs(2)-func2.subs(1)) + '{1}'
        answer2 += f'={latexify(slope)}$'
        answer = minipagify(answer1, answer2)
    else: # Eq vs. eq
        slope = Rational(getInt(-7,7),2)
        func1 = LinFunc(slope, randint(-7,7))
        func2 = LinFunc(slope, randint(-7,7))

        problem = signify(func1.getStdForm(mult=randint(1,3))) + r' \newline '
        problem += signify(func2.getPtSlope(getInt(-4,4), notation='y'))

        answer = r'$\text{Slope}=' + latexify(slope) + '$'

    return problem, answer

for jj in range(10):
    problem, answer = MatchTheSlopes(3)
    print(problem)
    print(answer, r'\\ \\')