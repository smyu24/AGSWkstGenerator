from .pro_gen import *

def getproblemandanswer(code, farr):
    if(code == "1-1-1"):
        pro, ans1, ans2 = Naming_Decimal_Places(farr)
    elif(code == "1-1-2"):
        pro, ans1, ans2 = readingandwriting(farr)
    elif(code == "1-1-3"):
        pro, ans1, ans2 = rounding(farr)

    elif(code == "1-2-1"):
        pro, ans1, ans2 = divandfac(farr)
    elif(code == "1-2-2"):
        pro, ans1, ans2 = factoring(farr)
    elif(code == "1-2-3"):
        pro, ans1, ans2 = monomials(farr)
    elif(code == "1-2-4"):
        pro, ans1, ans2 = common_factors(farr)
    elif(code == "1-2-5"):
        pro, ans1, ans2 = Leastcommon_factors(farr)

    elif(code == "1-3-1"):
        pro, ans1, ans2 = ConvertingFractionsandDecimals(farr)
    elif(code == "1-3-2"):
        pro, ans1, ans2 = Convertingbetweenpercents(farr)
    elif(code == "1-3-3"):
        pro, ans1, ans2 = setfor33(farr)
    elif(code == "1-3-4"):
        pro, ans1, ans2 = Addingandsubtracting(farr)
    elif(code == "1-3-5"):
        pro, ans1, ans2 = Addinganddecimals(farr)
    elif(code == "1-3-6"):
        pro, ans1, ans2 = fractionsandmixed(farr)
    elif(code == "1-3-7"):
        pro, ans1, ans2 = Dividingintegers(farr)
    elif(code == "1-3-8"):
        pro, ans1, ans2 = Multiplyingintegers(farr)
    elif(code == "1-3-9"):
        pro, ans1, ans2 = Multiplyingdecimals(farr)
    elif(code == "1-3-10"):
        pro, ans1, ans2 = multianddivisioncombi(farr)
    elif(code == "1-3-11"):
        pro, ans1, ans2 = Orderofoperations(farr)

    elif(code == "1-4-1"):
        pro, ans1, ans2 = thisisfor41(farr)
    elif(code == "1-4-2"):
        pro, ans1, ans2 = thisisfor42(farr)
    elif(code == "1-4-3"):
        pro, ans1, ans2 = thisisfor43(farr)

    elif(code == "1-5-1"):
        pro, ans1, ans2 = thisisfor51(farr)
    elif(code == "1-5-2"):
        pro, ans1, ans2 = thisisfor52(farr)
    elif(code == "1-5-3"):
        pro, ans1, ans2 = thisisfor53(farr)
    elif(code == "1-5-4"):
        pro, ans1, ans2 = thisisfor54(farr)
    elif(code == "1-5-5"):
        pro, ans1, ans2 = thisisfor55(farr)
    elif(code == "1-5-6"):
        pro, ans1, ans2 = thisisfor56(farr)
    elif(code == "1-5-7"):
        pro, ans1, ans2 = thisisfor57(farr)

    elif(code == "1-6-1"):
        pro, ans1, ans2 = thisisfor61(farr)
    elif(code == "1-6-2"):
        pro, ans1, ans2 = thisisfor62(farr)
    elif(code == "1-6-3"):
        pro, ans1, ans2 = thisisfor63(farr)
    elif(code == "1-6-4"):
        pro, ans1, ans2 = thisisfor64(farr)

    elif(code == "1-7-1"):
        pro, ans1, ans2 = thisisfor71(farr)
    elif(code == "1-7-2"):
        pro, ans1, ans2 = thisisfor72(farr)
    elif(code == "1-7-3"):
        pro, ans1, ans2 = thisisfor73(farr)
    elif(code == "1-7-4"):
        pro, ans1, ans2 = thisisfor74(farr)
    elif(code == "1-7-5"):
        pro, ans1, ans2 = thisisfor75(farr)

    elif(code == "1-8-1"):
        pro, ans1, ans2 = thisisfor81(farr)
    elif(code == "1-8-3"):
        pro, ans1, ans2 = thisisfor83(farr)
    elif(code == "1-8-4"):
        pro, ans1, ans2 = thisisfor84(farr)
    elif(code == "1-8-5"):
        pro, ans1, ans2 = thisisfor85(farr)
    elif(code == "1-8-6"):
        pro, ans1, ans2 = thisisfor86(farr)

    elif(code == "1-9-1"):
        pro, ans1, ans2 = thisisfor91(farr)
    elif(code == "1-9-2"):
        pro, ans1, ans2 = thisisfor92(farr)


    """
    elif(code == "1-9-3"):
        pro, ans1, ans2 = thisisfor93(farr)
    elif(code == "1-9-4"):
        pro, ans1, ans2 = thisisfor94(farr)

    elif(code == "1-10-1"):
        pro, ans1, ans2 = thisisfor101(farr)
    elif(code == "1-10-2"):
        pro, ans1, ans2 = thisisfor102(farr)
    elif(code == "1-10-3"):
        pro, ans1, ans2 = thisisfor103(farr)

    elif(code == "1-11-1"):
        pro, ans1, ans2 = thisisfor111(farr)
    elif(code == "1-11-2"):
        pro, ans1, ans2 = thisisfor112(farr)
    elif(code == "1-11-3"):
        pro, ans1, ans2 = thisisfor113(farr)
    """

    return (pro, ans1, ans2)