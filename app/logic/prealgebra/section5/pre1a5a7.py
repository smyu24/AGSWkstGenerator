import fractions
import sympy
import random
from fractions import Fraction


def Whole_Inequality_Graph_Template(line_length, symbol):
    line_length = int(line_length)

    number_line_size = -7  # "the zero" starting place
    MINIMUM_NUMBERLINE_SIZE = 4  # plus minus 4
    while (number_line_size + 7) + MINIMUM_NUMBERLINE_SIZE < line_length or (number_line_size + 7) - MINIMUM_NUMBERLINE_SIZE > line_length:
        if (number_line_size + 7) + MINIMUM_NUMBERLINE_SIZE < line_length:
            number_line_size = number_line_size + 3
        elif (number_line_size + 7) - MINIMUM_NUMBERLINE_SIZE > line_length:
            number_line_size = number_line_size - 3

    deviation = 0
    number_line_domain = 0
    copy = []
    out = []
    out = [r'\begin{tikzpicture}[line width=1pt,line cap=round,x=.5cm,y=.5cm]']
    out.append(r'\clip (0,-0.8) rectangle (14,1);')
    out.append(r'\draw  [<->,thick]    (0,0) -- (14,0);')
    out.append(r'\foreach \x in {1,2,...,13}')
    out.append(r'\draw (\x,-2pt) -- (\x,2pt) node [anchor=north,below=3pt]')
    out.append(r'{')
    out.append(fr'$\scriptstyle \the\numexpr{number_line_size} + 1*\x\relax$')
    out.append(r'};')
    copy = [
        r'\begin{tikzpicture}[line width=1pt,line cap=round,x=.5cm,y=.5cm]']
    copy.append(r'\clip (0,-0.8) rectangle (14,1);')
    copy.append(r'\draw  [<->,thick]    (0,0) -- (14,0);')
    copy.append(r'\foreach \x in {1,2,...,13}')
    copy.append(r'\draw (\x,-2pt) -- (\x,2pt) node [anchor=north,below=3pt]')
    copy.append(r'{')
    copy.append(fr'$\scriptstyle \the\numexpr{number_line_size} + 1*\x\relax$')
    copy.append(r'};')
    # out.append(fr'{$\scriptstyle \the\numexpr-{number_line_size}+1*\x\relax$};)')-7 + 1*
    # out.append(r"{}{}{}".format('{$\scriptstyle \the\numexpr-', str(number_line_size), '+1*\x\relax$};)'))
    if symbol == '>':
        out.append(
            fr'\draw[->,very thick,red,-latex] ({(-1 * number_line_size) + line_length}, 0) -- (12,0);')
        out.append(
            fr'\draw[red, fill=white, thick] ({(-1 * number_line_size) + line_length},0) circle (-2pt);')

    elif symbol == '<':
        out.append(
            fr'\draw[<-,very thick,red,latex-] (2,0) -- ({(-1 * number_line_size) + line_length},0);')
        out.append(
            fr'\draw[red, fill=white, thick] ({(-1 * number_line_size) + line_length},0) circle (-2pt);')

    elif symbol == '>=':
        out.append(
            fr'\draw[->,very thick,red,-latex] ({(-1 * number_line_size) + line_length},0) -- (12,0);')
        out.append(
            fr'\draw[red, fill=red, very thick] ({(-1 * number_line_size) + line_length},0) circle (-2pt);')

    elif symbol == '<=':
        out.append(
            fr'\draw[<-,very thick,red,latex-] (2,0) -- ({(-1 * number_line_size) + line_length},0);')
        out.append(
            fr'\draw[red, fill=red, very thick] ({(-1 * number_line_size) + line_length},0) circle (-2pt);')

    out.append(r'\end{tikzpicture}')
    copy.append(r'\end{tikzpicture}')
    return(''.join(out), ''.join(copy))


def Decimal_Inequality_Graph_Template(line_length, symbol):
    line_length = float(line_length)
    number_line_size = -2  # "the zero" starting place
    MINIMUM_NUMBERLINE_SIZE = 1  # plus minus 4
    while (number_line_size + 2) + MINIMUM_NUMBERLINE_SIZE < line_length or (number_line_size + 2) - MINIMUM_NUMBERLINE_SIZE > line_length:
        if (number_line_size + 2) + MINIMUM_NUMBERLINE_SIZE < line_length:
            number_line_size = number_line_size + 1
        elif (number_line_size + 2) - MINIMUM_NUMBERLINE_SIZE > line_length:
            number_line_size = number_line_size - 1

    deviation = 0
    number_line_domain = 0
    copy = []
    out = []
    out = [r'\begin{tikzpicture}[line width=1pt,line cap=round,x=1cm,y=.5cm]']
    out.append(r'\clip (0,-0.8) rectangle (7,1);')
    out.append(r'\draw  [<->,thick]    (0,0) -- (7,0);')
    out.append(r'\foreach \x in {1,2,...,6}')
    out.append(r'\draw (\x,-2pt) -- (\x,2pt) node [anchor=north,below=3pt]')
    out.append(r'{')
    out.append(fr'$\scriptstyle \the\numexpr{number_line_size} + 1*\x\relax$')
    out.append(r'};')

    copy = [r'\begin{tikzpicture}[line width=1pt,line cap=round,x=1cm,y=.5cm]']
    copy.append(r'\clip (0,-0.8) rectangle (7,1);')
    copy.append(r'\draw  [<->,thick]    (0,0) -- (7,0);')
    copy.append(r'\foreach \x in {1,2,...,6}')
    copy.append(r'\draw (\x,-2pt) -- (\x,2pt) node [anchor=north,below=3pt]')
    copy.append(r'{')
    copy.append(fr'$\scriptstyle \the\numexpr{number_line_size} + 1*\x\relax$')
    copy.append(r'};')
    if symbol == '>':
        out.append(
            fr'\draw[->,very thick,red,-latex] ({(-1 * number_line_size) + line_length}, 0) -- (7,0);')
        out.append(
            fr'\draw[red, fill=white, thick] ({(-1 * number_line_size) + line_length},0) circle (-2pt);')

    elif symbol == '<':
        out.append(
            fr'\draw[<-,very thick,red,latex-] (0,0) -- ({(-1 * number_line_size) + line_length},0);')
        out.append(
            fr'\draw[red, fill=white, thick] ({(-1 * number_line_size) + line_length},0) circle (-2pt);')

    elif symbol == '>=':
        out.append(
            fr'\draw[->,very thick,red,-latex] ({(-1 * number_line_size) + line_length},0) -- (7,0);')
        out.append(
            fr'\draw[red, fill=red, very thick] ({(-1 * number_line_size) + line_length},0) circle (-2pt);')

    elif symbol == '<=':
        out.append(
            fr'\draw[<-,very thick,red,latex-] (0,0) -- ({(-1 * number_line_size) + line_length},0);')
        out.append(
            fr'\draw[red, fill=red, very thick] ({(-1 * number_line_size) + line_length},0) circle (-2pt);')

    out.append(r'\end{tikzpicture}')
    copy.append(r'\end{tikzpicture}')
    return(''.join(out), ''.join(copy))


def else_situation(sym_1):
    if sym_1 == '<':
        sym_1 = '>'
        return(sym_1)
    elif sym_1 == '>':
        sym_1 = '<'
        return(sym_1)
    elif sym_1 == '>=':
        sym_1 = '<='
        return(sym_1)
    elif sym_1 == '<=':
        sym_1 = '>='
        return(sym_1)


def hard_diff():
    first = ""
    second = ""
    if random.randint(1, 2) == 1:
        checker = ""
        variable = random.choice(
            ['x', 'y', 'a', 'b', 'z', 'p', 't', 'q', 'k', 'u', 'r', 'd', 'w', 's', 'h', 'v'])

        number_one = random.randint(1, 30)
        number_two = random.randint(1, 30)
        number_three = random.randint(1, 30)

        sym_1 = random.choice(["+", "-"])
        negative = ["", "-"]
        inequality_sign = random.choice([">", "<", ">=", "<="])
        x = sympy.Symbol(str(variable))

        problem = ""
        answer = ""
#problem = fr"({str(variable)} {str(sym_1)} {str(number_one)}) / {str(number_three)} {str(inequality_sign)} {str(number_two)}"

        if random.randint(1, 2) == 1:  # division
            if random.randint(1, 2) == 1:
                problem = fr"{str(variable)} / {str(number_three)} {str(sym_1)} {str(number_one)} {str(inequality_sign)} {str(number_two)}"
            else:
                problem = fr"{str(number_two)} {str(inequality_sign)} {str(variable)} / {str(number_three)} {str(sym_1)} {str(number_one)}"
            #print("problem", problem)
            answer = sympy.solvers.inequalities.reduce_rational_inequalities(
                [[sympy.sympify(problem)]], x)
        else:  # multiplication
            if random.randint(1, 2) == 1:
                problem = fr"{str(random.choice(negative))} {str(number_one)} * {str(variable)} {str(sym_1)} {str(number_three)} {str(inequality_sign)} {str(number_two)}"
            else:
                problem = fr"{str(number_two)} {str(inequality_sign)} {str(random.choice(negative))} {str(number_one)} * {str(variable)} {str(sym_1)} {str(number_three)}"
            #print("problem", problem)
            answer = sympy.solvers.inequalities.reduce_rational_inequalities(
                [[sympy.sympify(problem)]], x)

        answer = str(answer)
        if str(answer).find("oo") <= 10:
            # print(answer[str(answer).find("&") + 3:-1]) #print(answer[str(answer).find("&") + 3:-1])
            checker = answer[str(answer).find("&") + 3:-1]
            #print(checker, "checker")
            list(checker)
            checker = checker.split()
            # print(checker)
            if str(checker[0]) == str(variable):
                # print("noraml")
                #print(checker[2:3], "inequal")
                #print(checker[3:], "numba")
                # print(float(Fraction(checker[3:])))
                if str(float(Fraction(checker[2])))[-2:] == ".0":
                    first, second = Whole_Inequality_Graph_Template(
                        float(checker[2]), checker[1])
                else:
                    first, second = Decimal_Inequality_Graph_Template(
                        float(Fraction(checker[2])), checker[1])
        else:
            # print("else")
            # print("HERERE--------------------")
            #print(answer[1:str(answer).find("&") - 2])
            checker = answer[1:str(answer).find("&") - 2]
            #print(checker, "checker")
            list(checker)
            checker = checker.split()
            # print(checker)
            if str(checker[0]) == str(variable):
                # print("noraml")
                #print(checker[2:3], "inequal")
                #print(checker[3:], "numba")
                # print(float(Fraction(checker[3:])))
                if str(float(Fraction(checker[2])))[-2:] == ".0":
                    first, second = Whole_Inequality_Graph_Template(
                        float(checker[2]), checker[1])
                else:
                    first, second = Decimal_Inequality_Graph_Template(
                        float(Fraction(checker[2])), checker[1])
            else:
                if str(float(Fraction(checker[0])))[-2:] == ".0":
                    first, second = Whole_Inequality_Graph_Template(
                        float(checker[0]), else_situation(checker[1]))
                else:
                    first, second = Decimal_Inequality_Graph_Template(
                        float(Fraction(checker[0])), else_situation(checker[1]))
        #print(problem, answer)
        if random.randint(1, 2) == 1:
            return(sympy.latex(sympy.sympify(problem, evaluate=False), fold_short_frac=False, mode="inline"), first, second)
        else:
            return(sympy.latex(sympy.sympify(problem), fold_short_frac=False, mode="inline"), first, second)
    else:
        checker = ""
        variable = random.choice(
            ['x', 'y', 'a', 'b', 'z', 'p', 't', 'q', 'k', 'u', 'r', 'd', 'w', 's', 'h', 'v'])

        number_one = random.randint(1, 30)
        number_two = random.randint(1, 30)
        number_three = random.randint(1, 30)

        sym_1 = random.choice(["+", "-"])
        negative = ["", "-"]
        inequality_sign = random.choice([">", "<", ">=", "<="])
        x = sympy.Symbol(str(variable))

        problem = ""
        answer = ""
        if random.randint(1, 2) == 1:
            problem = fr"{str(random.choice(negative))} ({str(variable)} {str(sym_1)} {str(number_one)}) / {str(number_three)} {str(inequality_sign)} {str(number_two)}"
        else:
            problem = fr"{str(number_two)} {str(inequality_sign)} {str(random.choice(negative))} ({str(variable)} {str(sym_1)} {str(number_one)}) / {str(number_three)} "
        answer = sympy.solvers.inequalities.reduce_rational_inequalities(
            [[sympy.sympify(problem)]], x)

        answer = str(answer)
        if str(answer).find("oo") <= 10:
            # print(answer[str(answer).find("&") + 3:-1]) #print(answer[str(answer).find("&") + 3:-1])
            checker = answer[str(answer).find("&") + 3:-1]
            #print(checker, "checker")
            list(checker)
            checker = checker.split()
            # print(checker)
            if str(checker[0]) == str(variable):
                # print("noraml")
                #print(checker[2:3], "inequal")
                #print(checker[3:], "numba")
                # print(float(Fraction(checker[3:])))
                if str(float(Fraction(checker[2])))[-2:] == ".0":
                    first, second = Whole_Inequality_Graph_Template(
                        float(checker[2]), checker[1])
                else:
                    first, second = Decimal_Inequality_Graph_Template(
                        float(Fraction(checker[2])), checker[1])
        else:
            # print("else")
            # print("HERERE--------------------")
            #print(answer[1:str(answer).find("&") - 2])
            checker = answer[1:str(answer).find("&") - 2]
            #print(checker, "checker")
            list(checker)
            checker = checker.split()
            # print(checker)
            if str(checker[0]) == str(variable):
                # print("noraml")
                #print(checker[2:3], "inequal")
                #print(checker[3:], "numba")
                # print(float(Fraction(checker[3:])))
                if str(float(Fraction(checker[2])))[-2:] == ".0":
                    first, second = Whole_Inequality_Graph_Template(
                        float(checker[2]), checker[1])
                else:
                    first, second = Decimal_Inequality_Graph_Template(
                        float(Fraction(checker[2])), checker[1])
            else:
                if str(float(Fraction(checker[0])))[-2:] == ".0":
                    first, second = Whole_Inequality_Graph_Template(
                        float(checker[0]), else_situation(checker[1]))
                else:
                    first, second = Decimal_Inequality_Graph_Template(
                        float(Fraction(checker[0])), else_situation(checker[1]))
        #print(problem, answer)
        return(sympy.latex(sympy.sympify(problem, evaluate=False), fold_short_frac=False, mode="inline"), first, second)


def integer_1():
    return random.randint(1, 20)


def integer_2():
    return random.randint(-10, 10)


def integer_3():
    return random.randint(1, 50)


def integer_4():
    return random.randint(-50, 50)


def Solving_Multi_Step_Inequalities(option_difficulty='easy', expr='latex'):
    problem = ""
    answer = ""
    temp = ""
    holder = ""

    half_1 = ""
    half_2 = ""

    sym_1 = random.choice(["+", "-"])
    sym_2 = random.choice(["+", "-"])

    var1 = random.choice(['x', 'y', 'a', 'b', 'z', 'p',
                         't', 'q', 'k', 'u', 'r', 'd', 'w', 's', 'h', 'v'])

    if option_difficulty == 1:
        x = sympy.Symbol(var1)

        if random.randint(1, 2) == 1:
            half_1 = fr'{str(integer_1())} * {str(var1)} {str(sym_1)} {str(integer_1())} * {str(var1)}'
            half_2 = fr'{str(integer_2())}'
        else:
            half_1 = fr'{str(integer_1())} * {str(var1)} {str(sym_1)} {str(integer_1())} {str(sym_2)} {str(integer_1())}'
            half_2 = fr'{str(integer_2())}'

        answer = sympy.latex(sympy.sympify(half_1, evaluate=False)) + r" = " + sympy.latex(sympy.sympify(half_2, evaluate=False))
        temp = sympy.Eq(sympy.sympify(half_1), sympy.sympify(half_2))
        holder = sympy.solve(temp, x)

    elif option_difficulty == 2:
        x = sympy.Symbol(var1)
        rand = random.randint(1, 3)
        if rand == 1:
            half_1 = fr'{str(integer_1())} * {str(var1)} {str(sym_1)} {str(integer_1())} {str(sym_2)} {str(integer_1())} * {str(var1)}'
            half_2 = fr'{str(integer_2())}'
        elif rand == 2:
            half_1 = fr'{str(integer_1())} * ( {str(integer_3())} * {str(var1)} {str(sym_1)} {str(integer_3())} {str(sym_2)} {str(integer_1())} * {str(var1)} )'
            half_2 = fr'{str(integer_2())}'
        else:
            half_1 = fr'{str(integer_3())} * ( {str(integer_3())} {str(sym_1)} {str(integer_3())} * {str(var1)} )'
            half_2 = fr'{str(integer_4())}'

        answer = sympy.latex(sympy.sympify(half_1, evaluate=False)) + r" = " + sympy.latex(sympy.sympify(half_2, evaluate=False))
        temp = sympy.Eq(sympy.sympify(half_1), sympy.sympify(half_2))
        holder = sympy.solve(temp, x)

    elif option_difficulty == 3:
        sym_3 = random.choice(["+", "-"])
        x = sympy.Symbol(var1)
        rand = random.randint(1, 3)
        if rand == 1:
            half_1 = fr'{str(integer_3())} * {str(var1)} {str(sym_1)} {str(integer_3())} {str(sym_2)} {str(integer_3())} * {str(var1)} {str(sym_3)} {str(integer_3())} * {str(var1)}'
            half_2 = fr'{str(integer_4())}'
        elif rand == 2:
            half_1 = fr'{str(integer_3())} * {str(var1)} {str(sym_1)} {str(integer_3())} * ( {str(integer_4())} {str(sym_2)} {str(integer_3())} * {str(var1)} )'
            half_2 = fr'{str(integer_4())}'
        else:
            half_1 = fr'{str(integer_3())} * ( {str(integer_3())} {str(sym_1)} {str(integer_3())} * {str(var1)} ) {str(sym_2)} {str(integer_3())}'
            half_2 = fr'{str(integer_3())} {str(sym_3)} {str(integer_3())} * {str(var1)}'

        answer = sympy.latex(sympy.sympify(half_1, evaluate=False)) + r" = " + sympy.latex(sympy.sympify(half_2, evaluate=False))
        temp = sympy.Eq(sympy.sympify(half_1), sympy.sympify(half_2))
        holder = sympy.solve(temp, x)
        holder = holder.pop()
        if str(holder).find("/") != -1:
            holder = str(holder)
            #find numerator and denominator
            print(holder[:holder.find("/")])
            print(holder[holder.find("/") + 1:])
        holder = sympy.sympify(fractions.Fraction(str(holder)))
        
        print(holder)
    return(sympy.latex(holder, fold_short_frac=False, mode="inline"), str(answer))