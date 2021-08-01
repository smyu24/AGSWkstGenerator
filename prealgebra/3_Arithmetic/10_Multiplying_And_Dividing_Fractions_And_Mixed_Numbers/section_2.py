# Second Section

import fractions
import math
import random
from fractions import Fraction


def Multiplying_And_Dividing_Fractions_And_Mixed_Numbers_2(option_difficulty, option_random):
    problemsets = []
    answerset = []
    temp = 0
    list_temp = []
    one = 0
    two = 0
    temp = 0
    value = 0
    holder = ''
    negative = ['-', '']

    if option_difficulty == "easy":
        one = float("0." + str(random.randint(1, 9)))
        two = float("0." + str(random.randint(1, 9)))

    elif option_difficulty == "medium":
        one = float(random.choice(negative) +
                    str(random.randint(1, 3)) + "." + str(random.randint(1, 9)))
        two = float(random.choice(negative) +
                    str(random.randint(1, 3)) + "." + str(random.randint(1, 9)))

    elif option_difficulty == "hard":
        one = float(random.choice(negative) +
                    str(random.randint(1, 9)) + "." + str(random.randint(1, 9)))
        two = float(random.choice(negative) +
                    str(random.randint(1, 9)) + "." + str(random.randint(1, 9)))

    one = fractions.Fraction(str(one))
    two = fractions.Fraction(str(two))
    print(one,two)
    temp = str(one / two)
    temp.replace("Fraction(", '')
    temp.replace(")", '')
    print(temp)
    list_temp = list(temp)
    print(list_temp)
    value = temp.find("/")
    if len(list_temp) > 1:
      if abs(int(''.join(list_temp[:value]))) >= int(''.join(list_temp[value + 1:])):
          answerset.append(
              int(int(''.join(list_temp[:value])) / int(''.join(list_temp[value + 1:]))))
          holder = Fraction(int(''.join(list_temp[:value])) % int(
              ''.join(list_temp[value + 1:])), int(''.join(list_temp[value + 1:])))
          holder = str(holder)
          holder.replace('Fraction(', '')
          holder.replace(')', '')
          answerset.append(holder)
      else:
          answerset.append(temp)
    elif len(list_temp) <= 1:
      answerset.append(temp)
    problemsets.append("$ " + str(one) + " \div " + str(two) + " $")
    return(problemsets, answerset)


a, b = Multiplying_And_Dividing_Fractions_And_Mixed_Numbers_2("easy", False)
print(a, b)
a, b = Multiplying_And_Dividing_Fractions_And_Mixed_Numbers_2("medium", False)
print(a, b)
a, b = Multiplying_And_Dividing_Fractions_And_Mixed_Numbers_2("hard", False)
print(a, b)
