import random
import math
from num2words import num2words

def insert_comma_1(num):
    num = int(num)
    return (f"{num:,}")

def insert_comma_2(num):
    num = float(num)
    return (f"{num:,}")

def latexify(input, option="inline"):
    if option == "inline":
        return input 
    else:
        return '\[' + input + '\]'

def Decimal_Places_Answer_Generation(set, wholenumber='yes'):
    whole = ["Ones", "Tens", "Hundreds", "", "Thousands", "Ten Thousands",
             "Hundred Thousands", "", "Millions", "Ten Millions", "Hundred Millions", "", "Billions"]
    decimals = ["Tenths", "Hundredths", "Thousandths", "Ten Thousandths",
                "Hundred Thousandths", "Millionth", "Ten Millionths", "Hundred Millionth", "Billionths"]
#from the decimal point
    split = 0
    location = 0
    if wholenumber == 'yes':
        split = set[set.rfind("e") + 1:]
        for i in range(1, len(split)):
            location += 1
        return whole[location]
    else:
        if set.rfind("e") + 1 < set.rfind("."):
            split = set[set.rfind("e") + 1:set.rfind(".")]
            for i in range(1, len(split)):
                location += 1
            return whole[location]
        else:
            split = set[set.rfind(".") + 1:set.rfind("e") + 1]
            for i in range(1, len(split)):
                if split[i - 1].isdigit() == True:
                    location += 1
            return decimals[location]

def reg_truncate(n):
    n = float(n)
    return(int(n * 1000) / 1000)

def insert_overline(problemsets):
    ticker = True
    while ticker == True:
        problemsets = str(problemsets)
        a = random.randint(0, len(problemsets) - 1)
        list(problemsets)
        if problemsets[a] != "." and problemsets[a] != ",":
            ticker = False
    
    problemsets = str(problemsets)
    problemsets = problemsets[:a] + r"\overline" + problemsets[a:]
    return(problemsets, a)


def min_max_checker(option_min, option_max):
    option_min = int(option_min)
    option_max = int(option_max)
    if option_min == 0 and option_max == 0:
        return(True)
    return(False)

def decimals_generator(option_difficulty, option_min, option_max):
    problem = ""
    if min_max_checker(option_min, option_max) == True:
        if option_difficulty == "easy": 
            integer_only = random.randint(1, 999)
            decimal = random.random()
            if integer_only % 2 == 0: 
                problem = "{:.1f}".format(integer_only + decimal)
            else:
                problem = "{:.2f}".format(integer_only + decimal)

        elif option_difficulty == "medium":
            integer_only = random.randint(9, 9999)
            decimal = random.random()
            decimal_2 = "{:.2f}".format(decimal)
            if integer_only % 2 == 0:
                if (float(decimal_2) * 100) % 2 == 0:
                    problem  = "{:.1f}".format(integer_only + float(decimal))
                else:
                    problem = "{:.2f}".format(integer_only + float(decimal))
            else:
                problem = "{:.3f}".format(integer_only + float(decimal))

        elif option_difficulty == "hard":
            integer_only = random.randint(99, 99999999)
            decimal = random.random()
            if integer_only % 2 == 0:
                problem = "{:.2f}".format(integer_only + decimal)
            else:
                problem = "{:.3f}".format(integer_only + decimal)
    
    else: 
        option_max = option_max - 1
        if option_difficulty == "easy": 
            integer_only = random.randint(option_min, option_max)
            decimal = random.random()
            if integer_only % 2 == 0: 
                problem = "{:.1f}".format(integer_only + decimal)
            else:
                problem = "{:.2f}".format(integer_only + decimal)

        elif option_difficulty == "medium":
            integer_only = random.randint(option_min, option_max)
            decimal = random.random()
            decimal_2 = "{:.2f}".format(decimal)
            if integer_only % 2 == 0:
                if (float(decimal_2) * 100) % 2 == 0:
                    problem  = "{:.1f}".format(integer_only + float(decimal))
                else:
                    problem = "{:.2f}".format(integer_only + float(decimal))
            else:
                problem = "{:.3f}".format(integer_only + float(decimal))

        elif option_difficulty == "hard":
            integer_only = random.randint(option_min, option_max)
            decimal = random.random()
            if integer_only % 2 == 0:
                problem = "{:.2f}".format(integer_only + decimal)
            else:
                problem = "{:.3f}".format(integer_only + decimal)
    return(reg_truncate(problem))

def whole_generator(option_difficulty, option_min, option_max):
    after_comma = []
    problemsets = 0
    if min_max_checker(option_min, option_max) == True:
        if option_difficulty == 1:
            problemsets = random.randint(1, 999)

        elif option_difficulty == 2:
            problemsets = random.randint(1000, 999999)

        elif option_difficulty == 3:
            problemsets = random.randint(999999, 999999999)
    else:
        if option_difficulty == 1:
            problemsets = random.randint(option_min, option_max)

        elif option_difficulty == 2:
            problemsets = random.randint(option_min, option_max)

        elif option_difficulty == 3:
            problemsets = random.randint(option_min, option_max)

    after_comma = insert_comma_1(problemsets)
    after_comma = insert_overline(after_comma)
    return(after_comma[0], -1 * (after_comma[1] - len(str(problemsets))))

def Decimal_Places(option_difficulty="easy", expr="latex", option_1="whole", option_min=0, option_max=0):
    problemsets = ""
    answersets = ""
    if option_1 == "1-1-1-1":
        problemsets = whole_generator(option_difficulty, option_min, option_max)
        if expr == 'latex':
          return(latexify(problemsets[0]), Decimal_Places_Answer_Generation(problemsets[0]))
        else:
          return(problemsets[0], Decimal_Places_Answer_Generation(problemsets[0]))
    else:
        problemsets = insert_overline(insert_comma_2(decimals_generator(option_difficulty, option_min, option_max)))
        if expr == 'latex':
          return(latexify(problemsets[0]), Decimal_Places_Answer_Generation(problemsets[0], "no"))
        else: 
          return(problemsets[0], Decimal_Places_Answer_Generation(problemsets[0], "no"))

#SECTION 2 ####################################################################################
# SECTION ONE (Write each as a numeral)

def min_max_checker(option_min, option_max):
    option_min = int(option_min)
    option_max = int(option_max)
    if option_min == 0 and option_max == 0:
        return(True)
    return(False)

def Number_Generator(max,integers):
  numbers = []
  final = []
  answers = []
  for i in range(integers):
    numbers.append(random.randint(1, 9))
  zeros = "0" * max
  zeros = [*zeros] # unpacking ()

  final.append(str(numbers.pop()))
  final = final+zeros

  for i in range(len(numbers)):
    index = random.randint(1, len(final) - 1)
    final[index] = str(numbers.pop())
  answers = ''.join(final) # append get rid of zeros
  return answers

def Reading_And_Writing_Whole_Numbers(option_difficulty='easy', expr='latex', option_min = 0, option_max = 0):  
  problem = ''
  answer = ''
  if min_max_checker(option_min, option_max) == True:
    if option_difficulty == 1:
      max = random.randint(2, 4)
      integers = random.randint(1, 2)
      problem = Number_Generator(max, integers)
      answer = num2words(problem, lang='en')

    elif option_difficulty == 2:
      max = random.randint(3, 5)
      integers = random.randint(2, 4)
      problem = Number_Generator(max, integers)
      answer = num2words(problem, lang='en')

    elif option_difficulty == 3:
      max = 8
      integers = random.randint(5, 7)
      problem = Number_Generator(max, integers)
      answer = num2words(problem, lang='en')
  
  else:
    problem = random.randint(option_max, option_min)
    answer = num2words(problem, lang='en')

  if expr == 'latex':
    return insert_comma_1(int(problem)), answer   
  else:
    return insert_comma_1(int(problem)), answer      

def readingandwritingrequest(option_difficulty="easy", expr="latex", option_1="whole", option_min=0, option_max=0):
    problem, answer = Reading_And_Writing_Whole_Numbers(option_difficulty, expr, option_min , option_max)
    return problem, answer
###################################################################################
#section 3
def insert_overline2(problemsets):
    ticker = True
    while ticker == True:
        problemsets = str(problemsets)
        a = random.randint(0, len(problemsets) - 2)
        list(problemsets)
        if problemsets[a] != "." and problemsets[a] != ",":
            ticker = False
    
    problemsets = str(problemsets)
    problemsets = problemsets[:a] + r"\overline" + problemsets[a:]

    a = (((problemsets.rfind('e')) - len(problemsets)) * -1) - 1
    return(problemsets , a)

def rounding(problemsets, underscores):
    inversed_under = underscores * -1
    skipper = (inversed_under) + 1
    pass_through = False
    accepted = 0
    empty = ''
    while pass_through == False:
        if problemsets[skipper] == ',' or problemsets[skipper] == '.':
            skipper += 1
        elif int(problemsets[skipper]) >= 5:
            cut = problemsets[inversed_under + 1:]
            for i in range(len(cut)):
                if cut[i] == ',':
                    empty = empty + ','
                else:
                    empty = empty + '0'
            other_half = problemsets[:inversed_under + 1]
            other_half = list(''.join(other_half))
            if int(str(other_half[-1])) != 9:
                other_half[-1] = str(int(str(other_half[-1])) + 1)
            else:
                other_half[-1] = str(0)
                # check for commas next
                if other_half[other_half.index('o') - 2] == 9 or other_half[other_half.index('o') - 2] == ',':
                    if other_half[other_half.index('o') - 3] == 9 or other_half[other_half.index('o') - 2] == ',':
                        if other_half[other_half.index('o') - 4] == 9 or other_half[other_half.index('o') - 2] == ',':
                            other_half[other_half.index('o') - 5] = str(int(other_half[other_half.index('o') - 4]) + 1)
                        else: 
                            other_half[other_half.index('o') - 4] = str(int(other_half[other_half.index('o') - 4]) + 1)
                    else:
                        other_half[other_half.index('o') - 3] = str(int(other_half[other_half.index('o')- 3]) + 1)
                else:
                    other_half[other_half.index('o') - 2] = str(int(other_half[other_half.index('o') - 2]) + 1)


            problemsets = ''.join(other_half) + empty
            pass_through = True
        else:
            cut = problemsets[inversed_under + 1:]
            for i in range(len(cut)):
                if cut[i] == ',':
                    empty = empty + ','
                else:
                    empty = empty + '0'
            other_half = problemsets[:inversed_under + 1]
            problemsets = other_half + ''.join(empty)
            pass_through = True
    return(problemsets)

def Rounding_Number_Section_1(option_difficulty='easy',expr='latex', localmin=0, localmax=0):
    problemsets = ""
    temp_problem = []
    temp = ""
    if(localmin == localmax):
        if(option_difficulty == 1):
            problemsets = random.randint(100, 99999)
        elif(option_difficulty == 2):
            problemsets = random.randint(1000, 999999)
        elif(option_difficulty == 3):
            problemsets = random.randint(10000, 89999999)
    else:
        problemsets = random.randint(localmin, localmax)
    problemsets = list(str(problemsets))
    temp_problem = insert_comma_1(''.join(problemsets))
    temp_problem, temp = insert_overline2(temp_problem)
    temp_problem = rounding(temp_problem, temp)
    if expr == 'latex':
        return(latexify(insert_comma_1(''.join(problemsets))), latexify(temp_problem))
    else:
        return(insert_comma_1(''.join(problemsets)), temp_problem) 
#####################################################################################
def Commanizer(problemsets):
    questions = ""
    comma_d = ""
    decimal_subtract = 0
    amount_commas = len(str(problemsets))
    period = str(problemsets).find(".")
    if period != -1:
        decimal_subtract = amount_commas - (period + 1)
        amount_commas = (amount_commas - 1) // 3
    questions = list(str(problemsets))
    if amount_commas >= 1:
        questions.insert((-3 - decimal_subtract), ",")
    if amount_commas >= 2:
        questions.insert((-7 - decimal_subtract), ",")
    if amount_commas >= 3:
        questions.insert((-11 - decimal_subtract), ",")

    comma_d = "".join(questions)
    return(comma_d)

def Rounding_Number_Section_2(option_difficulty=1 ,expr='latex', localmin=0, localmax=0):
    problemsets = ""
    underscores = ""
    answerset = []
    after_comma = []
    filler = ""
    wordify = ""

    if(localmin == localmax):
        if option_difficulty == 1:
            problemsets = random.randint(1000, 1000000)
            underscores = random.randint(2, len(str(problemsets)) - 1)
        elif option_difficulty == 2:
            problemsets = random.randint(1000000, 10000000000)
            underscores = random.randint(4, len(str(problemsets)) - 1)
        elif option_difficulty == 3:
            problemsets = random.randint(1000000, 10000000000)
            underscores = random.randint(4, len(str(problemsets)) - 1)
    else:
        problemsets = random.randint(localmin, localmax)
        underscores = random.randint(4, len(str(problemsets)) - 1)

    filler = "1" + "0" * underscores
    wordify = num2words(filler, lang='en')
    answerset = round(problemsets, -underscores)
    after_comma = Commanizer(answerset)
    if expr == 'latex':
        prob = latexify(insert_comma_1(problemsets)) + "; " + wordify
        return(prob, latexify(after_comma))
    else:
        prob = insert_comma_1(problemsets) + "; " + wordify
        return(prob, after_comma)
##############################################################################################
def insert_overline3(problemsets):
    ticker = True
    while ticker == True:
        problemsets = str(problemsets)
        a = random.randint(0, len(problemsets) - 2)
        list(problemsets)
        if problemsets[a] != "." and problemsets[a] != ",":
            ticker = False
    
    problemsets = str(problemsets)
    problemsets = problemsets[:a] + r"\overline" + problemsets[a:]

    a = (((problemsets.rfind('e')) - len(problemsets)) * -1) - 1
    return(problemsets , a)


def rounding(problemsets, underscores):
    inversed_under = underscores * -1
    skipper = (inversed_under) + 1
    pass_through = False
    accepted = 0
    empty = ''
    while pass_through == False:
        if problemsets[skipper] == ',' or problemsets[skipper] == '.':
            skipper += 1
        elif int(problemsets[skipper]) >= 5:
            cut = problemsets[inversed_under + 1:]
            for i in range(len(cut)):
                if cut[i] == ',':
                    empty = empty + ','
                else:
                    empty = empty + '0'
            other_half = problemsets[:inversed_under + 1]
            other_half = list(''.join(other_half))
            if int(str(other_half[-1])) != 9:
                other_half[-1] = str(int(str(other_half[-1])) + 1)
            else:
                other_half[-1] = str(0)
                # check for commas next
                if other_half[other_half.index('o') - 2] == 9 or other_half[other_half.index('o') - 2] == ',':
                    if other_half[other_half.index('o') - 3] == 9 or other_half[other_half.index('o') - 2] == ',':
                        if other_half[other_half.index('o') - 4] == 9 or other_half[other_half.index('o') - 2] == ',':
                            other_half[other_half.index('o') - 5] = str(int(other_half[other_half.index('o') - 4]) + 1)
                        else: 
                            other_half[other_half.index('o') - 4] = str(int(other_half[other_half.index('o') - 4]) + 1)
                    else:
                        other_half[other_half.index('o') - 3] = str(int(other_half[other_half.index('o')- 3]) + 1)
                else:
                    other_half[other_half.index('o') - 2] = str(int(other_half[other_half.index('o') - 2]) + 1)
            problemsets = ''.join(other_half) + empty
            pass_through = True
        else:
            cut = problemsets[inversed_under + 1:]
            for i in range(len(cut)):
                if cut[i] == ',':
                    empty = empty + ','
                else:
                    empty = empty + '0'
            other_half = problemsets[:inversed_under + 1]
            problemsets = other_half + ''.join(empty)
            pass_through = True
    return(problemsets)


def Rounding_Number_Section_3(option_difficulty=1 ,expr='latex', localmin=0, localmax=0):
    problemsets = ""
    temp_problem = []
    temp = ""

    if(localmin == localmax):
        if(option_difficulty == 1):
            problemsets = "0." + str(random.randint(1000, 8999))
        elif(option_difficulty == 2):
            problemsets = "0." + str(random.randint(1000, 89999))
        elif(option_difficulty == 3):
            problemsets = "0." + str(random.randint(10000, 899999))
    else:
        problemsets = "0." + str(random.randint(localmin, localmax))
    
    
    problemsets = list(str(problemsets))
    temp_problem = ''.join(problemsets)
    temp_problem, temp = insert_overline3(temp_problem)
    problemsets = str(temp_problem)
    temp_problem = rounding(temp_problem, temp)
    temp_problem = temp_problem[:temp_problem.rfind("e") + 2]
    if expr == 'latex':
        return(latexify(problemsets), latexify(temp_problem))
    else:
        return(problemsets, temp_problem) 