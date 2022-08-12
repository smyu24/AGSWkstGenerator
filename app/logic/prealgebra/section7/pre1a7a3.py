#fix number bases gathering problems
from sympy import symbols,latex,sympify,powsimp
import random
import re

def isprime(n):
    return re.compile(r'^1?$|^(11+)\1+$').match('1' * n) is None

def Powers_Of_Products(difficulty='easy', expr='latex' , option_1=2 , option_2=10 , option_3=2 , option_4=20):
  '''
  option_1 = int min
  option_2 = int max
  option_3 = int min
  option_4 = int max
  '''
  x,y,z,a,b,c = symbols('x,y,z,a,b,c',commutative=False)
  varlist=['x','y','z','a','b','c']
  random.shuffle(varlist)
  var1 = varlist.pop()
  var2 = varlist.pop()
  var3 = varlist.pop()

  primeNumbers = [x for x in range(100) if isprime(x)]

  intA = random.randint(option_1,option_2)
  intB = random.randint(option_1,option_2)
  intC = random.randint(option_1,option_2)
  intD = random.randint(option_1,option_2)

  intE = random.randint(option_3,option_4)
  intF = random.randint(option_3,option_4)
  intG = random.randint(option_3,option_4)
  intH = random.randint(option_3,option_4)
  intI = random.randint(option_3,option_4)
  intJ = random.randint(option_3,option_4)


  if difficulty == 1:
    choices = random.randint(1,2)
    if choices == 1: # case1
      expression = fr'({intA} * {var1}**{intB} )**{intD}'
      expression_answer = fr'{intA}**{intD} * {var1}**({intB*intD}) '
    elif choices == 2: # case2
      expression = fr'({intA}**{intB} * {var1}**{intC} )**{intD}'
      expression_answer = fr'{intA}**({intB*intD}) * {var1}**({intC*intD})'

  elif difficulty == 2:
    choices = random.randint(1,2)
    if choices == 1: # case1
      expression = fr'({intA} * {var1}**{intB} *{var2}**{intC})**{intD}'
      expression_answer = fr'{intA}**{intD} * {var1}**{intB*intD}*{var2}**{intC*intD} '
    elif choices == 2: # case2
      expression = fr'({intA}**{intB} * {var1}**{intC} *{var2}**{intD})**{intE}'
      expression_answer = fr'{intA}**{intB+intE} * {var1}**{intC*intE} * {var2}**{intE*intD}'

  elif difficulty == 3:
    expression = fr'({intA}**{intB} * {var1}**{intC} *{var2}**{intD}* {intA}**{intE} * {var2}**{intF} *{var1}**{intG})**{intI}'
    expression_answer = fr'{intA}**{intB*intI+intE*intI} * {var1}**{intC*intI + intG*intI} *{var2}**{intD*intI+intF*intI}'


  problem = '$'+latex(sympify(expression, evaluate = False))+'$'
  answer = '$'+latex(sympify(expression_answer, evaluate = False))+'$'
  return problem , answer