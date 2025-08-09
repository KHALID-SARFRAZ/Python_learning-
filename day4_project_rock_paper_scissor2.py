
import random
def main():

    a = int(input("what do you choose? type 0 for" 
              "rock 1 for paper and 2 for scissors\n"))

    b = random.randint(0,2)
    
    if a >= 0 or a < 3:
        
        if a == b:
            print(f"You both chose {a}. its a draw")
        elif a > b:
            print(f"you chose {a}. and computer chose {b}. you win")
        else:
            print(f"you chose{a} and computer chose{b}. you loose")
    
    else:
        print("Enter a valid response!!!")
main()

