import random

def money_truncate(n):
    return("{:,.2f}".format(float(n)))

def money_formatter(sent):
    return("\$" + str(sent))

def percentify(sent):
    return str(sent) + "\\%"


def Markup_Discount_and_Tax(option_difficulty = 'easy', expr = 'latex'): # COMBINE EASY AND HARD
    intA = random.randint(1,90)
    intB = random.randint(1,90)
    decimal = str(random.randint(1,99))
    if int(decimal) < 10:
        decimal = "0"+str(decimal)
    floatA = str(random.randint(10, 99)) + "." + str(decimal)
    
    decimal_2 = str(random.randint(1,99))
    if int(decimal_2) < 10:
        decimal_2 = "0"+str(decimal_2)
    floatB = str(random.randint(1000, 1999)) + "." + str(decimal_2)

    cheap_items = ["a CD", "a Vinyl CD", "a desk", "a game", "a book", "a keyboard", "a notebook", "a mouse", "a pack of batteries", "a bag of chips", "a box of medicine", "a pair of earbuds", "a camera", "a movie ticket", 'a DVD' , 'a comic book', 'an oil change', 'a pen', 'a book','a camera','an airpod']
    expensive_items = ['a computer' , 'a macbook' ,'a telescope','a camera','a snow board', 'concert tickets', 'a telescope']

    action_up = ['Mark up', 'Tax']
    action_down = ['Sale', 'Discount']
    
    answer = ""
    case = random.randint(1,2)
    sentence = ""
    if option_difficulty == 1:
        """Cost of [cheap_items] :  $  floatA
                [action_up] : intA %
                x = floatA *intA * 100
                Cost of a comic book: $$$ 99.95
                Markup : 95%
                Answer :  $194.03"""
        if case == 1:
            sentence = "The cost of " + str(random.choice(cheap_items)) + ": \$" + money_truncate(floatA) + r"\\" + str(random.choice(action_up)) + " : " + percentify(intA)
            answer = money_formatter(money_truncate((float(floatA) * float("0." + str(intA))) + float(floatA)))

        else:
            sentence = "Cost of " + str(random.choice(cheap_items)) + ": \$" + money_truncate(floatA) + r"\\" + str(random.choice(action_down)) + " : " + percentify(intA)
            answer = money_formatter(money_truncate(float(floatA) - (float(floatA) * float("0." + str(intA)))))
   
    elif option_difficulty == 2:
        """Cost of [items] :  $  floatA
                [action_down] : intA %
                x = floatA *(1-intA) * 100
                Cost of an oil change: $$$ 1237.51
                Discount : 18%
                Answer :  $1,014.76"""
        if case == 1:
            sentence = "The cost of " + str(random.choice(expensive_items)) + ": \$" + str(money_truncate(floatB)) + r"\\" + str(random.choice(action_up)) + " : " + percentify(intB)
            answer = money_formatter(money_truncate((float(floatB) * float("0." + str(intB))) + float(floatB)))

        else:
            sentence = "Cost of " + str(random.choice(expensive_items)) + ": \$" + str(money_truncate(floatB)) + r"\\" + str(random.choice(action_down)) + " : " + percentify(intB)
            answer = money_formatter(money_truncate(float(floatB) - (float(floatB) * float("0." + str(intB)))))
    
    elif option_difficulty == 3:
        """  - case 1
        - Cost of [cheap_items] : $\$$ floatA
        - [action_up] : intA %
        - [action_down] : intB %

        - case 2
        - Cost of [expensive_items] : $\$$ floatA
        - [action_up] : intA %
        - [action_down] : intB %"""
        if case == 1:
            sentence = "The cost of " + str(random.choice(cheap_items)) + ": \$" + str(money_truncate(floatA)) + r"\\" + str(random.choice(action_up)) + " : " + percentify(intA) + ", " + str(random.choice(action_down)) + " : " + percentify(intB)
            up = 0
            up = (float(floatA) * float("0." + str(intA))) + float(floatA)
            answer = money_formatter(money_truncate(float(up) - (float(up) * float("0." + str(intB)))))
        
        else:
            sentence = "The cost of " + str(random.choice(expensive_items)) + ": \$" + str(money_truncate(floatB)) + r"\\" + str(random.choice(action_down)) + " : " + percentify(intB) + ", " + str(random.choice(action_up)) + " : " + percentify(intA)
            down = 0
            down = float(floatB) - (float(floatB) * float("0." + str(intB)))
            answer = money_formatter(money_truncate( (float(down) * float("0." + str(intA))) + float(down) ))
         
    return(sentence,answer)


def solver(a,b,c,d,pos):
    if pos == 1:
        return(str((int(b) * int(c)) / int(d)))
    elif pos == 2:
        return(str((int(a) * int(d)) / int(c)))
    elif pos == 3:
        return(str((int(a) * int(d)) / int(b)))
    elif pos == 4:
        return((int(b) * int(c)) / int(a))

def fractionizer(a, b):
    return r"\frac{" + str(a) + "}{" + str(b) + "}"

def type_check(a):
    if str(float(a))[-2:] == ".0":
        a = int(a)
    return(a)

