#int(), or eval(), float()

x = float(input("Gimme a float?:"))

sum = x + 6

print("Total = ", sum)
print(type(x))

x = eval(input("give me any type of number?:"))

sum = x + 6

print("Total = ", sum)
print(type(x))

x = int(input("How old are you?:"))

sum = x + 6

print("Total = ", sum)
print(type(x))