print("Bank Loan & Interest Rate Approver")
age = int(input("How old are you?: "))
is_employed = bool(input("Are you employed?: "))
credit_score = int(input("Credit Score: "))
annual_income = float(input("What is your annual income?: "))
has_collateral = bool(input("Do you have any collateral (True/False)"))

base_rate = 0.0

if age >= 21 and is_employed == True:
    print("Accepted Baseline, you are old enough and you have job")

    if credit_score >= 750:
        print("Age pass, has job, You have a high credit score")
            
        if annual_income >= 100000:
            print("High income")
            base_rate = 4.5
            print("Approved at", base_rate)

        else:
            base_rate = 5.0
            print("Approved at", base_rate)

    elif credit_score >= 600 and credit_score < 750:
        if annual_income <= 40000:
            base_rate = 9.5
            print("Increased risk rate: Approved at", base_rate)

        elif has_collateral == True:
            base_rate = 7.0
            print("Approved at base interest rate:", base_rate)

        else:
            base_rate = 8.0
            print("Base rate with no collateral is", base_rate)

    elif credit_score < 600:
        print("Rejected: Credit Score Too Low")

    else:
        print("Failed")     

else: 
    print("Rejected: Fails baseline criteria")
