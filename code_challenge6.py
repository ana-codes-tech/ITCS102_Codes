
w = int(input("Enter size "))
z = 1
for x in range(w):
    for y in range(x + 1):
        if z<= 1:
            print(z, end=" ")
            z = z + 1
    print()
