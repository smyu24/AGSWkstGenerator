import math
import random

def Divisibility_And_Factors_1(option_difficulty, option_random):
  problemsets = ""
  temp_problem = []
  answerset = []
  temp = ""
  dividing_number = ""

  if option_difficulty == "easy":
    problemsets = random.randint(1, 99)
    dividing_number = random.randint(1,10)

  elif option_difficulty == "medium":
    problemsets = random.randint(99, 999)
    dividing_number = random.randint(1, 20)

  elif option_difficulty == "hard":
    problemsets = random.randint(1000, 9999)
    dividing_number = random.randint(1,30)

  temp_problem = str(problemsets), " by ", str(dividing_number)
  temp_problem = ''.join(temp_problem)

    #answer generation...
  temp = problemsets/dividing_number
  if temp % 1 != 0:
    answerset = "No"
  else:
    answerset = "Yes"
  return(temp_problem, answerset)

a,b = Divisibility_And_Factors_1("medium", False)

print(a, "\n", b)


