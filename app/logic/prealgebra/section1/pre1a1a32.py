#Section Two
from num2words import num2words

import math
import random

def insert_comma(num):
    num = int(num)
    return (f"{num:,}")


def latexify(input, option="inline"):
    if option == "inline":
        return r"$" + input + r"$"
    else:
        return '\[' + input + '\]'


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
  if amount_commas >= 1:
    questions.insert((-3 - decimal_subtract), ",")
  if amount_commas >= 2:
    questions.insert((-7 - decimal_subtract), ",")
  if amount_commas >= 3:
    questions.insert((-11 - decimal_subtract), ",")

  comma_d = "".join(questions)
  return(comma_d)


def Rounding_Number_Section_2(option_difficulty = 1, expr = 'latex', localmin = 0, localmax = 0):
    problemsets = ""
    underscores = ""
    answerset = []
    after_comma = []
    filler = ""
    wordify = ""

    if(localmin == localmax):
        if option_difficulty == 1:
            problemsets = random.randint(1000, 1000000)
            underscores = random.randint(2, len(str(problemsets)) - 1)
        elif option_difficulty == 2:
            problemsets = random.randint(1000000, 10000000000)
            underscores = random.randint(4, len(str(problemsets)) - 1)
        elif option_difficulty == 3:
            problemsets = random.randint(1000000, 10000000000)
            underscores = random.randint(4, len(str(problemsets)) - 1)
    else:
        problemsets = random.randint(localmin, localmax)
        underscores = random.randint(4, len(str(problemsets)) - 1)
    filler = "1" + str("0" * underscores)
    wordify = num2words(filler, lang='en')
    answerset = round(problemsets, -underscores)
    after_comma = Commanizer(answerset)
    pro = latexify(insert_comma(problemsets)) +"; " + wordify
    if expr == 'latex':
        return(pro, after_comma)
    else:
        return(pro, wordify, after_comma)