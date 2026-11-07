#final working code
isRaining = True

while isRaining == True:
    x = bool(input("Is it raining outside? (True/False)"))

    if x == True:
        print("Continuing Loop")
        continue
    else:
        break

#experimentation/practice, mystery why it continues even when input is false
isRaining = True

while isRaining == True:
    x = bool(input("Is it raining outside? (True/False)"))

    if x == True:
        print("Continuing Loop")
        continue
    elif x == False:
        break
    else:
        break

#make the loop stop when input is false
isRaining = True

while isRaining == True:
    x = input("Is it raining outside? (True/False)")

    if x == "True":
        print("Continuing Loop")
        continue
    elif x == "False":
        break
    else:
        break
