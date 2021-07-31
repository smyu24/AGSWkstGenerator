# SECTION ONE (Write each as a numeral)
from num2words import num2words

import math
import random
#from word2number import w2n | If you want to use this, pip install "!pip install word2number"

#-------- Global variables 
option_difficulty = "easy"
option_random = False
option_total_problem_number_per_page = 30

#-------- Local Variables / number generator 
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

def Reading_And_Writing_Whole_Numbers(option_difficulty, option_random):  
  if option_difficulty == "easy":
    """Generate up to two digits worth of numbers and then add zeros at the end"""
    for i in range(option_total_problem_number_per_page):
      max = random.randint(5, 7)
      integers = random.randint(1, 2)
      temp = Number_Generator(max, integers)
      print(temp)
      answerset = ""
      temp = num2words(temp, lang='en')
      print(temp)

      print("------------------------------------------")
  elif option_difficulty == "medium":
    """1,380 or 50,290"""
    for i in range(option_total_problem_number_per_page):
      max = random.randint(4, 6)
      integers = random.randint(2, 4)
      temp = Number_Generator(max, integers)
      print(temp)
      answerset = ""
      temp = num2words(temp, lang='en')
      print(temp)

      print("------------------------------------------")
  elif option_difficulty == "hard":
    """548,898,783 or 791,821,637"""
    for i in range(option_total_problem_number_per_page):
      max = 8
      integers = random.randint(7, 8)
      temp = Number_Generator(max, integers)
      print(temp)
      answerset = ""
      temp = num2words(temp, lang='en')
      print(temp)

      print("------------------------------------------")
  return temp      
Reading_And_Writing_Whole_Numbers("hard", False)

#print(w2n.word_to_num("two million three thousand nine hundred and eighty four"))