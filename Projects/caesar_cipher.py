alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.
def encrypt(original_text,shift_amount):
    secret_word=""
    for letter in original_text:
       # print(alphabet.index(letter)) # this will print the letter index position
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position= shifted_position % len(alphabet) # TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?
        secret_word += alphabet[shifted_position]

    print(f"Your secrete word is: {secret_word}")
# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a message.

#encrypt(original_text=text, shift_amount=shift)

# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.


def decrypt(original_text, shift_amount):
    decrypt_word=""
    for letter in original_text:
       # print(alphabet.index(letter)) # this will print the letter index position
        shifted_position = alphabet.index(letter) - shift_amount  # /*or short */ shift_amount *= -1
        shifted_position= shifted_position % len(alphabet) # TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?
        decrypt_word += alphabet[shifted_position]
    print(f"Your secrete word is: {decrypt_word}")

# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.
def caesar():
    try:

        if direction=="encode":
            encrypt(original_text=text, shift_amount=shift)
        elif direction=="decode":

            decrypt(original_text=text,shift_amount=shift)
        else:
            print("Invalid.")
    except ValueError:
        print("Invalid input. Please enter a valid input")
caesar()

