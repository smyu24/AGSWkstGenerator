"""import os;from pathlib import Path
print(os.getcwd())
fff = os.getcwd()
fff1 = Path(fff)
print(fff1.parent, type(fff1))

import sys; sys.path.append(str(fff1.parent))
import loader"""
from .loader import *

def Evaluate_Equation_1(difficulty=1, expr="latex"):
  problem = ""
  answer = ""
  variables = random.choice(['x', 'y', 'a', 'b', 'z', 'p', 't', 'q', 'k', 'u', 'r', 'd', 'w', 's', 'h', 'v'])
  x = Symbol('x',real=True)
  if difficulty == 1:   # Easy
    choice = random.randint(1,2)
    intA = getInt()
    intB = getInt( 2 , 4 ) # always positive
    intC = getInt()
    intD = getInt()
    fracA = getFrac()
    if choice == 1:
      answer = latex(simplify(Rational( intC - intB ,intA)))
      answerpool = [intD,fracA,answer]
      random.shuffle(answerpool)
      if abs(intA) == 1:
          intA = str(intA)[:-1]
      problem = f"${intA} x + {intB} = {intC} , x={answerpool[0]};x={answerpool[1]};x={answerpool[2]}$"
    elif choice == 2:
      answer = latex(simplify(Rational( intC  , intA+intB)))
      answerpool = [intD,fracA,answer]
      random.shuffle(answerpool)
      if abs(intA) == 1:
          intA = str(intA)[:-1]
      if abs(intB) == 1:
          intB = str(intB)[:-1]
      problem = f'${intA} x + {intB} x = {intC} , x={answerpool[0]};x={answerpool[1]};x={answerpool[2]}$'

  elif difficulty == 2 or difficulty == 3:   # Medium and Hard
    choice = random.randint(1,2)
    intA = getInt()
    intB = getInt()
    intC = getInt()
    intD = getInt()
    intE = getInt()
    fracA = getFrac()
    if choice == 1:
      answer = latex(simplify(Rational( intC - intC ,intA + intB)))
      answerpool = [intD,fracA,answer]
      random.shuffle(answerpool)
      plusorminus = random.randint(1,2)
      problem = f"${intA} x + {intB} x + {intC} = {intD}, x={answerpool[0]};x={answerpool[1]};x={answerpool[2]}$"
    elif choice == 2:
      answer = latex(simplify(Rational( intC  , intA+intB)))
      answerpool = [intD,fracA,answer]
      random.shuffle(answerpool)
      problem = f'${intA} x + {intB} x = {intC} , x={answerpool[0]};x={answerpool[1]};x={answerpool[2]}$'
  return problem , answer


def Evaluate_Equation_2(difficulty=1, expr='latex'):
    if difficulty == 1: # easy
        slope = randint(2,9) if randint(0,1) else Rational(1,randint(2,9))
        func = LinFunc(slope, getInt(-9,9))
        mult = S.One

        problem = signify(func.getSlopeInt()) + r' \newline '
    elif difficulty == 2: # medium
        func = LinFunc(randint(2,9), getInt(-15,15))
        mult = sympify(randint(2,7)) if randint(0,1) else Rational(1,randint(2,7))

        problem = fr'{func.label}({func.variable}) = {latex(mult)}\left({str(func)}\right)'
        problem = signify(problem) + r' \newline '
    elif difficulty == 3: # hard
        func = QuadFunc(randint(1,4), randint(-5,5), randint(-9,9))
        mult = sympify(randint(2,5)) if randint(0,1) else Rational(1,randint(2,5))

        problem = fr'{func.label}({func.variable}) = {latex(mult)}\left({str(func)}\right)'
        problem = signify(problem) + r' \newline '

    inputs = random.sample(list(range(-10,11)),3)
    inputs.sort()
    problem += fr'$({inputs[0]},_), ({inputs[1]},_), ({inputs[2]},_)$'
    problem = problem.replace('_', r'\underline{\hspace{4mm}}')

    outputs = [func.subs(jj) for jj in inputs]
    outputs = [latexify(mult*jj, func.precision) for jj in outputs]
    if expr=='latex':
        answer = fr'$({inputs[0]}, {outputs[0]}), ({inputs[1]}, {outputs[1]}), ({inputs[2]}, {outputs[2]})$'
    else:
        answer = outputs

    return problem, answer


def Evaluate_Equation_3(difficulty=1, expr='latex'):
    if difficulty == 1: # easy
        func1 = LinFunc(randint(1,9), randint(1,9))
        func2 = LinFunc(randint(1,9), randint(1,9), label='g')
    elif difficulty == 2: # medium
        func1 = LinFunc(getInt(-9,9), getInt(-9,9))
        func2 = LinFunc(getInt(-9,9), getInt(-9,9), label='g')
    elif difficulty == 3: # hard
        func1 = LinFunc(Rational(getInt(-9,9),randint(2,7)), Rational(getInt(-9,9),randint(2,7)))
        func2 = LinFunc(Rational(getInt(-9,9),randint(2,7)), Rational(getInt(-9,9),randint(2,7)), label='g')

    problem = signify(func1.getSlopeInt()) + r' \newline '
    problem += signify(func2.getSlopeInt()) + r' \newline '

    input = getInt(-9,9)
    problem += fr'${func1.label}({input}) = \qquad,\qquad {func2.label}({input}) = \qquad$'

    outputs = [latexify(func1.subs(input)), latexify(func2.subs(input))]
    if expr == 'latex':
        answer = fr'${func1.label}({input}) = {outputs[0]},\qquad {func2.label}({input}) = {outputs[1]}$'
    else:
        answer = outputs

    return problem, answer
