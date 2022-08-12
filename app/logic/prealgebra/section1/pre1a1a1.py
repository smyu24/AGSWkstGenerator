import random
import math

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

def decimals_generator(option_difficulty, option_min, option_max):
    if(option_min == option_max):
        if option_difficulty == 1: 
            integer_only = random.randint(1, 999)
            decimal = random.random()
            if integer_only % 2 == 0: 
                problem = "{:.1f}".format(integer_only + float(decimal))
            else:
                problem = "{:.2f}".format(integer_only + float(decimal))

        elif option_difficulty == 2:
            integer_only = random.randint(9, 9999)
            decimal = random.random()
            decimal_2 = "{:.2f}".format(decimal)
            if integer_only % 2 == 0:
                problem  = "{:.1f}".format(integer_only + float(decimal))
            else:
                problem = "{:.2f}".format(integer_only + float(decimal))

        elif option_difficulty == 3:
            integer_only = random.randint(99, 99999999)
            decimal = random.random()
            if integer_only % 2 == 0:
                problem = "{:.2f}".format(integer_only + float(decimal))
            else:
                problem = "{:.3f}".format(integer_only + float(decimal))
    else:
        integer_only = random.randint(option_min, option_max)
        decimal = random.random()
        if integer_only % 2 == 0:
            problem = "{:.2f}".format(integer_only + float(decimal))
        else:
            problem = "{:.3f}".format(integer_only + float(decimal))

    return(reg_truncate(problem))

def whole_generator(option_difficulty, option_min, option_max):
    temp_problem = []
    after_comma = []

    if(option_min == option_max):
        if option_difficulty == 1:
            problemsets = random.randint(1, 999)
        elif option_difficulty == 2:
            problemsets = random.randint(1000, 999999)
        elif option_difficulty == 3:
            problemsets = random.randint(999999, 999999999)
    else:
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
