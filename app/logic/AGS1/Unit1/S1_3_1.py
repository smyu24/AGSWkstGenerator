#1.3.1 Reading The Table
# absolute path of the parent directory to the sys.path

import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from loader import signify, tableGenerator
import random

#section 1
def Reading_The_Table(difficulty=1, expr='latex'):
    header = [r'$n$'] + signify(list(range(1,11)))
    outputs =  [r'f(n)']

    if difficulty == 1: # easy
        outputs += random.sample(list(range(-10,31)), 10)
    elif difficulty == 2: # medium
        outputs += random.sample(list(range(-30,51)), 10)
    elif difficulty == 3: # hard
        outputs += random.sample(list(range(-100,301)), 10)

    problem = tableGenerator(header, [signify(outputs)])

    if difficulty == 1: # easy
        choices = random.sample(list(range(1,11)), 2)           # random inputs
        choices += random.sample(outputs[1:], 2)                # random outputs
        solutions = [outputs[choices[0]], outputs[choices[1]]]
        solutions += [outputs.index(choices[2]), outputs.index(choices[3])]

        parta = fr'(a) Find $f({choices[0]})$. \newline '
        partb = fr'(b) Find $f({choices[1]})$. \newline '
        partc = fr'(c) Find $n$ such that $f(n) = {choices[2]}$. \newline '
        partd = fr'(d) Find $n$ such that $f(n) = {choices[3]}$. \newline '
        answer = fr'(a) $f({choices[0]}) = {solutions[0]}$ \newline '
        answer += fr'(b) $f({choices[1]}) = {solutions[1]}$ \newline '
        answer += fr'(c) $n = {solutions[2]}$. \newline (d) $n = {solutions[3]}$. \newline '
    elif difficulty >= 2: # medium and hard
        choices = random.sample(outputs[2:-1], 2)               # random outputs
        solutions = [outputs.index(choices[0]), outputs.index(choices[1])]
        if difficulty == 2:
            shifts = [1,1]
        elif difficulty == 3:    # random shifts
            shifts = [random.randint(1,solutions[0]-1), random.randint(1,10-solutions[1])]
        solutions.insert(1,outputs[solutions[0]-shifts[0]])      # put solutions in same order as problem
        solutions.append(outputs[solutions[2]+shifts[1]])

        parta = fr'(a) When $f(n) = {choices[0]}$, what is the value of $n$? \newline '
        partb = fr'(b) What is the value of $f(n-{shifts[0]})$? \newline '
        partc = fr'(c) When $f(n) = {choices[1]}$, what is the value of $n$? \newline '
        partd = fr'(d) What is the value of $f(n+{shifts[1]})$? \newline '
        answer = fr'(a) $n = {solutions[0]}$ \newline '
        answer += fr'(b) $f(n-{shifts[0]}) = f({solutions[0]}-{shifts[0]}) = f({solutions[0]-shifts[0]}) = {solutions[1]}$ \newline '
        answer += fr'(c) $n = {solutions[2]}$ \newline '
        answer += fr'(d) $f(n+{shifts[1]}) = f({solutions[2]}+{shifts[1]}) = f({solutions[2]+shifts[1]}) = {solutions[3]}$ \newline'
    
    problem += parta + partb + partc + partd

    return problem, answer
  

for i in range(4):
    problem, answer = Reading_The_Table(3)
    print(problem)
    print(answer)
    print(r'ss')