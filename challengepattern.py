#A left arrowhead
for x in range(7):
  if x <= 3:
    for y in range(3-x):
      print(" ", end="")

    for y in range(x + 1):
      print("*", end="")


  else:
    for y in range(x - 3):
      print(" ", end="")
    for y in range(7-x):
      print("*", end="")
  print()
