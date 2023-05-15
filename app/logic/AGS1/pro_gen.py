from .Unit1.S1_1_1 import Evaluate_Equation_1, Evaluate_Equation_2, Evaluate_Equation_3
from .Unit1.S1_1_2 import Graph_The_Ordered_Pairs
from .Unit1.S1_2_1 import Fill_In_The_Sequence_1, Fill_In_The_Sequence_2, Fill_In_The_Sequence_3
from .Unit1.S1_2_2 import The_Meaning_Of_An_Exponent_1, The_Meaning_Of_An_Exponent_2
from .Unit1.S1_2_3 import Finding_Patterns_In_Geometric_Shapes
from .Unit1.S1_3_1 import Reading_The_Table
from .Unit1.S1_3_2 import Arithmetic_Sequences_1, Arithmetic_Sequences_2, Arithmetic_Sequences_3
from .Unit1.S1_3_3 import Geometric_Sequence_Problem
from .Unit1.S1_3_4 import So_Should_We_Use_Recursive_Or_Explicit
from .Unit1.S1_4_1 import Arithmetic_Explicit_Recursive
from .Unit1.S1_4_2 import AGS_Find_The_Slope_Section_1, AGS_Find_The_Slope_Section_2, AGS_Find_The_Slope_Section_3, AGS_Find_The_Slope_Section_4
from .Unit1.S1_5_1 import Information_To_Geometric_Sequence
from .Unit1.S1_5_2 import Slope_Intercept_Form_1, Slope_Intercept_Form_2
#from .Unit1.S1_5_3 import Geometric_Sequence_To_Explicit_Recursive
from .Unit1.S1_6_1 import AGS_Percent_Change
from .Unit1.S1_6_2 import Is_It_Arithmetic_Or_Geometric_Sequence
from .Unit1.S1_8_1 import Fill_The_Gap
from .Unit1.S1_9_1 import Which_Grows_Faster
#from .Unit1.S1_10_1 import _ (not done, will do later)


from random import randint, choice

'''
AGS 1 Section 1-1-1
'''
def M_Evaluate_Equation(twoDarr):
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
        tANSmasterSeed = r"\task " + str(problem) + r"\par" + temp_answer + "\\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"

      elif(twoDarr[total][0] == '1-1-1-2'):
        problem, answer = Evaluate_Equation_2(twoDarr[total][1], "latex")

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\par" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"

      elif(twoDarr[total][0] == '1-1-1-3'):
        problem, answer = Evaluate_Equation_3(twoDarr[total][1], "latex")

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\par" + temp_answer + " \\vspace{2cm}"
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
def M_Graph_The_Ordered_Pairs(twoDarr):
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
        tANSmasterSeed = r"\task " + str(problem) + r"\par" + temp_answer + " \\vspace{1cm}"
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
def M_Fill_In_The_Seq(twoDarr):
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
        problem, answer = Fill_In_The_Sequence_1(twoDarr[total][1]) # error

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\par" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"

      elif(twoDarr[total][0] == '1-2-1-2'):
        problem, answer = Fill_In_The_Sequence_2( choice(["lin", "exp", "neither"]) )

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\par" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"

      elif(twoDarr[total][0] == '1-2-1-3'):
        problem, answer = Fill_In_The_Sequence_3(twoDarr[total][1]) # error

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\par" + temp_answer + " \\vspace{2cm}"
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
def M_The_Meaning_Of_An_Exp(twoDarr):
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
        tANSmasterSeed = r"\task " + str(problem) + r"\par" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"

      elif(twoDarr[total][0] == '1-2-2-2'):
        problem, answer = The_Meaning_Of_An_Exponent_2(twoDarr[total][1])

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\par" + temp_answer + " \\vspace{2cm}"
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
def M_Finding_Patterns_In_Geo_Seq(twoDarr):
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
        problem, answer = Finding_Patterns_In_Geometric_Shapes( choice(["lin", "exp"]) )

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\par" + temp_answer + " \\vspace{2cm}"
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
def M_Reading_The_Table(twoDarr):
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
        tANSmasterSeed = r"\task " + str(problem) + r"\par" + temp_answer + " \\vspace{2cm}"
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
def M_Arithmetic_Seq(twoDarr):
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
        tANSmasterSeed = r"\task " + str(problem) + r"\par" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"

      elif(twoDarr[total][0] == '1-3-2-2'):
        problem, answer = Arithmetic_Sequences_2(twoDarr[total][1])

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\par" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"

      elif(twoDarr[total][0] == '1-3-2-3'):
        problem, answer = Arithmetic_Sequences_3(twoDarr[total][1])

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\par" + temp_answer + " \\vspace{2cm}"
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
def M_Geo_Seq_Problem(twoDarr):
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
        tANSmasterSeed = r"\task " + str(problem) + r"\par" + temp_answer + " \\vspace{2cm}"
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
def M_So_Should_We_Use(twoDarr):
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
        tANSmasterSeed = r"\task " + str(problem) + r"\par" + temp_answer + " \\vspace{2cm}"
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
def M_Arithmetic_Explicit_Recursive(twoDarr):
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
        tANSmasterSeed = r"\task " + str(problem) + r"\par" + temp_answer + " \\vspace{2cm}"
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
def M_AGS_Find_The_Slope(twoDarr):
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
        tANSmasterSeed = r"\task " + str(problem) + r"\par" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"

      elif(twoDarr[total][0] == '1-4-2-2'):
        problem, answer = AGS_Find_The_Slope_Section_2(twoDarr[total][1])

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\par" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"

      elif(twoDarr[total][0] == '1-4-2-3'):
        problem, answer = AGS_Find_The_Slope_Section_3(twoDarr[total][1])

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\par" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"

      elif(twoDarr[total][0] == '1-4-2-4'):
        problem, answer = AGS_Find_The_Slope_Section_4(twoDarr[total][1])

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\par" + temp_answer + " \\vspace{2cm}"
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
def M_Information_To_Geometric_Sequence(twoDarr):
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
        problem, answer = Information_To_Geometric_Sequence(randint(1,4), kind='exp')

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\par" + temp_answer + " \\vspace{2cm}"
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
def M_Slope_Intercept(twoDarr):
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
        tANSmasterSeed = r"\task " + str(problem) + r"\par" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"

      elif(twoDarr[total][0] == '1-5-2-2'):
        problem, answer = Slope_Intercept_Form_2(twoDarr[total][1])

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\par" + temp_answer + " \\vspace{2cm}"
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
def M_Geometric_Seq_To_Explicit_Recursive(twoDarr):
  #Geometric_Sequence_To_Explicit_Recursive (Not DONE)
  return

'''
AGS 1 Section 1-6-1
'''
def M_AGS_Percentage_Change(twoDarr):
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
        tANSmasterSeed = r"\task " + str(problem) + r"\par" + temp_answer + " \\vspace{2cm}"
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
def M_Is_It_Arith_Or_Geo_Seq(twoDarr):
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
        problem, answer = Is_It_Arithmetic_Or_Geometric_Sequence(randint(1,3))

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\par" + temp_answer + " \\vspace{2cm}"
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
def M_Fill_The_Gap(twoDarr):
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
        tANSmasterSeed = r"\task " + str(problem) + r"\par" + temp_answer + " \\vspace{2cm}"
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
def M_Which_Grows_Faster(twoDarr):
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
        tANSmasterSeed = r"\task " + str(problem) + r"\par" + temp_answer + " \\vspace{2cm}"
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
def M_Information_To_Arith_Seq(twoDarr):
  return



# from .Unit2.S2_1_1 import _ (not done, will do later)
from .Unit2.S2_2_1 import Find_The_Slope
# from .Unit2.S2_2_2 import Indicate_The_Relationship
from .Unit2.S2_2_3 import Solve_The_Following_Equations
from .Unit2.S2_2_4 import Find_The_Recursive_And_Explicit_Equations
from .Unit2.S2_3_1 import Rules_Of_Exponents
from .Unit2.S2_3_2 import Details_Of_Linear_And_Geometric_Sequences_1, Details_Of_Linear_And_Geometric_Sequences_2, Details_Of_Linear_And_Geometric_Sequences_3
from .Unit2.S2_3_3 import Fill_In_The_Blanks
from .Unit2.S2_3_4 import Find_The_Slope_Table
from .Unit2.S2_4_1 import Square_Roots
from .Unit2.S2_4_2 import Fill_In_The_Table
from .Unit2.S2_5_1 import Higher_Order_Roots
from .Unit2.S2_5_2 import Evaluate_The_Function
from .Unit2.S2_6_1 import Percent_Increase_Decrease
# from .Unit2.S2_6_2 import Monthly_Exponential
from .Unit2.S2_7_1 import FillInTheTable
from .Unit2.S2_7_2 import radicalandfractionexponent
from .Unit2.S2_7_3 import xinterceptyintercept, GraphXintYint_2_7_3
from .Unit2.S2_8_1 import FillInTheMeansTable
from .Unit2.S2_10_1 import LinearForms_2_10_1
# from .Unit2.S2_10_2 import _
from .Unit2.S2_11_1 import comparedifferent


'''
AGS 1 Section 2-1-1
'''
# def _(twoDarr):
#   masterSeed = []
#   ANSmasterSeed = []
#   newpageanswer = []
#   tmasterSeed = ""
#   tANSmasterSeed = ""

#   for total in range(len(twoDarr)):
#     midMasterSeed = ""
#     midANSmasterSeed = ""
#     midnewanswer = ""

#     for i in range(twoDarr[total][2]):
#       if(twoDarr[total][0] == '1-9-1-1'):
#         problem, answer = _( )

#         tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
#         temp_answer = "{\\color{red}" + str(answer) + "}"
#         tANSmasterSeed = r"\task " + str(problem) + r"\par" + temp_answer + " \\vspace{2cm}"
#         tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"

#       midMasterSeed += tmasterSeed
#       midANSmasterSeed += tANSmasterSeed
#       midnewanswer += tnewpageanswer

#     ANSmasterSeed.append(midANSmasterSeed)
#     masterSeed.append(midMasterSeed)
#     newpageanswer.append(midnewanswer)

#   return (masterSeed, ANSmasterSeed, newpageanswer)


'''
AGS 1 Section 2-2-1
'''
def M_Find_The_Slope(twoDarr):
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
      if(twoDarr[total][0] == '2-2-1-1'):
        problem, answer = Find_The_Slope( randint(1,3) ) # graphical fig, no mult diff; issues

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\par" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"

      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)


# '''
# AGS 1 Section 2-2-2
# '''
# # NO CODE

'''
AGS 1 Section 2-2-3
'''
def M_Solve_The_Following_Equations(twoDarr):
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
      if(twoDarr[total][0] == '2-2-3-1'):
        problem, answer = Solve_The_Following_Equations( twoDarr[total][1], "latex", randint(1,2) ) # no graph fig

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\par" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"

      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
AGS 1 Section 2-2-4
'''
def M_Find_The_Recursive_And_Explicit_Equations(twoDarr):
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
      if(twoDarr[total][0] == '2-2-4-1'):
        problem, answer = Find_The_Recursive_And_Explicit_Equations() # no mult diff, has tables figures

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\par" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"

      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
AGS 1 Section 2-3-1
'''
def M_Rules_Of_Exponents(twoDarr):
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
      if(twoDarr[total][0] == '2-3-1-1'):
        problem, answer = Rules_Of_Exponents( twoDarr[total][1] ) # no graph fig

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\par" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"

      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)


'''
AGS 1 Section 2-3-2
'''
def M_Details_Of_Linear_And_Geometric_Sequences(twoDarr):
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
      if(twoDarr[total][0] == '2-3-2-1'):
        problem, answer = choice( [Details_Of_Linear_And_Geometric_Sequences_1( randint(1,7) ), Details_Of_Linear_And_Geometric_Sequences_2( randint(1,8) ), Details_Of_Linear_And_Geometric_Sequences_3( randint(1,4) )] ) # has graphs

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\par" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"

      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
AGS 1 Section 2-3-3
'''
def M_Fill_In_The_Blanks(twoDarr):
  masterSeed = []
  ANSmasterSeed = []
  newpageanswer = []
  tmasterSeed = ""
  tANSmasterSeed = ""

  for total in range(len(twoDarr)):
    midMasterSeed = ""
    midANSmasterSeed = ""
    midnewanswer = ""

    for i in range(twoDarr[total][2]): # MAKE SURE THERE ARE TWO SECTIONS AVAIL IN SQL
      if(twoDarr[total][0] == '2-3-3-1'):
        problem, answer = Fill_In_The_Blanks(kind='lin') # has tables

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\par" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"

      if(twoDarr[total][0] == '2-3-3-2'):
        problem, answer = Fill_In_The_Blanks(kind='geo')

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\par" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"

      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
AGS 1 Section 2-3-4
'''
def M_Find_The_Slope_Table(twoDarr):
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
      if(twoDarr[total][0] == '2-3-4-1'):
        problem, answer = Find_The_Slope_Table( randint(1,3) ) # has graphs, tables

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\par" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"

      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)


'''
AGS 1 Section 2-4-1
'''
def M_Square_Roots(twoDarr):
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
      if(twoDarr[total][0] == '2-4-1-1'):
        problem, answer = Square_Roots() # no mult diff

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\par" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"

      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)


'''
AGS 1 Section 2-4-2
'''
def M_Fill_In_The_Table(twoDarr):
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
      if(twoDarr[total][0] == '2-4-2-1'):
        problem, answer = Fill_In_The_Table( randint(1,2) ) # has tables, no mult diff

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\par" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"

      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)


'''
AGS 1 Section 2-5-1
'''
def M_Higher_Order_Roots(twoDarr):
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
      if(twoDarr[total][0] == '2-5-1-1'):
        problem, answer = Higher_Order_Roots() # no mult diff

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\par" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"

      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
AGS 1 Section 2-5-2
'''
def M_Evaluate_The_Function(twoDarr):
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
      if(twoDarr[total][0] == '2-5-2-1'):
        problem, answer = Evaluate_The_Function( randint(1, 5) )

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\par" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"

      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)


'''
AGS 1 Section 2-6-1
'''
def M_Percent_Increase_Decrease(twoDarr):
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
      if(twoDarr[total][0] == '2-6-1-1'):
        problem, answer = Percent_Increase_Decrease() # has tables, no mult diff

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\par" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"

      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
AGS 1 Section 2-6-2
'''
def M_Monthly_Exponential(twoDarr):
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
      if(twoDarr[total][0] == '2-6-2-1'):
        problem, answer = Monthly_Exponential( randint(1,2) ) # some issues with generator, no mult diff,

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\par" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"

      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)


'''
AGS 1 Section 2-7-1
'''
def M_FillInTheTable(twoDarr):
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
      if(twoDarr[total][0] == '2-7-1-1'):
        problem, answer = FillInTheTable( choice(['lin','exp']) )

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\par" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"

      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)


'''
AGS 1 Section 2-7-2
'''
def M_radicalandfractionexponent(twoDarr):
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
      if(twoDarr[total][0] == '2-7-2-1'):
        problem, answer = radicalandfractionexponent( randint(1,3), "latex", choice(['r','e']) )

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\par" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"

      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)


'''
AGS 1 Section 2-7-3
'''
def M_GraphXintYint_2_7_3(twoDarr):
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
      if(twoDarr[total][0] == '2-7-3-1'):
        problem, answer = xinterceptyintercept( randint(1,2) )

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\par" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"

      if(twoDarr[total][0] == '2-7-3-2'):
        problem, answer = GraphXintYint_2_7_3( choice(['lin', 'exp']) )

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\par" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"

      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)


'''
AGS 1 Section 2-8-1
'''
def M_FillInTheMeansTable(twoDarr):
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
      if(twoDarr[total][0] == '2-8-1-1'):
        problem, answer = FillInTheMeansTable()

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\par" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"

      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)


'''
AGS 1 Section 2-10-1
'''
def M_LinearForms_2_10_1(twoDarr):
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
      if(twoDarr[total][0] == '2-10-1-1'):
        problem, answer = LinearForms_2_10_1( 1 )

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\par" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"

      if(twoDarr[total][0] == '2-10-1-2'):
        problem, answer = LinearForms_2_10_1( 2 )

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\par" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"

      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)


'''
AGS 1 Section 2-11-1
'''
def M_comparedifferent(twoDarr):
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
      if(twoDarr[total][0] == '2-11-1-1'):
        problem, answer = comparedifferent( randint(1,2) )

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\par" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"

      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)





r"""
from .Unit3.S3_1_1 import _
from .Unit3.S3_2_1 import _
from .Unit3.S3_2_2 import _
from .Unit3.S3_3_1 import _
from .Unit3.S3_3_2 import _
from .Unit3.S3_3_3 import _
from .Unit3.S3_4_1 import _
from .Unit3.S3_4_2 import _
from .Unit3.S3_4_3 import _
from .Unit3.S3_4_4 import _
from .Unit3.S3_5_1 import _
from .Unit3.S3_6_1 import _
"""

'''
AGS 1 Section 3-1-1
'''
# Find_The_Value_Of_X_3_1_1()


'''
AGS 1 Section 3-2-1
'''
# # Point_Of_Intersection_3_2_1(expr='sympy',option='standard'); Point_Of_Intersection_3_2_1(expr='sympy',option='point_slope')


'''
AGS 1 Section 3-2-2
'''
# PWChars(randint(3,5), cont=False)
#SECTION 2: SeqFeats()

'''
AGS 1 Section 3-3-1
'''
# LinSysTable_3_3_1()

'''
AGS 1 Section 3-3-2
'''
#

'''
AGS 1 Section 3-3-3
'''
# NOT SURE CHECK DOCS AND EVERYTHING

'''
AGS 1 Section 3-4-1
'''
#

'''
AGS 1 Section 3-4-2
'''
#

'''
AGS 1 Section 3-4-4
'''
#

'''
AGS 1 Section 3-5-1
'''
#

'''
AGS 1 Section 3-6-1
'''
#