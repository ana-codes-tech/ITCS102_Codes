import getpass
bankname = "Vanana"
password = "Sekretongmalupit"
banknumber = "109169"

n = input("Enter bank name -----> ")
p = getpass.getpass("Enter bank password -----> ")
bn = input("Enter bank number -----> ")

if bankname == n or banknumber == bn and password == p:
	print("Log in Successful")
else:
	print("Access denied: Try other ways to log in")