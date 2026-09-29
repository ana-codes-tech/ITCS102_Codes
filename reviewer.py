age = int(input("AGE:->"))
rev = float(input("REVENUE ->"))
cc = int(input("CREDIT SCORE:->"))
yrs = float(input("YEARS IN BUSSINESS:->"))
has_defaults = bool(input("FILE FOR BANKRUPTCY:->"))
collateral = input("COLLATERAL NAME:->")
c_val = float(input("COLLATERAL VALUE:->"))


max_loan = 0
base_fee = 0

if age >= 21 and yrs >= 2 and has_defaults == False:
    print("baseline passed")

    #tier 1
    if cc >= 720:
        print("Credit score passed tier 1")
        max_loan = 3 * rev

        if rev >= 50000:
            print("above 50k rev")
            base_fee = max_loan * 0.015
            print("base fee is set to", base_fee)
        else: 
            print("rev below 50k")
            base_fee = max_loan * 0.025
            print("base fee it set to", base_fee)
    #tier 2
    elif cc >= 620 and cc < 720:
        print("passed cc given range")
        max_loan = 1.5 * rev

        if yrs >= 5:
            base_fee = max_loan * 0.02
        else:
            base_fee = max_loan * 0.035
    #tier 3
    elif cc < 620:
        print("credit score too low according to tier 3")
    else:
        print("invalid")
else:
    print("Rejected did not pass baseline")
