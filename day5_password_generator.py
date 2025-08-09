
# letters = ['a','b','c','d','e','f','A','B','C','D','E','F']
# numbers = ['0','1','2','3','4','5','6','7','8','9']
# symbols = ['!','#','$','%','&','(',')','*','+']

# import random

# print("Welcome to the PyPassword Generator!")
# nr_letters = int(input("How many letters would you like in your password?\nEnter amount:  "))
# nr_symbols = int(input("How many symbols would you like?\nEnter amount: "))
# nr_numbers = int(input("How many numbers would you like?\nEnter amount: "))

# # Easy Level:

# password = ""

# for i in range(0,nr_letters):
#     password += random.choice(letters)

# for i in range(0,nr_symbols):
    
#     password += random.choice(symbols)

# for i in range(0,nr_numbers):
     
#     password += random.choice(numbers)

# print(f"Your Password is: {password}")


letters = ['a','b','c','d','e','f','A','B','C','D','E','F']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']

import random

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\nEnter amount:  "))
nr_symbols = int(input("How many symbols would you like?\nEnter amount: "))
nr_numbers = int(input("How many numbers would you like?\nEnter amount: "))

# Easy Level:

password = []

for i in range(0,nr_letters):
    password.append(random.choice(letters))

for i in range(0,nr_symbols):
    
    password.append(random.choice(symbols))

for i in range(0,nr_numbers):
     
    password.append(random.choice(numbers))
    random.shuffle(password)

print(f"Your Password is: {password}")

passwordNew = ""

for i in password:
    passwordNew += i
    
print("your passoword is: ",passwordNew)
