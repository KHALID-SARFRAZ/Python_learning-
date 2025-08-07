def main():
    print("welcome to python delivery service!!")
    size = input("what size of pizza do you want? S,M or L: ")
    extra_cheese = input("do you want extra cheese? Y or N: ")
    pepperoni = input("do you want pepperoni? Y or N:")

    bill = 0

    if size == "S":
        bill += 15
    elif size == "M":
        bill += 20
    else: 
        bill += 25
    
    if extra_cheese == "Y":
        if size == "S":
            bill += 3
        elif size == "M":
            bill += 5
        else:
            bill += 7

    if pepperoni == "Y":
        if size == "S":
            bill += 2
        elif size == "M":
            bill += 4
        else:
            bill += 6
    print(f"your final bill is: ${bill}")
main()