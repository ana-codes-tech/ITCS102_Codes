#Create make a python script that operates the following output
#PESO DOMINATOR
#MONEY = 4572 (random)
# 1000, 500, 200, 100, 50, 20, 10, 5, 1

Fullname = input("What is your full name? ")
print("Good day!", Fullname, "Welcome to Vanella Bankya")

Bank_number = int(input("Type your 6 digits Bank number:"))
print("Bank acount number",Bank_number, "found successfully.") 

money = int(input("Enter amount to DEPOSIT "))


thousand = money // 1000
thousand_reduced = money % 1000

five_hundred = thousand_reduced // 500
fiveh_reduced = thousand_reduced % 500

two_hundred = fiveh_reduced // 200
twoh_reduced = fiveh_reduced % 200

one_hundred = twoh_reduced // 100
oneh_reduced = twoh_reduced % 100

fifty = oneh_reduced // 50
fifty_reduced = oneh_reduced % 50

twenty = fifty_reduced // 20
twenty_reduced = fifty_reduced % 20

ten = twenty_reduced // 10
ten_reduced = twenty_reduced % 10

five = ten_reduced // 5
five_reduced = ten_reduced % 5

one = five_reduced // 1
one_reduced = five_reduced % 1

print("1000 - ",thousand)
print("500 - ",five_hundred)
print("200 - ",two_hundred)
print("100 - ",one_hundred)
print("50 - ",fifty)
print("20 - ",twenty)
print("10 - ",ten)
print("5 - ",five)
print("1 - ",one)