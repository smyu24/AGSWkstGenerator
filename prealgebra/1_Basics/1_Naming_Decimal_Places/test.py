# SECTION ONE

import math
import random

#whole numbers only 199 or 11,717,555

def Commanizer(problemsets):
  questions = ""
  answersets= 0
  decimal_subtract = 0
  amount_commas = len(str(problemsets))
  period = str(problemsets).find(".")
  if period != -1:
    decimal_subtract = amount_commas - (period + 1)
  amount_commas = (amount_commas - 1) // 3
  questions = problemsets
  questions = list(str(questions))
  if amount_commas >= 1:
    questions.insert((-3 - decimal_subtract), ",")
  if amount_commas >= 2:
    questions.insert((-7 - decimal_subtract), ",")

  underbar = random.randint(1, len(str(problemsets)) + amount_commas)
  while questions[underbar * -1] == ",": 
    underbar = random.randint(1, len(str(problemsets)) + amount_commas)
  # get underwcores. Run again id it lands on comma
  answersets = "".join(questions)
  return(answersets, underbar)


def Decimal_Places(option_difficulty, option_random):
  problemsets = ""
  underscores = ""
  temp_problem = []
  after_comma = []
  if option_difficulty == "easy":
    problemsets = random.randint(1, 999)

  elif option_difficulty == "medium":
    problemsets = random.randint(1000, 999999)

  elif option_difficulty == "hard":
    problemsets = random.randint(999999, 999999999)
  
  after_comma = Commanizer(problemsets)
  temp_problem = list(str(after_comma[0]))
  temp_problem.insert((after_comma[1] * -1), "\overline{")
  if after_comma[1] == 1: # MUST FIX
    temp_problem.insert(len(after_comma[0]) + 1, "}")
  else:
    temp_problem.insert((after_comma[1] * -1) + 1, "}")
  temp_problem = ''.join(temp_problem)
  #after_comma = Commanizer(problemsets)
  
  return(temp_problem, underscores)

a,b = Decimal_Places("medium", False)

print(a,b)


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