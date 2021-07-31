#Section One

import math
import random

#-------- Global variables 
option_difficulty = "easy"
option_random = False
option_total_problem_number_per_page = 30

#-------- Local Variables / number generator 

def Commanizer(problemsets, temp):
  questions = ""
  answersets = 0
  decimal_subtract = 0
  place_track = 0
  amount_commas = len(str(problemsets))
  period = str(problemsets).find(".")
  if period != -1:
    decimal_subtract = amount_commas - (period + 1)
  amount_commas = (amount_commas - 1) // 3
  questions = problemsets
  if amount_commas >= 1:
    questions.insert((-3 - decimal_subtract), ",")
  if amount_commas >= 2:
    questions.insert((-7 - decimal_subtract), ",")
  answersets = "".join(questions)
  place_track = answersets.rfind(str(temp))
  print("placetrack: ", place_track)
  return(answersets, place_track)


def Rounding_Number(option_difficulty, option_random):
  problemsets = ""
  underscores = ""
  temp_problem = []
  after_comma = []
  cut = []
  other_half = []
  temp = ""
  problemsets = random.randint(10000, 99999999)
  print(problemsets)
  underscores = random.randint(1, len(str(problemsets)) - 1)
  print(underscores)
  problemsets = list(str(problemsets))
  if int(problemsets[(underscores * -1)]) >= 5:
    cut = problemsets[underscores * -1:]
    empty = "0" * (len(cut))
    empty = list(empty)
    other_half = problemsets[:underscores * -1]
    temp = int(''.join(other_half)) + 1
    other_half = list(str(temp))
    problemsets = other_half + empty
    print("otherHALF: ", other_half)
    if int(other_half[-1]) != 0:
      temp = other_half[-1]
    else:
      temp = other_half[-2]
    print("temp: ", temp)
    print("completed: ", problemsets)
  else:
    cut = problemsets[underscores * -1:]
    empty = "0" * (len(cut))
    empty = list(empty)
    other_half = problemsets[:underscores * -1]
    problemsets = other_half + empty
    if int(other_half[-1]) != 0:
      temp = other_half[-1]
    else:
      temp = other_half[-2]
    print("temp: ", temp)
    print("DONE: ", problemsets)

  after_comma = Commanizer(problemsets, temp)
  temp_problem = list(after_comma[0])
  print(temp_problem)
  temp_problem.insert(after_comma[1], "\overline{")
  if underscores == 1:
    temp_problem.insert(-1 * len(empty), "}")

#only the last one doesnt work

  else:
    temp_problem.insert(after_comma[1] + 2, "}")
    print("else")
    
  print("other_half: ", len(other_half), "\n problemsets: ", len(problemsets) - after_comma[1] - 1)
  return(temp_problem) 

a = Rounding_Number("easy", False)

print("a", a)

#temp = num2words(temp, lang='en')