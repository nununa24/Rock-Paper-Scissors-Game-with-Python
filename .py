import random

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

# 1st Option (long version)
user_choise = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
if user_choise == 0:
    print(rock)
elif user_choise == 1:
    print(paper)
elif user_choise == 2:
    print(scissors)
else:
    print("Wrong choise!!!")

computer_choise = random.randint(0,2)
print(f"Computer choise: {computer_choise}")

if user_choise == 0:
    if computer_choise == 0:
        print(rock)
        print("It's a draw!")
    elif computer_choise == 1:
        print(paper)
        print("You lose!")
    else:
        print(scissors)
        print("You win!")
if user_choise == 1:
    if computer_choise == 0:
        print(rock)
        print("You win!")
    elif computer_choise == 1:
        print(paper)
        print("It's a draw!")
    else:
        print(scissors)
        print("You lose!")
if user_choise == 2:
    if computer_choise == 0:
        print(rock)
        print("You lose!")
    elif computer_choise ==1:
        print(paper)
        print("You win!")
    else:
        print(scissors)
        print("It's a draw!")


# 2st Option
game_images = [rock, paper, scissors]

user_choise = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
if user_choise >= 0 and user_choise <= 2:
    print(game_images[user_choise])

computer_choise = random.randint(0,2)
print("Computer choise:")
print(game_images[computer_choise])

if user_choise >= 3 or user_choise < 0:
    print("Wrong choise. You lose!")
elif user_choise == 0 and computer_choise == 2:
    print("You win!")
elif computer_choise == 0 and user_choise == 2:
    print("You lose!")
elif computer_choise > user_choise:
    print("You lose!")
elif user_choise > computer_choise:
    print("You win!")
elif user_choise == computer_choise:
    print("It's a draw!")
