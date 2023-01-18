import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from loader import getInt, sample, variables
from sympy import *
from random import randint

# AGS1.2.3.1 - rules of exponents 
# instruction : Use rules of exponents to rewrite each of the expressions with only one exponent.
def getExpandedForm(base, exp, start=1):
    if base>0:
        factors = exp*[latex(base)]
    else:
        factors = exp*[r'\left(' + latex(base) + r'\right)']
    if start != 1:
        factors = [latex(start)] + factors
    return (r' \times ').join(factors)

def getExponentForm(base, exp, start=1, posExpOnly=False):
    start = latex(start)

    if posExpOnly==True and exp<0:
        return r'\frac{' + start + r'}{' + getExponentForm(base, abs(exp)) + r'}'
    
    baseStr = latex(base)
    if type(base)!=int or base<0:
        baseStr = r'\left(' + baseStr + r'\right)'
    expStr = r'^{' + latex(exp) + r'}'
    
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

def Rules_Of_Exponents(difficulty=1, expr="latex", posExpOnly=False):
    base = getInt(2,10)
    exp1 = getInt(2,10)
    exp2 = getInt(2,10)

    if difficulty==1: # easy
        if randint(0,1):
            problem = getExponentForm(base,exp1) + r'\cdot '
            problem += getExponentForm(base, exp2)
            expAns = exp1 + exp2
        else:
            problem = r'\frac{' + getExponentForm(base,exp1) + r'}{'
            problem += getExponentForm(base, exp2) + r'}'
            expAns = exp1 - exp2

    if difficulty==2: # medium
        exp3 = getInt(2,10)
        case = randint(1,3)
        if case == 1:
            problem = fr'\left({getExponentForm(base, exp1)}\right)^{exp2} \cdot'
            problem += getExponentForm(base, exp3)
            expAns = exp1*exp2 + exp3
        elif case == 2:
            problem = r'\frac{' + getExponentForm(base,exp1) + r'}{'
            problem += getExponentForm(base, exp2) + r'}'
            problem = r'\left(' + problem + fr'\right)^{exp3}'
            expAns = exp3*(exp1 - exp2)
        else:
            problem = fr'\left({getExponentForm(base, exp1)}\right)^{exp2}'
            problem = r'\frac{' + problem + r'}{' + getExponentForm(base, exp3) + r'}'
            expAns = exp1*exp2 - exp3

    if difficulty==3: # hard
        var1,var2,var3,var4 = sample(variables,4)
        case = randint(1,4)
        if case == 1:
            problem = fr'\left({var3}^{var4}\right)^{var1}\cdot {var3}^{var2}'
            answer = powsimp(powdenest(((var3**var4)**var1)*var3**var2, force=True), force=True)
        elif case == 2:
            problem = r'\left(\left(\frac{' + fr'{base}^{var1}' + r'}{' + fr'{base}^{var3}'
            problem += r'}\right)^' + fr'{var2}\right)^{var4}'
            answer = powsimp(powdenest( ((base**var1 / base**var3)**var2)**var4, force=True), force=True)
        elif case == 3:
            problem = fr'\left({var3}^{var4}\right)^{var1}\cdot {var3}^{var2}'
            answer = powsimp(powdenest( ((var3**var4)**var1)*var3**var2 , force=True), force=True)
        else:
            problem = r'\left(\left(\frac{' + fr'{var1}^{var2}' + r'}{' + fr'{var1}^{var3}'
            problem += r'}\right)^' + fr'{var2}\right)^{var4}'
            answer = powsimp(powdenest( ((var1**var2 / var1**var3)**var2)**var4, force=True), force=True)
        
    if expr == "latex":
        problem = '$' + problem + '$'
        if difficulty<3:
            answer = '$' + getExponentForm(base, expAns, posExpOnly=posExpOnly) + '$'
        else:
            answer = f'${latex(answer)}$'
    else:
        answer = {'base': base, 'exp': expAns} if difficulty<3 else answer

    return problem, answer