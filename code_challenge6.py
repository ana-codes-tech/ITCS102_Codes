w = int(input("Enter size "))
z = 0
for x in range(w):
    if z != w:
        for y in range(x + 1):
            if z != w:
                z = z + 1
                print(z, end=" ")
            elif z == w:
                print("", end=" ")
        print(" ")
