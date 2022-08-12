from sympy import symbols, sympify, latex
import random

def Exponent_Division(difficulty='easy', expr='latex' , option_1=2 , option_2=10 , option_3=2 , option_4=20):
  x,y,z,a,b,c = symbols('x,y,z,a,b,c')
  varlist=['x','y','z','a','b','c']
  random.shuffle(varlist)
  var1 = varlist.pop()
  var2 = varlist.pop()
  var3 = varlist.pop()
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
      expression = fr'{var1}**{intB} / {var1}**{intD}'
    elif choices == 2: # case2
      expression = fr'({intE}*{var2}**{intB}) / ({intF}*{var2}**{intD})'
  elif difficulty == 2:
    choices = random.randint(1,2)
    if choices == 1: # case1
      expression = fr'({intG}*{var1}**{intB} )/ ({intH}*{var1}**{intD})'
    elif choices == 2: # case2
      expression = fr'({intE}*{var2}**{intB}) / ({intF}*{var2}**{intD})'
  elif difficulty == 3:
    choices = random.randint(1,2)
    if choices == 1: # case1
      expression = fr'({intG}*{var1}**{intB}*{var2}**{intC} )/ ({intH}*{var1}**{intD}*{var2}**{intA})'
    elif choices == 2: # case2
      expression = fr'({intE}*{var2}**{intB}*{var1}**{intG}) / ({intF}*{var2}**{intD}*{var1}**{intH})'
    elif choices == 3: # case3
      expression = fr'({intE}*{var2}**{intB}*{var1}**{intG}*{var3}**{intI}) / ({intF}*{var2}**{intD}*{var1}**{intH}*{var3}**{intJ})'



  problem = '$'+latex(sympify(expression, evaluate = False))+'$'
  answer = '$'+latex(sympify(expression))+'$'

  return problem , answer