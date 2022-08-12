from .Unit1.S1_1_1 import Evaluate_Equation_1, Evaluate_Equation_2, Evaluate_Equation_3
from .Unit1.S1_1_2 import Graph_The_Ordered_Pairs
from .Unit1.S1_2_1 import Fill_In_The_Sequence_1, Fill_In_The_Sequence_2, Fill_In_The_Sequence_3
"""
from .Unit1.S1_2_2 import The_Meaning_Of_An_Exponent_1, The_Meaning_Of_An_Exponent_2
from .Unit1.S1_2_3 import Finding_Patterns_In_Geometric_Shapes
from .Unit1.S1_3_1 import Reading_The_Table
from .Unit1.S1_3_2 import Arithmetic_Sequences_1, Arithmetic_Sequences_2, Arithmetic_Sequences_3
from .Unit1.S1_3_3 import Geometric_Sequence_Problem
from .Unit1.S1_3_4 import So_Should_We_Use_Recursive_Or_Explicit
from .Unit1.S1_4_1 import Arithmetic_Explicit_Recursive
from .Unit1.S1_4_2 import AGS_Find_The_Slope_Section_1, AGS_Find_The_Slope_Section_2, AGS_Find_The_Slope_Section_3, AGS_Find_The_Slope_Section_4
from .Unit1.S1_5_1 import infoToSeq
from .Unit1.S1_5_2 import Slope_Intercept_Form_1, Slope_Intercept_Form_2, Slope_Intercept_Form_3
#from .Unit1.S1_5_3 import Geometric_Sequence_To_Explicit_Recursive
#not done, but close (done somewhere else)
from .Unit1.S1_6_1 import AGS_Percent_Change
from .Unit1.S1_6_2 import Is_It_Arithmetic_Or_Geometric_Sequence
from .Unit1.S1_8_1 import Fill_The_Gap
from .Unit1.S1_9_1 import Which_Grows_Faster

from .Unit2.S2_1_1 import _
from .Unit2.S2_2_1 import MatchTheSlopes
"""

"""from .Unit2.S2_1_1 import _
from .Unit2.S2_1_1 import _
from .Unit2.S2_1_1 import _
from .Unit2.S2_1_1 import _
from .Unit2.S2_1_1 import _
from .Unit2.S2_1_1 import _
from .Unit2.S2_1_1 import _
from .Unit2.S2_1_1 import _
from .Unit2.S2_1_1 import _
from .Unit2.S2_1_1 import _
from .Unit2.S2_1_1 import _"""

import math
import random
from sympy import latex, sympify

'''
AGS 1 Section 1-1-1
'''
def M_Evaluate_Equation(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
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
      if(twoDarr[total][0] == '1-1-1-1'):
        problem, answer = Evaluate_Equation_1(twoDarr[total][1], "latex")

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "$ {\\color{red}" + str(answer) + "} $"
        tANSmasterSeed = r"\task " + str(problem) + r"\\" + temp_answer + "\\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"

      elif(twoDarr[total][0] == '1-1-1-2'):
        problem, answer = Evaluate_Equation_2(twoDarr[total][1], "latex")

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\\" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"

      elif(twoDarr[total][0] == '1-1-1-3'):
        problem, answer = Evaluate_Equation_3(twoDarr[total][1], "latex")

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

'''
AGS 1 Section 1-1-2
'''
def M_Graph_The_Ordered_Pairs(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
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
      if(twoDarr[total][0] == '1-1-2-1'):
        problem, answer = Graph_The_Ordered_Pairs(twoDarr[total][1])

        tmasterSeed = "\\task " + str(problem) + " \\vspace{1cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\\" + temp_answer + " \\vspace{1cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{1cm}"

      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
AGS 1 Section 1-2-1
'''
def M_Fill_In_The_Seq(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
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
        problem, answer = Fill_In_The_Sequence_1(twoDarr[total][1])

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\\" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"
      
      elif(twoDarr[total][0] == '1-2-1-2'):
        problem, answer = Fill_In_The_Sequence_2(twoDarr[total][1])

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\\" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"
      
      elif(twoDarr[total][0] == '1-2-1-3'):
        problem, answer = Fill_In_The_Sequence_3(twoDarr[total][1])

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
  
'''
AGS 1 Section 1-2-2
'''

'''
AGS 1 Section 1-2-3
'''

'''
AGS 1 Section 1-3-1
'''

'''
AGS 1 Section 1-3-2
'''

'''
AGS 1 Section 1-3-3
'''

'''
AGS 1 Section 1-3-4
'''

'''
AGS 1 Section 1-4-1
'''

'''
AGS 1 Section 1-4-2
'''

'''
AGS 1 Section 1-5-1
'''

'''
AGS 1 Section 1-5-2
'''

'''
AGS 1 Section 1-5-3
'''

'''
AGS 1 Section 1-6-1
'''
'''
AGS 1 Section 1-6-2
'''
'''
AGS 1 Section 1-8-1
'''
'''
AGS 1 Section 1-9-1
'''
#1.10.1 Information to Arithmetic(?) Sequence.

#instruction: write the explicit equation for each geometric sequence.
# random.randint(1,4), no easy, medium, hard, and "lin"