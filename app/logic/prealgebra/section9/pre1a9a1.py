import random
import sympy
import fractions

def fix_zero_neg(input):
    if int(input) == 0:
        return 0
    else:
        return input


def add_basic_plot_padding(input):
    plot=[]
    plot.append(r"\begin{tikzpicture}[scale=.5,extended line/.style={shorten >=-#1,shorten <=-#1},]")
    plot.append(r"\draw [help lines] (-6,-6) grid (6,6);")

    plot.append(r"\draw [<->](0,-6.2)--(0,6.2) node[right]{$y$};")
    plot.append(r"\draw [<->](-6.2,0)--(6.2,0) node[right]{$x$};")

    plot.append(r"\foreach \x in {-6,-5,-4,-3,-2,-1,1,2,3,4,5,6}")
    plot.append(r"\draw (\x,1pt) -- (\x,-3pt) node[anchor=north] {\x};")
    plot.append(r"\foreach \y in {-6,-5,-4,-3,-2,-1,1,2,3,4,5,6}")
    plot.append(r"\draw (1pt,\y) -- (-3pt,\y) node[anchor=east] {\y};")

    plot.append(fr"{input}")
    plot.append(r"\end{tikzpicture}")
    return(''.join(plot))


def Find_The_Slope_Section_1(option_difficulty="easy", expr="latex"):
    rise = ""
    run = ""
    problem = ""
    answer = ""
    negative = ["", "-"]

    intA = fix_zero_neg(str(random.choice(negative)) + str(random.randint(0, 5)))
    intB = fix_zero_neg(str(random.choice(negative)) + str(random.randint(0, 5)))
    intC = fix_zero_neg(str(random.choice(negative)) + str(random.randint(0, 5)))
    intD = fix_zero_neg(str(random.choice(negative)) + str(random.randint(0, 5)))
    intA_2 = fix_zero_neg(str(random.choice(negative)) + str(random.randint(0, 5)))
    intB_2 = fix_zero_neg(str(random.choice(negative)) + str(random.randint(0, 5)))
    intC_2 = fix_zero_neg(str(random.choice(negative)) + str(random.randint(0, 5)))
    intD_2 = fix_zero_neg(str(random.choice(negative)) + str(random.randint(0, 5)))

    if option_difficulty == 1:
        if random.randint(1, 2) == 1:
            #point_1 = ( intA , 0 )
            #point_2 = ( intB , intC)
            while abs(int(intB) - int(intA)) == 0:
                intB = str(random.choice(negative)) + str(random.randint(0, 5))
                intA = str(random.choice(negative)) + str(random.randint(0, 5))
            problem = fr"\drawaline`{intA}~`{0}~`{intB}~`{intC}~"
            if abs(int(intB) - int(intA)) == 0:
                Find_The_Slope_Section_1(option_difficulty, expr)
            rise = int(intC)
            run = (int(intB) - int(intA))

        else:
            # point 3 ( 0 , intA_2)
            # point 4 ( intB_2 , intC_2)
            if abs(int(intB_2)) == 0:
                Find_The_Slope_Section_1(option_difficulty, expr)
            while abs(int(intB_2)) == 0:
                intB_2 = str(random.choice(negative)) + str(random.randint(0, 5))
            problem = fr"\drawaline`{0}~`{intA_2}~`{intB_2}~`{intC_2}~"
            rise = (int(intC_2) - int(intA_2))
            run = (int(intB_2))
        answer = fractions.Fraction(rise, run)
        problem = problem.replace('`', "{")
        problem = problem.replace('~', "}")
        if answer == 0:
            answer = "Zero Slope" # Horizontal
        elif abs(run) == 0:
            answer = "Undefined Slope" # Vertical
        return add_basic_plot_padding(problem), answer

    elif option_difficulty == 2 or option_difficulty == 3:
        if random.randint(1, 2) == 1:
            #point_1 = ( intA , 0 )
            #point_2 = ( intB , intC)
            while abs(int(intB) - int(intA)) == 0:
                intB = str(random.choice(negative)) + str(random.randint(0, 5))
                intA = str(random.choice(negative)) + str(random.randint(0, 5))
            problem = fr"\drawaline`{intA}~`{intD}~`{intB}~`{intC}~"
            if abs(int(intB) - int(intA)) == 0:
                Find_The_Slope_Section_1(option_difficulty, expr)
            rise = int(intC) - int(intD)
            run = (int(intB) - int(intA))

        else:
            # point 3 ( 0 , intA_2)
            # point 4 ( intB_2 , intC_2)
            if abs(int(intB_2)) == 0:
                Find_The_Slope_Section_1(option_difficulty, expr)
            while abs(int(intB_2) - int(intD_2)) == 0:
                intB_2 = str(random.choice(negative)) + str(random.randint(0, 5))
                intD_2 = str(random.choice(negative)) + str(random.randint(0, 5))
            problem = fr"\drawaline`{intD_2}~`{intA_2}~`{intB_2}~`{intC_2}~"
            rise = (int(intC_2) - int(intA_2))
            run = (int(intB_2) - int(intD_2))

        answer = fractions.Fraction(rise, run)
        problem = problem.replace('`', "{")
        problem = problem.replace('~', "}")
        if answer == 0:
            answer = "Zero Slope" # Horizontal
        elif abs(run) == 0:
            answer = "Undefined Slope" # Vertical
        return(str(add_basic_plot_padding(problem)), answer)


def Find_The_Slope_Section_2(option_difficulty="easy", expr="latex"):
    rise = ""
    run = ""
    problem = ""
    answer = ""
    negative = ["", "-"]
    filler = ""

    intA = fix_zero_neg(str(random.choice(negative)) + str(random.randint(1,10)))
    intB = fix_zero_neg(str(random.choice(negative)) + str(random.randint(1,10)))
    intC = fix_zero_neg(str(random.choice(negative)) + str(random.randint(1,10)))
    intD = fix_zero_neg(str(random.choice(negative)) + str(random.randint(1,10)))
    intE = fix_zero_neg(str(random.choice(negative)) + str(random.randint(1,20)))
    intF = fix_zero_neg(str(random.choice(negative)) + str(random.randint(1,20)))
    intG = fix_zero_neg(str(random.choice(negative)) + str(random.randint(1,20)))
    intH = fix_zero_neg(str(random.choice(negative)) + str(random.randint(1,20)))

    if option_difficulty == 1:
        problem = fr'( {intA} , {intB} ), ( {intC} , {intD})'
        rise = (int(intD) - int(intB))
        run = (int(intC) - int(intA))

        answer = fr'{rise} / {run}'
        answer = sympy.sympify(answer)
        if run == 0:
            answer = "Undefined"

    elif option_difficulty == 2 or option_difficulty == 3:
        filler = random.randint(1,3)
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

    print("here", problem, answer)
    return( ('$'+ str(sympy.latex(sympy.sympify(problem, evaluate=False))) + "$"), (str(sympy.latex(answer))) )


def Find_The_Slope_Section_3(option_difficulty="easy", expr="latex"):
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

    if option_difficulty == 1:
        half_1 = r'y'
        if int(intA) == 1:
            half_2 = fr'x {sym_1} {intC}'
        elif int(intA) == -1:
            half_2 = fr'- x {sym_1} {intC}'
        else:
            half_2 = fr'{intA} * x {sym_1} {intC}'

        half_1 = sympy.sympify(half_1, evaluate = False)
        half_2 = sympy.sympify(half_2, evaluate = False)

        problem = str(sympy.latex(half_1)) + " = " + str(sympy.latex(half_2, mode = "plain"))

        answer = sympy.sympify(intA)

    elif option_difficulty == 2:
        filler = random.randint(1,3)
        if filler == 1:
            half_1 = r'y'
            half_2 = fr'{intA} / {intB} * x {sym_1} {intH}'

            half_1 = sympy.sympify(half_1, evaluate = False)
            half_2 = sympy.sympify(half_2, evaluate = False)

            problem = str(sympy.latex(half_1)) + " = " + str(sympy.latex(half_2))

            answer = sympy.sympify(str(intA) + " / " + str(intB))

        elif filler == 2:
            half_1 = fr'{intG} * y'
            half_2 = fr'{intC} * x {sym_1} {intH}'

            half_1 = sympy.sympify(half_1, evaluate = False)
            half_2 = sympy.sympify(half_2, evaluate = False)

            problem = str(sympy.latex(half_1)) + " = " + str(sympy.latex(half_2))

            answer = sympy.sympify(str(intC) + " / " + str(intG))

        else:
            half_1 = fr'{intC} * y {sym_1} {intH}'
            half_2 = fr'{intG} * x'

            half_1 = sympy.sympify(half_1, evaluate = False)
            half_2 = sympy.sympify(half_2, evaluate = False)

            problem = str(sympy.latex(half_1)) + " = " + str(sympy.latex(half_2))

            answer = sympy.sympify(str(intG) + " / " + str(intC))

    elif option_difficulty == 3:
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

            answer = sympy.sympify(answer)

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

            answer = sympy.sympify(answer)

        elif filler == 3:
            half_1 = fr'x / {intF} {sym_1} y / {intG}'
            half_2 = r'1'
#intC intG
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

            answer = sympy.sympify(answer)

        elif filler == 4:
            half_1 = fr'{intH} * x {sym_1} {intG} * y + {intE}'
            half_2 = r'0'

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

            answer = sympy.sympify(answer)
        else:
            if random.randint(1,2) == 1:
                problem = r'x = {intF}' # x = intf || y=  intf
                answer = r'Undefined'
            else:
                problem = fr'y = {intF}'
                answer = r'0'
    return( ('$'+ str(problem) + "$"), (str(sympy.latex(answer))) )

