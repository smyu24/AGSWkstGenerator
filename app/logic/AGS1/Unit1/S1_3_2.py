#1.3.2 Arithmetic Sequences

# absolute path of the parent directory to the sys.path

import os; import sys; import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from loader import ArithSeq, signify, getInt, latexify 
import sympy; from sympy import Rational
from random import randint, choice

#section 1
def getArith(start,diff,num):
  compiledlist=[]
  curr_term=start
  for i in range(1,num+1):
    compiledlist.append(curr_term)
    curr_term = curr_term + diff
  return compiledlist

def Arithmetic_Sequences_1(difficulty=1, expr="latex"):
  choicelist1=[1,2,3,4,5,6,7,8,9,10]
  choicelist2=[-10,-9,-8,-7,-6,-5,-4,-3,-2,-1]
  if difficulty == 1:
    case=randint(1,2)
    if case == 1:
      rand1=randint(1,10)
      rand2=choice(choicelist1)
      arith=[]
      arith = getArith(rand1,rand2,5)
    if case == 2:
      rand1=randint(-10,-1)
      rand2=choice(choicelist2)
      arith=[]
      arith = getArith(rand1,rand2,5)
    problem = r'$\text{Sequence:} '+fr'{arith[0]} , {arith[1]}, {arith[2]} , {arith[3]}, {arith[4]}$'
    answer = '$'+str(rand2)+'$'
    return problem,answer
    
  elif difficulty == 2:
    case=randint(1,2)
    if case == 1:
      numerator1 = randint(1,5)
      denominator1 = randint(2,5)
      numerator2 = randint(1,5)
      denominator2 = randint(2,5)
      start= Rational(numerator1,denominator1)
      diff= Rational(numerator2,denominator2)
      arith=[]
      arith.append(sympy.simplify(start))
      for i in range(4):
        arith.append(sympy.simplify(arith[i] + diff))
    if case == 2:
      numerator1 = randint(1,5)
      denominator1 = randint(2,5)
      numerator2 = randint(-5,-1)
      denominator2 = randint(2,5)
      start= Rational(numerator1,denominator1)
      diff= Rational(numerator2,denominator2)
      arith=[]
      arith.append(sympy.simplify(start))
      for i in range(4):
        arith.append(sympy.simplify(arith[i] + diff))
    
    if expr == 'latex':
      latexify=[]
      for iv in range(len(arith)):
        latexify.append(sympy.latex(arith[iv]))
      problem = r'$\text{Sequence:} '+fr'{latexify[0]} , {latexify[1]}, {latexify[2]} , {latexify[3]}, {latexify[4]}$'
      answer = '$'+sympy.latex(sympy.simplify(diff))+'$'
      return problem,answer
    else:
      problem = r'\text{Sequence:} '+fr'{arith[0]} , {arith[1]}, {arith[2]} , {arith[3]}, {arith[4]}'
      answer = sympy.simplify(diff)
      return problem,answer

  elif difficulty == 3:
    case=randint(1,2)
    if case == 1:
      front = randint(2,5)
      numerator1 = randint(1,7)
      denominator1 = randint(2,7)
      numerator2 = randint(1,5)
      denominator2 = randint(2,5)
      start= front*Rational(numerator1,denominator1)
      diff= Rational(numerator2,denominator2)
      arith=[]
      arith.append(sympy.simplify(start))
      for i in range(4):
        arith.append(sympy.simplify(arith[i] + diff))
    if case == 2:
      front = randint(2,5)
      numerator1 = randint(1,7)
      denominator1 = randint(2,7)
      numerator2 = randint(-5,-1)
      denominator2 = randint(2,5)
      start= front * Rational(numerator1,denominator1)
      diff= Rational(numerator2,denominator2)
      arith=[]
      arith.append(sympy.simplify(start))
      for i in range(4):
        arith.append(sympy.simplify(arith[i] + diff))

    if expr == 'latex':
      latexify=[]
      for iv in range(len(arith)):
        num , dem = arith[iv].as_numer_denom()
        front= num//dem
        top = num%dem
        bot = dem
        if top == 0:
          lat= str(front)
        elif front == 0:
          lat= r'\frac{'+str(top)+'}{'+str(bot)+'}'
        else:
          lat= str(front)+r'\frac{'+str(top)+'}{'+str(bot)+'}'
        latexify.append(lat)
      problem = r'$\text{Sequence:} '+fr'{latexify[0]} , {latexify[1]}, {latexify[2]} , {latexify[3]}, {latexify[4]}$'
      answer = '$'+sympy.latex(sympy.simplify(diff))+'$'
      return problem,answer
    else:
      problem = r'\text{Sequence:} '+fr'{arith[0]} , {arith[1]}, {arith[2]} , {arith[3]}, {arith[4]}'
      answer = sympy.simplify(diff)
      return problem,answer
'''
for i in range(5):
  a , b = Arithmatic_Sequence_Explicit(1,"latex")
  print(a," common diff: ",b)
for i in range(5):
  a , b = Arithmatic_Sequence_Explicit(2,"latex")
  print(a," common diff: ",b)
for i in range(50):
  a , b = Arithmatic_Sequence_Explicit(3,"latex")
  print(a," common diff: ",b,r"\newline")
'''





#section 2
def Arithmetic_Sequences_2(difficulty=1, expr="latex"):
  choicelist1=[1,2,3,4,5,6,7,8,9,10]
  choicelist2=[-10,-9,-8,-7,-6,-5,-4,-3,-2,-1]
  if difficulty == 1:
    case=randint(1,2)
    if case == 1:
      rand1=randint(1,10)
      rand2=choice(choicelist1)
      arith=[]
      arith = getArith(rand1,rand2,5)
    if case == 2:
      rand1=randint(-10,-1)
      rand2=choice(choicelist2)
      arith=[]
      arith = getArith(rand1,rand2,5)
    if expr == 'latex':
      problem = r'$\text{Sequence:} '+fr'{arith[0]} , {arith[1]}, {arith[2]} , {arith[3]}, {arith[4]}$'
      if rand2 > 0:
        answer = '$'+r'f(n)=f(n-1)+'+str(rand2)+'$, $f(1)='+f'{arith[0]}'+'$'
      else:
        answer = '$'+r'f(n)=f(n-1)'+str(rand2)+'$, $f(1)='+f'{arith[0]}'+'$'
    else:
      problem = r'\text{Sequence:} '+fr'{arith[0]} , {arith[1]}, {arith[2]} , {arith[3]}, {arith[4]}'
      if diff > 0:
        answer = r'f(n)=f(n-1)+'+str(rand2)+', f(1)='+f'{arith[0]}'
      else:
        answer = r'f(n)=f(n-1)'+str(rand2)+', f(1)='+f'{arith[0]}'
    return problem,answer
    
  elif difficulty == 2:
    case=randint(1,2)
    if case == 1:
      numerator1 = randint(1,5)
      denominator1 = randint(2,5)
      numerator2 = randint(1,5)
      denominator2 = randint(2,5)
      start= Rational(numerator1,denominator1)
      diff= Rational(numerator2,denominator2)
      arith=[]
      arith.append(sympy.simplify(start))
      for i in range(4):
        arith.append(sympy.simplify(arith[i] + diff))
    if case == 2:
      numerator1 = randint(1,5)
      denominator1 = randint(2,5)
      numerator2 = randint(-5,-1)
      denominator2 = randint(2,5)
      start= Rational(numerator1,denominator1)
      diff= Rational(numerator2,denominator2)
      arith=[]
      arith.append(sympy.simplify(start))
      for i in range(4):
        arith.append(sympy.simplify(arith[i] + diff))
    
    if expr == 'latex':
      latexify=[]
      for iv in range(len(arith)):
        latexify.append(sympy.latex(arith[iv]))
      problem = r'$\text{Sequence:} '+fr'{latexify[0]} , {latexify[1]}, {latexify[2]} , {latexify[3]}, {latexify[4]}$'
      if diff > 0:
        answer = '$'+r'f(n)=f(n-1)+'+sympy.latex(sympy.simplify(diff))+'$, $f(1)='+f'{arith[0]}'+'$'
      else:
        answer = '$'+r'f(n)=f(n-1)'+sympy.latex(sympy.simplify(diff))+'$, $f(1)='+f'{arith[0]}'+'$'
    else:
      problem = r'\text{Sequence:} '+fr'{arith[0]} , {arith[1]}, {arith[2]} , {arith[3]}, {arith[4]}'
      if diff > 0:
        answer = r'f(n)=f(n-1)+'+str(sympy.simplify(diff))+', f(1)='+f'{arith[0]}'
      else:
        answer = r'f(n)=f(n-1)'+str(sympy.simplify(diff))+', f(1)='+f'{arith[0]}'
    return problem,answer

  elif difficulty == 3:
    case=randint(1,2)
    if case == 1:
      front = randint(2,5)
      numerator1 = randint(1,7)
      denominator1 = randint(2,7)
      numerator2 = randint(1,5)
      denominator2 = randint(2,5)
      start= front*Rational(numerator1,denominator1)
      diff= Rational(numerator2,denominator2)
      arith=[]
      arith.append(sympy.simplify(start))
      for i in range(4):
        arith.append(sympy.simplify(arith[i] + diff))
    if case == 2:
      front = randint(2,5)
      numerator1 = randint(1,7)
      denominator1 = randint(2,7)
      numerator2 = randint(-5,-1)
      denominator2 = randint(2,5)
      start= front * Rational(numerator1,denominator1)
      diff= Rational(numerator2,denominator2)
      arith=[]
      arith.append(sympy.simplify(start))
      for i in range(4):
        arith.append(sympy.simplify(arith[i] + diff))

    if expr == 'latex':
      latexify=[]
      for iv in range(len(arith)):
        num , dem = arith[iv].as_numer_denom()
        front= num//dem
        top = num%dem
        bot = dem
        if top == 0:
          lat= str(front)
        elif front == 0:
          lat= r'\frac{'+str(top)+'}{'+str(bot)+'}'
        else:
          lat= str(front)+r'\frac{'+str(top)+'}{'+str(bot)+'}'
        latexify.append(lat)
      problem = r'$\text{Sequence:} '+fr'{latexify[0]} , {latexify[1]}, {latexify[2]} , {latexify[3]}, {latexify[4]}$'
      if diff > 0:
        answer = '$'+r'f(n)=f(n-1)+'+sympy.latex(sympy.simplify(diff))+'$, $f(1)='+f'{latexify[0]}'+'$'
      else:
        answer = '$'+r'f(n)=f(n-1)'+sympy.latex(sympy.simplify(diff))+'$, $f(1)='+f'{latexify[0]}'+'$'
      return problem,answer
    else:
      problem = r'\text{Sequence:} '+fr'{arith[0]} , {arith[1]}, {arith[2]} , {arith[3]}, {arith[4]}'
      answer = sympy.simplify(diff)
      return problem,answer

for i in range(5):
  a , b = Arithmetic_Sequences_2(1,"latex")
  print(a," common diff: ",b)

for i in range(5):
  a , b = Arithmetic_Sequences_2(2,"latex")
  print(a," common diff: ",b)
for i in range(50):
  a , b = Arithmetic_Sequences_2(3,"latex")
  print(a," common diff: ",b,r"\newline")


def getSeqAnswer(seq, prob='common', blanks=False, expr="latex", numTerms=6):
    if expr=="latex":
        answer = ''
        if prob in ['common','all'] :
            answer += '$d = ' if type(seq)==ArithSeq else '$r = '
            answer += latexify(seq.common, seq.precision) + '$'
        if prob in ['explicit','all']:
            if len(answer)>0:
                answer += r' \newline '
            answer += '$' + seq.getExplicit() + r' \quad\text{or}\quad ' + seq.getExplicit(0) + '$'
        if prob in ['recursive','all']:
            if len(answer)>0:
                answer += r' \newline '
            answer += '$' + seq.getRecursive() + r' \quad\text{or}\quad ' + seq.getRecursive(0) + '$'
        
        if blanks:
            if len(answer)>0:
                answer += r' \newline '
            answer += signify(seq.getSeqStr(range(1,numTerms+1))) 
    else:
        seq.getTerms(numTerms)
        answer = seq

    return answer


#section 3
def Arithmetic_Sequences_3(difficulty=1, prob='common', blanks=False, expr="latex"):
    if difficulty == 1: # easy
        if randint(0,1):
            arith = ArithSeq(randint(1,10), [1,randint(1,10)])
        else:
            arith = ArithSeq(randint(-10,-1), [1,randint(-10,-1)])
    
    elif difficulty == 2: # medium (TODO)
        if randint(0,1):
            arith = ArithSeq(Rational(randint(1,5),randint(2,5)), [1,randint(-5,5)])
        else:
            arith = ArithSeq(Rational(randint(-5,-1),randint(2,5)), [1,randint(-5,5)])

    elif difficulty == 3: # hard (TODO)
        if randint(0,1):
            arith = ArithSeq(Rational(randint(1,7),randint(2,7)), [1,Rational(randint(1,5),randint(2,5))])
        else:
            arith = ArithSeq(Rational(getInt(-7,7),randint(2,7)), [1,Rational(randint(-5,-1),randint(2,5))])
    
    nums = [1,2,'','','',''] if blanks else [1,2,3,4,5]
    problem = signify(arith.getSeqStr(nums))
    answer = getSeqAnswer(arith, prob, blanks, expr)
            
    return problem, answer

for i in range(10):
    problem, answer = Arithmetic_Sequences_3(3, 'explicit', blanks=True)
    print(problem, r'\\')
    print(answer, r'\\ \\')