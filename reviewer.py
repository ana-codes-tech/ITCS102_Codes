age = int(input("AGE:->"))
rev = float(input("REVENUE ->"))
cc = int(input("CREDIT SCORE:->"))
yrs = float(input("YEARS IN BUSSINESS:->"))
has_defaults = bool(int(input("FILE FOR BANKRUPTCY? (1=YES, 0=NO):-> "))) 
collateral = input("COLLATERAL NAME:->")
c_val = float(input("COLLATERAL VALUE:->"))


max_loan = 0
base_fee = 0

if age >= 21 and has_defaults == False and yrs >= 2.0:
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

        #collateral
        if c_val >= max_loan:
            print("collateral", collateral, "with a value of", c_val, "is accepted")
        else:
            print("Rejected: Insufficient collateral valu for", collateral)

        #surcharge
        if c_val % 5000 != 0:
            base_fee += 250
            print("ADDITIONAL CHARGE ADDED TO BASE FEE, total base fee is", base_fee)
        else:
            print("collateral value divisible by 5000")

    #tier 2
    elif cc >= 620 and cc < 720:
        print("passed cc given range")
        max_loan = 1.5 * rev

        if yrs >= 5:
            base_fee = max_loan * 0.02
        else:
            base_fee = max_loan * 0.035

        #collateral
        if c_val >= max_loan:
            print("collateral", collateral, "with a value of", c_val, "is accepted")
        else:
            print("Rejected: Insufficient collateral valu for", collateral)
    
        #surcharge
        if c_val % 5000 != 0:
            base_fee += 250
            print("ADDITIONAL CHARGE ADDED TO BASE FEE, total base fee is", base_fee)
        else:
            print("collateral value divisible by 5000")
    #tier 3
    elif cc < 620:
        print("credit score too low according to tier 3")
    else:
        print("invalid")
else:
    print("Rejected did not pass baseline")
