from sympy import Eq, solve_linear_system, Matrix
import sympy as sp

eq1 = sp.Function('eq1')
eq2 = sp.Function('eq2')

x,y = sp.symbols('x y')

eq1 = Eq(2*x-y, -4) # equal to 2*x-y=4
eq2 = Eq(3*x-1, -2)


row1 = [2, -1, -4]
row2 = [3, -1, -2]

system = Matrix([row1, row2])

print(solve_linear_system(system, x, y))
"""
eq1 = sp.Function('eq1')
x,y = sp.symbols('x y')

eq1 = Eq(2*x-y, -4) # equal to 2*x-y=4

row1 = [2, -1, -4]

system = Matrix([row1])

print(solve_linear_system(system, x, y))
"""


"""
from sympy import Eq, solve_linear_system, Matrix
import sympy as sp

eq1 = sp.Function('eq1')
        x,y,z,t = sp.symbols('x y z t') #, cls=Function
        # CAN SYMBOLS BE A SYMBLE?
        a = random.choice(addition_expression)
        print(a)
        if a == '-':
            eq1 = Eq(x * (y - z), t) # equal to 2*x-y=-4
        elif a == '+':
            eq1 = Eq(x * (y + z), t)
        print(eq1)
        row1 = [str(random.randint(2, 10)), str(random.randint(1, 10)), str(random.randint(1, 10))]
        system = Matrix([row1])
        #print(solve_linear_system(system, x, y, z))
        print(sp.solve(eq1))"""