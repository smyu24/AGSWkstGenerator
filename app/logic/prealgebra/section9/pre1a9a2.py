import random

def fix_zero_neg(input):
    if int(input) == 0:
        return 0
    else:
        return input


def linear_graph_line_formatter(slope, integer):
    output = ""
    output = r'\LinearEquation`{a}~`{b}~'.format(a = slope, b = integer)
    output = output.replace("`", "{")
    output = output.replace("~", "}")
    return output


def Graphing_Lines_Slope_Intersect(option_difficulty="easy", expr="latex"):
    half_1 = ""
    half_2 = ""

    problem = ""
    answer = ""
    negative = ["", "-"]

    sym_1 = random.choice(["-", "+"])

    intA = fix_zero_neg(str(random.choice(negative)) + str(random.randint(2,10)))
    intB = fix_zero_neg(str(random.randint(1,10)))
    intC = fix_zero_neg(str(random.randint(1,10)))
    intD = fix_zero_neg(str(random.choice(negative)) + str(random.randint(1,10)))

    if option_difficulty == 1:
        half_1 = r'y'
        half_2 = fr'{intA} x {sym_1} {intB}'

        problem = str(half_1) + " = " + str(half_2)
        if sym_1 == "+":
            sym_1 = ""
        answer = str(linear_graph_line_formatter(intA, str(sym_1) + str(intB)))

    elif option_difficulty == 2:
        half_1 = r'y'
        half_2 = fr'\frac`{intA}~`{intB}~ x {sym_1} {intC}'

        half_2 = half_2.replace("`", "{")
        half_2 = half_2.replace("~", "}")

        problem = str(half_1) + " = " + str(half_2)
        if sym_1 == "+":
            sym_1 = ""

        answer = str(linear_graph_line_formatter(str(intA) + " / " + str(intB), str(sym_1) + str(intC)))

    elif option_difficulty == 3:
        if random.randint(1,2) == 1:
            half_1 = r'y'
            answer = "0"
        else:
            half_1 = r'x'
            answer = "Undefined"
        half_2 = fr'{intD}'


        problem = str(half_1) + " = " + str(half_2)
    return("$ " + str(problem) + " $", answer)
