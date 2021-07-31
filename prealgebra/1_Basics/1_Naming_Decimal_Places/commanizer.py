def Commanizer(problemsets):
  questions = ""
  answersets= 0
  decimal_subtract = 0
  amount_commas = len(str(problemsets))
  period = str(problemsets).find(".")
  if period != -1:
    print("-----------------------------------")
    decimal_subtract = amount_commas - (period + 1)
    print(period) # correct
    print("space", decimal_subtract) # space of decimals to be subtracted out of total
  print(amount_commas)
  amount_commas = (amount_commas - 1) // 3
  print("amount_commas", amount_commas) # the amount of commas that are going to be "inserted"
  questions = problemsets
  questions = list(str(questions))
  print(questions)
  if amount_commas >= 1:
    questions.insert((-3 - decimal_subtract), ",")
  if amount_commas >= 2:
    questions.insert((-7 - decimal_subtract), ",")
  print("PLACES:", amount_commas)


  # get underwcores. Run again id it lands on comma
  print("question", questions)
  answersets = "".join(questions)
  print("answersets", answersets)