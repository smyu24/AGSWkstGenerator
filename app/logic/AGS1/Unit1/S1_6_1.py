# 1.6.1 Percent Change (part of prealg?) (DONE)

from fractions import Fraction
import random
"""A LOT FOF MODULE 8
1.6.1 Percent Change(part of prealg?)
11 % increase 1.11
40 % decrease 0.6"""

# First Section
def Percents_Fractions_Decimal_Conversion_1(difficulty= 1, expr="latex"):
    problemsets = []
    answerset = []
    temp = 0
    list_temp = []

    if(difficulty == 1):        # Easy
        problemsets.append("0." + str(random.randint(1, 99)))

    elif(difficulty == 2):      # Medium
        problemsets.append(str(random.randint(1, 99)) +
                           "." + str(random.randint(1, 99)))

    elif(difficulty == 3):      # Hard
        problemsets.append(str(random.randint(-999, 999)) +
                           "." + str(random.randint(1, 999)))

    temp = round(float(str(problemsets[0])) * 100, 2)
    list_temp = list(str(temp))
    if int(list_temp[-1]) == 0:
        temp = int(temp)
    answerset.append(str(temp) + "%")

    return(answerset[0], problemsets[0])

# Second Section
def Percents_Fractions_Decimal_Conversion_2(difficulty = 1, option_random = "latex"):
    problemsets = []
    answerset = []
    temp = 0
    list_temp = []

    if(difficulty == 1):        # Easy
        problemsets.append("0." + str(random.randint(1, 99)))

    elif(difficulty == 2):      # Medium
        problemsets.append(str(random.randint(1, 20)) +
                           "." + str(random.randint(1, 99)))

    elif(difficulty == 3):      # Hard
        problemsets.append(str(random.randint(1, 999)) +
                           "." + str(random.randint(1, 999)))

    temp = round(float(str(problemsets[0])) * 100, 2)
    list_temp = list(str(temp))
    if int(list_temp[-1]) == 0:
        temp = int(temp)
    answerset.append(str(temp) + "%")
    return(problemsets[0], answerset[0])


# Third Section NEED ALTERNATE TO FRACTION
def Percents_Fractions_Decimal_Conversion_3(difficulty=1, option_random="latex"):
    problemsets_1 = []
    problemsets_2 = []
    answerset = []
    temp = 0
    list_temp = []
    percent = 0
    replace = ""
    holder = 0

    if(difficulty == 1):        # Easy
        problemsets_2.append("0." + str(random.randint(1, 99)))

    elif(difficulty == 2):      # Medium
        problemsets_2.append("0." + str(random.randint(1, 999)))

    elif(difficulty == 3):      # Hard
        problemsets_2.append("0." + str(random.randint(1, 9999)))

    temp = round(float(str(problemsets_2[0])) * 100, 2)

    list_temp = list(str(temp))
    if int(list_temp[-1]) == 0:
        temp = int(temp)
    problemsets_1.append(str(temp) + "%")

    percent = Fraction(problemsets_2[0])
    percent = str(percent)
    percent.replace("Fraction(", '')
    percent.replace(")", '')
    answerset.append(percent)
    return(problemsets_1[0], answerset[0])


# Fourth Section
def Percents_Fractions_Decimal_Conversion_4(difficulty = 1, option_random="latex"):
    problemsets_1 = []
    problemsets_2 = []
    answerset = []
    temp = 0
    list_temp = []
    percent = 0
    replace = ""
    holder = 0

    if(difficulty == 1):        # Easy
        problemsets_2.append("0." + str(random.randint(1, 99)))

    elif(difficulty == 2):      # Medium
        problemsets_2.append("0." + str(random.randint(1, 999)))

    elif(difficulty == 3):      # Hard
        problemsets_2.append("0." + str(random.randint(1, 9999)))

    temp = round(float(str(problemsets_2[0])) * 100, 2)

    list_temp = list(str(temp))
    if int(list_temp[-1]) == 0:
        temp = int(temp)
    problemsets_1.append(str(temp) + "%")

    percent = Fraction(problemsets_2[0])
    percent = str(percent)
    percent.replace("Fraction(", '')
    percent.replace(")", '')
    answerset.append(percent)
    return(answerset[0], problemsets_1[0])

def percentify(num):
    if str(float(num))[-2:] == ".0":
        num = int(num)
    return(str(num) + "%")


def inc_dec_formatter(num, choice):
    num = str(num)
    if choice == True:
        return(num + " Increase")
    elif choice == False:
        return(num + " Decrease")

measurements = ["miles", "grams", "ft", "minutes", "seconds",
                "meters", "kilos", "dollars", "liters", "tons"]
pick = [True, False]
def Finding_Percent_Change_Section_1(difficulty=1, expr='latex'):
    problem = ""
    answer = 0
    type = ""

    intA = random.randint(1, 100)
    intB = random.randint(1, 200)
    floatA = float(str(random.randint(1, 99)) +
                   "." + str(random.randint(1, 9)))
    floatB = float(str(random.randint(1, 199)) +
                   "." + str(random.randint(1, 9)))

    chosen = random.choice(pick)
    if difficulty == 1:  # From 82 to 38
        type = False
        problem = "From " + str(intA) + " to " + str(intB)
        answer = (intB - intA) / intA
        if intB >= intA:
            answer = answer + 1
            type = True
        else:
            answer = float(answer) * -1
        return(problem, inc_dec_formatter(percentify(round(100 * round(answer, 4), 2)), type))

    elif difficulty == 2:  # What percent of  81.88  is  122 ?
        if chosen == True:
            type = False
            problem = "From " + str(intA) + " to " + str(floatB)
            answer = (floatB - intA) / intA
            if floatB >= intA:
                answer = answer + 1
                type = True
            else:
                answer = float(answer) * -1
            return(problem, inc_dec_formatter(percentify(round(100 * round(answer, 4), 2)), type))
        else:
            type = False
            problem = "From " + str(floatB) + " to " + str(intB)
            answer = (intB - floatB) / floatB
            if intB >= floatB:
                answer = answer + 1
                type = True
            else:
                answer = float(answer) * -1
            return(problem, inc_dec_formatter(percentify(round(100 * round(answer, 4), 2)), type))

    elif difficulty == 3:  # 76% of what is 188.12 ? || 144.26  is  23%  of what?
        if chosen == True:
            type = False
            problem = "From " + str(floatA) + " to " + str(floatB)
            answer = (floatB - floatA) / floatA
            if floatB >= floatA:
                answer = answer + 1
                type = True
            else:
                answer = float(answer) * -1
            return(problem, inc_dec_formatter(percentify(round(100 * round(answer, 4), 2)), type))
        else:
            type = False
            problem = "From " + str(floatB) + " to " + str(floatA)
            answer = (floatA - floatB) / floatB
            if floatA >= floatB:
                answer = answer + 1
                type = True
            else:
                answer = float(answer) * -1
            return(problem, inc_dec_formatter(percentify(round(100 * round(answer, 4), 2)), type))


def Finding_Percent_Change_Section_2(difficulty=1, expr='latex'):
    problem = ""
    answer = 0
    type = ""
    measure = random.choice(measurements)

    intA = random.randint(1, 100)
    intB = random.randint(1, 200)
    floatA = float(str(random.randint(1, 99)) +
                   "." + str(random.randint(1, 9)))
    floatB = float(str(random.randint(1, 199)) +
                   "." + str(random.randint(1, 9)))

    chosen = random.choice(pick)
    if difficulty == 1:  # From 82 to 38
        type = False
        problem = "From " + str(intA) + " " + str(measure) + \
            " to " + str(intB) + " " + str(measure)
        answer = (intB - intA) / intA
        if intB >= intA:
            answer = answer + 1
            type = True
        else:
            answer = float(answer) * -1
        return(problem, inc_dec_formatter(percentify(round(100 * round(answer, 4), 2)), type))

    elif difficulty == 2:  # What percent of  81.88  is  122 ?
        if chosen == True:
            type = False
            problem = "From " + str(intA) + " " + str(measure) + \
                " to " + str(floatB) + " " + str(measure)
            answer = (floatB - intA) / intA
            if floatB >= intA:
                answer = answer + 1
                type = True
            else:
                answer = float(answer) * -1
            return(problem, inc_dec_formatter(percentify(round(100 * round(answer, 4), 2)), type))
        else:
            type = False
            problem = "From " + \
                str(floatB) + " " + str(measure) + \
                " to " + str(intB) + " " + str(measure)
            answer = (intB - floatB) / floatB
            if intB >= floatB:
                answer = answer + 1
                type = True
            else:
                answer = float(answer) * -1
            return(problem, inc_dec_formatter(percentify(round(100 * round(answer, 4), 2)), type))

    elif difficulty == 3:  # 76% of what is 188.12 ? || 144.26  is  23%  of what?
        if chosen == True:
            type = False
            problem = "From " + \
                str(floatA) + " " + str(measure) + " to " + \
                str(floatB) + " " + str(measure)
            answer = (floatB - floatA) / floatA
            if floatB >= floatA:
                answer = answer + 1
                type = True
            else:
                answer = float(answer) * -1
            return(problem, inc_dec_formatter(percentify(round(100 * round(answer, 4), 2)), type))
        else:
            type = False
            problem = "From " + \
                str(floatB) + " " + str(measure) + " to " + \
                str(floatA) + " " + str(measure)
            answer = (floatA - floatB) / floatB
            if floatA >= floatB:
                answer = answer + 1
                type = True
            else:
                answer = float(answer) * -1
            return(problem, inc_dec_formatter(percentify(round(100 * round(answer, 4), 2)), type))


def money_truncate(n):
    return("{:,.2f}".format(float(n)))


def money_formatter(sent):
    return("\$" + str(sent))


def percentify(sent):
    return str(sent) + "\%"

# COMBINE EASY AND HARD
def Markup_Discount_and_Tax(difficulty=1, expr='latex'):
    intA = random.randint(1, 90)
    intB = random.randint(1, 90)
    decimal = str(random.randint(1, 99))
    if int(decimal) < 10:
        decimal = "0"+str(decimal)
    floatA = str(random.randint(10, 99)) + "." + str(decimal)

    decimal_2 = str(random.randint(1, 99))
    if int(decimal_2) < 10:
        decimal_2 = "0"+str(decimal_2)
    floatB = str(random.randint(1000, 1999)) + "." + str(decimal_2)

    cheap_items = ["a CD", "a Vinyl CD", "a desk", "a game", "a book", "a keyboard", "a notebook", "a mouse", "a pack of batteries", "a bag of chips",
                   "a box of medicine", "a pair of earbuds", "a camera", "a movie ticket", 'a DVD', 'a comic book', 'an oil change', 'a pen', 'a book', 'a camera', 'an airpod']
    expensive_items = ['a computer', 'a macbook', 'a telescope',
                       'a camera', 'a snow board', 'concert tickets', 'a telescope']

    action_up = ['Mark up', 'Tax']
    action_down = ['Sale', 'Discount']

    answer = ""
    case = random.randint(1, 2)
    sentence = ""
    if difficulty == 1:     # Easy
        """Cost of [cheap_items] :  $  floatA
                [action_up] : intA %
                x = floatA *intA * 100
                Cost of a comic book: $$$ 99.95
                Markup : 95%
                Answer :  $194.03"""
        if case == 1:
            sentence = "The cost of " + str(random.choice(cheap_items)) + ": \$" + money_truncate(
                floatA) + r"\\" + str(random.choice(action_up)) + " : " + percentify(intA)
            answer = money_formatter(money_truncate(
                (float(floatA) * float("0." + str(intA))) + float(floatA)))

        else:
            sentence = "Cost of " + str(random.choice(cheap_items)) + ": \$" + money_truncate(
                floatA) + r"\\" + str(random.choice(action_down)) + " : " + percentify(intA)
            answer = money_formatter(money_truncate(
                float(floatA) - (float(floatA) * float("0." + str(intA)))))

    elif difficulty == 2:   # Medium
        """Cost of [items] :  $  floatA
                [action_down] : intA %
                x = floatA *(1-intA) * 100
                Cost of an oil change: $$$ 1237.51
                Discount : 18%
                Answer :  $1,014.76"""
        if case == 1:
            sentence = "The cost of " + str(random.choice(expensive_items)) + ": \$" + str(
                money_truncate(floatB)) + r"\\" + str(random.choice(action_up)) + " : " + percentify(intB)
            answer = money_formatter(money_truncate(
                (float(floatB) * float("0." + str(intB))) + float(floatB)))

        else:
            sentence = "Cost of " + str(random.choice(expensive_items)) + ": \$" + str(
                money_truncate(floatB)) + r"\\" + str(random.choice(action_down)) + " : " + percentify(intB)
            answer = money_formatter(money_truncate(
                float(floatB) - (float(floatB) * float("0." + str(intB)))))

    elif difficulty == 3:   # Hard
        """  - case 1
        - Cost of [cheap_items] : $\$$ floatA
        - [action_up] : intA %
        - [action_down] : intB %

        - case 2
        - Cost of [expensive_items] : $\$$ floatA
        - [action_up] : intA %
        - [action_down] : intB %"""
        if case == 1:
            sentence = "The cost of " + str(random.choice(cheap_items)) + ": \$" + str(money_truncate(floatA)) + r"\\" + str(
                random.choice(action_up)) + " : " + percentify(intA) + ", " + str(random.choice(action_down)) + " : " + percentify(intB)
            up = 0
            up = (float(floatA) * float("0." + str(intA))) + float(floatA)
            answer = money_formatter(money_truncate(
                float(up) - (float(up) * float("0." + str(intB)))))

        else:
            sentence = "The cost of " + str(random.choice(expensive_items)) + ": \$" + str(money_truncate(floatB)) + r"\\" + str(
                random.choice(action_down)) + " : " + percentify(intB) + ", " + str(random.choice(action_up)) + " : " + percentify(intA)
            down = 0
            down = float(floatB) - (float(floatB) * float("0." + str(intB)))
            answer = money_formatter(money_truncate(
                (float(down) * float("0." + str(intA))) + float(down)))

    return(sentence, answer)

def AGS_Percent_Change(difficulty = 1, expr = "latex"):
    return random.choice([Percents_Fractions_Decimal_Conversion_1(difficulty, expr), Percents_Fractions_Decimal_Conversion_2(difficulty, expr), Percents_Fractions_Decimal_Conversion_3(difficulty, expr), Percents_Fractions_Decimal_Conversion_4(difficulty, expr), Finding_Percent_Change_Section_1(difficulty, expr), Finding_Percent_Change_Section_2(difficulty, expr), Markup_Discount_and_Tax(difficulty, expr)])
a,b = AGS_Percent_Change(1, "latex")
print(a,b)