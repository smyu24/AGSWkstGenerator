# First Section

import math
import random
import sympy as sp
import fractions

def Whole_Inequality_Graph_Template(line_length, symbol):
    line_length = int(line_length)
    number_line_size = -7 # "the zero" starting place
    MINIMUM_NUMBERLINE_SIZE = 4 #plus minus 4
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
    copy = [r'\begin{tikzpicture}[line width=1pt,line cap=round,x=.5cm,y=.5cm]']
    copy.append(r'\clip (0,-0.8) rectangle (14,1);')
    copy.append(r'\draw  [<->,thick]    (0,0) -- (14,0);')
    copy.append(r'\foreach \x in {1,2,...,13}')
    copy.append(r'\draw (\x,-2pt) -- (\x,2pt) node [anchor=north,below=3pt]')
    copy.append(r'{')
    copy.append(fr'$\scriptstyle \the\numexpr{number_line_size} + 1*\x\relax$')
    copy.append(r'};')
    #out.append(fr'{$\scriptstyle \the\numexpr-{number_line_size}+1*\x\relax$};)')-7 + 1*
    #out.append(r"{}{}{}".format('{$\scriptstyle \the\numexpr-', str(number_line_size), '+1*\x\relax$};)'))
    if symbol == '>':
        out.append(fr'\draw[->,very thick,red,-latex] ({(-1 * number_line_size) + line_length}, 0) -- (12,0);')
        out.append(fr'\draw[red, fill=white, thick] ({(-1 * number_line_size) + line_length},0) circle (-2pt);')
        
    elif symbol == '<':
        out.append(fr'\draw[<-,very thick,red,latex-] (2,0) -- ({(-1 * number_line_size) + line_length},0);')
        out.append(fr'\draw[red, fill=white, thick] ({(-1 * number_line_size) + line_length},0) circle (-2pt);')
        
    elif symbol == '>=':
        out.append(fr'\draw[->,very thick,red,-latex] ({(-1 * number_line_size) + line_length},0) -- (12,0);')
        out.append(fr'\draw[red, fill=red, very thick] ({(-1 * number_line_size) + line_length},0) circle (-2pt);')
        
    elif symbol == '<=':
        out.append(fr'\draw[<-,very thick,red,latex-] (2,0) -- ({(-1 * number_line_size) + line_length},0);')
        out.append(fr'\draw[red, fill=red, very thick] ({(-1 * number_line_size) + line_length},0) circle (-2pt);')
        
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

def Solving_One_Step_Inequalities_Adding_Subtracting(option_difficulty = 'easy', expr = 'latex'):
    problemsets = []
    answerset = []
    another = []
    choices = ['x', 'y', 'a', 'b', 'z', 'p', 't', 'q', 'k', 'u', 'r', 'd', 'w', 's', 'h', 'v']
    addition_expression = ['+', '-']
    negative = ['-', '']
    sym_1 = ''
    sym_1 = ''
    variables = []
    numerals = []
    equation = ''
    ran = 0
    receivant = ""
    inequal_symbols = ['>', '<', '>=', '<=']
    if option_difficulty == 1: # greater/less than or equal to included (positive variables and number range from -5 to 5)  x − 1 > 6
        variables.append(random.choice(choices))
        sym_1 = random.choice(inequal_symbols)
        sym_2 = random.choice(addition_expression)
        numerals.append(str(random.randint(1, 5)))
        numerals.append(str(random.choice(negative)) + str(random.randint(1, 5)))

        x = sp.symbols(variables[0])
        
        ran = random.randint(1,4)
 
        if ran == 1:
            equation = '{} {} {} {} {}'.format(variables[0], sym_2, numerals[0], str(sym_1) , str(numerals[1]))
            problemsets.append(sp.latex(sp.sympify(equation),fold_short_frac=False, mode="inline"))
            if sym_2 == '+':
                numerals[1] = int(numerals[1]) - int(numerals[0])
            else:
                numerals[1] = int(numerals[1]) + int(numerals[0])
            receivant = Whole_Inequality_Graph_Template(numerals[1], sym_1)
            answerset.append(receivant[0])
            another.append(receivant[1])
        elif ran == 2:
            equation = '{} {} {} {} {}'.format(str(numerals[0]), sym_2, variables[0], str(sym_1), str(numerals[1]))
            problemsets.append(sp.latex(sp.sympify(equation),fold_short_frac=False, mode="inline"))
            numerals[1] = int(numerals[1]) - int(numerals[0])
            if sym_2 == '-':
                sym_1 = else_situation(sym_1)
                numerals[1] = int(numerals[1]) * -1
            receivant = Whole_Inequality_Graph_Template(numerals[1], sym_1)
            answerset.append(receivant[0])
            another.append(receivant[1])
        elif ran == 3:# inequal first
            equation = '{} {} {} {} {}'.format(str(numerals[1]), str(sym_1), variables[0], sym_2, str(numerals[0]))
            problemsets.append(sp.latex(sp.sympify(equation),fold_short_frac=False, mode="inline"))
            if sym_2 == '+':
                numerals[1] = int(numerals[1]) - int(numerals[0])
            else:
                numerals[1] = int(numerals[1]) + int(numerals[0])
            receivant = Whole_Inequality_Graph_Template(numerals[1], else_situation(sym_1))
            answerset.append(receivant[0])
            another.append(receivant[1])
        else:
            equation = '{} {} {} {} {}'.format(str(numerals[1]), str(sym_1), str(numerals[0]), sym_2, variables[0])
            problemsets.append(sp.latex(sp.sympify(equation),fold_short_frac=False, mode="inline"))
            numerals[1] = int(numerals[1]) - int(numerals[0])
            if sym_2 == '-':
                sym_1 = else_situation(sym_1)
                numerals[1] = int(numerals[1]) * -1
            receivant = Whole_Inequality_Graph_Template(numerals[1], else_situation(sym_1))
            answerset.append(receivant[0])
            another.append(receivant[1])


    elif option_difficulty == 2: # greater/less than or equal to included, but with a greater number threshhold and possibility of negative variables -x−14>−12
        if str(random.choice(negative)) == '-':
            variables.append('-' + str(random.choice(choices)))
            sym_1 = random.choice(inequal_symbols)
            sym_2 = random.choice(addition_expression)
            numerals.append(str(random.randint(1, 10)))
            numerals.append(str(random.choice(negative)) + str(random.randint(1, 10)))

            x = sp.symbols(variables[0])

            ran = random.randint(1,2)

            if ran == 1:
                equation = '{} {} {} {} {}'.format(variables[0], sym_2, numerals[0], str(sym_1) , str(numerals[1]))
                problemsets.append(sp.latex(sp.sympify(equation),fold_short_frac=False, mode="inline"))
                if sym_2 == '+':
                    numerals[1] = int(numerals[1]) - int(numerals[0])
                else:
                    numerals[1] = int(numerals[1]) + int(numerals[0])
                receivant = Whole_Inequality_Graph_Template(int(numerals[1]) * -1, else_situation(sym_1))
                answerset.append(receivant[0])
                another.append(receivant[1])
            else: # inequal first
                equation = '{} {} {} {} {}'.format(str(numerals[1]), str(sym_1), variables[0], sym_2, str(numerals[0]))
                problemsets.append(sp.latex(sp.sympify(equation),fold_short_frac=False, mode="inline"))
                if sym_2 == '+':
                    numerals[1] = int(numerals[1]) - int(numerals[0])
                else:
                    numerals[1] = int(numerals[1]) + int(numerals[0])
                receivant = Whole_Inequality_Graph_Template(int(numerals[1]) * -1, sym_1)
                answerset.append(receivant[0])
                another.append(receivant[1])
        else:
            variables.append(random.choice(choices))
            sym_1 = random.choice(inequal_symbols)
            sym_2 = random.choice(addition_expression)
            numerals.append(str(random.randint(1, 10)))
            numerals.append(str(random.choice(negative)) + str(random.randint(1, 10)))

            x = sp.symbols(variables[0])

            ran = random.randint(1,4)

   
            if ran == 1:
                equation = '{} {} {} {} {}'.format(variables[0], sym_2, numerals[0], str(sym_1) , str(numerals[1]))
                problemsets.append(sp.latex(sp.sympify(equation),fold_short_frac=False, mode="inline"))
                if sym_2 == '+':
                    numerals[1] = int(numerals[1]) - int(numerals[0])
                else:
                    numerals[1] = int(numerals[1]) + int(numerals[0])
                receivant = Whole_Inequality_Graph_Template(numerals[1], sym_1)
                answerset.append(receivant[0])
                another.append(receivant[1])
            elif ran == 2:
                equation = '{} {} {} {} {}'.format(str(numerals[0]), sym_2, variables[0], str(sym_1), str(numerals[1]))
                problemsets.append(sp.latex(sp.sympify(equation),fold_short_frac=False, mode="inline"))
                numerals[1] = int(numerals[1]) - int(numerals[0])
                if sym_2 == '-':
                    sym_1 = else_situation(sym_1)
                    numerals[1] = int(numerals[1]) * -1
                receivant = Whole_Inequality_Graph_Template(numerals[1], sym_1)
                answerset.append(receivant[0])
                another.append(receivant[1])
            elif ran == 3:# inequal first
                equation = '{} {} {} {} {}'.format(str(numerals[1]), str(sym_1), variables[0], sym_2, str(numerals[0]))
                problemsets.append(sp.latex(sp.sympify(equation),fold_short_frac=False, mode="inline"))
                if sym_2 == '+':
                    numerals[1] = int(numerals[1]) - int(numerals[0])
                else:
                    numerals[1] = int(numerals[1]) + int(numerals[0])
                receivant = Whole_Inequality_Graph_Template(numerals[1], else_situation(sym_1))
                answerset.append(receivant[0])
                another.append(receivant[1])
            else:
                equation = '{} {} {} {} {}'.format(str(numerals[1]), str(sym_1), str(numerals[0]), sym_2, variables[0])
                problemsets.append(sp.latex(sp.sympify(equation),fold_short_frac=False, mode="inline"))
                numerals[1] = int(numerals[1]) - int(numerals[0])
                if sym_2 == '-':
                    sym_1 = else_situation(sym_1)
                    numerals[1] = int(numerals[1]) * -1
                receivant = Whole_Inequality_Graph_Template(numerals[1], else_situation(sym_1))
                answerset.append(receivant[0])
                another.append(receivant[1])
    
    
    elif option_difficulty == 3: # all of the above, and some more... (larger num threshhold)
        if str(random.choice(negative)) == '-':
            variables.append('-' + str(random.choice(choices)))
            sym_1 = random.choice(inequal_symbols)
            sym_2 = random.choice(addition_expression)
            numerals.append(str(random.randint(10, 30)))
            numerals.append(str(random.choice(negative)) + str(random.randint(10, 30)))

            x = sp.symbols(variables[0])

            ran = random.randint(1,2)
 
            if ran == 1:
                equation = '{} {} {} {} {}'.format(variables[0], sym_2, numerals[0], str(sym_1) , str(numerals[1]))
                problemsets.append(sp.latex(sp.sympify(equation),fold_short_frac=False, mode="inline"))
                if sym_2 == '+':
                    numerals[1] = int(numerals[1]) - int(numerals[0])
                else:
                    numerals[1] = int(numerals[1]) + int(numerals[0])
                receivant = Whole_Inequality_Graph_Template(int(numerals[1]) * -1, else_situation(sym_1))
                answerset.append(receivant[0])
                another.append(receivant[1])
            else: # inequal first
                equation = '{} {} {} {} {}'.format(str(numerals[1]), str(sym_1), variables[0], sym_2, str(numerals[0]))
                problemsets.append(sp.latex(sp.sympify(equation),fold_short_frac=False, mode="inline"))
                if sym_2 == '+':
                    numerals[1] = int(numerals[1]) - int(numerals[0])
                else:
                    numerals[1] = int(numerals[1]) + int(numerals[0])
                receivant = Whole_Inequality_Graph_Template(int(numerals[1]) * -1, sym_1)
                answerset.append(receivant[0])
                another.append(receivant[1])
        else:
            variables.append(random.choice(choices))
            sym_1 = random.choice(inequal_symbols)
            sym_2 = random.choice(addition_expression)
            numerals.append(str(random.randint(10, 30)))
            numerals.append(str(random.choice(negative)) + str(random.randint(10, 30)))

            x = sp.symbols(variables[0])

            ran = random.randint(1,4)

            if ran == 1:
                equation = '{} {} {} {} {}'.format(variables[0], sym_2, numerals[0], str(sym_1) , str(numerals[1]))
                problemsets.append(sp.latex(sp.sympify(equation),fold_short_frac=False, mode="inline"))
                if sym_2 == '+':
                    numerals[1] = int(numerals[1]) - int(numerals[0])
                else:
                    numerals[1] = int(numerals[1]) + int(numerals[0])
                receivant = Whole_Inequality_Graph_Template(numerals[1], sym_1)
                answerset.append(receivant[0])
                another.append(receivant[1])
            elif ran == 2:
                equation = '{} {} {} {} {}'.format(str(numerals[0]), sym_2, variables[0], str(sym_1), str(numerals[1]))
                problemsets.append(sp.latex(sp.sympify(equation),fold_short_frac=False, mode="inline"))
                numerals[1] = int(numerals[1]) - int(numerals[0])
                if sym_2 == '-':
                    sym_1 = else_situation(sym_1)
                    numerals[1] = int(numerals[1]) * -1
                receivant = Whole_Inequality_Graph_Template(numerals[1], sym_1)
                answerset.append(receivant[0])
                another.append(receivant[1])
            elif ran == 3:# inequal first
                equation = '{} {} {} {} {}'.format(str(numerals[1]), str(sym_1), variables[0], sym_2, str(numerals[0]))
                problemsets.append(sp.latex(sp.sympify(equation),fold_short_frac=False, mode="inline"))
                if sym_2 == '+':
                    numerals[1] = int(numerals[1]) - int(numerals[0])
                else:
                    numerals[1] = int(numerals[1]) + int(numerals[0])
                receivant = Whole_Inequality_Graph_Template(numerals[1], else_situation(sym_1))
                answerset.append(receivant[0])
                another.append(receivant[1])
            else:
                equation = '{} {} {} {} {}'.format(str(numerals[1]), str(sym_1), str(numerals[0]), sym_2, variables[0])
                problemsets.append(sp.latex(sp.sympify(equation),fold_short_frac=False, mode="inline"))
                numerals[1] = int(numerals[1]) - int(numerals[0])
                if sym_2 == '-':
                    sym_1 = else_situation(sym_1)
                    numerals[1] = int(numerals[1]) * -1
                receivant = Whole_Inequality_Graph_Template(numerals[1], else_situation(sym_1))
                answerset.append(receivant[0])
                another.append(receivant[1])

    return(problemsets[0], answerset[0], another[0])
