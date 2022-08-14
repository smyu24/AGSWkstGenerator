import sympy, fractions, random, latextable
from sympy import *

from texttable import Texttable
from tabulate import tabulate

# #1.4.2 Find the slope.
# Section 1
# instruction: Find the slope for each line based on the given representation.

# # Latex setup required in preamble

# \newcommand{\drawaline}[4]{
# \draw [extended line=1cm,stealth-stealth] (#1,#2)--(#3,#4);
# \fill [black](#1,#2) circle(4pt);
# \fill [black](#3,#4) circle(4pt);
# }

def fix_zero_neg(input):
    if int(input) == 0:
        return 0
    else:
        return input

def AGS_Find_The_Slope_Section_1(difficulty=1, expr="latex"):
    startgraph = r'\begin{tikzpicture}[scale=.5,extended line/.style={shorten >=-#1,shorten <=-#1},]\draw [help lines] (-6,-6) grid (6,6);'
    startgraph += r'\draw [<->](0,-6.2)--(0,6.2) node[right]{$y$};\draw [<->](-6.2,0)--(6.2,0) node[right]{$x$};'
    startgraph += r'\foreach \x in {-6,-5,-4,-3,-2,-1,1,2,3,4,5,6}\draw (\x,1pt) -- (\x,-3pt) node[anchor=north] {\x};'
    startgraph += r'\foreach \y in {-6,-5,-4,-3,-2,-1,1,2,3,4,5,6}\draw (1pt,\y) -- (-3pt,\y) node[anchor=east] {\y};'

    endgraph = r'\end{tikzpicture}'

    rise = ""
    run = ""
    problem = ""
    answer = ""
    negative = ["", "-"]

    intA = fix_zero_neg(str(random.choice(negative)) +
                        str(random.randint(0, 5)))
    intB = fix_zero_neg(str(random.choice(negative)) +
                        str(random.randint(0, 5)))
    intC = fix_zero_neg(str(random.choice(negative)) +
                        str(random.randint(0, 5)))
    intD = fix_zero_neg(str(random.choice(negative)) +
                        str(random.randint(0, 5)))
    intA_2 = fix_zero_neg(str(random.choice(negative)) +
                          str(random.randint(0, 5)))
    intB_2 = fix_zero_neg(str(random.choice(negative)) +
                          str(random.randint(0, 5)))
    intC_2 = fix_zero_neg(str(random.choice(negative)) +
                          str(random.randint(0, 5)))
    intD_2 = fix_zero_neg(str(random.choice(negative)) +
                          str(random.randint(0, 5)))

    if difficulty == 1:     # Easy
        if random.randint(1, 2) == 1:
            #point_1 = ( intA , 0 )
            #point_2 = ( intB , intC)
            while abs(int(intB) - int(intA)) == 0:
                intB = str(random.choice(negative)) + str(random.randint(0, 5))
                intA = str(random.choice(negative)) + str(random.randint(0, 5))
            problem = fr"\drawaline`{intA}~`{0}~`{intB}~`{intC}~"
            if abs(int(intB) - int(intA)) == 0:
                AGS_Find_The_Slope_Section_1(difficulty, expr)
            rise = int(intC)
            run = (int(intB) - int(intA))

        else:
            # point 3 ( 0 , intA_2)
            # point 4 ( intB_2 , intC_2)
            if abs(int(intB_2)) == 0:
                AGS_Find_The_Slope_Section_1(difficulty, expr)
            while abs(int(intB_2)) == 0:
                intB_2 = str(random.choice(negative)) + \
                    str(random.randint(0, 5))
            problem = fr"\drawaline`{0}~`{intA_2}~`{intB_2}~`{intC_2}~"
            rise = (int(intC_2) - int(intA_2))
            run = (int(intB_2))
        answer = fractions.Fraction(rise, run)
        problem = problem.replace('`', "{")
        problem = problem.replace('~', "}")
        if answer == 0:
            answer = "Zero Slope"  # Horizontal
        elif abs(run) == 0:
            answer = "Undefined Slope"  # Vertical

    elif difficulty == 2 or difficulty == 3:    # Medium or hard
        if random.randint(1, 2) == 1:
            #point_1 = ( intA , 0 )
            #point_2 = ( intB , intC)
            while abs(int(intB) - int(intA)) == 0:
                intB = str(random.choice(negative)) + str(random.randint(0, 5))
                intA = str(random.choice(negative)) + str(random.randint(0, 5))
            problem = fr"\drawaline`{intA}~`{intD}~`{intB}~`{intC}~"
            if abs(int(intB) - int(intA)) == 0:
                AGS_Find_The_Slope_Section_1(difficulty, expr)
            rise = int(intC) - int(intD)
            run = (int(intB) - int(intA))

        else:
            # point 3 ( 0 , intA_2)
            # point 4 ( intB_2 , intC_2)
            if abs(int(intB_2)) == 0:
                AGS_Find_The_Slope_Section_1(difficulty, expr)
            while abs(int(intB_2) - int(intD_2)) == 0:
                intB_2 = str(random.choice(negative)) + \
                    str(random.randint(0, 5))
                intD_2 = str(random.choice(negative)) + \
                    str(random.randint(0, 5))
            problem = fr"\drawaline`{intD_2}~`{intA_2}~`{intB_2}~`{intC_2}~"
            rise = (int(intC_2) - int(intA_2))
            run = (int(intB_2) - int(intD_2))

        answer = fractions.Fraction(rise, run)
        problem = problem.replace('`', "{")
        problem = problem.replace('~', "}")
        if answer == 0:
            answer = "Zero Slope"  # Horizontal
        elif abs(run) == 0:
            answer = "Undefined Slope"  # Vertical

    problem = startgraph + problem + endgraph

    return(problem, answer)


def problem_terms_gen(start, ratio, interateby):
    indexes = []
    terms = []
    terms.append(str(start))
    indexes.append(str(random.randint(-10, 10)))
    for i in range(random.randint(3, 7)):
        terms.append(str(int(terms[-1]) + int(ratio)))
        indexes.append(str(int(indexes[-1]) + int(interateby)))
    return indexes, terms


def table_selector(rows):
    table = Texttable()
    table.set_cols_align(["c"] * 2)
    table.set_deco(Texttable.HEADER | Texttable.VLINES)
    table.add_rows(rows)
    if random.randint(1, 2) == 1:
        return(tabulate(rows, headers='firstrow', tablefmt='latex'))
    else:
        return(latextable.draw_latex(table))


def AGS_Find_The_Slope_Section_2(difficulty=1, expr="latex"):
    problem = ""
    answer = ""
    x_layer = ""
    y_layer = ""

    if difficulty == 1:     # Easy
        start = random.randint(-10, 10)
        interateby = 1
        if random.randint(1, 2) == 1:
            ratio = random.randint(-5, -1)
        else:
            ratio = random.randint(1, 5)
        x_layer, y_layer = problem_terms_gen(start, ratio, interateby)

        rows = []
        for i in range(len(x_layer)):
            rows.append([])
            rows[i].append(x_layer[i])
            rows[i].append(y_layer[i])
        rows.insert(0, ['x', 'y'])

        problem = table_selector(rows)
        answer = ratio

    elif difficulty == 2:   # Medium
        interateby = random.randint(-3, 3)
        start = random.randint(-15, 15)
        ratio = random.randint(-15, 15)
        x_layer, y_layer = problem_terms_gen(start, ratio, interateby)

        rows = []
        for i in range(len(x_layer)):
            rows.append([])
            rows[i].append(x_layer[i])
            rows[i].append(y_layer[i])
        rows.insert(0, ['x', 'y'])

        problem = table_selector(rows)
        if interateby != 0:
            answer = Rational(ratio, interateby)
        else:
            answer = 0

    elif difficulty == 3:   # Hard
        start = random.randint(-50, 50)
        ratio = random.randint(-50, 50)
        interateby = random.randint(-5, 5)
        x_layer, y_layer = problem_terms_gen(start, ratio, interateby)

        rows = []
        for i in range(len(x_layer)):
            rows.append([])
            rows[i].append(x_layer[i])
            rows[i].append(y_layer[i])
        rows.insert(0, ['x', 'y'])

        problem = table_selector(rows)
        if interateby != 0:
            answer = Rational(ratio, interateby)
        else:
            answer = 0

    if len(str(answer)) >= 8:
        AGS_Find_The_Slope_Section_2(difficulty, expr)
    return problem, answer


def AGS_Find_The_Slope_Section_3(difficulty=1, expr="latex"):
    problem = ""
    answer = ""

    half_1 = ""  # SPLIT DA HALVES
    half_2 = ""

    negative = ["", "-"]
    filler = ""

    sym_1 = random.choice(["+", "-"])

    intA = fix_zero_neg(str(random.choice(negative)) +
                        str(random.randint(1, 10)))
    intB = fix_zero_neg(str(random.choice(negative)) +
                        str(random.randint(1, 10)))
    intC = fix_zero_neg(str(random.randint(2, 10)))
    intD = fix_zero_neg(str(random.randint(1, 10)))
    intE = fix_zero_neg(str(random.choice(negative)) +
                        str(random.randint(1, 20)))
    intF = fix_zero_neg(str(random.choice(negative)) +
                        str(random.randint(1, 20)))
    intG = fix_zero_neg(str(random.randint(2, 20)))
    intH = fix_zero_neg(str(random.randint(1, 20)))

    if difficulty == 1:     # Easy
        half_1 = fr'y'
        if int(intA) == 1:
            half_2 = fr'x {sym_1} {intC}'
        elif int(intA) == -1:
            half_2 = fr'- x {sym_1} {intC}'
        else:
            half_2 = fr'{intA} * x {sym_1} {intC}'

        half_1 = sympy.sympify(half_1, evaluate=False)
        half_2 = sympy.sympify(half_2, evaluate=False)

        problem = str(sympy.latex(half_1)) + " = " + \
            str(sympy.latex(half_2, mode="plain"))

        answer = "$ " + str(intA) + " $"

    elif difficulty == 2:   # Medium
        filler = random.randint(1, 3)
        if filler == 1:
            half_1 = fr'y'
            half_2 = fr'{intA} / {intB} * x {sym_1} {intH}'

            half_1 = sympy.sympify(half_1, evaluate=False)
            half_2 = sympy.sympify(half_2, evaluate=False)

            problem = str(sympy.latex(half_1)) + " = " + \
                str(sympy.latex(half_2))

            answer = "$ " + \
                str(sympy.latex(sympy.sympify(str(intA) + " / " + str(intB)))) + " $"

        elif filler == 2:
            half_1 = fr'{intG} * y'
            half_2 = fr'{intC} * x {sym_1} {intH}'

            half_1 = sympy.sympify(half_1, evaluate=False)
            half_2 = sympy.sympify(half_2, evaluate=False)

            problem = str(sympy.latex(half_1)) + " = " + \
                str(sympy.latex(half_2))

            answer = "$ " + \
                str(sympy.latex(sympy.sympify(str(intC) + " / " + str(intG)))) + " $"

        else:
            half_1 = fr'{intC} * y {sym_1} {intH}'
            half_2 = fr'{intG} * x'

            half_1 = sympy.sympify(half_1, evaluate=False)
            half_2 = sympy.sympify(half_2, evaluate=False)

            problem = str(sympy.latex(half_1)) + " = " + \
                str(sympy.latex(half_2))

            answer = "$ " + \
                str(sympy.latex(sympy.sympify(str(intG) + " / " + str(intC)))) + " $"

    elif difficulty == 3:   # Hard
        filler = random.randint(1, 5)
        if filler == 1:
            y = sympy.Symbol("y")
            # intB  x ±  intA  y= intD
            problem = fr'{int(intD) + 1} * x {sym_1} {intC} * y = {intA}'

            half_1 = fr'{int(intD) + 1} * x {sym_1} {intC} * y'
            half_2 = fr'{intA}'

            half_1 = sympy.sympify(half_1, evaluate=False)
            half_2 = sympy.sympify(half_2, evaluate=False)

            problem = str(sympy.latex(half_1)) + " = " + \
                str(sympy.latex(half_2))
            filler = sympy.Eq(half_1, half_2)
            filler = str(sympy.solve(filler, y))
            filler = filler[1:-1]
            filler = filler.split()
            for i in range(len(filler)):
                if filler[i].find("x") != -1:
                    answer = filler[i]
            answer = answer.replace("x", "1")

            answer = "$ " + str(sympy.latex(sympy.sympify(answer))) + " $"

        elif filler == 2:
            half_1 = fr'{intG} * x {sym_1} {intC} * y'
            half_2 = fr'{intB}'

            y = sympy.Symbol("y")
            half_1 = sympy.sympify(half_1, evaluate=False)
            half_2 = sympy.sympify(half_2, evaluate=False)

            problem = str(sympy.latex(half_1)) + " = " + \
                str(sympy.latex(half_2))
            filler = sympy.Eq(half_1, half_2)
            filler = str(sympy.solve(filler, y))
            filler = filler[1:-1]
            filler = filler.split()
            for i in range(len(filler)):
                if filler[i].find("x") != -1:
                    answer = filler[i]
            answer = answer.replace("x", "1")

            answer = "$ " + str(sympy.latex(sympy.sympify(answer))) + " $"

        elif filler == 3:
            half_1 = fr'x / {intF} {sym_1} y / {intG}'
            half_2 = fr'1'
# intC intG
            y = sympy.Symbol("y")
            half_1 = sympy.sympify(half_1, evaluate=False)
            half_2 = sympy.sympify(half_2, evaluate=False)

            problem = str(sympy.latex(half_1)) + " = " + \
                str(sympy.latex(half_2))
            filler = sympy.Eq(half_1, half_2)
            filler = str(sympy.solve(filler, y))
            filler = filler[1:-1]
            filler = filler.split()
            for i in range(len(filler)):
                if filler[i].find("x") != -1:
                    answer = filler[i]
            answer = answer.replace("x", "1")

            answer = "$ " + str(sympy.latex(sympy.sympify(answer))) + " $"

        elif filler == 4:
            half_1 = fr'{intH} * x {sym_1} {intG} * y + {intE}'
            half_2 = fr'0'

            y = sympy.Symbol("y")
            half_1 = sympy.sympify(half_1, evaluate=False)
            half_2 = sympy.sympify(half_2, evaluate=False)

            problem = str(sympy.latex(half_1)) + " = " + \
                str(sympy.latex(half_2))
            filler = sympy.Eq(half_1, half_2)
            filler = str(sympy.solve(filler, y))
            filler = filler[1:-1]
            filler = filler.split()
            for i in range(len(filler)):
                if filler[i].find("x") != -1:
                    answer = filler[i]
            answer = answer.replace("x", "1")

            answer = "$ " + str(sympy.latex(sympy.sympify(answer))) + " $"
        else:
            if random.randint(1, 2) == 1:
                problem = fr'x = {intF}'  # x = intf || y=  intf
                answer = fr'Undefined'
            else:
                problem = fr'y = {intF}'
                answer = fr'0'
            answer = "$ " + str(answer) + " $"

    return("$ " + str(problem) + " $", answer)


def AGS_Find_The_Slope_Section_4(difficulty=1, expr="latex"):
    rise = ""
    run = ""
    problem = ""
    answer = ""
    negative = ["", "-"]
    filler = ""

    intA = fix_zero_neg(str(random.choice(negative)) +
                        str(random.randint(1, 10)))
    intB = fix_zero_neg(str(random.choice(negative)) +
                        str(random.randint(1, 10)))
    intC = fix_zero_neg(str(random.choice(negative)) +
                        str(random.randint(1, 10)))
    intD = fix_zero_neg(str(random.choice(negative)) +
                        str(random.randint(1, 10)))
    intE = fix_zero_neg(str(random.choice(negative)) +
                        str(random.randint(1, 20)))
    intF = fix_zero_neg(str(random.choice(negative)) +
                        str(random.randint(1, 20)))
    intG = fix_zero_neg(str(random.choice(negative)) +
                        str(random.randint(1, 20)))
    intH = fix_zero_neg(str(random.choice(negative)) +
                        str(random.randint(1, 20)))

    if difficulty == 1:     # Easy
        problem = fr'( {intA} , {intB} ), ( {intC} , {intD})'
        rise = (int(intD) - int(intB))
        run = (int(intC) - int(intA))

        answer = fr'{rise} / {run}'
        answer = sympy.sympify(answer)
        if run == 0:
            answer = "Undefined"

    elif difficulty == 2 or difficulty == 3:    # Medium or hard
        filler = random.randint(1, 3)
        if filler == 1:
            problem = fr'( {intE} , {intF} ), ( {intG} , {intH})'
            rise = (int(intH) - int(intF))
            run = (int(intG) - int(intE))

        elif filler == 2:
            problem = fr'( {intE} , {intF} ), ( {intG} , {intH})'
            rise = (int(intH) - int(intF))
            run = (int(intG) - int(intE))

        elif filler == 3:
            problem = fr'( {intE} , {intF} ), ( {intG} , {intF})'
            rise = (int(intF) - int(intF))
            run = (int(intG) - int(intE))

        answer = fr'{rise} / {run}'
        answer = sympy.sympify(answer)
        if run == 0:
            answer = "Undefined"

    return(sympy.latex(sympy.sympify(problem, evaluate=False)), answer)
