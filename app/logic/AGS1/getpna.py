from .pro_gen import *

def getproblemandanswer(code, farr):
    if(code == "1-1-1"):
        pro, ans1, ans2 = M_Evaluate_Equation(farr)
    elif(code == "1-1-2"):
        pro, ans1, ans2 = M_Graph_The_Ordered_Pairs(farr)
    elif(code == "1-2-1"):
        pro, ans1, ans2 = M_Fill_In_The_Seq(farr)
    elif(code == "1-2-2"):
        pro, ans1, ans2 = M_The_Meaning_Of_An_Exp(farr)
    elif(code == "1-2-3"):
        pro, ans1, ans2 = M_Finding_Patterns_In_Geo_Seq(farr)
    elif(code == "1-3-1"):
        pro, ans1, ans2 = M_Reading_The_Table(farr)
    elif(code == "1-3-2"):
        pro, ans1, ans2 = M_Arithmetic_Seq(farr)
    elif(code == "1-3-3"):
        pro, ans1, ans2 = M_Geo_Seq_Problem(farr)
    elif(code == "1-3-4"):
        pro, ans1, ans2 = M_So_Should_We_Use(farr)
    elif(code == "1-4-1"):
        pro, ans1, ans2 = M_Arithmetic_Explicit_Recursive(farr)
    elif(code == "1-4-2"):
        pro, ans1, ans2 = M_AGS_Find_The_Slope(farr)
    elif(code == "1-5-1"):
        pro, ans1, ans2 = M_Information_To_Geometric_Sequence(farr)
    elif(code == "1-5-2"):
        pro, ans1, ans2 = M_Slope_Intercept(farr)
    elif(code == "1-5-3"):
        pro, ans1, ans2 = M_Geometric_Seq_To_Explicit_Recursive(farr)
    elif(code == "1-6-1"):
        pro, ans1, ans2 = M_AGS_Percentage_Change(farr)
    elif(code == "1-6-2"):
        pro, ans1, ans2 = M_Is_It_Arith_Or_Geo_Seq(farr)
    elif(code == "1-8-1"):
        pro, ans1, ans2 = M_Fill_The_Gap(farr)
    elif(code == "1-9-1"):
        pro, ans1, ans2 = M_Which_Grows_Faster(farr)
    elif(code == "1-10-1"):
        pro, ans1, ans2 = M_Information_To_Arith_Seq(farr)

    
    # elif(code == "2-1-1"):
    #     pro, ans1, ans2 = M_(farr)
    # elif(code == "2-2-1"):
    #     pro, ans1, ans2 = M_Find_The_Slope(farr)
    # elif(code == "2-2-2"):
    #     pro, ans1, ans2 = M_Indicate_The_Relationship(farr)
    # elif(code == "2-2-3"):
    #     pro, ans1, ans2 = M_Solve_The_Following_Equations(farr) # (diff=1, expr="latex", lvl=1) ONLY LVL 1 & 2
    # elif(code == "2-2-4"):
    #     pro, ans1, ans2 = M_Find_The_Recursive_And_Explicit_Equations(farr) 
    # elif(code == "2-3-1"):
    #     pro, ans1, ans2 = M_Rules_Of_Exponents(farr) #(difficulty=1, expr="latex", posExpOnly=False):
    # elif(code == "2-3-2"):
    #     pro, ans1, ans2 = M_Details_Of_Linear_And_Geometric_Sequences(farr)
    # elif(code == "2-3-3"):
    #     pro, ans1, ans2 = M_Fill_In_The_Blanks(farr) # kind='geo'; kind='exp'
    # elif(code == "2-3-4"):
    #     pro, ans1, ans2 = M_Find_The_Slope_Table(farr) # only one mode
    # elif(code == "2-4-1"):
    #     pro, ans1, ans2 = M_Square_Roots(farr)
    # elif(code == "2-4-2"):
    #     pro, ans1, ans2 = M_Fill_In_The_Table(farr)
    # elif(code == "2-5-1"):
    #     pro, ans1, ans2 = M_Higher_Order_Roots(farr) 
    # elif(code == "2-5-2"):
    #     pro, ans1, ans2 = M_Evaluate_The_Function(farr) 
    # elif(code == "2-6-1"):
    #     pro, ans1, ans2 = M_Percent_Increase_Decrease(farr) # NO MULT DIFFICULTY
    # elif(code == "2-6-2"):
    #     pro, ans1, ans2 = M_Monthly_Exponential(farr)
    # elif(code == "2-7-1"):
    #     pro, ans1, ans2 = M_(farr) #
    # elif(code == "2-7-2"):
    #     pro, ans1, ans2 = M_(farr)
    # elif(code == "2-7-3"):
    #     pro, ans1, ans2 = M_(farr)
    # elif(code == "2-8-1"):
    #     pro, ans1, ans2 = M_(farr)
    # elif(code == "2-10-1"):
    #     pro, ans1, ans2 = M_(farr)
    # elif(code == "2-10-2"):
    #     pro, ans1, ans2 = M_(farr)
    # elif(code == "2-11-1"):
    #     pro, ans1, ans2 = M_(farr)


    # elif(code == "3-"):
    #     pro, ans1, ans2 = M_(farr)
    # elif(code == "3-"):
    #     pro, ans1, ans2 = M_(farr)
    # elif(code == "3-"):
    #     pro, ans1, ans2 = M_(farr)


    return (pro, ans1, ans2)