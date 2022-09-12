# 1.5.2 Slope & Slope Intercept Form (DONE)
# section 1
# instruction: Use the middle column in each of the given tables to write the process or number patterns that relate the input to the output. Then create both a recursive and explicit function rule.

# # latex code to plot two points


# \documentclass[letterpaper,12pt]{book}%
# \usepackage[T1]{fontenc}%
# \usepackage[utf8]{inputenc}%
# \usepackage{lmodern}%
# \usepackage{textcomp}%
# \usepackage{lastpage}%
# \usepackage{multicol}%

# \usepackage{tikz}%\usetikzlibrary{arrows}

# \newcommand{\drawpoints}[6]{
# \fill [black](#1,#2) circle(6pt) node[right]{$#5$};
# \fill [black](#3,#4) circle(6pt) node[right]{$#6$};
# }
# \begin{document}
# \begin{tikzpicture}[scale=.28,extended line/.style={shorten >=-#1,shorten <=-#1},]
# \draw [help lines] (-10,-10) grid (10,10);
# % Euclidean
# \draw [<->](0,-10.2)--(0,10.2) node[right]{$y$};
# \draw [<->](-10.2,0)--(10.2,0) node[right]{$x$};

# % draw ticks and its labels
# \foreach \x in {-10,,,,,-5,,,,,,,,5,,,,,10}
# \draw (\x,1pt) -- (\x,-3pt) node[anchor=north] {\small\x};
# \foreach \y in {-10,,,,,-5,,,,,,,,5,,,,,10}
# \draw (1pt,\y) -- (-3pt,\y) node[anchor=east] {\small\y}; 

# \drawpoints{2}{3}{4}{5}

# \end{tikzpicture}
# \end{document}

import random, fractions, sympy

def fix_zero_neg(input):
    if int(input) == 0:
        return 0 
    else:
        return input

def linear_graph_line_formatter(slope, integer):
    output = ""
    output = r'\LinearEquation`{a}~`{b}~'.format(a = slope, b = integer)
    output = output.replace("`", "{")
    output = output.replace("~", "}")
    return output

def two_point_graph(one, one_2, two, two_2, vari_1, vari_2):
    # latex code to plot two points
    out = []
    inputted = ""
    out.append(r'\begin{tikzpicture}[scale=.28,extended line/.style={shorten >=-#1,shorten <=-#1},]')
    out.append(r'\draw [help lines] (-10,-10) grid (10,10);')
    out.append(r'\draw [<->](0,-10.2)--(0,10.2) node[right]{$y$};')
    out.append(r'\draw [<->](-10.2,0)--(10.2,0) node[right]{$x$};')

    out.append(r'\foreach \x in {-10,,,,,-5,,,,,,,,5,,,,,10}')
    out.append(r'\draw (\x,1pt) -- (\x,-3pt) node[anchor=north] {\small\x};')
    out.append(r'\foreach \y in {-10,,,,,-5,,,,,,,,5,,,,,10}')
    out.append(r'\draw (1pt,\y) -- (-3pt,\y) node[anchor=east] {\small\y};')
    inputted = fr'\drawpoints`{one}~`{one_2}~`{two}~`{two_2}~`{vari_1}~`{vari_2}~'
    inputted = inputted.replace('`', '{')
    inputted = inputted.replace('~', '}')
    out.append(inputted)

    out.append(r'\end{tikzpicture}')
    return ''.join(out)


def Slope_Intercept_Form_1(difficulty=1, expr="latex"):
    half_1 = ""
    half_2 = ""

    problem = ""
    answer = ""
    case = random.randint(1,3)

    sym_1 = random.choice(["-", "+"])
    variables_1 = random.choice(['E', 'K', 'U', 'R', 'D', 'W', 'G', 'H', 'V'])
    variables_2 = random.choice(['X', 'Y', 'A', 'B', 'Z', 'P', 'T'])

    intA = str(random.randint(-10,10))
    intB = str(random.randint(-10,10))
    intC = str(random.randint(-10,10))
    intD = str(random.randint(-10,10))

    if case == 1:
        half_1 = fr'{variables_1}({intA},{intB})'
        half_2 = fr'{variables_2}({intC},{intD})'
        problem = "$" + half_1 + ", " + half_2 + "$"
        problem = problem + " " + str(two_point_graph(intA, intB, intC, intD, variables_1, variables_2))
        if int(intA)-int(intC) == 0:
            answer = "Undefined"
        else:
            answer = fractions.Fraction(int(intB)-int(intD),int(intA)-int(intC)) # if denom is 0, then undefine

    elif case == 2:
        half_1 = fr''
        half_2 = fr''
        
        answer = str(linear_graph_line_formatter(str(intA) + " / " + str(intB), str(sym_1) + str(intC)))
    
    elif case == 3:
        if random.randint(1,2) == 1:
            half_1 = fr'y'
            answer = "0"
        else:
            half_1 = fr'x'
            answer = "Undefined"
        half_2 = fr'{intD}'
        

        problem = str(half_1) + " = " + str(half_2)
    return(str(problem) + r"\\What is the Slope?", "Slope (m) = " + "$" + str(answer) + "$")


for i in range(3):
    problem, answer = Slope_Intercept_Form_1(1, "latex")
    print(problem, answer)




# section 2
# Instruction : Find the slope,  m  , and the y-intercept,  b  , for each line. Then write an equation for the line.  y=mx+b


def Slope_Intercept_Form_2(difficulty=1, expr="latex"):
    problem = ""
    answer = ""

    half_1 = "" # SPLIT DA HALVES
    half_2 = ""

    negative = ["", "-"]
    filler = ""

    sym_1 = random.choice(["+", "-"])

    intA = fix_zero_neg(str(random.choice(negative)) + str(random.randint(1,10)))
    intB = fix_zero_neg(str(random.choice(negative)) + str(random.randint(1,10)))
    intC = fix_zero_neg(str(random.randint(2,10)))
    intD = fix_zero_neg(str(random.randint(1,10)))
    intE = fix_zero_neg(str(random.choice(negative)) + str(random.randint(1,20)))
    intF = fix_zero_neg(str(random.choice(negative)) + str(random.randint(1,20)))
    intG = fix_zero_neg(str(random.randint(2,20)))
    intH = fix_zero_neg(str(random.randint(1,20)))

    if difficulty == 1:     # Easy
        half_1 = fr'y'
        if int(intA) == 1:
            half_2 = fr'x {sym_1} {intC}'
        elif int(intA) == -1:
            half_2 = fr'- x {sym_1} {intC}'
        else:
            half_2 = fr'{intA} * x {sym_1} {intC}'

        half_1 = sympy.sympify(half_1, evaluate = False)
        half_2 = sympy.sympify(half_2, evaluate = False)

        problem = str(sympy.latex(half_1)) + " = " + str(sympy.latex(half_2, mode = "plain"))
        
        answer = "m = " + "$ " + str(intA) + " $", "b = " + "$ " + str(intC) + " $" 

    elif difficulty == 2:   # Medium
        filler = random.randint(1,3)
        if filler == 1:
            half_1 = fr'y'
            half_2 = fr'{intA} / {intB} * x {sym_1} {intH}'

            half_1 = sympy.sympify(half_1, evaluate = False)
            half_2 = sympy.sympify(half_2, evaluate = False)

            problem = str(sympy.latex(half_1)) + " = " + str(sympy.latex(half_2))

            answer = "$ "+ str(sympy.latex(sympy.sympify(str(intA) + " / " + str(intB)))) + " $"
        
        elif filler == 2:
            half_1 = fr'{intG} * y'
            half_2 = fr'{intC} * x {sym_1} {intH}'

            half_1 = sympy.sympify(half_1, evaluate = False)
            half_2 = sympy.sympify(half_2, evaluate = False)

            problem = str(sympy.latex(half_1)) + " = " + str(sympy.latex(half_2))
            
            answer = "$ "+ str(sympy.latex(sympy.sympify(str(intC) + " / " + str(intG)))) + " $"
        
        else:
            half_1 = fr'{intC} * y {sym_1} {intH}'
            half_2 = fr'{intG} * x'

            half_1 = sympy.sympify(half_1, evaluate = False)
            half_2 = sympy.sympify(half_2, evaluate = False)

            problem = str(sympy.latex(half_1)) + " = " + str(sympy.latex(half_2))
            
            answer = "$ "+ str(sympy.latex(sympy.sympify(str(intG) + " / " + str(intC)))) + " $"

    elif difficulty == 3:   # Hard
        filler = random.randint(1,5)
        if filler == 1:
            y = sympy.Symbol("y")
            problem = fr'{int(intD) + 1} * x {sym_1} {intC} * y = {intA}' # intB  x ±  intA  y= intD

            half_1 = fr'{int(intD) + 1} * x {sym_1} {intC} * y'
            half_2 = fr'{intA}'

            half_1 = sympy.sympify(half_1, evaluate = False)
            half_2 = sympy.sympify(half_2, evaluate = False)

            problem = str(sympy.latex(half_1)) + " = " + str(sympy.latex(half_2))
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
            half_1 = sympy.sympify(half_1, evaluate = False)
            half_2 = sympy.sympify(half_2, evaluate = False)

            problem = str(sympy.latex(half_1)) + " = " + str(sympy.latex(half_2))
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

            y = sympy.Symbol("y")
            half_1 = sympy.sympify(half_1, evaluate = False)
            half_2 = sympy.sympify(half_2, evaluate = False)

            problem = str(sympy.latex(half_1)) + " = " + str(sympy.latex(half_2))
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
            half_1 = sympy.sympify(half_1, evaluate = False)
            half_2 = sympy.sympify(half_2, evaluate = False)

            problem = str(sympy.latex(half_1)) + " = " + str(sympy.latex(half_2))
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
            if random.randint(1,2) == 1:
                problem = fr'x = {intF}' # x = intf || y=  intf
                answer = fr'Undefined'
            else:
                problem = fr'y = {intF}'
                answer = fr'0'
            answer = "$ "+ str(answer) + " $" ##

    return("$ " + str(problem) + " $", answer)


# for i in range(3):
#     problem, answer = Slope_Intercept_Form_2(1, "latex")
#     print(problem, answer)

# for i in range(3):
#     problem, answer = Slope_Intercept_Form_2(2, "latex")
#     print(problem, answer)

# for i in range(3):
#     problem, answer = Slope_Intercept_Form_2(3, "latex")
#     print(problem, answer)