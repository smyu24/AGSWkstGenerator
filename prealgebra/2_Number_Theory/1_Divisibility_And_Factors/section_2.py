#Second Section
import math
import random

def Divisibility_And_Factors_2(option_difficulty, option_random):
  problemsets = ""
  answerset = []
  temp = []
  header_numbers = []

  if option_difficulty == "easy":
    problemsets = random.randint(1, 99)
    while len(temp) != 3:
      header_numbers.append(random.randint(2,10))
      for i in header_numbers:
        if i not in temp:
          temp.append(i)

  elif option_difficulty == "medium":
    problemsets = random.randint(50, 500)
    while len(temp) != 5:
      header_numbers.append(random.randint(2,20))
      for i in header_numbers:
        if i not in temp:
          temp.append(i)

  elif option_difficulty == "hard":
    problemsets = random.randint(500, 9999)
    while len(temp) != 7:
      header_numbers.append(random.randint(2,20))
      for i in header_numbers:
        if i not in temp:
          temp.append(i)

  header_numbers = temp
  header_numbers.sort()
    #answer generation...
  for i in range(len(header_numbers)):
      if problemsets/header_numbers[i] % 1 == 0:
        answerset.append(header_numbers[i])

  if len(answerset) == 0:
    answerset.append("None")
  return(header_numbers, problemsets, answerset)

a,b,c = Divisibility_And_Factors_2("easy", False)

print(a, "\n", b, "\n", c)
