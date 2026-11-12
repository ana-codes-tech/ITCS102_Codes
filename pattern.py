#task 2
n = 7
for x in range(n):
    for y in range(x,n - 1):
        print("-", end="")
    for y in range(x+1):
        print("*", end="")
    for y in range(1, y + 1):
        print("*", end="")


    print()

#hollow
n = 7
for x in range(n):
    for y in range(n):
        if x + y == 6:
            print("*", end="")
        else:
            print("-", end="")

    for y in range(x+1):
            print("*", end="")
    print()

#task 3
n = 5
for x in range(n):
    for y in range(n):
        if x + y == 4 or x + y == y or x == 5 or n == x:
            print("*", end="")
        else:
            print(" ", end="")
    print()
