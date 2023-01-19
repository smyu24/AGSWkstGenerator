from .section1.pre1a1a1 import Decimal_Places
from .section1.pre1a1a2 import readingandwritingrequest
from .section1.pre1a1a31 import Rounding_Number_Section_1
from .section1.pre1a1a32 import Rounding_Number_Section_2
from .section1.pre1a1a33 import Rounding_Number_Section_3

from .section2.pre1a2a11 import Divisibility_And_Factors_Section_1
from .section2.pre1a2a12 import Divisibility_And_Factors_Section_2
from .section2.pre1a2a2 import Factoring_Num_Section_1, Factoring_Num
from .section2.pre1a2a31 import Factoring_Monomials_Section_1, Factoring_Monomials_Section_2
from .section2.pre1a2a32 import Greatest_Common_Factor_Section_1, Greatest_Common_Factor_Section_2
from .section2.pre1a2a4 import  Least_Common_Multiple

from .section3.pre1a3a1 import Fractions_And_Decimals_Conversion
from .section3.pre1a3a2 import Percents_Fractions_Decimal_Conversion_1, Percents_Fractions_Decimal_Conversion_2, Percents_Fractions_Decimal_Conversion_3, Percents_Fractions_Decimal_Conversion_4
from .section3.pre1a3a3 import VariablesAndVerbalExpression
from .section3.pre1a3a4 import Adding_And_Subtracting_Integers_1, Adding_And_Subtracting_Integers_2
from .section3.pre1a3a5 import Adding_And_Subtracting_Decimals_1, Adding_And_Subtracting_Decimals_2
from .section3.pre1a3a6 import Adding_And_Subtracting_Fractions_And_Mixed_Numbers_1, Adding_And_Subtracting_Fractions_And_Mixed_Numbers_2
from .section3.pre1a3a7 import Dividing_Integers_1, Dividing_Integers_2
from .section3.pre1a3a8 import Multiplying_Integers_1, Multiplying_Integers_2
from .section3.pre1a3a9 import Multiplying_Decimals_1, Multiplying_Decimals_2
from .section3.pre1a3a10 import Multiplying_And_Dividing_Fractions_And_Mixed_Numbers_1, Multiplying_And_Dividing_Fractions_And_Mixed_Numbers_2
from .section3.pre1a3a11 import Order_Of_Operations_1

from .section4.pre1a4a1 import Evaluating_Variable_Expressions_1
from .section4.pre1a4a2 import Simplifying_Variable_Expressions_1
from .section4.pre1a4a3 import Distributive_Property_1

from .section5.pre1a5a1 import One_step_Equations_With_Integers_1
from .section5.pre1a5a2 import One_step_Equations_With_Decimals_1
from .section5.pre1a5a3 import One_step_Equations_With_Fractions_1
from .section5.pre1a5a4 import One_step_Word_Problems_1
from .section5.pre1a5a5 import Two_step_Equations_With_Integers_1
from .section5.pre1a5a6 import Two_step_Equations_With_Decimals_1
from .section5.pre1a5a7 import Solving_Multi_Step_Inequalities

from .section6.pre1a6a1 import Graphing_One_Variable_Inequalities_1
from .section6.pre1a6a2 import Solving_One_Step_Inequalities_Adding_Subtracting
from .section6.pre1a6a3 import Solving_One_Step_Inequalities_Multiplication_Division
from .section6.pre1a6a4 import Solving_Two_Step_Inequalities

from .section7.pre1a7a1 import exponent_problem_generator
from .section7.pre1a7a2 import Exponent_Division
from .section7.pre1a7a3 import Powers_Of_Products
from .section7.pre1a7a4 import Scientific_Notation_Section_1, Scientific_Notation_Section_2, Scientific_Notation_Section_3, Scientific_Notation_Section_4
from .section7.pre1a7a5 import Square_Roots_Section_1

from .section8.pre1a8a1 import Fractions_Decimals_and_Percents_Section_1, Percents_Fractions_Decimal_Conversion_22, Percents_Fractions_Decimal_Conversion_33, Percents_Fractions_Decimal_Conversion_44
from .section8.pre1a8a3 import Finding_Percent_Change_Section_1, Finding_Percent_Change_Section_2
from .section8.pre1a8a4 import Markup_Discount_and_Tax
from .section8.pre1a8a5 import Proportions_Section_1, Proportions_Section_2
from .section8.pre1a8a6 import Simple_And_Compound_Interest_Section_1, Simple_And_Compound_Interest_Section_2

from.section9.pre1a9a1 import Find_The_Slope_Section_1, Find_The_Slope_Section_2, Find_The_Slope_Section_3
from.section9.pre1a9a2 import Graphing_Lines_Slope_Intersect


import math
import random

def LatexCreation(problem, answer):
  masterSeed = "\\task $" + str(problem) + "$ \\vspace{2cm}"
  temp_answer = "{\\color{red}" + answer + "}"
  ANSmasterSeed = "\\task $" + str(problem) + "\\\\" + temp_answer + "$ \\vspace{2cm}"
  newpageanswer = "\\task $" + temp_answer + "$ \\vspace{2cm}"

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
Pre Algebra Section 1-1
'''
def Naming_Decimal_Places(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
  masterSeed = []
  ANSmasterSeed = []
  newpageanswer = []
  tmasterSeed = ""
  tANSmasterSeed = ""


  for total in range(len(twoDarr)):
    midMasterSeed = ""
    midANSmasterSeed = ""
    midnewanswer = ""

    for i in range(twoDarr[total][2]):
      problem, answer = Decimal_Places(twoDarr[total][1], "latex", twoDarr[total][0], int(twoDarr[total][3]), int(twoDarr[total][4]))
      tmasterSeed, tANSmasterSeed, tnewpageanswer = LatexCreation(problem, answer)
      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
Pre Algebra Section 1-2
'''
def readingandwriting(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
  masterSeed = []
  ANSmasterSeed = []
  newpageanswer = []
  tmasterSeed = ""
  tANSmasterSeed = ""


  for total in range(len(twoDarr)):
    midMasterSeed = ""
    midANSmasterSeed = ""
    midnewanswer = ""
    for i in range(twoDarr[total][2]):
      problem, answer = readingandwritingrequest(twoDarr[total][1], "latex", int(twoDarr[total][3]), int(twoDarr[total][4]))

      if(twoDarr[total][0] == '1-1-2-1'):
        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + answer + "}"
        tANSmasterSeed = "\\task " + str(problem) + "\\\\" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"
      else:
        tmasterSeed = "\\task " + str(answer) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + problem + "}"
        tANSmasterSeed = "\\task " + str(answer) + "\\\\" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"

      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
Pre Algebra Section 1-3
'''
def rounding(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
  masterSeed = []
  ANSmasterSeed = []
  newpageanswer = []
  tmasterSeed = ""
  tANSmasterSeed = ""


  for total in range(len(twoDarr)):
    midMasterSeed = ""
    midANSmasterSeed = ""
    midnewanswer = ""
    for i in range(twoDarr[total][2]):
      if(twoDarr[total][0] == '1-1-3-1'):
        problem, answer = Rounding_Number_Section_1(twoDarr[total][1], "latex", int(twoDarr[total][3]), int(twoDarr[total][4]))
        tmasterSeed, tANSmasterSeed, tnewpageanswer = LatexCreation(problem, answer)
      elif(twoDarr[total][0] == '1-1-3-2'):
        problem, answer = Rounding_Number_Section_2(twoDarr[total][1], "latex", int(twoDarr[total][3]), int(twoDarr[total][4]))

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + answer + "}"
        tANSmasterSeed = "\\task " + str(problem) + "\\\\$" + temp_answer + "$ \\vspace{2cm}"
        tnewpageanswer = "\\task $" + temp_answer + "$ \\vspace{2cm}"
      elif(twoDarr[total][0] == '1-1-3-3'):
        problem, answer = Rounding_Number_Section_3(twoDarr[total][1], "latex", int(twoDarr[total][3]), int(twoDarr[total][4]))
        tmasterSeed, tANSmasterSeed, tnewpageanswer = LatexCreation(problem, answer)

      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
Pre Algebra Section 2-1
'''
def divandfac(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
  masterSeed = []
  ANSmasterSeed = []
  newpageanswer = []
  tmasterSeed = ""
  tANSmasterSeed = ""


  for total in range(len(twoDarr)):
    midMasterSeed = ""
    midANSmasterSeed = ""
    midnewanswer = ""
    for i in range(twoDarr[total][2]):
      if(twoDarr[total][0] == '1-2-1-1'):
        problem, answer = Divisibility_And_Factors_Section_1(twoDarr[total][1], "latex", int(twoDarr[total][3]), int(twoDarr[total][4]))
        tmasterSeed, tANSmasterSeed, tnewpageanswer = LatexCreation(problem, answer)
      elif(twoDarr[total][0] == '1-2-1-2'):
        preset,  problem, answer = Divisibility_And_Factors_Section_2(twoDarr[total][1], "latex", int(twoDarr[total][3]), int(twoDarr[total][4]))
        tmasterSeed =  "\\task "+ "Check out the divisibility by following [" + str(preset) +"] for " + "$" + str(problem) + "$ \\vspace{2cm}"
        temp_answer = "{\\color{red}" + answer + "}"
        tANSmasterSeed = "\\task $" + str(problem) + "\\\\" + temp_answer + "$ \\vspace{2cm}"
        tnewpageanswer = "\\task $" + temp_answer + "$ \\vspace{2cm}"

      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
Pre Algebra Section 2-2
'''
def factoring(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
  masterSeed = []
  ANSmasterSeed = []
  newpageanswer = []
  tmasterSeed = ""
  tANSmasterSeed = ""


  for total in range(len(twoDarr)):
    midMasterSeed = ""
    midANSmasterSeed = ""
    midnewanswer = ""
    for i in range(twoDarr[total][2]):
      if(twoDarr[total][0] == '1-2-2-1'):
        problem, answer = Factoring_Num_Section_1(twoDarr[total][1], "latex", int(twoDarr[total][3]), int(twoDarr[total][4]))
        tmasterSeed = "\\task $" + str(problem) + "$ \\vspace{2cm}"
        temp_answer = "{\\color{red}" + answer + "}"
        tANSmasterSeed = "\\task $" + str(problem) + "$\\\\" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"
      elif(twoDarr[total][0] == '1-2-2-2'):
        problem, answer = Factoring_Num(twoDarr[total][1], "latex", int(twoDarr[total][3]), int(twoDarr[total][4]))
        tmasterSeed, tANSmasterSeed, tnewpageanswer = LatexCreation(problem, answer)

      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
Pre Algebra Section 2-3
'''
def monomials(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
  masterSeed = []
  ANSmasterSeed = []
  newpageanswer = []
  tmasterSeed = ""
  tANSmasterSeed = ""


  for total in range(len(twoDarr)):
    midMasterSeed = ""
    midANSmasterSeed = ""
    midnewanswer = ""
    for i in range(twoDarr[total][2]):
      if(twoDarr[total][0] == '1-2-3-1'):
        problem, answer = Factoring_Monomials_Section_1(twoDarr[total][1], "latex", int(twoDarr[total][3]), int(twoDarr[total][4]))
        tmasterSeed, tANSmasterSeed, tnewpageanswer = LatexCreation(problem, answer)
      elif(twoDarr[total][0] == '1-2-3-2'):
        problem, answer = Factoring_Monomials_Section_2(twoDarr[total][1], "latex", int(twoDarr[total][3]), int(twoDarr[total][4]))
        tmasterSeed, tANSmasterSeed, tnewpageanswer = LatexCreation(problem, answer)

      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
Pre Algebra Section 2-4
'''
def common_factors(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
  masterSeed = []
  ANSmasterSeed = []
  newpageanswer = []
  tmasterSeed = ""
  tANSmasterSeed = ""


  for total in range(len(twoDarr)):
    midMasterSeed = ""
    midANSmasterSeed = ""
    midnewanswer = ""
    for i in range(twoDarr[total][2]):
      if(twoDarr[total][0] == '1-2-4-1'):
        problem, answer = Greatest_Common_Factor_Section_1(twoDarr[total][1], "latex", int(twoDarr[total][3]), int(twoDarr[total][4]))
        tmasterSeed, tANSmasterSeed, tnewpageanswer = LatexCreation(problem, answer)
      elif(twoDarr[total][0] == '1-2-4-2'):
        problem, answer = Greatest_Common_Factor_Section_2(twoDarr[total][1], "latex", int(twoDarr[total][3]), int(twoDarr[total][4]))
        tmasterSeed, tANSmasterSeed, tnewpageanswer = LatexCreation(problem, answer)

      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
Pre Algebra Section 2-5
'''
def Leastcommon_factors(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
  masterSeed = []
  ANSmasterSeed = []
  newpageanswer = []
  tmasterSeed = ""
  tANSmasterSeed = ""


  for total in range(len(twoDarr)):
    midMasterSeed = ""
    midANSmasterSeed = ""
    midnewanswer = ""
    for i in range(twoDarr[total][2]):
      if(twoDarr[total][0] == '1-2-5-1'):
        problem, answer = Least_Common_Multiple(twoDarr[total][1], "latex", int(twoDarr[total][3]), int(twoDarr[total][4]))
        tmasterSeed, tANSmasterSeed, tnewpageanswer = LatexCreation(problem, answer)

      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
Pre Algebra Section 3-1
'''
def ConvertingFractionsandDecimals(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
  masterSeed = []
  ANSmasterSeed = []
  newpageanswer = []
  tmasterSeed = ""
  tANSmasterSeed = ""


  for total in range(len(twoDarr)):
    midMasterSeed = ""
    midANSmasterSeed = ""
    midnewanswer = ""
    for i in range(twoDarr[total][2]):
      if(twoDarr[total][0] == '1-3-1-1'):
        problem, answer = Fractions_And_Decimals_Conversion(twoDarr[total][1], "latex", int(twoDarr[total][3]), int(twoDarr[total][4]))
        tmasterSeed = "\\task $" + str(problem) + "$ \\vspace{2cm}"
        temp_answer = "{\\color{red}" + answer + "}"
        tANSmasterSeed = "\\task $" + str(problem) + "$\\\\" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"
      elif(twoDarr[total][0] == '1-3-1-2'):
        problem, answer = Fractions_And_Decimals_Conversion(twoDarr[total][1], "latex", int(twoDarr[total][3]), int(twoDarr[total][4]))
        tmasterSeed = "\\task $" + str(answer) + "$ \\vspace{2cm}"
        temp_answer = "{\\color{red}" + problem + "}"
        tANSmasterSeed = "\\task $" + str(answer) + "$\\\\" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"

      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
Pre Algebra Section 3-2
'''
def Convertingbetweenpercents(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
  masterSeed = []
  ANSmasterSeed = []
  newpageanswer = []
  tmasterSeed = ""
  tANSmasterSeed = ""


  for total in range(len(twoDarr)):
    midMasterSeed = ""
    midANSmasterSeed = ""
    midnewanswer = ""
    for i in range(twoDarr[total][2]):
      if(twoDarr[total][0] == '1-3-2-1'):
        problem, answer = Percents_Fractions_Decimal_Conversion_1(twoDarr[total][1], "latex", int(twoDarr[total][3]), int(twoDarr[total][4]))
        tmasterSeed = "\\task $ " + str(problem)[2:-2] + "\\% $ \\vspace{2cm}"
        temp_answer = "{\\color{red}" + answer[2:-2] + "}"
        tANSmasterSeed = "\\task $ " + str(problem)[2:-2] + "\\% \\\\" + temp_answer + "$ \\vspace{2cm}"
        tnewpageanswer = "\\task $" + temp_answer + "$ \\vspace{2cm}"

      elif(twoDarr[total][0] == '1-3-2-2'):
        problem, answer = Percents_Fractions_Decimal_Conversion_2(twoDarr[total][1], "latex", int(twoDarr[total][3]), int(twoDarr[total][4]))
        tmasterSeed = "\\task " + str(problem)[2:-2] + "\\% \\vspace{2cm}"
        temp_answer = "{\\color{red}" + answer[2:-2] + "\\%}"
        tANSmasterSeed = "\\task $ " + str(problem)[2:-2] + "\\% \\\\" + temp_answer + "$ \\vspace{2cm}"
        tnewpageanswer = "\\task $" + temp_answer + "$ \\vspace{2cm}"

      elif(twoDarr[total][0] == '1-3-2-3'):
        problem, answer = Percents_Fractions_Decimal_Conversion_3(twoDarr[total][1], "latex", int(twoDarr[total][3]), int(twoDarr[total][4]))
        tmasterSeed = "\\task $ " + str(problem)[2:-2] + "\\% $ \\vspace{2cm}"
        temp_answer = "{\\color{red}" + answer[2:-2] + "}"
        tANSmasterSeed = "\\task $ " + str(problem)[2:-2] + "\\% \\\\" + temp_answer + "$ \\vspace{2cm}"
        tnewpageanswer = "\\task $" + temp_answer + "$ \\vspace{2cm}"

      elif(twoDarr[total][0] == '1-3-2-4'):
        answer, problem = Percents_Fractions_Decimal_Conversion_4(twoDarr[total][1], "latex", int(twoDarr[total][3]), int(twoDarr[total][4]))
        tmasterSeed = "\\task $ " + str(answer) + "$ \\vspace{2cm}"
        temp_answer = "{\\color{red}" + problem[2:-2] + "}"
        tANSmasterSeed = "\\task $ " + str(answer) + " \\\\" + temp_answer + "$ {\\color{red} \\%}  \\vspace{2cm}"
        tnewpageanswer = "\\task $" + temp_answer + "$ \\vspace{2cm}"

      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
Pre Algebra Section 3-3
'''
def setfor33(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
  masterSeed = []
  ANSmasterSeed = []
  newpageanswer = []
  tmasterSeed = ""
  tANSmasterSeed = ""


  for total in range(len(twoDarr)):
    midMasterSeed = ""
    midANSmasterSeed = ""
    midnewanswer = ""
    for i in range(twoDarr[total][2]):
      if(twoDarr[total][0] == '1-3-3-1'):
        problem, answer = VariablesAndVerbalExpression(1, twoDarr[total][1], "latex", 10, int(twoDarr[total][3]), int(twoDarr[total][4]))
        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red} $" + answer + "$ }"
        tANSmasterSeed = "\\task " + str(problem) + "\\\\" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"
      elif(twoDarr[total][0] == '1-3-3-2'):
        answer, problem = VariablesAndVerbalExpression(2, twoDarr[total][1], "latex", 10, int(twoDarr[total][3]), int(twoDarr[total][4]))
        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red} $" + answer + "$ }"
        tANSmasterSeed = "\\task " + str(problem) + "\\\\" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"
      elif(twoDarr[total][0] == '1-3-3-3'):
        problem, answer = VariablesAndVerbalExpression(3, twoDarr[total][1], "latex", 10, int(twoDarr[total][3]), int(twoDarr[total][4]))
        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red} $" + answer + "$ }"
        tANSmasterSeed = "\\task " + str(problem) + "\\\\" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"

      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
Pre Algebra Section 3-4
'''
def Addingandsubtracting(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
  masterSeed = []
  ANSmasterSeed = []
  newpageanswer = []
  tmasterSeed = ""
  tANSmasterSeed = ""


  for total in range(len(twoDarr)):
    midMasterSeed = ""
    midANSmasterSeed = ""
    midnewanswer = ""
    for i in range(twoDarr[total][2]):
      if(twoDarr[total][0] == '1-3-4-1'):
        problem, answer = Adding_And_Subtracting_Integers_1(twoDarr[total][1], "latex", int(twoDarr[total][3]), int(twoDarr[total][4]))
        tmasterSeed, tANSmasterSeed, tnewpageanswer = LatexCreation(str(problem)[2:-2], str(answer)[1:-1])
      elif(twoDarr[total][0] == '1-3-4-2'):
        problem, answer = Adding_And_Subtracting_Integers_2(twoDarr[total][1], "latex", int(twoDarr[total][3]), int(twoDarr[total][4]))
        tmasterSeed, tANSmasterSeed, tnewpageanswer = LatexCreation(str(problem)[2:-2], str(answer)[1:-1])

      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
Pre Algebra Section 3-5
'''
def Addinganddecimals(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
  masterSeed = []
  ANSmasterSeed = []
  newpageanswer = []
  tmasterSeed = ""
  tANSmasterSeed = ""


  for total in range(len(twoDarr)):
    midMasterSeed = ""
    midANSmasterSeed = ""
    midnewanswer = ""
    for i in range(twoDarr[total][2]):
      if(twoDarr[total][0] == '1-3-5-1'):
        problem, answer = Adding_And_Subtracting_Decimals_1(twoDarr[total][1], "latex", int(twoDarr[total][3]), int(twoDarr[total][4]))
        tmasterSeed, tANSmasterSeed, tnewpageanswer = LatexCreation(str(problem)[2:-2], str(answer)[1:-1])
      elif(twoDarr[total][0] == '1-3-5-2'):
        problem, answer = Adding_And_Subtracting_Decimals_2(twoDarr[total][1], "latex", int(twoDarr[total][3]), int(twoDarr[total][4]))
        tmasterSeed, tANSmasterSeed, tnewpageanswer = LatexCreation(str(problem)[2:-2], str(answer)[1:-1])

      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
Pre Algebra Section 3-6
'''
def fractionsandmixed(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
  masterSeed = []
  ANSmasterSeed = []
  newpageanswer = []
  tmasterSeed = ""
  tANSmasterSeed = ""


  for total in range(len(twoDarr)):
    midMasterSeed = ""
    midANSmasterSeed = ""
    midnewanswer = ""
    for i in range(twoDarr[total][2]):
      if(twoDarr[total][0] == '1-3-6-1'):
        problem, answer = Adding_And_Subtracting_Fractions_And_Mixed_Numbers_1(twoDarr[total][1], "latex", int(twoDarr[total][3]), int(twoDarr[total][4]))
        tmasterSeed, tANSmasterSeed, tnewpageanswer = LatexCreation(str(problem), str(answer))
      elif(twoDarr[total][0] == '1-3-6-2'):
        problem, answer = Adding_And_Subtracting_Fractions_And_Mixed_Numbers_2(twoDarr[total][1], "latex", int(twoDarr[total][3]), int(twoDarr[total][4]))
        tmasterSeed, tANSmasterSeed, tnewpageanswer = LatexCreation(str(problem), str(answer))

      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
Pre Algebra Section 3-7
'''
def Dividingintegers(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
  masterSeed = []
  ANSmasterSeed = []
  newpageanswer = []
  tmasterSeed = ""
  tANSmasterSeed = ""


  for total in range(len(twoDarr)):
    midMasterSeed = ""
    midANSmasterSeed = ""
    midnewanswer = ""
    for i in range(twoDarr[total][2]):
      if(twoDarr[total][0] == '1-3-7-1'):
        problem, answer = Dividing_Integers_1(twoDarr[total][1], "latex", int(twoDarr[total][3]), int(twoDarr[total][4]))
        tmasterSeed, tANSmasterSeed, tnewpageanswer = LatexCreation(str(problem), str(answer)[1:-1])
      elif(twoDarr[total][0] == '1-3-7-2'):
        problem, answer = Dividing_Integers_2(twoDarr[total][1], "latex", int(twoDarr[total][3]), int(twoDarr[total][4]))
        tmasterSeed, tANSmasterSeed, tnewpageanswer = LatexCreation(str(problem), str(answer)[1:-1])

      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
Pre Algebra Section 3-8
'''
def Multiplyingintegers(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
  masterSeed = []
  ANSmasterSeed = []
  newpageanswer = []
  tmasterSeed = ""
  tANSmasterSeed = ""


  for total in range(len(twoDarr)):
    midMasterSeed = ""
    midANSmasterSeed = ""
    midnewanswer = ""
    for i in range(twoDarr[total][2]):
      if(twoDarr[total][0] == '1-3-8-1'):
        problem, answer = Multiplying_Integers_1(twoDarr[total][1], "latex", int(twoDarr[total][3]), int(twoDarr[total][4]))
        tmasterSeed, tANSmasterSeed, tnewpageanswer = LatexCreation(str(problem)[2:-2], str(answer)[1:-1])
      elif(twoDarr[total][0] == '1-3-8-2'):
        problem, answer = Multiplying_Integers_2(twoDarr[total][1], "latex", int(twoDarr[total][3]), int(twoDarr[total][4]))
        tmasterSeed, tANSmasterSeed, tnewpageanswer = LatexCreation(str(problem)[2:-2], str(answer)[1:-1])

      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
Pre Algebra Section 3-9
'''
def Multiplyingdecimals(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
  masterSeed = []
  ANSmasterSeed = []
  newpageanswer = []
  tmasterSeed = ""
  tANSmasterSeed = ""


  for total in range(len(twoDarr)):
    midMasterSeed = ""
    midANSmasterSeed = ""
    midnewanswer = ""
    for i in range(twoDarr[total][2]):
      if(twoDarr[total][0] == '1-3-9-1'):
        problem, answer = Multiplying_Decimals_1(twoDarr[total][1], "latex", int(twoDarr[total][3]), int(twoDarr[total][4]))
        tmasterSeed, tANSmasterSeed, tnewpageanswer = LatexCreation(str(problem)[2:-2], str(answer)[2:-2])
      elif(twoDarr[total][0] == '1-3-9-2'):
        problem, answer = Multiplying_Decimals_2(twoDarr[total][1], "latex", int(twoDarr[total][3]), int(twoDarr[total][4]))
        tmasterSeed, tANSmasterSeed, tnewpageanswer = LatexCreation(str(problem)[2:-2], str(answer)[2:-2])

      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
Pre Algebra Section 3-10
'''
def multianddivisioncombi(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
  masterSeed = []
  ANSmasterSeed = []
  newpageanswer = []
  tmasterSeed = ""
  tANSmasterSeed = ""


  for total in range(len(twoDarr)):
    midMasterSeed = ""
    midANSmasterSeed = ""
    midnewanswer = ""
    for i in range(twoDarr[total][2]):
      if(twoDarr[total][0] == '1-3-10-1'):
        problem, answer = Multiplying_And_Dividing_Fractions_And_Mixed_Numbers_1(twoDarr[total][1], "latex", int(twoDarr[total][3]), int(twoDarr[total][4]))
        tmasterSeed, tANSmasterSeed, tnewpageanswer = LatexCreation(str(problem), str(answer))
      elif(twoDarr[total][0] == '1-3-10-2'):
        problem, answer = Multiplying_And_Dividing_Fractions_And_Mixed_Numbers_2(twoDarr[total][1], "latex", int(twoDarr[total][3]), int(twoDarr[total][4]))
        tmasterSeed, tANSmasterSeed, tnewpageanswer = LatexCreation(str(problem), str(answer))

      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
Pre Algebra Section 3-11
'''
def Orderofoperations(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
  masterSeed = []
  ANSmasterSeed = []
  newpageanswer = []
  tmasterSeed = ""
  tANSmasterSeed = ""


  for total in range(len(twoDarr)):
    midMasterSeed = ""
    midANSmasterSeed = ""
    midnewanswer = ""
    for i in range(twoDarr[total][2]):
      if(twoDarr[total][0] == '1-3-11-1'):
        problem, answer = Order_Of_Operations_1(twoDarr[total][1], "latex", int(twoDarr[total][3]), int(twoDarr[total][4]))
        tmasterSeed, tANSmasterSeed, tnewpageanswer = LatexCreation(str(problem)[2:-2], str(answer)[1:-1])

      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
Pre Algebra Section 4-1
'''
def thisisfor41(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
  masterSeed = []
  ANSmasterSeed = []
  newpageanswer = []
  tmasterSeed = ""
  tANSmasterSeed = ""


  for total in range(len(twoDarr)):
    midMasterSeed = ""
    midANSmasterSeed = ""
    midnewanswer = ""
    for i in range(twoDarr[total][2]):
      if(twoDarr[total][0] == '1-4-1-1'):
        problem, answer = Evaluating_Variable_Expressions_1(twoDarr[total][1], "latex")
        tmasterSeed = "\\task $" + str(problem) + "$ \\vspace{2cm}"
        temp_answer = "{\\color{red} $" + str(answer) + "$ }"
        tANSmasterSeed = "\\task $" + str(problem) + "$ \\\\" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"

      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
Pre Algebra Section 4-2
'''
def thisisfor42(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
  masterSeed = []
  ANSmasterSeed = []
  newpageanswer = []
  tmasterSeed = ""
  tANSmasterSeed = ""


  for total in range(len(twoDarr)):
    midMasterSeed = ""
    midANSmasterSeed = ""
    midnewanswer = ""
    for i in range(twoDarr[total][2]):
      if(twoDarr[total][0] == '1-4-2-1'):
        problem, answer = Simplifying_Variable_Expressions_1(twoDarr[total][1], 0, int(twoDarr[total][3]), int(twoDarr[total][4]))
        tmasterSeed, tANSmasterSeed, tnewpageanswer = LatexCreation(str(problem), str(answer))

      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
Pre Algebra Section 4-3
'''
def thisisfor43(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
  masterSeed = []
  ANSmasterSeed = []
  newpageanswer = []
  tmasterSeed = ""
  tANSmasterSeed = ""


  for total in range(len(twoDarr)):
    midMasterSeed = ""
    midANSmasterSeed = ""
    midnewanswer = ""
    for i in range(twoDarr[total][2]):
      if(twoDarr[total][0] == '1-4-3-1'):
        problem, answer = Distributive_Property_1(twoDarr[total][1], "latex", int(twoDarr[total][3]), int(twoDarr[total][4]))
        tmasterSeed, tANSmasterSeed, tnewpageanswer = LatexCreation(str(problem), str(answer)[2:-2])

      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
Pre Algebra Section 5-1
'''
def thisisfor51(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
  masterSeed = []
  ANSmasterSeed = []
  newpageanswer = []
  tmasterSeed = ""
  tANSmasterSeed = ""


  for total in range(len(twoDarr)):
    midMasterSeed = ""
    midANSmasterSeed = ""
    midnewanswer = ""
    for i in range(twoDarr[total][2]):
      if(twoDarr[total][0] == '1-5-1-1'):
        problem, answer = One_step_Equations_With_Integers_1(twoDarr[total][1], "latex")
        tmasterSeed, tANSmasterSeed, tnewpageanswer = LatexCreation(str(problem), str(answer)[2:-2])

      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
Pre Algebra Section 5-2
'''
def thisisfor52(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
  masterSeed = []
  ANSmasterSeed = []
  newpageanswer = []
  tmasterSeed = ""
  tANSmasterSeed = ""

  for total in range(len(twoDarr)):
    midMasterSeed = ""
    midANSmasterSeed = ""
    midnewanswer = ""
    for i in range(twoDarr[total][2]):
      if(twoDarr[total][0] == '1-5-2-1'):
        problem, answer = One_step_Equations_With_Decimals_1(twoDarr[total][1], 0)
        tmasterSeed, tANSmasterSeed, tnewpageanswer = LatexCreation(str(problem), str(answer))

      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
Pre Algebra Section 5-3
'''
def thisisfor53(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
  masterSeed = []
  ANSmasterSeed = []
  newpageanswer = []
  tmasterSeed = ""
  tANSmasterSeed = ""


  for total in range(len(twoDarr)):
    midMasterSeed = ""
    midANSmasterSeed = ""
    midnewanswer = ""
    for i in range(twoDarr[total][2]):
      if(twoDarr[total][0] == '1-5-3-1'):
        problem, answer = One_step_Equations_With_Fractions_1(twoDarr[total][1], 0)
        tmasterSeed, tANSmasterSeed, tnewpageanswer = LatexCreation(str(problem), str(answer))

      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
Pre Algebra Section 5-4
'''
def thisisfor54(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
  masterSeed = []
  ANSmasterSeed = []
  newpageanswer = []
  tmasterSeed = ""
  tANSmasterSeed = ""


  for total in range(len(twoDarr)):
    midMasterSeed = ""
    midANSmasterSeed = ""
    midnewanswer = ""
    for i in range(twoDarr[total][2]):
      if(twoDarr[total][0] == '1-5-4-1'):
        problem, answer = One_step_Word_Problems_1(twoDarr[total][1], 0)
        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = "\\task " + str(problem) + "\\\\$" + temp_answer + "$ \\vspace{2cm}"
        tnewpageanswer = "\\task $" + temp_answer + "$ \\vspace{2cm}"

      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
Pre Algebra Section 5-5
'''
def thisisfor55(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
  masterSeed = []
  ANSmasterSeed = []
  newpageanswer = []
  tmasterSeed = ""
  tANSmasterSeed = ""


  for total in range(len(twoDarr)):
    midMasterSeed = ""
    midANSmasterSeed = ""
    midnewanswer = ""
    for i in range(twoDarr[total][2]):
      if(twoDarr[total][0] == '1-5-5-1'):
        problem, answer = Two_step_Equations_With_Integers_1(twoDarr[total][1], 0)
        tmasterSeed, tANSmasterSeed, tnewpageanswer = LatexCreation(str(problem), str(answer)[2:-2])

      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
Pre Algebra Section 5-6
'''
def thisisfor56(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
  masterSeed = []
  ANSmasterSeed = []
  newpageanswer = []
  tmasterSeed = ""
  tANSmasterSeed = ""


  for total in range(len(twoDarr)):
    midMasterSeed = ""
    midANSmasterSeed = ""
    midnewanswer = ""
    for i in range(twoDarr[total][2]):
      if(twoDarr[total][0] == '1-5-6-1'):
        problem, answer = Two_step_Equations_With_Decimals_1(twoDarr[total][1], 0)
        tmasterSeed, tANSmasterSeed, tnewpageanswer = LatexCreation(str(problem), str(answer))

      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
Pre Algebra Section 5-7
'''
def thisisfor57(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
  masterSeed = []
  ANSmasterSeed = []
  newpageanswer = []
  tmasterSeed = ""
  tANSmasterSeed = ""


  for total in range(len(twoDarr)):
    midMasterSeed = ""
    midANSmasterSeed = ""
    midnewanswer = ""
    for i in range(twoDarr[total][2]):
      if(twoDarr[total][0] == '1-5-7-1'):
        problem, answer = Solving_Multi_Step_Inequalities(twoDarr[total][1], 0)
        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = "\\task " + str(problem) + "\\\\$" + temp_answer + "$ \\vspace{2cm}"
        tnewpageanswer = "\\task $" + temp_answer + "$ \\vspace{2cm}"


      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)


'''
Pre Algebra Section 6-1
'''
def thisisfor61(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
  masterSeed = []
  ANSmasterSeed = []
  newpageanswer = []
  tmasterSeed = ""
  tANSmasterSeed = ""


  for total in range(len(twoDarr)):
    midMasterSeed = ""
    midANSmasterSeed = ""
    midnewanswer = ""
    for i in range(twoDarr[total][2]):
      if(twoDarr[total][0] == '1-6-1-1'):
        problem, temp_answer, blankpro = Graphing_One_Variable_Inequalities_1(twoDarr[total][1], 0)
        problem = problem + "\\par" + blankpro
        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        tANSmasterSeed = "\\task " + str(problem) + "\\par" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"

      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
Pre Algebra Section 6-2
'''
def thisisfor62(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
  masterSeed = []
  ANSmasterSeed = []
  newpageanswer = []
  tmasterSeed = ""
  tANSmasterSeed = ""


  for total in range(len(twoDarr)):
    midMasterSeed = ""
    midANSmasterSeed = ""
    midnewanswer = ""
    for i in range(twoDarr[total][2]):
      if(twoDarr[total][0] == '1-6-2-1'):
        problem, temp_answer, blankpro = Solving_One_Step_Inequalities_Adding_Subtracting(twoDarr[total][1], 0)
        problem = problem + "\\par" + blankpro
        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        tANSmasterSeed = "\\task " + str(problem) + "\\par" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"

      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
Pre Algebra Section 6-3
'''
def thisisfor63(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
  masterSeed = []
  ANSmasterSeed = []
  newpageanswer = []
  tmasterSeed = ""
  tANSmasterSeed = ""


  for total in range(len(twoDarr)):
    midMasterSeed = ""
    midANSmasterSeed = ""
    midnewanswer = ""
    for i in range(twoDarr[total][2]):
      if(twoDarr[total][0] == '1-6-3-1'):
        problem, temp_answer, blankpro = Solving_One_Step_Inequalities_Multiplication_Division(twoDarr[total][1], 0)
        problem = problem + "\\par" + blankpro
        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        tANSmasterSeed = "\\task " + str(problem) + "\\par" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"

      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
Pre Algebra Section 6-4
'''
def thisisfor64(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
  masterSeed = []
  ANSmasterSeed = []
  newpageanswer = []
  tmasterSeed = ""
  tANSmasterSeed = ""


  for total in range(len(twoDarr)):
    midMasterSeed = ""
    midANSmasterSeed = ""
    midnewanswer = ""
    for i in range(twoDarr[total][2]):
      if(twoDarr[total][0] == '1-6-4-1'):
        problem, temp_answer, blankpro = Solving_Two_Step_Inequalities(twoDarr[total][1], 0)
        problem = problem + "\\par" + blankpro
        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        tANSmasterSeed = "\\task " + str(problem) + "\\par" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"

      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
Pre Algebra Section 7-1
'''
def thisisfor71(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
  masterSeed = []
  ANSmasterSeed = []
  newpageanswer = []
  tmasterSeed = ""
  tANSmasterSeed = ""


  for total in range(len(twoDarr)):
    midMasterSeed = ""
    midANSmasterSeed = ""
    midnewanswer = ""
    for i in range(twoDarr[total][2]):
      if(twoDarr[total][0] == '1-7-1-1'):
        problem, answer = exponent_problem_generator(twoDarr[total][1], 0)
        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = "\\task " + str(problem) + "\\\\" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"


      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
Pre Algebra Section 7-2
'''
def thisisfor72(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
  masterSeed = []
  ANSmasterSeed = []
  newpageanswer = []
  tmasterSeed = ""
  tANSmasterSeed = ""


  for total in range(len(twoDarr)):
    midMasterSeed = ""
    midANSmasterSeed = ""
    midnewanswer = ""
    for i in range(twoDarr[total][2]):
      if(twoDarr[total][0] == '1-7-2-1'):
        problem, answer = Exponent_Division(twoDarr[total][1], 0, 2, 10, 2, 20)
        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = "\\task " + str(problem) + "\\\\" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"

      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
Pre Algebra Section 7-3
'''
def thisisfor73(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
  masterSeed = []
  ANSmasterSeed = []
  newpageanswer = []
  tmasterSeed = ""
  tANSmasterSeed = ""


  for total in range(len(twoDarr)):
    midMasterSeed = ""
    midANSmasterSeed = ""
    midnewanswer = ""
    for i in range(twoDarr[total][2]):
      if(twoDarr[total][0] == '1-7-3-1'):
        problem, answer = Powers_Of_Products(twoDarr[total][1], 0, 2, 10, 2, 20)
        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = "\\task " + str(problem) + "\\\\" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"

      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
Pre Algebra Section 7-4
'''
def thisisfor74(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
  masterSeed = []
  ANSmasterSeed = []
  newpageanswer = []
  tmasterSeed = ""
  tANSmasterSeed = ""


  for total in range(len(twoDarr)):
    midMasterSeed = ""
    midANSmasterSeed = ""
    midnewanswer = ""
    for i in range(twoDarr[total][2]):
      if(twoDarr[total][0] == '1-7-4-1'):
        problem, answer = Scientific_Notation_Section_1(twoDarr[total][1], 0)
        tmasterSeed, tANSmasterSeed, tnewpageanswer = LatexCreation(str(problem), str(answer))
      elif(twoDarr[total][0] == '1-7-4-2'):
        problem, answer = Scientific_Notation_Section_2(twoDarr[total][1], 0)
        tmasterSeed, tANSmasterSeed, tnewpageanswer = LatexCreation(str(problem), str(answer))
      elif(twoDarr[total][0] == '1-7-4-3'):
        problem, answer = Scientific_Notation_Section_3(twoDarr[total][1], 0)
        tmasterSeed, tANSmasterSeed, tnewpageanswer = LatexCreation(str(problem), str(answer))
      elif(twoDarr[total][0] == '1-7-4-4'):
        problem, answer = Scientific_Notation_Section_4(twoDarr[total][1], 0)
        tmasterSeed, tANSmasterSeed, tnewpageanswer = LatexCreation(str(problem), str(answer))

      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
Pre Algebra Section 7-5
'''
def thisisfor75(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
  masterSeed = []
  ANSmasterSeed = []
  newpageanswer = []
  tmasterSeed = ""
  tANSmasterSeed = ""


  for total in range(len(twoDarr)):
    midMasterSeed = ""
    midANSmasterSeed = ""
    midnewanswer = ""
    for i in range(twoDarr[total][2]):
      if(twoDarr[total][0] == '1-7-5-1'):
        problem, answer = Square_Roots_Section_1(twoDarr[total][1], 0)
        tmasterSeed, tANSmasterSeed, tnewpageanswer = LatexCreation(str(problem), str(answer))

      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
Pre Algebra Section 8-1
'''
def thisisfor81(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
  masterSeed = []
  ANSmasterSeed = []
  newpageanswer = []
  tmasterSeed = ""
  tANSmasterSeed = ""


  for total in range(len(twoDarr)):
    midMasterSeed = ""
    midANSmasterSeed = ""
    midnewanswer = ""
    for i in range(twoDarr[total][2]):
      if(twoDarr[total][0] == '1-8-1-1'):
        problem, answer = Fractions_Decimals_and_Percents_Section_1(twoDarr[total][1], 0)
        tmasterSeed, tANSmasterSeed, tnewpageanswer = LatexCreation(str(problem), str(answer))

      elif(twoDarr[total][0] == '1-8-1-2'):
        problem, answer = Percents_Fractions_Decimal_Conversion_22(twoDarr[total][1], 0)
        tmasterSeed, tANSmasterSeed, tnewpageanswer = LatexCreation(str(problem), str(answer))

      elif(twoDarr[total][0] == '1-8-1-3'):
        problem, answer = Percents_Fractions_Decimal_Conversion_33(twoDarr[total][1], 0)
        tmasterSeed, tANSmasterSeed, tnewpageanswer = LatexCreation(str(problem), str(answer))

      elif(twoDarr[total][0] == '1-8-1-4'):
        problem, answer = Percents_Fractions_Decimal_Conversion_44(twoDarr[total][1], 0)
        tmasterSeed, tANSmasterSeed, tnewpageanswer = LatexCreation(str(problem), str(answer))

      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
Pre Algebra Section 8-3
'''
def thisisfor83(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
  masterSeed = []
  ANSmasterSeed = []
  newpageanswer = []
  tmasterSeed = ""
  tANSmasterSeed = ""


  for total in range(len(twoDarr)):
    midMasterSeed = ""
    midANSmasterSeed = ""
    midnewanswer = ""
    for i in range(twoDarr[total][2]):
      if(twoDarr[total][0] == '1-8-3-1'):
        problem, answer = Finding_Percent_Change_Section_1(twoDarr[total][1], 0)
        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = "\\task " + str(problem) + "\\\\$" + temp_answer + " $\\vspace{2cm}"
        tnewpageanswer = "\\task $" + temp_answer + "$ \\vspace{2cm}"
      elif(twoDarr[total][0] == '1-8-3-2'):
        problem, answer = Finding_Percent_Change_Section_2(twoDarr[total][1], 0)
        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = "\\task " + str(problem) + "\\\\$" + temp_answer + " $\\vspace{2cm}"
        tnewpageanswer = "\\task $" + temp_answer + "$ \\vspace{2cm}"

      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
Pre Algebra Section 8-4
'''
def thisisfor84(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
  masterSeed = []
  ANSmasterSeed = []
  newpageanswer = []
  tmasterSeed = ""
  tANSmasterSeed = ""


  for total in range(len(twoDarr)):
    midMasterSeed = ""
    midANSmasterSeed = ""
    midnewanswer = ""
    for i in range(twoDarr[total][2]):
      if(twoDarr[total][0] == '1-8-4-1'):
        problem, answer = Markup_Discount_and_Tax(twoDarr[total][1], 0)
        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = "\\task " + str(problem) + "\\\\$" + temp_answer + " $\\vspace{2cm}"
        tnewpageanswer = "\\task $" + temp_answer + "$ \\vspace{2cm}"

      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
Pre Algebra Section 8-5
'''
def thisisfor85(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
  masterSeed = []
  ANSmasterSeed = []
  newpageanswer = []
  tmasterSeed = ""
  tANSmasterSeed = ""


  for total in range(len(twoDarr)):
    midMasterSeed = ""
    midANSmasterSeed = ""
    midnewanswer = ""
    for i in range(twoDarr[total][2]):
      if(twoDarr[total][0] == '1-8-5-1'):
        problem, answer = Proportions_Section_1(twoDarr[total][1], 0)
        tmasterSeed = "\\task $" + str(problem) + "$ \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = "\\task $" + str(problem) + "$\\\\$" + temp_answer + " $\\vspace{2cm}"
        tnewpageanswer = "\\task $" + temp_answer + "$ \\vspace{2cm}"
      elif(twoDarr[total][0] == '1-8-5-2'):
        problem, answer = Proportions_Section_2(twoDarr[total][1], 0)
        tmasterSeed = "\\task $" + str(problem) + "$ \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = "\\task $" + str(problem) + "$\\\\$" + temp_answer + " $\\vspace{2cm}"
        tnewpageanswer = "\\task $" + temp_answer + "$ \\vspace{2cm}"

      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
Pre Algebra Section 8-6
'''
def thisisfor86(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
  masterSeed = []
  ANSmasterSeed = []
  newpageanswer = []
  tmasterSeed = ""
  tANSmasterSeed = ""


  for total in range(len(twoDarr)):
    midMasterSeed = ""
    midANSmasterSeed = ""
    midnewanswer = ""
    for i in range(twoDarr[total][2]):
      if(twoDarr[total][0] == '1-8-6-1'):
        problem, answer = Simple_And_Compound_Interest_Section_1(twoDarr[total][1], 0)
        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\\$" + temp_answer + " $\\vspace{2cm}"
        tnewpageanswer = "\\task $" + temp_answer + "$ \\vspace{2cm}"

      elif(twoDarr[total][0] == '1-8-6-2'):
        problem, answer = Simple_And_Compound_Interest_Section_2(twoDarr[total][1], 0)
        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = "\\task " + str(problem) + r"\\$" + temp_answer + " $\\vspace{2cm}"
        tnewpageanswer = "\\task $" + temp_answer + "$ \\vspace{2cm}"

      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
Pre Algebra Section 9-1
'''
def thisisfor91(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
  masterSeed = []
  ANSmasterSeed = []
  newpageanswer = []
  tmasterSeed = ""
  tANSmasterSeed = ""

  for total in range(len(twoDarr)):
    midMasterSeed = ""
    midANSmasterSeed = ""
    midnewanswer = ""
    for i in range(twoDarr[total][2]):
      if(twoDarr[total][0] == '1-9-1-1'): #####
        problem, answer = Find_The_Slope_Section_1(twoDarr[total][1], "latex")

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\\$" + temp_answer + " $\\vspace{2cm}"
        tnewpageanswer = "\\task $" + temp_answer + "$ \\vspace{2cm}"

      elif(twoDarr[total][0] == '1-9-1-2'):
        problem, answer = Find_The_Slope_Section_2(twoDarr[total][1], "latex")

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = "\\task " + str(problem) + r"\\$" + temp_answer + " $\\vspace{2cm}"
        tnewpageanswer = "\\task $" + temp_answer + "$ \\vspace{2cm}"

      elif(twoDarr[total][0] == '1-9-1-3'):
        problem, answer = Find_The_Slope_Section_3(twoDarr[total][1], "latex")

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = "\\task " + str(problem) + r"\\$" + temp_answer + " $\\vspace{2cm}"
        tnewpageanswer = "\\task $" + temp_answer + "$ \\vspace{2cm}"

      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
Pre Algebra Section 9-2
'''
def thisisfor92(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
  masterSeed = []
  ANSmasterSeed = []
  newpageanswer = []
  tmasterSeed = ""
  tANSmasterSeed = ""

  for total in range(len(twoDarr)):
    midMasterSeed = ""
    midANSmasterSeed = ""
    midnewanswer = ""
    for i in range(twoDarr[total][2]):
      if(twoDarr[total][0] == '1-9-2-1'):
        problem, answer = Graphing_Lines_Slope_Intersect(twoDarr[total][1], "latex")

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\\" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"

      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)


"""
'''
Pre Algebra Section 9-3
'''
def thisisfor93(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
  masterSeed = []
  ANSmasterSeed = []
  newpageanswer = []
  tmasterSeed = ""
  tANSmasterSeed = ""


  for total in range(len(twoDarr)):
    midMasterSeed = ""
    midANSmasterSeed = ""
    midnewanswer = ""
    for i in range(twoDarr[total][2]):
      if(twoDarr[total][0] == '1-9-3-1'):
        problem, answer = Find_The_Slope_Section_3(twoDarr[total][1], "latex")
        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = "\\task " + str(problem) + "\\\\" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"

      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)
"""