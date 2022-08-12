# First Section

import math
import random
import sympy

def addition_type(range_max, variable_one, variable_two):
    variable_one, variable_two = str(variable_one), str(variable_two)
    end_addition = [' plus ',' added with ',' increased by ', ' added to ']
    front_addition = ['The sum of ', 'The total of ']
    a = random.randint(1, range_max)
    printable_a = a
    b = random.randint(1, range_max)
    printable_b = b
    if a == 1:
        a = ''
        printable_a = a
    if b == 1:
        b = ''
        printable_b = b

    if random.randint(1,2) == 1:
        start = end_addition[random.randint(0,len(end_addition) - 1)]
        problem = "$" + str(printable_a) + str(variable_one) + "$" + start + "$" + str(printable_b) + str(variable_two) + "$"
        solution = fr"{a}{variable_one} + {b}{variable_two}"
        return problem, solution
  
    else:
        start = front_addition[random.randint(0,len(front_addition) - 1)]
        problem = start + "$" + str(printable_a) + str(variable_one) + "$" + ' and ' + "$" + str(printable_b) + str(variable_two) + "$"
        solution = fr"{a}{variable_one} + {b}{variable_two}"
        return problem,solution


def subtraction_type(range_max, variable_one, variable_two):
    variable_one, variable_two = str(variable_one), str(variable_two)
    end_subtraction = [' subtracted by ',' less than ',' less ', ' decreased by ' ,' subtracted from ']
    front_subtraction = ['The difference of ', 'The difference between ']

    a = random.randint(1, range_max)
    printable_a = a
    b = random.randint(1, range_max)
    printable_b = b
    if a == 1:
        a = ''
        printable_a = a
    if b == 1:
        b = ''
        printable_b = b

    if random.randint(1,2) == 1:
        start = end_subtraction[random.randint(0,len(end_subtraction) - 1)]
        problem = "$" + str(printable_a) + str(variable_one) + "$" + start + "$" + str(printable_b) + str(variable_two) + "$"
        solution = fr"{a}{variable_one} - {b}{variable_two}"
        return problem, solution
  
    else:
        start = front_subtraction[random.randint(0,len(front_subtraction) - 1)]
        problem = start + "$" + str(printable_a) + str(variable_one) + "$" + ' and ' + "$" + str(printable_b) + str(variable_two) + "$"
        solution = fr"{a}{variable_one} - {b}{variable_two}"
        return problem,solution


def multiplication_type(range_max, variable_one, variable_two):
    variable_one, variable_two = str(variable_one), str(variable_two)
    end_multiplication = [' times ' , ' times by ', ' multiplied by ']
    front_multiplication = ['The product of ']

    a = random.randint(1, range_max)
    printable_a = a
    b = random.randint(1, range_max)
    printable_b = b
    if a == 1:
        a = ''
        printable_a = a
    if b == 1:
        b = ''
        printable_b = b

    if random.randint(1,2) == 1:
        start = end_multiplication[random.randint(0,len(end_multiplication) - 1)]
        problem = "$" + str(printable_a) + variable_one + "$" + start + "$" + str(printable_b) + variable_two + "$"
        solution = fr"{a}{variable_one} \cdot {b}{variable_two}"
        return problem, solution
  
    else:
        start = front_multiplication[random.randint(0,len(front_multiplication) - 1)]
        problem = start + "$" + str(printable_a) + variable_one + "$" + ' and ' + "$" + str(printable_b) + variable_two + "$"
        solution = fr"{a}{variable_one} \cdot {b}{variable_two}"
        return problem, solution


def division_type(range_max, variable_one, variable_two):
    variable_one, variable_two = str(variable_one), str(variable_two)
    end_division = [' divided by '] 
    front_division = ['The ratio of ','The quotient of ']

    a = random.randint(1, range_max)
    printable_a = a
    b = random.randint(1, range_max)
    printable_b = b
    if a == 1:
        a = ''
        printable_a = a
    if b == 1:
        b = ''
        printable_b = b

    a=str(a)
    b=str(b)
    if random.randint(1,2) == 1:
        start = end_division[random.randint(0,len(end_division) - 1)]
        problem = "$" + str(printable_a) + variable_one + "$" + start + "$" + str(printable_b) + variable_two + "$"
        solution = r"\frac~{a}{b}`~{c}{d}`".format(a=a, b=variable_one, c=b, d=variable_two)
        solution = solution.replace("~","{",2)
        solution = solution.replace("`","}",2)
        return problem, solution
  
    else:
        start = front_division[random.randint(0,len(front_division) - 1)]
        problem = start + "$" + str(printable_a) + variable_one + "$" + ' and ' + "$" + str(printable_b) + variable_two + "$"
        solution = r"\frac~{a}{b}`~{c}{d}`".format(a=a, b=variable_one, c=b, d=variable_two)
        solution = solution.replace("~","{",2)
        solution = solution.replace("`","}",2)
        return problem,solution


def alge_easy(range_max, case):
    variable_set_first = ['Z','Y','X']
    variable_set_last = ['x', 'y','z']
    if case == 1:
        problem, solution = addition_type(range_max, random.choice(random.choice([variable_set_first, variable_set_last])), random.choice(random.choice([variable_set_first, variable_set_last])))
    elif case == 2:
        problem, solution = subtraction_type(range_max, random.choice(random.choice([variable_set_first, variable_set_last])), random.choice(random.choice([variable_set_first, variable_set_last])))
    elif case == 3:
        problem, solution = multiplication_type(range_max, random.choice(random.choice([variable_set_first, variable_set_last])), random.choice(random.choice([variable_set_first, variable_set_last])))
    elif case == 4:
        problem, solution = division_type(range_max, random.choice(random.choice([variable_set_first, variable_set_last])), random.choice(random.choice([variable_set_first, variable_set_last])))
    return problem, solution


def alge_medium(range_max, case):
    variable_set_first = ['Z','Y','X']
    variable_set_last = ['x', 'y','z']
    if case == 1:
        if random.randint(1,2) == 1:
            problem, solution = addition_type(range_max, random.randint(1,range_max - 1), random.randint(1,range_max - 1))
        else:
            problem, solution = addition_type(range_max, random.choice(random.choice([variable_set_first, variable_set_last])), random.randint(1,range_max - 1))
    elif case == 2: 
        if random.randint(1,2) == 1:
            problem, solution = subtraction_type(range_max, random.randint(1,range_max - 1), random.randint(1,range_max - 1))
        else:
            problem, solution = subtraction_type(range_max, random.choice(random.choice([variable_set_first, variable_set_last])), random.randint(1,range_max - 1))
    elif case == 3:
        if random.randint(1,2) == 1:
            problem, solution = multiplication_type(range_max, random.randint(1,range_max - 1), random.randint(1,range_max - 1))
        else:
            problem, solution = multiplication_type(range_max, random.choice(random.choice([variable_set_first, variable_set_last])), random.randint(1,range_max - 1))
    elif case == 4: 
        if random.randint(1,2) == 1:
            problem, solution = division_type(range_max, random.randint(1,range_max - 1), random.randint(1,range_max - 1))
        else:
            problem, solution = division_type(range_max, random.choice(random.choice([variable_set_first, variable_set_last])), random.randint(1,range_max - 1))
    return problem, solution
  

def word(range_max, one):
    sent = ""
    sent_2 = ""
    ender = ["Half of ", "One-third of ", "One-fourth of ", "One-fifth of "]
    index = random.randint(0, len(ender) - 1)
    sent = ender[index] + str(one) 
    sent_2 = fr'\frac~{one}`~{index + 2}`'
    sent_2 = sent_2.replace("~", "{")
    sent_2 = sent_2.replace("`", "}")
    return(sent, sent_2)

def powers(range_max, one):
    sent = ""
    sent_2 = ""
    ender = [" squared", " cubed", " to the fourth power", " to the fifth power"]
    index = random.randint(0, len(ender) - 1)
    sent = str(one) + ender[index]
    sent_2 = str(one) + " ^ "
    if index == 0:
        sent_2 = sent_2  + "2"
    elif index == 1:
        sent_2 = sent_2  + "3"
    elif index == 2:
        sent_2 = sent_2  + "4"
    elif index == 3:
        sent_2 = sent_2  + "5"
    return(sent, sent_2)

def alge_hard(range_max, case):
    variable_set_first = ['Z','Y','X']
    variable_set_last = ['x', 'y','z']
    problem = ""
    solution = ""
    if case == 1:
        if random.randint(1,2) == 1:
            problem, solution = powers(range_max, random.choice(random.choice([variable_set_first, variable_set_last])))
        else:
            problem, solution = powers(range_max, random.randint(1, range_max - 1))
    elif case == 2:
        if random.randint(1,2) == 1:
            problem, solution = word(range_max, random.choice(random.choice([variable_set_first, variable_set_last])))
        else:
            problem, solution = word(range_max, random.randint(1, range_max - 1))
    return(problem, solution)


def VariablesAndVerbalExpression(choice = 1, option_difficulty='easy', style='latex', range_max=10, localmin = 0, localmax = 10):
    problem = ""
    solution = ""
    case = 0
    if option_difficulty == 1: # Write each as an algebraic expression. || Write each as a verbal expression. || Evaluate each expression.
        if choice == 1: # Write each as an algebraic expression.
            case = random.randint(1,4)
            problem, solution=alge_easy(range_max, case)
            return problem, solution

        elif choice == 2: # Write each as a verbal expression.
            case = random.randint(1,4)
            solution, problem=alge_easy(range_max, case)
            return problem,solution 
      
        elif choice == 3: # Evaluate each expression.
            case = random.randint(1,4)
            problem, solution=alge_easy(range_max, case)
            return problem, solution

    elif option_difficulty == 2:
        if choice == 1: # Write each as an algebraic expression.
            case = random.randint(1,4)
            problem, solution=alge_medium(range_max, case)
            return problem, solution

        elif choice == 2: # Write each as a verbal expression.
            case = random.randint(1,4)
            solution, problem=alge_medium(range_max, case)
            return problem,solution 
      
        elif choice == 3: # Evaluate each expression.
            case = random.randint(1,4)
            problem, solution=alge_medium(range_max, case)
            return problem, solution

# EVAL NEEDS WORK SOLVING
    elif option_difficulty == 3: # n cubed || 6 squared || half of 14 || one third of a number
        if choice == 1: # Write each as an algebraic expression.
            case = random.randint(1,2)
            problem, solution=alge_hard(range_max, case)

        elif choice == 2: # Write each as a verbal expression.
            case = random.randint(1,2)
            problem, solution=alge_hard(range_max, case)

        elif choice == 3: # Evaluate each expression.
            case = random.randint(1,2)
            problem, solution=alge_hard(range_max, case)
        return problem, solution