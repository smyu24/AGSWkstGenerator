# First Section

import math
import random

def formatter(a, b):
  if random.randint(1,2) == 1:
    return str(a) + r"\text{ and } " + str(b) 
  else:
    return str(b) + r"\text{ and } " + str(a) 

def checker(first, second, third, fourth):
  smaller = ""
  bigger = ""
  fill = ""
  smaller = int(first) * int(fourth)
  bigger = int(second) * int(third)

  if bigger < smaller:
    fill = bigger
    bigger = smaller
    smaller = fill

  if (bigger) == (smaller):
    return "Yes"
  else: 
    return "No"

def fractionizer(a,b):
  return r"\frac{" + str(a) + "}{" + str(b) + "}"

def Proportions_Section_1(option_difficulty = 'easy', expr = "latex"):
  f_problem = ""
  answer = ""
  f_top = ""
  f_bottom = ""

  s_problem = ""
  s_top = ""
  s_bottom = ""

  if option_difficulty == 1:
    f_top = random.randint(1, 5)
    f_bottom = random.randint(1, 5)
    f_problem = fractionizer(str(f_top),str(f_bottom))

    s_top = int(f_top) * int(random.randint(1,5)) 
    s_bottom = int(f_bottom) * int(random.randint(1,5))
    s_problem = fractionizer(str(s_top), str(s_bottom))
    problem = formatter(f_problem, s_problem)
    answer = checker(f_top, f_bottom, s_top, s_bottom)
    if (answer == "No") and (random.randint(1,4) == 1 or 2 or 3):
        Proportions_Section_1(option_difficulty, expr)


  elif option_difficulty == 2:
    f_top = random.randint(1, 10)
    f_bottom = random.randint(1, 10)
    f_problem = r"\frac{" + str(f_top) + "}{" + str(f_bottom) + "}"

    s_top = int(f_top) * int(random.randint(1,10)) 
    s_bottom = int(f_bottom) * int(random.randint(1,10))
    s_problem = r"\frac{" + str(s_top) + "}{" + str(s_bottom) + "}"
    problem = formatter(f_problem, s_problem)
    answer = checker(f_top, f_bottom, s_top, s_bottom)
    if (answer == "No") and (random.randint(1,4) == 1 or 2 or 3):
        Proportions_Section_1(option_difficulty, expr)
  

  elif option_difficulty == 3:
    f_top = random.randint(1, 15)
    f_bottom = random.randint(1, 15)
    f_problem = r"\frac{" + str(f_top) + "}{" + str(f_bottom) + "}"

    s_top = int(f_top) * int(random.randint(1,15)) 
    s_bottom = int(f_bottom) * int(random.randint(1,15))
    s_problem = r"\frac{" + str(s_top) + "}{" + str(s_bottom) + "}"
    problem = formatter(f_problem, s_problem)
    answer = checker(f_top, f_bottom, s_top, s_bottom)
    if (answer == "No") and (random.randint(1,4) == 1 or 2 or 3):
        Proportions_Section_1(option_difficulty, expr)
  return problem, answer

def solver(a,b,c,d,pos):
    if pos == 1:
        return(str((int(b) * int(c)) / int(d)))
    elif pos == 2:
        return(str((int(a) * int(d)) / int(c)))
    elif pos == 3:
        return(str((int(a) * int(d)) / int(b)))
    elif pos == 4:
        return((int(b) * int(c)) / int(a))

def type_check(a):
    if str(float(a))[-2:] == ".0":
        a = int(a)
    return(a)

def Proportions_Section_2(option_difficulty='easy', expr="latex"):
    choices = ['x', 'y', 'a', 'b', 'z', 'p', 't', 'q', 'k', 'u', 'r', 'd', 'w', 's', 'h', 'v']
    
    f_problem = ""
    answer = ""
    f_top = ""
    f_bottom = ""

    s_problem = ""
    s_top = ""
    s_bottom = ""

    variable = random.choice(choices)
    which = random.randint(1,4)
    if option_difficulty == 1:
        f_top = random.randint(1, 5)
        f_bottom = random.randint(1, 5)
        
        s_top = int(f_top) * int(random.randint(1, 5))
        s_bottom = int(f_bottom) * int(random.randint(1, 5))

        if which == 1:
            f_top = variable
        elif which == 2:
            f_bottom = variable
        elif which == 3:
            s_top = variable
        elif which == 4:
            s_bottom = variable

        f_problem = fractionizer(str(f_top), str(f_bottom))
        s_problem = fractionizer(str(s_top), str(s_bottom))
        problem = formatter(f_problem, s_problem)
        answer = solver(str(f_top), str(f_bottom), str(s_top), str(s_bottom), which)
        answer = type_check(round(float(answer), 3))
        answer = str(variable) + " = " +str(answer)

    elif option_difficulty == 2:
        f_top = random.randint(1, 10)
        f_bottom = random.randint(1, 10)
        
        s_top = int(f_top) * int(random.randint(1, 10))
        s_bottom = int(f_bottom) * int(random.randint(1, 10))

        if which == 1:
            f_top = variable
        elif which == 2:
            f_bottom = variable
        elif which == 3:
            s_top = variable
        elif which == 4:
            s_bottom = variable

        f_problem = fractionizer(str(f_top), str(f_bottom))
        s_problem = fractionizer(str(s_top), str(s_bottom))
        problem = formatter(f_problem, s_problem)
        answer = solver(str(f_top), str(f_bottom), str(s_top), str(s_bottom), which)
        answer = type_check(round(float(answer), 3))
        answer = str(variable) + " = " +str(answer)


    elif option_difficulty == 3:
        f_top = random.randint(1, 15)
        f_bottom = random.randint(1, 15)
        
        s_top = int(f_top) * int(random.randint(1, 15))
        s_bottom = int(f_bottom) * int(random.randint(1, 15))

        if which == 1:
            f_top = variable
        elif which == 2:
            f_bottom = variable
        elif which == 3:
            s_top = variable
        elif which == 4:
            s_bottom = variable

        f_problem = fractionizer(str(f_top), str(f_bottom))
        s_problem = fractionizer(str(s_top), str(s_bottom))
        problem = formatter(f_problem, s_problem)
        answer = solver(str(f_top), str(f_bottom), str(s_top), str(s_bottom), which)
        answer = type_check(round(float(answer), 3))
        answer = str(variable) + " = " +str(answer)

    return problem, answer
