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

    return (pro, ans1, ans2)