# First Section

import math
import numbers
import random
import sympy as sp
import fractions

# from templates import *
def money_truncate(n):
    return("{:,.2f}".format(float(n)))


def reg_truncate(n):
    return(int(round(n, 3) * 1000) / 1000)


def money_formatter(sent):
    return("\$" + str(sent)) # \$ HHHHHHHHHHHHHEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRRRRREEEEEEEEE


def name_generator():
    name = ['James', 'Mary', 'Robert', 'Michael', 'Thomas', 'Christopher', 'Karen', 'Lisa', 'Susan', 'Elizabeth', 'Sandra', 'Ashley', 'Daniel', 'Anthony', 'Paul',
            'Sharon', 'Angela', 'Debra', 'Kelly', 'Joan', 'Kyle', 'Peter', 'Walter', 'Henry', 'Adam', 'Jack', 'Megan', 'Ann', 'Bryan', 'Logan', 'Beverly', 'Amber', 'Russell']
    return(random.choice(name))


def day_generator():
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
            'Saturday', 'Sunday', 'week']  # maybe add week? maybe mult weeks
    return(random.choice(days))


def number_generator(lower, upper):
    return(random.randint(lower, upper))


def dollar_generator():
    money = ''
    decimal = str(random.randint(1, 99))
    if int(decimal) < 10:
        decimal = "0" + str(decimal)

    money = str(random.randint(5, 50)) + "." + str(decimal)
    return(str("{:,.2f}".format(float(money))))


def fraction_generator():
    problem = ""
    numerator = 4
    denominator = 4
    while float(numerator / denominator) >= 1:
        numerator = random.randint(1, 4)
        denominator = random.randint(2, 5)
        problem = fractions.Fraction(numerator, denominator)
    return(problem)


def decimal_generator():
    return("0." + str(random.randint(1, 90)))


def variable_generator():
    choices = ['x', 'y', 'g', 'b', 'z', 'p', 't',
        'q', 'k', 'u', 'r', 'd', 'w', 's', 'h', 'v']
    return(random.choice(choices))


def bigger_num_generator(a):
    return(random.randint(int(a) + 1, int(a) + 21))


def word_fractions():
    avail = [["one half", 1/2], ["one third", 1/3], ["one fourth", 1/4], ["two thirds", 2/3], ["two fourths", 2/4],
        ["three fourths", 3/4], ["one sixth", 1/6], ["one eighth", 1/8], ["one tenth", 1/10], ["two tenths", 2/10], ["three fifth", 3/5]]
    return(random.choice(avail))


Description = [["At a restaurant, NAME_1 and his NUMBER_1 friends decided to split the bill evenly. If each person paid DOLLAR_1 then what was the total bill?", ["NAME_1", "NUMBER_1", "DOLLAR_1"], "DOLLAR_1 * (NUMBER_1 + 1)", True],
               ["Last DAYS_1 NAME_1 ran NUMBER_1 miles less than NAME_2. NAME_1 ran NUMBER_2 miles. How many miles did NAME_2 run?", [
                   "DAYS_1", "NAME_1", "NUMBER_1", "NAME_2", "NUMBER_2"], "NUMBER_2 + NUMBER_1", False],
               ["NAME_1 and their best friend found some money buried in a field. They split the money, each getting DOLLAR_1. How much money did they find?", [
                   "NAME_1", "DOLLAR_1"], "DOLLAR_1 * 2", True],
               ["Last DAYS_1, NAME_1 had DOLLAR_1. Over the weekend, he received some money for cleaning the house. He now has DOLLAR_SUM. How much money did he receive?", [
                   "DAYS_1", "NAME_1", "DOLLAR_1", "DOLLAR_2", "DOLLAR_SUM"], "DOLLAR_SUM - DOLLAR_1", True],
               ["After paying DOLLAR_1 for a salad, NAME_1 has DOLLAR_2. How much money did he have before buying the salad?", [
                   "NAME_1", "DOLLAR_1", "DOLLAR_2"], "DOLLAR_2 + DOLLAR_1", True],
               ["Your mother gave you DOLLAR_1 with which to buy a book. This covered FRACTION_1 of the cost. How much did the book cost?", [
                   "DOLLAR_1", "FRACTION_1"], "DOLLAR_1 / (FRACTION_1)", True],
               ["If the weight of a package is multiplied by NUMBER_1 the result is NUMBER_2 pounds. Find the weight of the package.", [
                   "NUMBER_1", "NUMBER_2"], "NUMBER_2 / NUMBER_1", False],
               ["A stray dog ate NUMBER_1 of your muffins. That was FRACTION_1 of all of them. How many did you start with?", [
                   "NUMBER_1", "FRACTION_1"], "NUMBER_1 / (FRACTION_1)", False],
               ["NAME_1’s NUMBER_1 buckets contain an equal amount of kilograms. If there is a total of NUMBER_2 kilograms, how many kilograms are in each bucket?", ["NAME_1", "NUMBER_1", "NUMBER_2"], "NUMBER_2 / NUMBER_1", False],
               ["NAME_1 went to the store and bought 5 sweatshirts. He spent DOLLAR_1. What was the price of each shirt?", ["NAME_1", "DOLLAR_1"], "DOLLAR_1 / 5", True],
               ["Last DAYS_1, NAME_1 had DOLLAR_1. For her birthday she received more money. She now has DOLLAR_SUM. How much money did she receive?", ["NAME_1", "DAYS_1", "DOLLAR_1", "DOLLAR_SUM"], "DOLLAR_SUM - DOLLAR_1", True]]


def generate_description(b):
    variables = b[1]
    names = 1
    days = 1
    number = 1
    dollar = 1
    fraction = 1
    dollar_sum = 0
    holder = 0
    for i in range(len(variables)):
        ada = str(variables[i])
        if ada[:-2] == "NAME":
            b[0] = b[0].replace("NAME_" + str(names), name_generator())
            names = names + 1

        elif ada[:-2] == "DAYS":
            b[0] = b[0].replace("DAYS_" + str(days), day_generator())
            days = days + 1

        elif ada[:-2] == "NUMBER":
            holder = number_generator(2, 20)
            b[0] = b[0].replace("NUMBER_" + str(number), str(holder))
            b[2] = b[2].replace("NUMBER_" + str(number), str(holder))
            number = number + 1

        elif ada[:-2] == "DOLLAR":
            holder = dollar_generator()
            dollar_sum = float(holder) + dollar_sum
            b[0] = b[0].replace("DOLLAR_" + str(dollar),
                                money_formatter(holder))
            b[2] = b[2].replace("DOLLAR_" + str(dollar), holder)
            dollar = dollar + 1

        elif ada == "DOLLAR_SUM":
            dollar_sum = money_truncate(dollar_sum)
            holder = money_formatter(dollar_sum)
            b[0] = b[0].replace("DOLLAR_SUM", str(holder))
            b[2] = b[2].replace("DOLLAR_SUM", str(dollar_sum))

        elif ada[:-2] == "FRACTION":
            if random.randint(1, 2) == 1:  # FRACTION PATH
                holder = fraction_generator()
                # EITHER FRACTION OR DECIMAL
                b[0] = b[0].replace("FRACTION_" + str(fraction), str(holder))
                # has to be decimal (truncated)
                b[2] = b[2].replace("FRACTION_" + str(fraction), str(holder))
                fraction = fraction + 1
            else:  # DECIMAL PATH
                holder = decimal_generator()
                # EITHER FRACTION OR DECIMAL
                b[0] = b[0].replace("FRACTION_" + str(fraction), str(holder))
                # has to be decimal (truncated)
                b[2] = b[2].replace("FRACTION_" + str(fraction), str(holder))
                fraction = fraction + 1

    if b[3] == True:
        return(b[0], money_formatter(money_truncate(sp.sympify(b[2]))))
    else:
        return(b[0], reg_truncate(sp.sympify(b[2])))

# DAYS WILL BE TAKEN FROM LIST DAYS; NAME WILL BE TAKEN FROM LIST NAME; NUMBER WILL BE GENERATED; DOLLAR WILL BE GENERATED, THEN FORMATTED WITH DOLLAR SIGN AND DECIMAL POINTS
# could change objects in the sentence by changing them straigt from the string (list)

# FIRST ONE IS THE QUESTION; SECOND ONE IS THE LIST OF ALL VARIABLES; THIRD ONE IS THE EQUATION; FOURTH ONE IS THE BOOLEAN (MONEY OR NOT)

Pure = [["The sum of NUMBER_1 and VARIABLE_1 is GREATER_1. What is VARIABLE_1?", ["NUMBER_1", "VARIABLE_1", "GREATER_1"], "GREATER_1 - NUMBER_1"],
        ["What is the sum of NUMBER_1 and NUMBER_2", [
            "NUMBER_1", "NUMBER_2"], "NUMBER_1 + NUMBER_2"],
        ["The product of VARIABLE_1 and NUMBER_1 is NUMBER_2. What is VARIABLE_1?", [
            "VARIABLE_1", "NUMBER_1", "NUMBER_2"], "NUMBER_2 / NUMBER_1"],
        ["The difference of NUMBER_1 and VARIABLE_1 is GREATER_1. What is VARIABLE_1?", [
            "NUMBER_1", "VARIABLE_1", "GREATER_1"], "GREATER_1 + NUMBER_1"],
        ["What is the difference of NUMBER_1 and NUMBER_2", [
            "NUMBER_1", "NUMBER_2"], "NUMBER_1 - NUMBER_2"],
        ["The quotient of VARIABLE_1 and NUMBER_1 is NUMBER_2. What is VARIABLE_1?", [
            "VARIABLE_1", "NUMBER_1", "NUMBER_2"], "NUMBER_2 * NUMBER_1"],
        ["NUMBER_1 times a number equals GREATER_1. What is the number?",
            ["NUMBER_1", "GREATER_1"], "GREATER_1 / NUMBER_1"],
        ["What number minus WORDFRAC_1 is equal to negative WORDFRAC_2?",
            ["WORDFRAC_1", "WORDFRAC_2"], "- WORDFRAC_2 + WORDFRAC_1"],
        ["What number plus WORDFRAC_1 is equal to negative WORDFRAC_2?",
            ["WORDFRAC_1", "WORDFRAC_2"], "- WORDFRAC_2 - WORDFRAC_1"],
        ["What number is WORDFRAC_1 of NUMBER_1?", [
            "WORDFRAC_1", "NUMBER_1"], "NUMBER_1 * WORDFRAC_1"],
        ["What's NUMBER_1\% of NUMBER_2.", ["NUMBER_1",
            "NUMBER_2"], "NUMBER_2 * (NUMBER_1 / 100)"],
        ["NUMBER_1 is NUMBER_2\% of what number?", [
            "NUMBER_1", "NUMBER_2"], "NUMBER_1 / (NUMBER_2 / 100)"],
        ["NUMBER_1\% of the number is GREATER_1. Find the number.", [
            "NUMBER_1", "GREATER_1"], "GREATER_1 / (NUMBER_1 / 100)"],
        ["If GREATER_1 : NUMBER_1 = VARIABLE_1 : NUMBER_2, what's the value of VARIABLE_1?", [
            "VARIABLE_1", "NUMBER_1", "NUMBER_2", "GREATER_1"], "(GREATER_1 / NUMBER_1) * NUMBER_2"],
        ["Given that GREATER_1 : NUMBER_1 = VARIABLE_1 : NUMBER_2,find the value of VARIABLE_1", [
            "VARIABLE_1", "NUMBER_1", "NUMBER_2", "GREATER_1"], "(GREATER_1 / NUMBER_1) * NUMBER_2"],
        ["If NUMBER_1\% of a number VARIABLE_1 is GREATER_1. Find the value of VARIABLE_1.", [
            "VARIABLE_1", "NUMBER_1", "GREATER_1"], "GREATER_1 / (NUMBER_1 / 100)"],
        ["I have the number GREATER_1 and the number NUMBER_1. I need to figure out what percentage NUMBER_1 is of GREATER_1.", [
            "NUMBER_1", "GREATER_1"], "NUMBER_1 / GREATER_1"]
        ]


def generate_pure(b):
    variables = b[1]
    variable = 1
    B_NUMBER = 0
    number = 1
    holder = 0
    word_fraction = 1
    for i in range(len(variables)):
        ada = str(variables[i])
        if ada[:-2] == "VARIABLE":
            b[0] = b[0].replace("VARIABLE_" + str(variable),
                                variable_generator())
            variable = variable + 1

        elif ada[:-2] == "GREATER":
            holder = bigger_num_generator(B_NUMBER)
            b[0] = b[0].replace("GREATER_1", str(holder))
            b[2] = b[2].replace("GREATER_1", str(holder))

        elif ada[:-2] == "NUMBER":
            holder = number_generator(2, 20)
            b[0] = b[0].replace("NUMBER_" + str(number), str(holder))
            b[2] = b[2].replace("NUMBER_" + str(number), str(holder))
            B_NUMBER = B_NUMBER + holder
            number = number + 1

        elif ada[:-2] == "WORDFRAC":
            holder = word_fractions()
            b[0] = b[0].replace(
                "WORDFRAC_" + str(word_fraction), str(holder[0]))
            b[2] = b[2].replace(
                "WORDFRAC_" + str(word_fraction), str(holder[1]))
            word_fraction = word_fraction + 1

    return(b[0], reg_truncate(sp.sympify(b[2])))


problems = [
    ["You and NUMBER_1 friends go to Johnny Rockets. You all split the bill equally. Each person’s share was DOLLAR_1. How much was the original bill? ", ["NUMBER_1", "DOLLAR_1"], "DOLLAR_1 * ( 1 + NUMBER_1 )", True],
    ["NAME_1 and their best friend found some money buried in a field. They split the money, each getting DOLLAR_1. How much money did they find?", ["NAME_1", "DOLLAR_1"], "DOLLAR_1 * 2", True],
    ["The cost for NUMBER_1 months of Napster is DOLLAR_1. What about how much is the cost for one month?", ["NUMBER_1", "DOLLAR_1"], "DOLLAR_1 / NUMBER_1", True],
    ["El Rodeo School has NUMBER_1 students. Hawthorne has NUMBER_2 more students than El Rodeo School. How many students are there at Hawthorne School?", ["NUMBER_1", "NUMBER_2"], "NUMBER_1 + NUMBER_2", False],
    ["From the first quiz to the second quiz, a score dropped NUMBER_1 points. The score on the second quiz was NUMBER_2. What was the first quiz score? ", ["NUMBER_1", "NUMBER_2"], "NUMBER_2 + NUMBER_1", False],
    ["A menu item from Mulberry St. is cut into NUMBER_1 equal pieces. Sold individually, each slice cost DOLLAR_1. What is the cost of the entire item at this rate?", ["NUMBER_1", "DOLLAR_1"], "NUMBER_1 * DOLLAR_1", True],
    ["At Costco, NUMBER_1 cans of Coke cost a total of DOLLAR_1. What is the cost per can? ", ["NUMBER_1", "DOLLAR_1"], "DOLLAR_1 / NUMBER_1", True],
    ["NAME_1 Loblaw is on a diet to lose weight. After losing NUMBER_1 pounds, NAME_1 weighs NUMBER_2 pounds. What was NAME_1 Loblaw’s weight before their diet?", ["NAME_1", "NUMBER_1", "NUMBER_2"], "NUMBER_1 + NUMBER_2", False],
    ["You need the weight of your dog. On the scale together, you both weigh a total of GREATER_1 pounds. After putting the dog down, your weight is NUMBER_1 pounds. What is the weight of the dog?", ["NUMBER_1", "GREATER_1"], "GREATER_1 - NUMBER_1", False],
    ["The temperature rose NUMBER_1 degrees to GREATER_1 F. What was the original temperature?", ["NUMBER_1", "GREATER_1"], "GREATER_1 - NUMBER_1", False],
    ["Griffith Park is GREATER_1 acres larger than Eagle Creek Park. If Griffith Park is NUMBER_1 acres, find the size of Eagle Creek Park.", ["NUMBER_1", "GREATER_1"], "GREATER_1 + NUMBER_1", False],
    ["Eagle Creek Park is NUMBER_1 acres smaller than Griffith Park. If Eagle Creek Park is GREATER_1 acres, find the size of Griffith Park.", ["NUMBER_1", "GREATER_1"], "GREATER_1 - NUMBER_1", False],
    ["After a withdrawal of DOLLAR_1, you have a checking account balance of DOLLAR_2 . What was the original balance? ", ["DOLLAR_1", "DOLLAR_2"], "DOLLAR_1 + DOLLAR_2", True],
    ["A large pile of books is divided into NUMBER_1 equal size stacks. Each stack has NUMBER_2 books. How many books were in the original pile? ", ["NUMBER_1", "NUMBER_2"], " NUMBER_1 * NUMBER_2", False],
    ["Each household in the United States receives about NUMBER_1 pieces of junk mail per year. Since there are 52 weeks in a year, about how many pieces are received each week? ", ["NUMBER_1"], "NUMBER_1 * 52 ", False],
    ["NAME_1 Kahne completed one lap of the NASCAR race in NUMBER_1 seconds. This was NUMBER_2 seconds faster than NAME_2 Johnson. What as NAME_2 Johnson’s lap time? ", ["NAME_1", "NAME_2", "NUMBER_1", "NUMBER_2"], "NUMBER_1 + NUMBER_2", False],
    ["The area of a rectangle is GREATER_1 cm squared. If the width is NUMBER_1 cm, find the length.", ["NUMBER_1", "GREATER_1"],"GREATER_1 / NUMBER_1", False],
    ["A deck of playing cards were dealt equally among NUMBER_1 players. Each player received NUMBER_2 cards. How many cards are in a deck? ", ["NUMBER_1", "NUMBER_2"], " NUMBER_1 * NUMBER_2", False],
    ["NAME_1 is cooking muffins. The recipe calls for GREATER_1 cups of sugar. She has already put in NUMBER_1 cups. How many more cups do they need to put in?", ["NAME_1", "NUMBER_1","GREATER_1"], "GREATER_1 - NUMBER_1", False]]

def generate_problem(b):
    variables= b[1]
    B_NUMBER= 0
    number= 1
    holder= 0
    names = 1
    days = 1
    dollar = 1
    fraction = 1
    dollar_sum = 0
    for i in range(len(variables)):
        ada = str(variables[i])
        if ada[:-2] == "NAME":
            b[0] = b[0].replace("NAME_" + str(names), name_generator())
            names = names + 1

        elif ada[:-2] == "DAYS":
            b[0] = b[0].replace("DAYS_" + str(days), day_generator())
            days = days + 1

        elif ada[:-2] == "NUMBER":
            holder = number_generator(2, 20)
            b[0] = b[0].replace("NUMBER_" + str(number), str(holder))
            b[2] = b[2].replace("NUMBER_" + str(number), str(holder))
            number = number + 1
            B_NUMBER = B_NUMBER + holder

        elif ada[:-2] == "DOLLAR":
            holder = dollar_generator()
            dollar_sum = float(holder) + dollar_sum
            b[0] = b[0].replace("DOLLAR_" + str(dollar),
                                money_formatter(holder))
            b[2] = b[2].replace("DOLLAR_" + str(dollar), holder)
            dollar = dollar + 1

        elif ada == "DOLLAR_SUM":
            dollar_sum = money_truncate(dollar_sum)
            holder = money_formatter(dollar_sum)
            b[0] = b[0].replace("DOLLAR_SUM", str(holder))
            b[2] = b[2].replace("DOLLAR_SUM", str(dollar_sum))

        elif ada[:-2] == "FRACTION":
            if random.randint(1, 2) == 1:  # FRACTION PATH
                holder = fraction_generator()
                # EITHER FRACTION OR DECIMAL
                b[0] = b[0].replace("FRACTION_" + str(fraction), str(holder))
                # has to be decimal (truncated)
                b[2] = b[2].replace("FRACTION_" + str(fraction), str(holder))
                fraction = fraction + 1
            else:  # DECIMAL PATH
                holder = decimal_generator()
                # EITHER FRACTION OR DECIMAL
                b[0] = b[0].replace("FRACTION_" + str(fraction), str(holder))
                # has to be decimal (truncated)
                b[2] = b[2].replace("FRACTION_" + str(fraction), str(holder))
                fraction = fraction + 1

        elif ada[: -2] == "GREATER":
            holder= bigger_num_generator(B_NUMBER)
            b[0]= b[0].replace("GREATER_1", str(holder))
            b[2]= b[2].replace("GREATER_1", str(holder))

    if b[3] == True:
        return(b[0], money_formatter(money_truncate(sp.sympify(b[2]))))
    else:
        return(b[0], reg_truncate(sp.sympify(b[2])))

def One_step_Word_Problems_1(option_difficulty, option_random):
    problemsets= []
    answerset= []
    all_expressions= ['+', '-', '*', '/']
    addition_expression= ['+', '-']
    mult_expression= ['*', '/']
    case= [1, 2, 3]
    negative= ['-', '']
    temp= random.choice(case)
    variables= []

    starting = [ Pure, Description, problems ] 
    # places is (Steven went to the store and bought five sweatshirts. He spent $45. What was the price of each shirt?).
    # Pick a place from a list, then something in relation to that place (hint, should do a list with two values ['store', 'shirt'])
    #
    # object is (How many boxes of envelopes can you buy with $12, if one box costs $3?).
    #
    # description is (Allie's dad has asked Allie and her little brothers to rake the leaves in their yard.
    # They rake all afternoon and fill a number of bags with leaves. Then, when Allie isn't looking, her brothers empty 5 of the bags to
    # make a giant leaf pile! Allie is frustrated that only 7 bags of leaves remain.)
    # which equation can you use to find the total number of bags b that Allie and her brothers fill with leaves?
    #
    # (At a restaurant, Bill and his four friends decided to divide the bill evenly. If each person paid $12, what was the total bill?)
    #
    # situation is (Last Saturday, Allyson had $38. For her birthday she received more money. She now has $90. How much money did she receive?).
    #
    # Find and enter equations (might be second section?!?!) https://i.pinimg.com/originals/cd/4e/33/cd4e339b764a4635dcac55a901011789.jpg
    b = random.choice(starting)

    if b == Pure:
        return(generate_pure(random.choice(b)))
    elif b == Description:
        return(generate_description(random.choice(b)))
    elif b == problems:
        return(generate_problem(random.choice(b)))
