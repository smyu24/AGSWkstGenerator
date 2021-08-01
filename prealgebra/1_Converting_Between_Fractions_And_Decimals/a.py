
import math
import random
from fractions import Fraction
from decimal import Decimal

def decimal_to_num_denom(n):
   to_fraction = Fraction.from_decimal(Decimal(n))
   numerator, denominator = to_fraction.numerator, to_fraction.denominator
   return {'numerator': numerator, 'denominator': denominator}

print(decimal_to_num_denom(2.1512))