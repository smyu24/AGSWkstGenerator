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
    elif(code == "2-2-1"):
        pro, ans1, ans2 = M_Find_The_Slope(farr)
    # elif(code == "2-2-2"):
    #     pro, ans1, ans2 = M_Indicate_The_Relationship(farr)
    elif(code == "2-2-3"):
        pro, ans1, ans2 = M_Solve_The_Following_Equations(farr)
    elif(code == "2-2-4"):
        pro, ans1, ans2 = M_Find_The_Recursive_And_Explicit_Equations(farr)
    elif(code == "2-3-1"):
        pro, ans1, ans2 = M_Rules_Of_Exponents(farr)
    elif(code == "2-3-2"):
        pro, ans1, ans2 = M_Details_Of_Linear_And_Geometric_Sequences(farr)
    elif(code == "2-3-3"):
        pro, ans1, ans2 = M_Fill_In_The_Blanks(farr)
    elif(code == "2-3-4"):
        pro, ans1, ans2 = M_Find_The_Slope_Table(farr)
    elif(code == "2-4-1"):
        pro, ans1, ans2 = M_Square_Roots(farr)
    elif(code == "2-4-2"):
        pro, ans1, ans2 = M_Fill_In_The_Table(farr)
    elif(code == "2-5-1"):
        pro, ans1, ans2 = M_Higher_Order_Roots(farr)
    elif(code == "2-5-2"):
        pro, ans1, ans2 = M_Evaluate_The_Function(farr)
    elif(code == "2-6-1"):
        pro, ans1, ans2 = M_Percent_Increase_Decrease(farr)
    # elif(code == "2-6-2"):
    #     pro, ans1, ans2 = M_Monthly_Exponential(farr) # issue
    elif(code == "2-7-1"):
        pro, ans1, ans2 = M_FillInTheTable(farr) # no mult; option='exp'
    elif(code == "2-7-2"):
        pro, ans1, ans2 = M_radicalandfractionexponent(farr) # (diff, "latex", "r" or "e")
    elif(code == "2-7-3"):
        pro, ans1, ans2 = M_GraphXintYint_2_7_3(farr) # NO MULT ; kind='exp' only para
    elif(code == "2-8-1"):
        pro, ans1, ans2 = M_FillInTheMeansTable(farr) # NO MULT DIFF
    elif(code == "2-10-1"):
        pro, ans1, ans2 = M_LinearForms_2_10_1(farr)
    # elif(code == "2-10-2"):
    #     pro, ans1, ans2 = M_(farr) # Case 1 for diff 1 and case 2 for diff 2
    elif(code == "2-11-1"):
        pro, ans1, ans2 = M_comparedifferent(farr)


    # elif(code == "3-1-1"):
    #     pro, ans1, ans2 = M_(farr)
    # elif(code == "3-2-1"):
    #     pro, ans1, ans2 = M_(farr)
    # elif(code == "3-2-2"):
    #     pro, ans1, ans2 = M_(farr)
    # elif(code == "3-3-1"):
    #     pro, ans1, ans2 = M_(farr)
    # elif(code == "3-3-2"):
    #     pro, ans1, ans2 = M_(farr)
    # elif(code == "3-3-3"):
    #     pro, ans1, ans2 = M_(farr)
    # elif(code == "3-4-1"):
    #     pro, ans1, ans2 = M_(farr)
    # elif(code == "3-4-2"):
    #     pro, ans1, ans2 = M_(farr)
    # elif(code == "3-4-3"):
    #     pro, ans1, ans2 = M_(farr)
    # elif(code == "3-4-4"):
    #     pro, ans1, ans2 = M_(farr)
    # elif(code == "3-5-1"):
    #     pro, ans1, ans2 = M_(farr)
    # elif(code == "3-6-1"):
    #     pro, ans1, ans2 = M_(farr)
    return (pro, ans1, ans2)
r"""REMEMBER NO & SIGNS IN SQL SECTIONS ROW
AGS1.3.1.1 - Find The Value of  x
    instruction : For each equation find the value of  x  that makes it true.
AGS1.3.2.1 - Point Of Intersection
    instruction : Graph each set of linear equations on the same set of axes. Name the coordinates of the point where the two lines intersect.
AGS1.3.2.2 - Increasin / Decreasing / Constant / Domain & Range
    instruction : For each graph and description do the following:
            -use interval notation to state where the function is increasing or decreasing
            -state the minimum or maximum if the function has them
            -write the domain and range of the function using interval notation
            -respond to the context-based question
    instruction : For each graph and description do the following:
            -use interval notation to state where the function is increasing or decreasing
            -state the minimum or maximum if the function has them
            -write the domain and range of the function using interval notation
            -respond to the context-based question
AGS1.3.3.1 - Fill In The Table & State The Point Of Intersection
    instruction : Fill in the table of values for each of the linear functions. Then state the point of intersection of the two lines.
AGS1.3.3.2 - Finding Features Of Function
    instruction " For each of the following functions, find the desired features.
    instruction : For each of the following functions, find the desired features.
AGS1.3.3.3 - Finding Explicit And Recursive Equations
    instruction : Find both the explicit and recursive equations for the tables.
AGS1.3.4.1 - Find The Indicated Values
    instruction : Find the indicated values & Find equation or graph the explicit function
AGS1.3.4.2 - Graph The New Equation
    Instruction : Two functions are graphed. Graph a new function on the same grid by adding the two given functions.
AGS1.3.4.3- Compare Two Functions
    Instruction : Use the graph to answer the following questions.
AGS1.3.4.4 - Domain & Range / Increasing or Decreasing
    Instruction : For each graph, identify the domain, range, and whether or not the function is increasing or decreasing.
AGS1.3.5.1 - Find The Indicated Values
    Instruction : Use the graph of each function to find the indicated values.
AGS1.3.6.1 - Function Transformations
    Instruction : Graph the equations.
    Instruction : Transfrom the graph from the given graph


"""