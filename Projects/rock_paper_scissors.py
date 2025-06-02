import random
#TODO:
    # 1. Rock wins against scissors
    # 2. Scissors win against paper.
    # 3. Paper wins against rock

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

image_choose = [rock,paper,scissors]


#prompt for the users
user_choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    # if user_choose==0:
    #     print(rock)
    # elif user_choose ==1:
    #     print(paper)
    # else:
    #     print(scissors)

if user_choose >= 0 or user_choose <=2:
    print(image_choose[user_choose])

computer_choose = random.randint(0, 2)
print(f"Computer choose: \n {image_choose[computer_choose]}")

# compare
if user_choose == computer_choose:
    print("It's a draw")
elif user_choose == 0 and computer_choose == 2\
        or user_choose == 2 and computer_choose == 1\
        or user_choose == 1 and computer_choose ==0:
    print("You win")
else:
    print("you lose")