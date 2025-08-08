def main():
    print("welcome to treasure hunt")
    print("your mission is to find the treasure")
    q = input("you\'re at a crossroad, where do you want to go? Type 'left' or 'right").lower()

    if q == "right":
        print("you fell into a hole. Game Over.")

    if q == "left":
        choice1 = input("do you want to swim or wait? Type 'swim' or 'wait'").lower()
        if choice1 == "wait":
            print("you died, a fucking shark ate you. Game Over.")
        elif choice1 == "swim":
            choice2 = input("which door do you want to open? Type 'red', 'blue' or 'yellow'").lower()
            if choice2 == "yellow":
                print("you found the treasure! you win!")
            elif choice2 == "red":
                print("you were captured by Orcs. Game Over.")
            elif choice2 == "Blue".lower():
                print("a really cute cat killed you. Game Over.")
            else:
                print("Ivalied Response.")
        else:
            print("Ivalied Response.")
    else:
        print("Ivalied Response.")
main()
