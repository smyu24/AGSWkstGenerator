from num2words import num2words
from .prepart1 import Decimal_Places, readingandwritingrequest, Rounding_Number_Section_1, Rounding_Number_Section_2, Rounding_Number_Section_3
from .prepart2 import Divisibility_And_Factors_Section_1, Divisibility_And_Factors_Section_2, Factoring_Num_Section_1, Factoring_Num, Factoring_Monomials_Section_1, Factoring_Monomials_Section_2, Greatest_Common_Factor_Section_1, Greatest_Common_Factor_Section_2, Least_Common_Multiple

import math
import random

def LatexCreation(problem, answer):
  masterSeed = "\\item $" + str(problem) + "$ \\vspace{2cm}"
  temp_answer = "{\\color{red}" + answer + "}"
  ANSmasterSeed = "\\item $" + str(problem) + "\\\\" + temp_answer + "$ \\vspace{2cm}"
  newpageanswer = "\\item $" + temp_answer + "$ \\vspace{2cm}"

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
Pre Algebra Section 1-1 
'''
def Naming_Decimal_Places(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
  masterSeed = ""
  ANSmasterSeed = ""
  newpageanswer = ""

  for total in range(len(twoDarr)):
    for i in range(twoDarr[total][2]):
      problem, answer = Decimal_Places(twoDarr[total][1], "latex", twoDarr[total][0], int(twoDarr[total][3]), int(twoDarr[total][4]))   
      tmasterSeed, tANSmasterSeed, tnewpageanswer = LatexCreation(problem, answer)
      masterSeed += tmasterSeed
      ANSmasterSeed += tANSmasterSeed
      newpageanswer += tnewpageanswer

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
Pre Algebra Section 1-2 
'''
def readingandwriting(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
  masterSeed = ""
  ANSmasterSeed = ""
  newpageanswer = ""

  for total in range(len(twoDarr)):
    for i in range(twoDarr[total][2]):
      problem, answer = readingandwritingrequest(twoDarr[total][1], "latex", int(twoDarr[total][3]), int(twoDarr[total][4]))   

      if(twoDarr[total][0] == '1-1-2-1'):
        tmasterSeed, tANSmasterSeed, tnewpageanswer = LatexCreation(problem, answer)
      else:
        tmasterSeed, tANSmasterSeed, tnewpageanswer = LatexCreation(answer, problem)
      masterSeed += tmasterSeed
      ANSmasterSeed += tANSmasterSeed
      newpageanswer += tnewpageanswer

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
Pre Algebra Section 1-3
'''
def rounding(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
  masterSeed = ""
  ANSmasterSeed = ""
  newpageanswer = ""

  for total in range(len(twoDarr)):
    for i in range(twoDarr[total][2]):
      if(twoDarr[total][0] == '1-1-3-1'):
        problem, answer = Rounding_Number_Section_1(twoDarr[total][1], "latex", int(twoDarr[total][3]), int(twoDarr[total][4]))   
        tmasterSeed, tANSmasterSeed, tnewpageanswer = LatexCreation(problem, answer)
      elif(twoDarr[total][0] == '1-1-3-2'):
        problem, answer = Rounding_Number_Section_2(twoDarr[total][1], "latex", int(twoDarr[total][3]), int(twoDarr[total][4]))   
        tmasterSeed, tANSmasterSeed, tnewpageanswer = LatexCreation(problem, answer)
      elif(twoDarr[total][0] == '1-1-3-3'):
        problem, answer = Rounding_Number_Section_3(twoDarr[total][1], "latex", int(twoDarr[total][3]), int(twoDarr[total][4]))   
        tmasterSeed, tANSmasterSeed, tnewpageanswer = LatexCreation(problem, answer)

      masterSeed += tmasterSeed
      ANSmasterSeed += tANSmasterSeed
      newpageanswer += tnewpageanswer

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
Pre Algebra Section 2-1
'''
def divandfac(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
  masterSeed = ""
  ANSmasterSeed = ""
  newpageanswer = ""

  for total in range(len(twoDarr)):
    for i in range(twoDarr[total][2]):
      if(twoDarr[total][0] == '1-2-1-1'):
        problem, answer = Divisibility_And_Factors_Section_1(twoDarr[total][1], "latex", int(twoDarr[total][3]), int(twoDarr[total][4]))   
        tmasterSeed, tANSmasterSeed, tnewpageanswer = LatexCreation(problem, answer)
      elif(twoDarr[total][0] == '1-2-1-2'):
        preset,  problem, answer = Divisibility_And_Factors_Section_2(twoDarr[total][1], "latex", int(twoDarr[total][3]), int(twoDarr[total][4]))   
        tmasterSeed =  "\\item "+ "Check out the divisibility by following [" + str(preset) +"]\\\\" + "$" + str(problem) + "$ \\vspace{2cm}"
        temp_answer = "{\\color{red}" + answer + "}"
        tANSmasterSeed = "\\item $" + str(problem) + "\\\\" + temp_answer + "$ \\vspace{2cm}"
        tnewpageanswer = "\\item $" + temp_answer + "$ \\vspace{2cm}"

      masterSeed += tmasterSeed
      ANSmasterSeed += tANSmasterSeed
      newpageanswer += tnewpageanswer

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
Pre Algebra Section 2-2
'''
def factoring(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
  masterSeed = ""
  ANSmasterSeed = ""
  newpageanswer = ""

  for total in range(len(twoDarr)):
    for i in range(twoDarr[total][2]):
      if(twoDarr[total][0] == '1-2-2-1'):
        problem, answer = Factoring_Num_Section_1(twoDarr[total][1], "latex", int(twoDarr[total][3]), int(twoDarr[total][4]))   
        tmasterSeed, tANSmasterSeed, tnewpageanswer = LatexCreation(problem, answer)
      elif(twoDarr[total][0] == '1-2-2-2'):
        problem, answer = Factoring_Num(twoDarr[total][1], "latex", int(twoDarr[total][3]), int(twoDarr[total][4]))   
        tmasterSeed, tANSmasterSeed, tnewpageanswer = LatexCreation(problem, answer)

      masterSeed += tmasterSeed
      ANSmasterSeed += tANSmasterSeed
      newpageanswer += tnewpageanswer

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
Pre Algebra Section 2-3
'''
def monomials(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
  masterSeed = ""
  ANSmasterSeed = ""
  newpageanswer = ""

  for total in range(len(twoDarr)):
    for i in range(twoDarr[total][2]):
      if(twoDarr[total][0] == '1-2-3-1'):
        problem, answer = Factoring_Monomials_Section_1(twoDarr[total][1], "latex", int(twoDarr[total][3]), int(twoDarr[total][4]))   
        tmasterSeed, tANSmasterSeed, tnewpageanswer = LatexCreation(problem, answer)
      elif(twoDarr[total][0] == '1-2-3-2'):
        problem, answer = Factoring_Monomials_Section_2(twoDarr[total][1], "latex", int(twoDarr[total][3]), int(twoDarr[total][4]))   
        tmasterSeed, tANSmasterSeed, tnewpageanswer = LatexCreation(problem, answer)
        
      masterSeed += tmasterSeed
      ANSmasterSeed += tANSmasterSeed
      newpageanswer += tnewpageanswer

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
Pre Algebra Section 2-4
'''
def common_factors(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
  masterSeed = ""
  ANSmasterSeed = ""
  newpageanswer = ""

  for total in range(len(twoDarr)):
    for i in range(twoDarr[total][2]):
      if(twoDarr[total][0] == '1-2-4-1'):
        problem, answer = Greatest_Common_Factor_Section_1(twoDarr[total][1], "latex", int(twoDarr[total][3]), int(twoDarr[total][4]))   
        tmasterSeed, tANSmasterSeed, tnewpageanswer = LatexCreation(problem, answer)
      elif(twoDarr[total][0] == '1-2-4-2'):
        problem, answer = Greatest_Common_Factor_Section_2(twoDarr[total][1], "latex", int(twoDarr[total][3]), int(twoDarr[total][4]))   
        tmasterSeed, tANSmasterSeed, tnewpageanswer = LatexCreation(problem, answer)
        
      masterSeed += tmasterSeed
      ANSmasterSeed += tANSmasterSeed
      newpageanswer += tnewpageanswer

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
Pre Algebra Section 2-5
'''
def Leastcommon_factors(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
  masterSeed = ""
  ANSmasterSeed = ""
  newpageanswer = ""

  for total in range(len(twoDarr)):
    for i in range(twoDarr[total][2]):
      if(twoDarr[total][0] == '1-2-5-1'):
        problem, answer = Least_Common_Multiple(twoDarr[total][1], "latex", int(twoDarr[total][3]), int(twoDarr[total][4]))   
        tmasterSeed, tANSmasterSeed, tnewpageanswer = LatexCreation(problem, answer)

      masterSeed += tmasterSeed
      ANSmasterSeed += tANSmasterSeed
      newpageanswer += tnewpageanswer

  return (masterSeed, ANSmasterSeed, newpageanswer)