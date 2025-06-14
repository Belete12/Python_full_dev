import random
from random import shuffle

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []

for char in range(0, nr_letters): # we add 1 because the range doesn't include the last digit
    random_char= random.choice(letters)
    password += random_char

for symbol in range(0, nr_symbols):
    random_symbol= random.choice(symbols)
    password += random_symbol

for number in range(0, nr_numbers):
    random_number=random.choice(numbers)
    password +=random_number
#rondom order
random.shuffle(password)
result = ''.join(password)
print(f"New password: {result}")

# we can also shuffle using for loops

password_forloop=""
for char in password:
    password_forloop += char
print(f"Your for loop shuffle passwo rd is: {password_forloop}")


# or use the below

def generate_password():
    #create an empty variable that holds the random generated number, letter, and symbols
    rand_letter =[]
    rand_symbol = []
    rand_number = []
    #generate the random number as user input

    for letter in letters:
        #compare user input and randome letter generated
        if len(rand_letter) < nr_letters:
            generate_rand_letter= random.choice(letter)
            rand_letter.append(generate_rand_letter)
    # print(rand_letter)

    for symbol in symbols:
       if len(rand_symbol) < nr_symbols:
           generate_rand_symbol = random.choice(symbol)
           rand_symbol.append(generate_rand_symbol)
#generate numbers
    for number in numbers:
        if len(rand_number) < nr_numbers:
            generate_rand_number = random.choice(number)
            rand_number.append(generate_rand_number)
    #now we need to shuffle and join togather

    result = rand_letter + rand_symbol + rand_number
    random.shuffle(result)
    password = ''.join(result)

    print(f"Your new Password is: {password}")


generate_password()