import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import random
import sympy

# !!!! No difficulty settings. Only one setting
# AGS1.3.1.1 - Find The Value of  x 

# section 1
# instruction : For each equation find the value of  x  that makes it true.

def Find_The_Value_Of_X_3_1_1():
    case=random.randint(1,4)
    variables = random.choice(['x', 'y', 'a', 'b', 'z', 'p', 't', 'q', 'k', 'u', 'r', 'd', 'w', 's', 'h', 'v'])
    x = sympy.symbols(str(variables))
    
    output=""
    other=""
    simple_symbol_1 = random.choice(["+", "-"])

    if case == 1:
        intA = random.randint(2,10)
        intB = random.choice([-5,-4,-3,-2,-1,1,2,3,4,5])
        if intB > 0 :
          output = fr'{intA} ** {variables}'
          other = fr'{intA} ** {intB}'
        else:
          output = fr'{intA} ** {variables}'
          other = sympy.Rational(1, intA**abs(intB))

        equation = sympy.Eq(sympy.sympify(output), sympy.sympify(other))
        return sympy.latex(equation), intB

    elif case == 2:
        intA = random.randint(2, 30)
        intB = random.randint(2, 30)
        intC = random.randint(2, 50)
        intD = random.randint(2, 50)

        output = fr'{intA} * {variables} {simple_symbol_1} {intB}'
        other = fr'{intC} * {variables} {simple_symbol_1} {intD}'

        equation = sympy.Eq(sympy.sympify(output), sympy.sympify(other))

        return sympy.latex(equation), sympy.latex(sympy.solve(equation,x))

    elif case == 3:
        intA = random.randint(2, 30)
        intB = random.randint(2, 30)
        intC = random.randint(-50, 50)
        output = fr'{intA} * {variables} {simple_symbol_1} {intB}'
        other = fr'{intC}'

        equation = sympy.Eq(sympy.sympify(output), sympy.sympify(other))

        return sympy.latex(equation), sympy.latex(sympy.solve(equation,x))
    elif case == 4:
        intA = random.randint(5, 10)
        intB = random.randint(2, 4)
        option = random.randint(1,5)

        if option == 1:
          output = fr'{intA} ^ {variables} '
          other = fr'{intA - 1} * {variables} + 1'
          equation = sympy.Eq(sympy.sympify(output), sympy.sympify(other,evaluate=False))

          return sympy.latex(equation), 1
        elif option == 2:
          output = fr'{intA} ^ {variables}'
          other = fr'{intA - intB} * {variables} + {intB}'
          equation = sympy.Eq(sympy.sympify(output), sympy.sympify(other,evaluate=False))

          return sympy.latex(equation), 1

        elif option == 3:
          output = fr'{intA} ^ {variables}'
          other = fr'1 / {intA} * {variables} + {intA} / {intA}'
          equation = sympy.Eq(sympy.sympify(output), sympy.sympify(other,evaluate=False))

          return sympy.latex(equation), 0

        elif option == 4:
          output = fr'{intA} ^ {variables}'
          other = fr'- (1 / {intA}) * {variables}'
          equation = sympy.Eq(sympy.sympify(output), sympy.sympify(other,evaluate=False))

          return sympy.latex(equation), -1

        elif option == 5:
          output = fr'{intA} ^ {variables}'
          other = fr'(1 / {intA}) * {variables} + ( {intA - 1} / {intA})'
          equation = sympy.Eq(sympy.sympify(output), sympy.sympify(other,evaluate=False))

          return sympy.latex(equation), 1