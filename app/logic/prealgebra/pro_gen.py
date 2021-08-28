from num2words import num2words

import math
import random

'''
Pre Algebra Section 1-1
'''
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

def decimal_gen(problemsets):
  after_comma = Commanizer(problemsets)
  temp_problem = list(str(after_comma[0]))
  temp_problem.insert((after_comma[1] * -1),  "\\overline")
  temp = ''.join(temp_problem)
  temp_problem = "\\item $" + temp + "$ \\vspace{2cm}"

  temp_answer = "{\color{red}" + str(after_comma[1]) + "}"
  newpageanswer = "\\item " + "{\color{red}" + str(after_comma[1]) + "}" + " \\vspace{0.5cm}"
  temp_answer = "\\item $" + temp + "\\\\" + temp_answer + "$ \\vspace{2cm}"
  return temp_problem, temp_answer, newpageanswer

def Decimal_Places(seed):
  print(seed)
  j = 2 #Handling num. of problem
  i = 3 #Handling min and max
  k = 1 #Handling number of problem

  temp_problem = ""
  temp_answer = ""
  after_comma = []
  masterSeed = ""
  ANSmasterSeed = ""
  newpageanswer = ""

  for tried in range(seed[0]):
    for prob in range(seed[j]):
      if(seed[i] == 0 and seed[i + 1] == 0):
        if(seed[k] == 1):
          problemsets = random.randint(1, 999)

        elif(seed[k] == 2):
          problemsets = random.randint(1000, 999999)

        elif(seed[k] == 3):
          problemsets = random.randint(999999, 999999999)

        temp_masterSeed, temp_ANSmasterSeed, temp_newpageanswer = decimal_gen(problemsets)
        masterSeed += temp_masterSeed
        ANSmasterSeed += temp_ANSmasterSeed
        newpageanswer += temp_newpageanswer

      else:
        problemsets = random.randint(seed[i], seed[i+1])
        temp_masterSeed, temp_ANSmasterSeed, temp_newpageanswer = decimal_gen(problemsets)
        masterSeed += temp_masterSeed
        ANSmasterSeed += temp_ANSmasterSeed
        newpageanswer += temp_newpageanswer

    j = j + 4
    i = i + 4 
    k = k + 4
  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
Pre Algebra Section 1-2 & 1-3
'''
def Number_Generator(max,integers):
  numbers = []
  final = []
  answers = []
  for i in range(integers):
    numbers.append(random.randint(1, 9))
  zeros = "0" * max
  zeros = [*zeros] # unpacking ()

  final.append(str(numbers.pop()))
  final = final+zeros

  for i in range(len(numbers)):
    index = random.randint(1, len(final) - 1)
    final[index] = str(numbers.pop())
  
  answers = ''.join(final) # append get rid of zeros
  return answers

def Reading_Numbers(seed):  
  j = 2
  i = 3
  temp_problem = ""
  temp_answer = ""
  after_comma = []
  masterSeed = ""
  ANSmasterSeed = ""
  Nansw = ""

  for tried in range(seed[0]):
    for prob in range(seed[j]):
      max = random.randint(seed[i], seed[i+1])
      integers = random.randint(1, 8)
      temp = Number_Generator(max, integers)
      temp_problem = "\\item $" + temp + "$ \\vspace{2cm}"
      masterSeed += temp_problem
      
      #answer
      temp_answer = num2words(temp, lang='en')
      Nansw += "\\item $" + "{\color{red}" + temp_answer + "}" + "$ \\vspace{2cm}"
      temp_answer = "{\color{red}" + temp_answer + "}"
      temp_answer = "\\item $" + temp + "\\\\" + temp_answer + "$ \\vspace{2cm}"
      ANSmasterSeed += temp_answer
    j = j + 4
    i = i + 3 
  
  return (masterSeed, ANSmasterSeed, Nansw)

def WritingNumber(seed):  
  j = 2
  i = 3
  temp_problem = ""
  temp_answer = ""
  after_comma = []
  masterSeed = ""
  ANSmasterSeed = ""
  Nansw = ""

  for tried in range(seed[0]):
    for prob in range(seed[j]):
      max = random.randint(seed[i], seed[i+1])
      integers = random.randint(1, 8)
      temp = Number_Generator(max, integers)
      temp_answer = num2words(temp, lang='en')
      ans_temp = temp_answer
      temp_answer = "\\item $" + temp_answer + "$ \\vspace{2cm}"
      masterSeed += temp_answer
      
      #answer
      Nansw += "\\item $" + "{\color{red}" + temp + "}" + "$ \\vspace{2cm}"
      temp_problem = "{\color{red}" + temp + "}"
      temp_problem = "\\item $" + ans_temp + "\\\\" + temp_problem + "$ \\vspace{2cm}"
      ANSmasterSeed += temp_problem
    j = j + 4
    i = i + 3 
  
  return (masterSeed, ANSmasterSeed, Nansw)

'''
Pre Algebra Section 1-4
'''
def Commanizer2(problemsets):
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


def Rounding_To_Word_Numbers(seed):
  print(seed)
  j = 2 #num of problem
  i = 3 #min and max
  k = 1 #difficulty
  temp_problem = ""
  temp_answer = ""
  after_comma = []
  masterSeed = ""
  ANSmasterSeed = ""
  Nansw = ""

  for tried in range(seed[0]):
    for prob in range(seed[j]):
      problemsets = random.randint(seed[i], seed[i+1])
      underscores = random.randint(2, len(str(problemsets)) - 1)
      answerset = []
      after_comma = []
      filler = "1" + "0" * underscores
      wordify = num2words(filler, lang='en')
      answerset = round(problemsets, -underscores)
      after_comma = Commanizer2(answerset)

      temp_problem = "\\item $" + str(problemsets) + "; " + wordify + "$ \\vspace{2cm}"
      masterSeed += temp_problem
      
      #answer
      Nansw += "\\item $" + "{\color{red}" + after_comma + "}" + "$ \\vspace{2cm}"
      temp_answer = "{\color{red}" + after_comma + "}"
      temp_answer = "\\item $" + str(problemsets) + "; " + wordify + "\\\\" + temp_answer + "$ \\vspace{2cm}"
      ANSmasterSeed += temp_answer
    j = j + 4
    i = i + 3 

  return (masterSeed, ANSmasterSeed, Nansw)

'''
Pre Algebra Section 2-1
'''
def Divisibility(seed):
  j = 0
  i = 1
  temp_problem = ""
  temp_answer = ""
  after_comma = []
  masterSeed = ""
  ANSmasterSeed = ""

  for tried in range(3):
    for prob in range(seed[j]):
      problemsets = random.randint(seed[i], seed[i+1])
      dividing_number = random.randint(1,10)
      temp =  str(problemsets) + " by " + str(dividing_number)
      temp_problem = "\\item $" + temp + "$ \\vspace{2cm}"
      masterSeed += temp_problem
      
      #answer
      temps = problemsets/dividing_number
      if temps % 1 != 0:
        temp_answer = "No"
      else:
        temp_answer = "Yes"

      temp_answer = "{\color{red}" + temp_answer + "}"
      temp_answer = "\\item $" + temp + "\\\\" + temp_answer + "$ \\vspace{2cm}"
      ANSmasterSeed += temp_answer
    j = j + 3
    i = i + 3 

  return masterSeed + "||" + ANSmasterSeed

'''
Pre Algebra Section 2-2
'''
def Factoring(seed):
  j = 0
  i = 1
  temp_problem = ""
  temp_answer = ""
  after_comma = []
  masterSeed = ""
  ANSmasterSeed = ""

  for tried in range(3):
    for prob in range(seed[j]):
      header_numbers = []
      temp = []
      answerset = []
      problemsets = random.randint(seed[i], seed[i+1])
      for k in range(6):
        header_numbers.insert(k, random.randint(1,10))

      for k in header_numbers:
        if k not in temp:
          temp.append(k)
      header_numbers = temp
      header_numbers.sort()

      for k in range(len(header_numbers)):
        if problemsets/header_numbers[k] % 1 == 0:
          answerset.append(header_numbers[k])

      if len(answerset) == 0:
        answerset.append("None")

      temp_problem = "\\item $" + str(problemsets) + "$ \\vspace{2cm}"
      masterSeed += temp_problem
      
      #answer
      answerset = str(answerset)
      answerset = answerset[1:-1]
      temp_answer = "{\color{red}" + str(answerset) + "}"
      temp_answer = "\\item $" + str(problemsets) + "\\\\" + temp_answer + "$ \\vspace{2cm}"
      ANSmasterSeed += temp_answer
    j = j + 3
    i = i + 3 

  return masterSeed + "||" + ANSmasterSeed