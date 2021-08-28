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


def Decimal_Places(seed):
  j = 0
  i = 1
  temp_problem = ""
  after_comma = []
  masterSeed = ""

  for tried in range(3):
    for prob in range(seed[j]):
      problemsets = random.randint(seed[i], seed[i+1])
      after_comma = Commanizer(problemsets)
      temp_problem = list(str(after_comma[0]))
      temp_problem.insert((after_comma[1] * -1),  "\\overline")
      temp_problem = ''.join(temp_problem)
      #temp_problem = "\\item$" + temp_problem + "$\\vspace{2cm}, " + str(after_comma[1])
      temp_problem = "\\item $" + temp_problem + "$ \\vspace{2cm}"
      masterSeed += temp_problem
    j = j + 3
    i = i + 3 
  
  return(masterSeed)