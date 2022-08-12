from ..prealgebra.pro_gen import *
from ..prealgebra.getpna import getproblemandanswer
def testseedmaster(i, seed):
    code = seed[i].replace(" ", "")
    farr = [[ str(seed[i] + (seed[i+1])).replace(" ", ""), int(seed[i+2]), int(seed[i+3]), 0, 0 ]]
    pro = []
    ans1 = []
    ans2 = []

    pro, ans1, ans2 = getproblemandanswer(code, farr)
    return (pro, ans1, ans2)
