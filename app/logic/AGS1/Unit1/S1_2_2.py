import sys; sys.path.insert(0, "..")

from loader import getInt, signify
from sympy import *
from random import randint, sample

# PRECURSOR FUNCT
def getExpandedForm(base, exp, start=1):
    """
    Return LaTeX formatted expanded exponential expression.
    
    Parameters
    ----------
        base : number (int, float, or Rational)
        exp : int
    """
    
    if base>0:
        factors = exp*[latex(base)]
    else:
        factors = exp*[r'\left(' + latex(base) + r'\right)']
    if start != 1:
        factors = [latex(start)] + factors
    return (r' \times ').join(factors)

def getExponentForm(base, exp, start=1):
    """Return LaTeX formatted exponential expression."""
    
    baseStr = latex(base)
    if type(base)!=int or base<0:
        baseStr = r'\left(' + baseStr + r'\right)'
    expStr = r'^{' + latex(exp) + r'}'
    start = latex(start)
    
    result = baseStr + expStr
    if start != '1':
        if type(base)!=int or base<0:
            result = start + result
        else:
            result = start + r'\cdot ' + result
    if base<0 and type(exp)==int: # Alternate solution for base<0; Does not handle case of start!=1
        baseStr = latex(abs(base))
        if type(base)!=int:
            baseStr = r'\left(' + baseStr + r'\right)'
        result += r' \text{ or } '
        alt = '-' + baseStr + expStr if exp%2==1 else baseStr + expStr
        result += alt

    return result


# ConvertToExponentForm
def The_Meaning_Of_An_Exponent_1(difficulty=1, expr="latex"):
    exp = getInt(4,9)
    
    if difficulty == 1: # easy
        base = getInt(1,10)
    if difficulty == 2: # medium
        base = getInt(-10,-1)
    if difficulty == 3: # hard
        base = sample([1,2,3,5,7,11,13],2)
        if randint(0,1):
            base[0] *= -1
        base = Rational(base[0],base[1]) if base[1]!=1 else Rational(base[1],base[0])
    
    problem = getExpandedForm(base, exp)
    if expr == 'latex':
        problem = '$' + problem + '$'
        answer = '$' + getExponentForm(base, exp) + '$'
    else:
        answer = {'base' : base, 'exp' : exp}

    return problem, answer

# ConvertToExpandedForm
def The_Meaning_Of_An_Exponent_2(difficulty=1, expr="latex"):
    exp = getInt(2,10)
    
    if difficulty == 1: # easy
        base = getInt(2,10)
        start = 1
        value = base**exp
    if difficulty == 2: # medium
        base = getInt(2,10)
        start = getInt(-10,20,exclude=[-1,0,1])
        value = start*base**exp
    if difficulty == 3: # hard
        base = sample([1,2,3,5,7],2)
        base = Rational(base[0],base[1]) if base[1]!=1 else Rational(base[1],base[0])
        start = getInt(-10,20,exclude=[-1,0,1])
        value = simplify(start*base**exp)
    
    problem = getExponentForm(base, exp, start)
    if expr == 'latex':
        problem = '$' + problem + '$'
        answer = '$' + getExpandedForm(base, exp, start) + r'$ \newline '
        answer += signify(latex(value))
    else:
        answer = {'base' : base, 'exp' : exp, 'start' : start, 'value' : value}

    return problem, answer

