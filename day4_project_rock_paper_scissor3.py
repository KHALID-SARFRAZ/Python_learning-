
import random
rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissor="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game_images = [rock,paper,scissor]

user_choice = int(input("What do you choose? Type 0 for rock, 1 for " \
"paper and 2 for scissors\nEnter choice: "))
computer_choice = random.randint(0,2)

print(f"Computer chose: {computer_choice}")

if 0 <= user_choice < 3:

    if user_choice == 0 and computer_choice == 2:
        print(f"You chose:\n{game_images[user_choice]} and computer chose:\n{game_images[computer_choice]}\nYou Win!")

    elif computer_choice > user_choice:
        print(f"You chose:\n{game_images[user_choice]} and computer chose:\n{game_images[computer_choice]}\nYou Lost")
        
    elif user_choice > computer_choice:
        print("you win")

    elif computer_choice == user_choice:
        print("It's a Draw!")

else:
    print("invalid choice. You loose!")