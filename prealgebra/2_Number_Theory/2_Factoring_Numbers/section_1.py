#First Section

import math
import random

def Factoring_Num(option_difficulty, option_random):
  problemsets = ""
  answerset = []
  temp = []

  if option_difficulty == "easy":
    problemsets = random.randint(10, 50)

  elif option_difficulty == "medium" or option_difficulty == "hard":
    problemsets = random.randint(50, 99)

    #answer generation...
  for i in range(1, int(problemsets / 2) + 1):
    if problemsets % i == 0:
      if i not in temp:
        temp.append(i)
      if int(problemsets/i) not in temp:
        temp.append(int(problemsets/i))

  return(problemsets, temp) # nothing yet

a,b = Factoring_Num("medium", False)
b.sort()
print(a, "\n", b, "\n")
