import math
import random
from num2words import num2words

#PY 1.1.2
def insert_comma_1(num):
    num = int(num)
    return (f"{num:,}")

def min_max_checker(option_min, option_max):
    option_min = int(option_min)
    option_max = int(option_max)
    if option_min == 0 and option_max == 0:
        return(True)
    return(False)

def Number_Generator(max,integers):
  numbers = []
  final = []
  answers = []
  for i in range(integers):
    numbers.append(random.randint(1, 9))
  zeros = "0" * max
  zeros = [*zeros]

  final.append(str(numbers.pop()))
  final = final+zeros

  for i in range(len(numbers)):
    index = random.randint(1, len(final) - 1)
    final[index] = str(numbers.pop())
  answers = ''.join(final) # append get rid of zeros
  return answers

def Reading_And_Writing_Whole_Numbers(option_difficulty='easy', expr='latex', option_min = 0, option_max = 0):
  problem = ''
  answer = ''
  if min_max_checker(option_min, option_max) == True:
    if option_difficulty == 1:
      max = random.randint(2, 4)
      integers = random.randint(1, 2)
      problem = Number_Generator(max, integers)
      answer = num2words(problem, lang='en')

    elif option_difficulty == 2:
      max = random.randint(3, 5)
      integers = random.randint(2, 4)
      problem = Number_Generator(max, integers)
      answer = num2words(problem, lang='en')

    elif option_difficulty == 3:
      max = 8
      integers = random.randint(5, 7)
      problem = Number_Generator(max, integers)
      answer = num2words(problem, lang='en')

  else:
    problem = random.randint(option_max, option_min)
    answer = num2words(problem, lang='en')

  if expr == 'latex':
    return insert_comma_1(int(problem)), answer
  else:
    return insert_comma_1(int(problem)), answer

def readingandwritingrequest(option_difficulty="easy", expr="latex", option_1="whole", option_min=0, option_max=0):
    problem, answer = Reading_And_Writing_Whole_Numbers(option_difficulty, expr, option_min , option_max)
    return problem, answer