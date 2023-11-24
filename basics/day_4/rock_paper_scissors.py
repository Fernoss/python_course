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

user_choice = int(input("Think you can beat a computer?\n"
      "Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))

if user_choice == 0:
    print(f"You chose:\n{rock}")
elif user_choice == 1:
    print(f"You chose:\n{paper}")
else:
    print(f"You chose:\n{scissors}")

# computer's random number
computer_choice = random.randint(0, 2)
if computer_choice == 0:
    print(f"Computer chose:\n{rock}")
elif computer_choice == 1:
    print(f"Computer chose:\n{paper}")
else:
    print(f"Computer chose:\n{scissors}")


# check who wins
if user_choice == computer_choice:
    print("That's a draw!")
elif user_choice == 0 and computer_choice != 1:
    print("You win!")
elif user_choice == 1 and computer_choice != 2:
    print("You win!")
elif user_choice == 2 and computer_choice != 0:
    print("You win!")
else:
    print("You lose! Better luck next time.")