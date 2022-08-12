import math
import random
import sympy


def perfecto_square(n):
   n = int(n)
   sq_root = int(math.sqrt(abs(n)))
   return (sq_root*sq_root) == n

def prime_check(n):
    if n == 1:
        return False
        # from 1 to sqrt(n) 
    for x in range(2, (int)(math.sqrt(n))+1):
        if n % x == 0:
            return False 
    return True

def Square_Roots_Section_1(option_difficulty = "easy", expr= "latex"):
  problemset = ""
  answerset = ""
  negative = ['-', '']
  if option_difficulty == 1:
    problemset = str(random.choice(negative)) + str(int(random.randint(1, 200)))
    while perfecto_square(problemset) == False:
      problemset = str(random.choice(negative)) + str(int(random.randint(1, 200)))

    if random.randint(1,2) == 1:
      problemset = str(problemset)
      answerset = sympy.sqrt(sympy.simplify(str(problemset)))
      problemset = r"- \sqrt{" + str(problemset) + "}"
      return(problemset, sympy.latex(sympy.simplify('-'+str(answerset))))
    else:
      answerset = sympy.simplify(sympy.sqrt(sympy.simplify(problemset)))
      problemset = r"\sqrt{" + str(problemset) + "}"
      return(problemset, sympy.latex(answerset))
    
  elif option_difficulty == 2:
    problemset = int(random.randint(1, 100))
    while prime_check(problemset) == True:
      problemset = int(random.randint(1, 100))
    if random.randint(1,2) == 1:
      problemset = str(problemset)
      answerset = sympy.sqrt(sympy.simplify(str(problemset)))
      problemset = r"- \sqrt{" + str(problemset) + "}"
      return(problemset, sympy.latex(sympy.simplify('-'+str(answerset))))
    else:
      answerset = sympy.simplify(sympy.sqrt(sympy.simplify(problemset)))
      problemset = r"\sqrt{" + str(problemset) + "}"
      return(problemset, sympy.latex(answerset))
  
  elif option_difficulty == 3:
    problemset = int(random.randint(100, 200))
    while prime_check(problemset) == True:
      problemset = int(random.randint(100, 200))
    if random.randint(1,2) == 1:
      problemset = str(problemset)
      answerset = sympy.sqrt(sympy.simplify(str(problemset)))
      problemset = r"- \sqrt{" + str(problemset) + "}"
      return(problemset, sympy.latex(sympy.simplify('-'+str(answerset))))
    else:
      answerset = sympy.simplify(sympy.sqrt(sympy.simplify(problemset)))
      problemset = r"\sqrt{" + str(problemset) + "}"
      return(problemset, sympy.latex(answerset))