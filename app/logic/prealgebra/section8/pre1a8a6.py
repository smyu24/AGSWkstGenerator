# First Section
import math
import random

def formatter(money, percent, year):
    return "Find the interest on a loan of "+ money_formatter(money_truncate(money)) + " that is borrowed at " + str(percent) + " for " + str(year) + " years."
# $34,100 at 4% for 3 years


def money_truncate(n):
    return("{:,.2f}".format(float(n)))


def money_formatter(sent):
    if str(sent)[-3:] == ".00":
        sent = str(sent)[:-3]
    return("\$" + str(sent))


def percentify(num):
    if str(float(num))[-2:] == ".0":
        num = int(num)
    return(str(num) + "\%")


def percent_generate_easy(): # no decimal
    return(percentify(random.randint(1, 15)))


def years_generate_easy():
    return(random.randint(1,10))


def money_easy():
    number = "000000"
    number = list(number)
    n = random.randint(2,4)
    number[random.randint(0,4)] = str(random.randint(1,9))
    if n == 4:
        number[random.randint(0,4)] = str(random.randint(1,9))
        number[random.randint(0,4)] = str(random.randint(1,9))
        number[random.randint(0,4)] = str(random.randint(1,9))
    elif n == 3:
        number[random.randint(0,4)] = str(random.randint(1,9))
        number[random.randint(0,4)] = str(random.randint(1,9))
    elif n == 2:
        number[random.randint(0,4)] = str(random.randint(1,9))
    return ''.join(number)


def Simple_And_Compound_Interest_Section_1(option_difficulty='easy', expr="latex"):
    problem = ""
    answer = ""
    money = ""
    percent = ""
    years = ""
    if option_difficulty == 1: # artificial random money gen
        money = str(money_easy())
        percent = str(percent_generate_easy())
        years = str(years_generate_easy())
        # Find the interest on a loan of $2500 that is borrowed at 9% for 7 months.
        problem = formatter(money, percent, years)
        answer = int(money) * (1 + ((int(percent[:-2]) / 100) * int(years)))
        answer = money_formatter(money_truncate(answer))

    elif option_difficulty == 2: # real random money gen
        money = str(random.randint(1000, 99999))
        percent = str(percent_generate_easy())
        years = str(years_generate_easy())
        # Find the interest on a loan of $2500 that is borrowed at 9% for 7 months.
        problem = formatter(money, percent, years)
        answer = int(money) * (1 + ((int(percent[:-2]) / 100) * int(years)))
        answer = money_formatter(money_truncate(answer))

    elif option_difficulty == 3:
        decimal = ["0.5", "0.25", "0.75", "0.128", "0.375", "0.05", "	0.8", "	0.9", "0.1", "0.4", "0.7", "0.6", "0.2", "0.3"]
        money = str(random.randint(1000, 99999))
        percent = str(percent_generate_easy())
        years = round(float(years_generate_easy()) + float(random.choice(decimal)), 3)
        # Find the interest on a loan of $2500 that is borrowed at 9% for 7 months.
        problem = formatter(money, percent, years)
        answer = int(money) * (1 + ((int(percent[:-2]) / 100) * float(years)))
        answer = money_formatter(money_truncate(answer))

    return problem, answer

def formatter_compound(money, percent, year, rate):
    return "If "+ money_formatter(money_truncate(money)) + " is compounded " + str(rate) + " at a rate of " + str(percent) + " for " + str(year) + " years."
# $7,300 at 7% compounded semiannually for 3 years

def money_formatter2(sent):
    if str(sent)[-3:] == ".00":
        sent = str(sent)[:-3]
    return("\$" + str(sent))

def Simple_And_Compound_Interest_Section_2(option_difficulty='easy', expr="latex"):
    problem = ""
    answer = ""
    money = ""
    percent = ""
    years = ""
    rate = ""
    rate = random.choice([["semiannually", 2], ["annually", 1], ["quarterly", 4], ["biannually", 2], ["trimonthly", 3], ["weekly", 52], ["bi-weekly", 26], ["daily", 365], ["monthly", 12], ["bi-monthly", 24]])
    if option_difficulty == 1: # artificial random money gen
        money = str(money_easy())
        percent = str(percent_generate_easy())
        years = str(years_generate_easy())
        problem = formatter_compound(money, percent, years, rate[0])
        answer = int(money) * (1 + ((int(percent[:-2]) / 100) / int(rate[1]))) ** (int(rate[1]) * int(years))  #A = P(1 + \frac{r}{n})^{nt}
        answer = money_formatter2(money_truncate(answer))

    elif option_difficulty == 2: # real random money gen
        money = str(random.randint(1000, 99999))
        percent = str(percent_generate_easy())
        years = str(years_generate_easy())
        problem = formatter_compound(money, percent, years, rate[0])
        answer = int(money) * (1 + ((int(percent[:-2]) / 100) / int(rate[1]))) ** (int(rate[1]) * int(years))  #A = P(1 + \frac{r}{n})^{nt}
        answer = money_formatter2(money_truncate(answer))

    elif option_difficulty == 3:
        decimal = ["0.5", "0.25", "0.75", "0.128", "0.375", "0.05", "	0.8", "	0.9", "0.1", "0.4", "0.7", "0.6", "0.2", "0.3"]
        money = str(random.randint(1000, 99999))
        percent = str(percent_generate_easy())
        years = round(float(years_generate_easy()) + float(random.choice(decimal)), 4)
        problem = formatter_compound(money, percent, years, rate[0])
        answer = int(money) * (1 + ((int(percent[:-2]) / 100) / int(rate[1]))) ** (int(rate[1]) * float(years))  #A = P(1 + \frac{r}{n})^{nt}
        answer = money_formatter2(money_truncate(answer))

    return problem, answer