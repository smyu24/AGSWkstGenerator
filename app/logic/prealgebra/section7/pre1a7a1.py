from sympy import symbols, sympify, latex
import random

def exponent_problem_generator(difficulty='easy', expr='latex' , option_1=2 , option_2=5 , option_3=2 , option_4=10):
  x,y,z,exp1,exp2 = symbols('x,y,z,exp1,exp2')
  varlist=['x','y','z']
  random.shuffle(varlist)
  var2 = varlist.pop()
  var1 = varlist.pop()
  intA = random.randint(option_1,option_2)
  intB = random.randint(option_1,option_2)
  intTEMP = random.randint(option_1,option_2)
  intTEMP2 = random.randint(option_1,option_2)

  intC = random.randint(option_3,option_4)
  intD = random.randint(option_3,option_4)

  if difficulty == 1:
    choices = random.randint(1,4)
    if choices == 1: # case1
      #expression = x**exp1 * x**exp2
      expression = fr'{intA}**{intB} * {intA}**{intTEMP}'
      expression_answer = fr'{intA}**{intB+intTEMP}'
      #answer = expression.subs([(x,intA) ,(exp1 , intB), (exp2 , intC)])
    elif choices == 2: # case2
      #expression = intC * x**exp1 * intD * x**exp2
      expression = fr'{intC}*{intA}**{intB} * {intD}*{intA}**{intTEMP}'
      expression_answer = fr'{intC*intD}*{intA}**{intB+intTEMP}'
      #answer = expression.subs([(x, intA) , (exp1 , intB) , (exp2 , intC)])
    elif choices == 3: # case3
      #expression = ( x**exp1 )**exp2
      expression = fr'({x}**{intA})**{intB}'
      expression_answer = fr'{x}**{intA*intB}'
      #answer = expression.subs([(x, intA) , (exp1 , intB) , (exp2 , intC)])
    elif choices == 4: # case3
      #expression = ( x**exp1 )**exp2
      expression = fr'({intTEMP}**{intA})**{intB}'
      expression_answer = fr'{intTEMP}**{intA*intB}'
      #answer = expression.subs([(x, intA) , (exp1 , intB) , (exp2 , intC)])
  elif difficulty == 2:
    choices = random.randint(1,3)
    if choices == 1: # case1
      expression = fr'{intA}**{intTEMP2} * {intA}**{intB} * {intA}**{intTEMP}'
      expression_answer = fr'{intA}**{intTEMP2+intTEMP+intB}'
    elif choices == 2: # case2
      expression = fr'{intC}*{intA}**{intTEMP2} * {intD}*{intA}**{intTEMP}'
      expression_answer = fr'{intC*intD}*{intA}**{intTEMP2+intTEMP}'
    elif choices == 3: # case3
      expression = fr'{intC}*{var1}**{intB} * {intD}*{var1}**{intTEMP} * {intA} *{var2}**{intB}'
      expression_answer = fr'{intC*intD*intA}*{var2}**{intTEMP}*{var1}**{intB+intTEMP}'
  elif difficulty == 3:
    choices = random.randint(1,3)
    if choices == 1: # case1
      expression = fr'({intA}**{intTEMP2} * {intA}**{intB} * {intA}**{intTEMP})**{intC}'
      expression_answer = fr'{intA}**{(intTEMP2+intTEMP+intB)*intC}'
    elif choices == 2: # case2
      expression = fr'{intC}*{intA}**{intTEMP2} * ({intD}*{intA}**{intTEMP})**{intB}'
      expression_answer = fr'{intC* intD**intB}*{intA}**{intTEMP2+intTEMP*intB}'
    elif choices == 3: # case3   
      expression = fr'({intC}*{var1}**{intB} * {intA}*{var1}**{intTEMP})**{intTEMP2} * {intA} *{var2}**{intB}'
      expression_answer = fr'{intC**intTEMP2 * intA**intTEMP2 *intA}*{var2}**{intTEMP}*{var1}**{intB*intTEMP2+intTEMP*intTEMP2}'

  problem = '$'+latex(sympify(expression, evaluate = False))+'$'
  answer = '$'+latex(sympify(expression_answer, evaluate = False))+'$'

  return problem , answer