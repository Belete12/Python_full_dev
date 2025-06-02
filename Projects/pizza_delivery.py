from random import choice

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

#TODO: 1. How much they need to pay based on their choice

# Small pizza (S): $15
# Medium pizza (M): $20
# Large pizza (L): $25

cost = 0
if size =="S":
    cost = 15
elif size == "M":
    cost = 20
elif size == "L":
    cost = 25
else:
    print("Invalid data")

#TODO 2. Add based on their pepperoni choice
if pepperoni == "Y":
    if size == "S":
        cost += 2
    else:
        cost +=3

#TODO 3. work their final bill based on whether they want extra cheese or not

if extra_cheese =="Y":
    cost +=1
print(f"Your total bill is ${cost}")