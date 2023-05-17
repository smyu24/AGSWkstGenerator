import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import sympy
import random

#given two functions, find the point of intersection
#fractions inc
#output point of intersection in a (x, y) format

def Systems_of_Equation(expr='sympy',option='standard',range_x=3,range_y=3,coeff_mult_range=5):
    '''
    expr = latex , sympy
    option = standard : ax + by = c
          point_slope : y=mx+b 
    range_x = location of solution for x-coordination(evenly distributed -3 to 3 or -10 to 10)
    range_y = location of solution for y-coordination(evenly distributed -3 to 3 or -10 to 10)
    coeff_mult_range= controller for dynamic range shift for the coeff of eqs
    '''
    x, y = sympy.symbols('x y')
    # Generate solution point first
    x = random.randint(-range_x, range_x)
    y = random.randint(-range_y, range_y)
    # Start from reduced echelon form (coeffs 1)
    c1 = [1, 0, x]
    c2 = [0, 1, y]
    def randNonZero():
        return random.choice([i for i in range(-coeff_mult_range, coeff_mult_range) if i != 0])
    # Add random (non-zero) multiple of equations (rows) to each other
    c1_mult = randNonZero()
    c2_mult = randNonZero()
    new_c1 = [c1[i] + c1_mult * c2[i] for i in range(len(c1))]
    new_c2 = [c2[i] + c2_mult * c1[i] for i in range(len(c2))]
    '''
    #For extra randomness, now add random (non-zero) multiples of original rows to themselves
    c1_mult = randNonZero()
    c2_mult = randNonZero()
    new_c1 = [new_c1[i] + c1_mult * c1[i] for i in range(len(c1))]
    new_c2 = [new_c2[i] + c2_mult * c2[i] for i in range(len(c2))]
    '''
    # construct Standard Form
    def standard_form_construct(coeffs): 
        # lots of edge cases for perfect formatting
        x_sign = '-' if coeffs[0] < 0 else ''
        # No redundant 1s
        x_coeff = str(abs(coeffs[0])) #if abs(coeffs[0]) != 1 else ''
        # If x coeff is 0, dont include x
        x_str = f'{x_sign}{x_coeff}*x' if coeffs[0] != 0 else ''
        # if x isn't included and y is positive, dont include operator
        op = ' - ' if coeffs[1] < 0 else (' + ' if x_str != '' else '')
        # No redundant 1s
        y_coeff = abs(coeffs[1]) #if abs(coeffs[1]) != 1 else ''
        # Don't include if 0, unless x is also 0 (probably never happens)
        y_str = f'{y_coeff}*y' #if coeffs[1] != 0 else ('' if x_str != '' else '0')
        lhs = f'{x_str}{op}{y_str}'
        rhs = f'{coeffs[2]}'
        return lhs , rhs
    
    # construct point slope form
    def pointslope_form_construct(coeffs):
        slope = sympy.Rational(-coeffs[0],coeffs[1])
        yint = sympy.Rational(coeffs[2],coeffs[1])
        lhs = 'y'
        rhs = f'{slope}*x + {yint}' if slope != 0 else (f'x + {yint}')
        return lhs , rhs
    
    if option == 'standard':
      eq1lhs , eq1rhs = standard_form_construct(new_c1)
      eq2lhs , eq2rhs = standard_form_construct(new_c2)

    elif option == 'point_slope':
      eq1lhs , eq1rhs = pointslope_form_construct(new_c1)
      eq2lhs , eq2rhs = pointslope_form_construct(new_c2)

    solution = [x,y]

    if expr == 'sympy':  
      return sympy.sympify(eq1lhs), sympy.sympify(eq1rhs), sympy.sympify(eq2lhs), sympy.sympify(eq2rhs), solution
    elif expr == 'latex':
      return sympy.latex(sympy.sympify(eq1lhs)) , sympy.latex(sympy.sympify(eq1rhs)),sympy.latex(sympy.sympify(eq2lhs)),sympy.latex(sympy.sympify(eq2rhs)) , solution