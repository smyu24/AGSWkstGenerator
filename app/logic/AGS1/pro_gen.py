from .Unit1.S1_1_1 import Evaluate_Equation_1, Evaluate_Equation_2, Evaluate_Equation_3
from .Unit1.S1_1_2 import Graph_The_Ordered_Pairs
from .Unit1.S1_2_1 import Fill_In_The_Sequence_1, Fill_In_The_Sequence_2, Fill_In_The_Sequence_3
from .Unit1.S1_2_2 import The_Meaning_Of_An_Exponent_1, The_Meaning_Of_An_Exponent_2
from .Unit1.S1_2_3 import Finding_Patterns_In_Geometric_Shapes
from .Unit1.S1_3_1 import Reading_The_Table
from .Unit1.S1_3_2 import Arithmetic_Sequences_1, Arithmetic_Sequences_2, Arithmetic_Sequences_3
from .Unit1.S1_3_3 import Geometric_Sequence_Problem
from .Unit1.S1_3_4 import So_Should_We_Use_Recursive_Or_Explicit

#-----
from .Unit1.S1_4_1 import Arithmetic_Explicit_Recursive
from .Unit1.S1_4_2 import AGS_Find_The_Slope_Section_1, AGS_Find_The_Slope_Section_2, AGS_Find_The_Slope_Section_3, AGS_Find_The_Slope_Section_4
from .Unit1.S1_5_1 import Information_To_Geometric_Sequence
from .Unit1.S1_5_2 import Slope_Intercept_Form_1, Slope_Intercept_Form_2
#from .Unit1.S1_5_3 import Geometric_Sequence_To_Explicit_Recursive
#not done, but close (done somewhere else)
from .Unit1.S1_6_1 import AGS_Percent_Change
from .Unit1.S1_6_2 import Is_It_Arithmetic_Or_Geometric_Sequence
from .Unit1.S1_8_1 import Fill_The_Gap
from .Unit1.S1_9_1 import Which_Grows_Faster
#from .Unit1.S1_10_1 import _
# not done, will do later

"""
from .Unit2.S2_1_1 import MatchTheSlopes
from .Unit2.S2_1_1 import _
from .Unit2.S2_1_1 import _
from .Unit2.S2_1_1 import _
from .Unit2.S2_1_1 import _
from .Unit2.S2_1_1 import _
from .Unit2.S2_1_1 import _
from .Unit2.S2_1_1 import _
from .Unit2.S2_1_1 import _
from .Unit2.S2_1_1 import _
from .Unit2.S2_1_1 import _
"""

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
  
#---------------------NOT DONE FROM HERE
'''
AGS 1 Section 1-2-2
'''
def M_The_Meaning_Of_An_Exp(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
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
        problem, answer = The_Meaning_Of_An_Exponent_1(twoDarr[total][1])

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\\" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"
      
      elif(twoDarr[total][0] == '1-2-2-2'):
        problem, answer = The_Meaning_Of_An_Exponent_2(twoDarr[total][1])

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
AGS 1 Section 1-2-3
'''
def M_Finding_Patterns_In_Geo_Seq(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
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
        problem, answer = Finding_Patterns_In_Geometric_Shapes(twoDarr[total][1])

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
AGS 1 Section 1-3-1
'''
def M_Reading_The_Table(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
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
        problem, answer = Reading_The_Table(twoDarr[total][1])

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
AGS 1 Section 1-3-2
'''
def M_Arithmetic_Seq(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
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
        problem, answer = Arithmetic_Sequences_1(twoDarr[total][1])

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\\" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"
      
      elif(twoDarr[total][0] == '1-3-2-2'):
        problem, answer = Arithmetic_Sequences_2(twoDarr[total][1])

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\\" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"
      
      elif(twoDarr[total][0] == '1-3-2-3'):
        problem, answer = Arithmetic_Sequences_3(twoDarr[total][1])

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
AGS 1 Section 1-3-3
'''
def M_Geo_Seq_Problem(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
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
        problem, answer = Geometric_Sequence_Problem(twoDarr[total][1])

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
AGS 1 Section 1-3-4
'''
def M_So_Should_We_Use(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
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
        problem, answer = So_Should_We_Use_Recursive_Or_Explicit(twoDarr[total][1])

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

#--------------------
'''
AGS 1 Section 1-4-1
'''
def M_Arithmetic_Explicit_Recursive(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
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
        problem, answer = Arithmetic_Explicit_Recursive(twoDarr[total][1], 'all', blanks=True)

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
AGS 1 Section 1-4-2
'''
def M_AGS_Find_The_Slope(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
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
        problem, answer = AGS_Find_The_Slope_Section_1(twoDarr[total][1])

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\\" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"
      
      elif(twoDarr[total][0] == '1-4-2-2'):
        problem, answer = AGS_Find_The_Slope_Section_2(twoDarr[total][1])

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\\" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"
      
      elif(twoDarr[total][0] == '1-4-2-3'):
        problem, answer = AGS_Find_The_Slope_Section_3(twoDarr[total][1])

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\\" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"
      
      elif(twoDarr[total][0] == '1-4-2-4'):
        problem, answer = AGS_Find_The_Slope_Section_4(twoDarr[total][1])

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
AGS 1 Section 1-5-1
'''
def M_Information_To_Geometric_Sequence(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
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
        problem, answer = Information_To_Geometric_Sequence(twoDarr[total][1], kind='exp')

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
AGS 1 Section 1-5-2
'''
def M_Slope_Intercept(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
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
        problem, answer = Slope_Intercept_Form_1(twoDarr[total][1])

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\\" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"
      
      elif(twoDarr[total][0] == '1-5-2-2'):
        problem, answer = Slope_Intercept_Form_2(twoDarr[total][1])

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
AGS 1 Section 1-5-3
'''
def M_Geometric_Seq_To_Explicit_Recursive(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
  #Geometric_Sequence_To_Explicit_Recursive (Not DONE)
  return

'''
AGS 1 Section 1-6-1
'''
def M_AGS_Percentage_Change(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
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
        problem, answer = AGS_Percent_Change(twoDarr[total][1])

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
AGS 1 Section 1-6-2
'''
def M_Is_It_Arith_Or_Geo_Seq(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
  #Is_It_Arithmetic_Or_Geometric_Sequence
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
        problem, answer = Is_It_Arithmetic_Or_Geometric_Sequence(twoDarr[total][1])

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
AGS 1 Section 1-8-1
'''
def M_Fill_The_Gap(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
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
        problem, answer = Fill_The_Gap() # only one setting

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
AGS 1 Section 1-9-1
'''
def M_Which_Grows_Faster(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
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
      if(twoDarr[total][0] == '1-9-1-1'):
        problem, answer = Which_Grows_Faster() # only one setting

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
AGS 1 Section 1-10-1
'''
#1.10.1 Information to Arithmetic(?) Sequence.

#instruction: write the explicit equation for each geometric sequence.
# random.randint(1,4), no easy, medium, hard, and "lin"
def M_Information_To_Arith_Seq(twoDarr): #MAIN CODE --------------------------------------------------------------------------------
  return
