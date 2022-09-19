import os; import sys; import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from loader import ArithSeq, latexify, signify
from random import randint

# section 1
# instruction : Find the next three terms in each sequence. Identify the common difference. Write a recursive function and an explicit function for each sequence.

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

def Arithmetic_Explicit_Recursive(difficulty=1, prob='common', blanks=False, expr="latex"):
    if difficulty == 1: # easy
        if randint(0,1):
            arith = ArithSeq(randint(1,10), randint(1,10))
        else:
            arith = ArithSeq(randint(-10,-1), randint(-10,-1))
    elif difficulty == 2:
        if randint(0,1):
            arith = ArithSeq(randint(1,20), randint(1,20))
        else:
            arith = ArithSeq(randint(-20,-1), randint(-20,-1))   
  
    else:
        if randint(0,1):
            arith = ArithSeq(randint(1,20), randint(1,30))
        else:
            arith = ArithSeq(randint(-20,-1), randint(-30,-1))

    nums = [1,2,'','','',''] if blanks else [1,2,3,4,5]
    problem = signify(arith.getSeqStr(nums))
    answer = getSeqAnswer(arith, prob, blanks, expr)
            
    return problem, answer

# for i in range(5):
#     problem, answer = Arithmetic_Explicit_Recursive(1, 'all', blanks=True)
#     print(problem, r'\\')
#     print(answer, r'\\')

# for i in range(5):
#     problem, answer = Arithmetic_Explicit_Recursive(2, 'all', blanks=True)
#     print(problem, r'\\')
#     print(answer, r'\\')

# for i in range(5):
#     problem, answer = Arithmetic_Explicit_Recursive(3, 'all', blanks=True)
#     print(problem, r'\\')
#     print(answer, r'\\')