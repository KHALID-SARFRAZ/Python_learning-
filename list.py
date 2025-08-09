
import random
list = ["ahmad","khalid","ammar","imbesat","arman"]

def main():
    a = random.randint(0, len(list)-1)

    if a == 0:
        print("ahmad")
    elif a == 1:
        print("khalid")
    elif a == 2:
        print("ammar")
    elif a == 3:
        print("imbesat")
    elif a == 4:
        print("arman")
    else:
        print("Invalid Response")
main()

#or you can use random.choice(sequence) to get a random element from the list

def main2():
    a = random.choice(list)
    print(a)
main2()

# second method is good but first method is lengthy and not efficient
#here is another way to do it using index of list

def main3():
    a = random.randint(0, len(list)-1)
    print(list[a])
main3()