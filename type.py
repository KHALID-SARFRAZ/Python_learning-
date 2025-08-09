def main():
    a = int(input("enter a number: "))
    b = int(input("enter another number:"))

    choice = input("what operation do you want to perfome?")

    if choice == "+":
        print(f"{a} + {b} = {a + b}")
    elif choice == "-":
        print(f"{a} - {b} = {a - b}")
    elif choice == "*":
        print(f"{a} * {b} = {a * b}")
    elif choice == "/":
        print(f"{a} / {b} = {a / b}")
    else:
        print("Invalid operation. Please try again.")
main()

