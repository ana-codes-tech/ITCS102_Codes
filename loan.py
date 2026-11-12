#string formatting
loan_amt = float(input("enter loan "))
years = int(input("enter years "))
month = years * 12
principal = loan_amt / month

running_total = loan_amt
loan_interest = 0 
monthly_pay = 0
rem_bal = loan_amt

print("|MONTH\t|\tPAYMENT\t\t|INTEREST\t|PRINCIPAL\t|\tBALANCE\t|")
for x in range(1, month + 1):
    rem_bal -= principal
    loan_interest = rem_bal * 0.00256
    monthly_pay = loan_interest + principal

   
    print(f"|{x} \t | {monthly_pay} \t |\t {loan_interest} \t | \t {principal} \t | \t {rem_bal}")
    print(f"| {x}\t|\t{monthly_pay}\t\t|\t{loan_interest}\t | \t {principal} \t | \t {rem_bal,2}")