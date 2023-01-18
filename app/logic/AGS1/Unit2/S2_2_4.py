import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

# AGS 2.2.4 - Find the recursive and explicit equations
# instruction : Find the recursive and explicit equationsfor the sequences in the tables.

from tabulate import tabulate
from texttable import Texttable

import latextable
import sympy
import random


def table_selector(rows):
    table = Texttable()
    table.set_cols_align(["c"] * 2)
    table.set_deco(Texttable.HEADER | Texttable.VLINES)
    table.add_rows(rows)
    return(latextable.draw_latex(table))

def arith_problem_terms_gen(start, ratio, interateby):
    indexes = []
    terms = []
    terms.append(str(start))
    indexes.append(str(random.randint(-10, 10)))
    for i in range(random.randint(3,6)):
        terms.append(str(int(terms[-1]) + int(ratio)))
        indexes.append(str(int(indexes[-1]) + int(interateby)))
    return indexes, terms

def explicit_function_formatter(ratio, variable, start, notation):
    return str(sympy.latex(sympy.sympify(fr'{notation} * ({variable} - 1) + {ratio}', evaluate = False), fold_short_frac=False))  + fr", {notation}(1) = {start}"


def recursive_function_formatter(start, variable, ratio, notation):
    return sympy.latex(sympy.sympify(fr'{start} + ({variable} - 1) * {ratio}', evaluate = False), fold_short_frac=False)

def dollar_signify(input):
    return(f"${input}$")

def explicit_function_formatter_g(ratio, variable, start, notation):
    return sympy.latex(sympy.sympify(fr'{start} * ({ratio}) ** ({variable} - 1)', evaluate = False), fold_short_frac=False)


def recursive_function_formatter_g(start, variable, ratio, notation):
    return sympy.latex(sympy.sympify(fr'{notation} *({variable}) * {ratio}', evaluate = False), fold_short_frac=False) + fr", {notation}(1) = {start}" # KEEPS DELETING THE PARATHESIS
    #f(x) = f(x-1) * R

def geo_problem_terms_gen(start, ratio, interateby):
    indexes = []
    terms = []
    terms.append(str(start))
    indexes.append(str(random.randint(-10, 10)))
    for i in range(random.randint(3,6)):
        terms.append(str(int(terms[-1]) * int(ratio)))
        indexes.append(str(int(indexes[-1]) + int(interateby)))
    return indexes, terms
    
def Find_The_Recursive_And_Explicit_Equations(expr="latex"):
  variable = random.choice(['x', 'y', 'a', 'b', 'z', 'p', 't'])
  notation = random.choice(['L', 'K', 'U', 'R', 'D', 'W', 'G', 'H', 'V'])
  function_start = notation + "(" + variable + ")"
  problem = ""
  answer = ""

  x_layer = ""
  y_layer = ""
  term = 1
  start = random.randint(-10, 10)

  if random.randint(1,2) == 1:
    ratio = random.randint(-20, -1)
  else:
    ratio = random.randint(1, 20)
  
  if random.randint(1,2) == 1:
    x_layer, y_layer = arith_problem_terms_gen(str(start), str(ratio), term)
    answer = "Recursive Function: " + dollar_signify(function_start + " = "+ explicit_function_formatter(start, variable, ratio, notation)), "Explicit Function: " + dollar_signify(function_start + " = " + recursive_function_formatter(start, variable, ratio, notation))
  else:
    x_layer, y_layer = geo_problem_terms_gen(str(start), str(ratio), term)
    answer = "Recursive Function: " + dollar_signify(function_start + " = "+ explicit_function_formatter_g(start, variable, ratio, notation)), "Explicit Function: " + dollar_signify(function_start + " = " + recursive_function_formatter_g(start, variable, ratio, notation))
 
  rows = []
  for i in range(len(x_layer)):
    rows.append([])
    rows[i].append(dollar_signify(x_layer[i]))
    rows[i].append(dollar_signify(y_layer[i]))
  rows.insert(len(rows), [dollar_signify("..."), dollar_signify("...")])
  rows.insert(0, [dollar_signify(str(variable)), dollar_signify(str(function_start))])
  problem = table_selector(rows)

  problem = problem.replace("\\begin{table}","")
  problem = problem.replace("\\end{table}","")
  return problem, r'\\'.join(answer)
