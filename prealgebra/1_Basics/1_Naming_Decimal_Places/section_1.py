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
  temp_problem.insert((after_comma[1] * -1), "\overline")
  #if after_comma[1] == 1: # MUST FIX
  #  temp_problem.insert(len(after_comma[0]) + 1, "\}")
  #else:
  #  temp_problem.insert((after_comma[1] * -1) + 1, "\}")
  temp_problem = ''.join(temp_problem)
  #after_comma = Commanizer(problemsets)
  
  return(temp_problem, after_comma[1])

a,b = Decimal_Places("medium", False)

print(a,b)


