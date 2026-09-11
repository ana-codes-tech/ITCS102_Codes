#write program that calculates total shipping charges using package details, location rules, and strict #conditional order

#Problem: Global Freight Calculator 
#is_express mean if rush or not, is_international if lalabas ng bansa

name = str(input("Sender Name:"))
type = str(input("Type of Item:"))
weight = float(input("Weight in kg:"))
distance = float(input("Distance in km:"))

isFragile = input("Fragile (Pick one: True/False): ") == "True"
is_express = input("Express (Pick one: True/False): ") == "True"
is_international =  input("International (Pick one: True/False): ") == "True"

total= 0
base_cost = (weight * 2.50) + (distance * 0.15)
total =+ base_cost 

print("Hello!", name, "Your total shipping payment is")

if weight <= 2.0 and distance <= 100 and not is_express and not is_international:
	total = 0
	print(total, "Congrats, Your Shipping is FREE!")	

elif is_international and is_express:
	total = (base_cost * 1.40) + 50
	print(total)

elif is_express or is_international and weight > 20:
	total = (base_cost * 1.20) + 25
	print(total)

elif weight > 30 or distance > 1000:
	total = base_cost + 30
	print(total)

else:
	total = base_cost
	print(total, "Standard rate")
