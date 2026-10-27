w = int(input("Enter size "))
z = 1
for x in range(5):
    for y in range(x + 1):
        print(z, end=" ")
        z = z + 1
    print()

print("change this")
w = int(input("Enter size "))
z = 1
for x in range(5):
    for y in range(w + 1):
        print(z, end=" ")
        z = z + 1
    print()