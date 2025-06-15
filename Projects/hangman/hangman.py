import random

# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.

#only if you have one variable but  it is not good if here are multiple variables there for use import and call the file name
# from hangman_words import  word_list
from hangman_art import logo, stages

#instead use the below import
# import hangman_art
import hangman_words
print(logo)
# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.
# TODO-4: Create a "placeholder" with the same number of blanks as the chosen_word
# TODO-5: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.

# TODO-1
# Use a while loop to let the user guess again.
# The loop should only stop once the user has guessed all the letters in the chosen_word.
# At that point display has no more blanks ("_"). Then you can tell the user they've won.

# TODO-2
    # Update the for loop so that previous guesses are added to the display String.
    # At the moment, when the user makes a new guess, the previous guess gets replaced by a "_". We need to fix that by updating the for loop

chosen_word = random.choice(hangman_words.word_list)
#print(chosen_word)

placeholder = "_"
length_word = len(chosen_word)
for len_number in range(length_word):
    placeholder +="_"

print(placeholder)

game_over = False
correct_letter = []
lives = 6
live_lost =0
while not game_over:

    # TODO-6: - Update the code below to tell the user how many lives they have left.
    print(f"**************************** you have {lives} /6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in correct_letter:
        print(f"You have already guessed {guess}")

    display = ""

    for letter in chosen_word:
        if guess == letter:
            display += letter
            correct_letter.append(guess)
        elif letter in correct_letter:
            display += letter
        else:
            display +="_"

    print(display)

    if "_" not in display:
       game_over = True
       print("You won!")
    # TODO-2: - If guess is not a letter in the chosen_word, Then reduce 'lives' by 1.
    #  If lives goes down to 0 then the game should stop and it should print "You lose."
    # TODO-3: - print the ASCII art from 'stages'
    #  that corresponds to the current number of 'lives' the user has remaining.

    # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
    #  e.g. You guessed d, that's not in the word. You lose a life.

    if guess not in chosen_word:
        lives -= 1
        live_lost +=1
        print(f"You guessed {guess}, that's not in the word. You lose a {live_lost} life.")
        if lives == 0:
            game_over = True
            print("You lose")
            # TODO 7: - Update the print statement below to give the user the correct word they were trying to guess.
            print(f"***********************YOU LOSE the word was {chosen_word} **********************")

        print(f"{lives} left {stages[lives]}")






