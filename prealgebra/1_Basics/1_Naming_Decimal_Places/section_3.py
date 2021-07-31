# SECTION THREE

import math
import random

#-------- Global variables 
option_difficulty = "hard"
option_random = False
option_total_problem_number_per_page = 30

#-------- Local Variables / number generator 

problemsets = []
answersets = []
underscores = []

#5.887472 or 23.77231

if option_difficulty == "easy": # get rid of 74.90 <--- problem!!! (EDGE 0)
  for i in range(option_total_problem_number_per_page):
    integer_only = random.randint(1, 9)
    decimal = random.random()
    if integer_only % 2 == 0: 
      problem = "{:.1f}".format(integer_only + decimal)
    else:
      problem = "{:.2f}".format(integer_only + decimal)

    problemsets.append(problem)
    underscores.append(random.randint(1, len(str(problemsets[i]))))

elif option_difficulty == "medium":
  for i in range(option_total_problem_number_per_page):
    integer_only = random.randint(1, 99)
    decimal = random.random()
    decimal_2 = "{:.2f}".format(decimal)
    if integer_only % 2 == 0:
      if (float(decimal_2) * 100) % 2 == 0:
        problem  = "{:.1f}".format(integer_only + float(decimal))
      elif int(str(decimal_2 * 100)[:1]) % 3 == 0:
        problem  = "{:.4f}".format(integer_only + float(decimal))
      else:
        problem = "{:.2f}".format(integer_only + float(decimal))
    else: #add one more (ten thousandth place) if the front is divisible by 2
      problem = "{:.3f}".format(integer_only + float(decimal))

    problemsets.append(problem)
    underscores.append(random.randint(1, len(str(problemsets[i]))))

elif option_difficulty == "hard":
  for i in range(option_total_problem_number_per_page):
    integer_only = random.randint(10, 100)
    decimal = random.random()
    if integer_only % 2 == 0:
      problem = "{:.8f}".format(integer_only + decimal)
    else:
      problem = "{:.7f}".format(integer_only + decimal)
    #will have two cutt off points

    problemsets.append(problem)
    underscores.append(random.randint(1, len(str(problemsets[i]))))

print(problemsets)
print("This is underscores", underscores) # start from the very back; disconcern the starting points. Think of it like digits