# SECTION TWO

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

#537,225.88 or 469,523.77

if option_difficulty == "easy": # get rid of 74.90 <--- problem!!! (EDGE 0)
  for i in range(option_total_problem_number_per_page):
    integer_only = random.randint(1, 99)
    decimal = random.random()
    if integer_only % 2 == 0: 
      problem = "{:.1f}".format(integer_only + decimal)
    else:
      problem = "{:.2f}".format(integer_only + decimal)

    problemsets.append(problem)
    underscores.append(random.randint(1, len(str(problemsets[i]))))

elif option_difficulty == "medium":
  for i in range(option_total_problem_number_per_page):
    integer_only = random.randint(9, 999)
    decimal = random.random()
    decimal_2 = "{:.2f}".format(decimal)
    if integer_only % 2 == 0:
      if (float(decimal_2) * 100) % 2 == 0:
        problem  = "{:.1f}".format(integer_only + float(decimal))
      else:
        problem = "{:.2f}".format(integer_only + float(decimal))
    else:
      problem = "{:.3f}".format(integer_only + float(decimal))

    problemsets.append(problem)
    underscores.append(random.randint(1, len(str(problemsets[i]))))

elif option_difficulty == "hard":
  for i in range(option_total_problem_number_per_page):
    integer_only = random.randint(99, 9999999)
    decimal = random.random()
    if integer_only % 2 == 0:
      problem = "{:.2f}".format(integer_only + decimal)
    else:
      problem = "{:.3f}".format(integer_only + decimal)

    problemsets.append(problem)
    underscores.append(random.randint(1, len(str(problemsets[i]))))

for i in range(option_total_problem_number_per_page):
  space = 0
  places = len(str(problemsets[i]))
  period = str(problemsets[i]).find(".")
  if period != -1:
    print("-----------------------------------")
    space = places - (period + 1)
    print(period) # correct
    print("space", space) # space of decimals to be subtracted out of total
  print(places)
  places = (period - 1) // 3
  print("places", places) # the amount of commas that are going to be "inserted"
  questions = problemsets[i]
  questions = list(questions)
  if places >= 1:
    questions.insert((-4 - space), ",")
  if places >= 2:
    questions.insert((-8 - space), ",")
  print("PLACES:", places)

  print("question", questions)
  answersets.append("".join(questions))
print(problemsets)
print(answersets)
print("This is underscores", underscores) # start from the very back; disconcern the starting points. Think of it like digits