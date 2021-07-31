# Clearing 0s in decimal places

class Decimal_clear():
  def __init__(self, decimal):
    self.decimal = decimal
  def drop_trail_decimal(self):
    """Get rid of trailing 0s at the end of decimal numbers"""
    decimal_times = self.decimal * 10
    return decimal_times / 10


placeholders = Decimal_clear(1.20)
placeholders.drop_trail_decimal()