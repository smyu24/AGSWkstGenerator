#Section Two
from num2words import num2words

import math
import random

#-------- Global variables 
option_difficulty = "easy"
option_random = False
option_total_problem_number_per_page = 30

#-------- Local Variables / number generator 

def Commanizer(problemsets):
  questions = ""
  comma_d = ""
  decimal_subtract = 0
  amount_commas = len(str(problemsets))
  period = str(problemsets).find(".")
  if period != -1:
    decimal_subtract = amount_commas - (period + 1)
  amount_commas = (amount_commas - 1) // 3
  questions = list(str(problemsets))
  print("b", questions)
  if amount_commas >= 1:
    questions.insert((-3 - decimal_subtract), ",")
  if amount_commas >= 2:
    questions.insert((-7 - decimal_subtract), ",")
  if amount_commas >= 3:
    questions.insert((-11 - decimal_subtract), ",")

  comma_d = "".join(questions)
  return(comma_d)


def Rounding_To_Word_Numbers(option_difficulty, option_random):
  problemsets = ""
  underscores = ""
  answerset = []
  after_comma = []
  filler = ""
  wordify = ""
  cut = 0

  if option_difficulty == "easy":
    problemsets = random.randint(1000, 1000000)
    underscores = random.randint(2, len(str(problemsets)) - 1)
  elif option_difficulty == "medium":
    problemsets = random.randint(1000000, 10000000000)
    underscores = random.randint(4, len(str(problemsets)) - 1)
  elif option_difficulty == "hard":
    problemsets = random.randint(1000000, 10000000000)
    underscores = random.randint(4, len(str(problemsets)) - 1)
  print(underscores)
  filler = "1" + "0" * underscores
  wordify = num2words(filler, lang='en') + "'s place"
  cut = wordify.rfind("one")
  if cut == 0:
    wordify = wordify[cut + 4:]
  print(wordify)

  print(problemsets)
  answerset = round(problemsets, -underscores)
  print(answerset)
  after_comma = Commanizer(answerset)
  print("ANSWER", after_comma)
  
  return(problemsets, wordify, after_comma)

a,b,c = Rounding_To_Word_Numbers("medium", False)

print(b)
print(a)
print(c)

#temp = num2words(temp, lang='en')