
import random
def main():
    print("welcome to rock paper scissor game")

    a = input("what do you choose? type 0 for rock, 1 for paper and 2 for scissor\n ")
    b = random.randint(0,2)

    if a == "0":
        if b == 0:
            print("you chose rock and computer chose rock. It's a draw.")
        elif b == 1:
            print("you chose rock and computer chose paper. You lose.")
        else:
            print("you chose rock and computer chose scissor. You win!")
    elif a == "1":
        if b == 0:
            print("you chose paper and computer chose rock. You win!")
        elif b == 1:
            print("you chose paper and computer chose paper. It's a draw.")
        else:
            print("you chose paper and computer chose scissor. You lose.")
    elif a == "2":
        if b == 0:
            print("you chose scissor and computer chose rock. You lose.")
        elif b == 1:
            print("you chose scissor and computer chose paper. You win!")
        else:
            print("you chose scissor and computer chose scissor. It's a draw.")

#main()

def main2():
    import random

# Mapping numbers to choices
choices = ["Rock", "Paper", "Scissors"]

# Ask for user input
user_choice = int(input("Enter 0 for Rock, 1 for Paper, 2 for Scissors: "))

# Validate input
if user_choice < 0 or user_choice > 2:
    print("Invalid choice! Please enter 0, 1, or 2.")
else:
    # Computer's random choice
    computer_choice = random.randint(0, 2)

    print(f"You chose: {choices[user_choice]}")
    print(f"Computer chose: {choices[computer_choice]}")

    # Determine winner
    if user_choice == computer_choice:
        print("It's a draw!")
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        print("You win!")
    else:
        print("You lose!")

#main2()


def main3():
    
