print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    total_cost=0
    if age <= 12:
        total_cost = 5
    elif age <= 18:
        total_cost = 7
    else:
        total_cost = 12
# - Ask the user if they want to take the photo
# - if yes add $3 on their final bill
# - if no print their rollercoaster charge

    want_pic = input("Do you want to have a photo? y or n: ")
    if want_pic == "y":
        total_cost +=3
    print(f"Your total bill is:  ${total_cost}")
    # else:
    #     print(f"Your total cost is : {total_cost}")

else:
    print("Sorry you have to grow taller before you can ride.")