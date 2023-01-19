import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from loader import LinFunc, getInt, latexify, signify, Rational, EmptySet, latex, PWFunc, graphPW, x
import random
import numpy as np
from random import randint

# NO SETTING OTHER THAN 1; no Hard medium, easy

# AGS1.3.2.2 - Increasin / Decreasing / Constant / Domain & Range
# section 1: lienar function
# instruction : For each graph and description do the following:


#prequisite

r"""
\documentclass{article} 
\usepackage{pgfplots} 
\usetikzlibrary{intersections}
\usetikzlibrary{patterns}
"""
# for generating data, create a "range" of +/3 that the randomizer can choose from (up or down)


def upAndDownGraph():
    problem = ""
    answer = ""

    x_points = []
    points = []

    x = 1
    x_points.append(x)
    points.append(np.random.randint(low = 0, high = 100) )

    for i in range( random.randint(4,10) ):
        x+=1
        x_points.append(x)
        points.append(np.random.randint(low = points[-1] - 3, high = points[-1] + 3))

    return x_points, points

def indexcount(obj, data):
    number_of = data.count(obj)
    saved = []
    if number_of > 1:
        temp = data
        for i in range(number_of):
            saved.append(data.index(obj))
            temp = temp[saved[-1] + 1:]
        # splice, then index again
    else:
        saved.append(data.index(obj))
    return saved


def compress_d(increasing, decreasing, stagnant):
    print(increasing)
    prev = 0
    for i in range(len(increasing)):
        if i+1 != len(increasing): # get rid of overstepping allocated index (approachable index)
            if increasing[i] + 1 == increasing[i+1]:
                increasing[i] = fr'[{increasing[i]}, {increasing[i+1]}]' # replace to [{one}, {two}], then replace as needed. No need to touch more since it already creates it in interval notation. join(''.join) the list with \cap for union
                # close the front in
                #increasing[i+1]
                # domains not properly compressing (only pairing

    print(decreasing)
    for i in range(len(decreasing)):
        if i+1 != len(decreasing):
            if decreasing[i] - 1 == decreasing[i+1]:
                decreasing[i] = fr'[{decreasing[i]}, {decreasing[i+1]}]'

    print(stagnant)
    for i in range(len(stagnant)):
        if i+1 != len(stagnant):
            if stagnant[i] == stagnant[i+1]:
                stagnant[i] = fr'[{stagnant[i]}, {stagnant[i+1]}]'

    return increasing, decreasing, stagnant


def graph_movement_conf(data, x):
    previous = 0
    continuousity = 0
    increasing = []
    decreasing = []
    stagnant = []

    for i in range(len(data)):
        temp = data[i]
        if temp > previous:
            #increasing
            continuousity+=1
            increasing.append(x[i])

        elif temp < previous:
            # decreasing
            continuousity+=1
            decreasing.append(x[i])

        elif temp == previous:
            # stagnant
            continuousity+=1
            stagnant.append(x[i])

        else:
            # disconect (discontinuous graph)
            continuousity=0

        previous = temp

    return compress_d(increasing, decreasing, stagnant)


def analyize_data(x, data):
    """
    look for max, min, median,possible ticks
    """
    details = []
    x_minimum = 0
    x_maximum = 0

    y_maximum = 0
    y_minimum = 0
    range_of_values = 0
    possible_ticks = 0
    numberTerms = x[-1]
    parsed_x_ticker = ""
    parsed_y_ticker = ""

    xvals = x
    xvals.sort()

    x_minimum = xvals[0]
    x_maximum = xvals[-1]

    copy = data
    copy.sort()

    y_maximum = copy[-1]
    y_minimum = copy[0]

    # WORKING ON THIS
    # calculate increase, decrease, minimum, maximum, domain, range
    details = []
    print(graph_movement_conf(data, x))
    details.append([]) #increasing
    details.append([]) #decreasing
    details.append(indexcount(y_minimum, data)) #minimum (multiple instances)
    # need indexcount interpreter
    details.append(indexcount(y_maximum, data)) #maximum
    details.append([xvals[0], xvals[-1]]) #domain (might have to add number of domains index later) ( do this after increasing and decreasing analization )
    details.append([copy[0], copy[-1]])#range

    print(details)

    """Increasing :
    Decreasing :
    Minumum :
    Maximum :
    Domain :
    Range :"""

    #print(y_minimum, y_maximum)
    range_of_values = y_maximum - y_minimum
    #print(range_of_values)

    if (range_of_values / numberTerms) < 1:
        # single ticker for y
        temp = y_minimum - random.randint(1,5)
        y_minimum = temp
        temp2 = y_maximum + random.randint(0,5)
        y_maximum = temp2
        parsed_y_ticker = fr"`{temp}, {temp + 1}, ..., {temp2}~"
        parsed_y_ticker=parsed_y_ticker.replace("`", "{")
        parsed_y_ticker=parsed_y_ticker.replace("~", "}")

    parsed_x_ticker = fr'`{x[0]}, {x[1]}, ..., {x[-1] + 1}~' # x1, x2, ..., xn
    parsed_x_ticker=parsed_x_ticker.replace("`", "{")
    parsed_x_ticker=parsed_x_ticker.replace("~", "}")

    #print("here", parsed_x_ticker, parsed_y_ticker)

    return x, data, x_minimum, x_maximum, y_minimum, y_maximum, parsed_x_ticker, parsed_y_ticker

def graph_gen(x, data, x_minimum, x_maximum, y_minimum, y_maximum, parsed_x_ticker, parsed_y_ticker):
    """
    data will come prepackaged in the form of a 2-d list
    x being the x values
    y being the randomized near values
    """
    out = []
    inputted = ""

    out.append(r'\begin{tikzpicture}\begin{axis}[axis on top,smooth,axis line style=very thick,axis x line=bottom,axis y line=left,grid=major,')
    out.append(fr'xmin={x_minimum}, xmax={x_maximum},ymin={y_minimum}, ymax={y_maximum},xtick={parsed_x_ticker},ytick={parsed_y_ticker}]')
    out.append(r'\addplot[mark=*,black] plot coordinates {')
    for i in range(len(x)): out.append(fr'({x[i]}, {data[i]})')
    out.append(r'};')
    out.append(r'\end{axis}')
    out.append(r'\end{tikzpicture}')
    return ''.join(out)

for i in range(10):
    one, two = upAndDownGraph()
    print("--<")
    print(graph_gen(*analyize_data(one, two)))
    print(">--")



def PWLinearChars(expr='latex'):
    endPts, pairs = [0], []

    for jj in range(randint(3,5)):
        slope = Rational(getInt(-6,6),randint(1,3))
        if jj == 0:
            func = LinFunc(slope, randint(-8,8))
        else:
            start = pairs[-1][0].subs(x,endPts[jj])
            func = LinFunc(slope, [endPts[jj],start])
        
        step = randint(3,6) if slope.q==1 else randint(1,3)*slope.q
        endPts.append(endPts[jj] + step)
        pairs.append([func.expr, fr'[{endPts[jj]},{endPts[jj+1]}]'])
    
    func = PWFunc(*pairs)

    problem = graphPW(func, contDot=True)

    rangeset = func.getRange()
    mins, maxes = func.solve(rangeset.inf), func.solve(rangeset.sup)
    
    inc, dec, const = EmptySet, EmptySet, EmptySet
    for expr, interval in func.pairs:
        if expr.coeff(x) > 0:
            inc = inc.union(interval)
        elif expr.coeff(x) < 0:
            dec = dec.union(interval)
        else:
            const = const.union(interval)

    answer = 'Domain: ' + signify(latex(func.domain)) + r'\newline '
    answer += 'Range: ' + signify(latex(rangeset)) + r'\newline '
    answer += 'Increasing: ' + (signify(latex(inc)) if inc!=EmptySet else 'None') + r'\newline '
    answer += 'Decreasing: ' + (signify(latex(dec)) if dec!=EmptySet else 'None') + r'\newline '
    answer += 'Constant: ' + (signify(latex(const)) if const!=EmptySet else 'None') + r'\newline '
    answer += 'Minimum: ' + signify(latexify(rangeset.inf)) + ', occurs at $x=' + str(mins)[1:-1] + r'$ \newline '
    answer += 'Maximum: ' + signify(latexify(rangeset.sup)) + ', occurs at $x=' + str(maxes)[1:-1] + r'$ \newline '

    return problem, answer

for jj in range(5):
    problem, answer = PWLinearChars()
    print(problem)
    print(answer)





# section 2 : table
# instruction : For each graph and description do the following:


# MISSING SECTION