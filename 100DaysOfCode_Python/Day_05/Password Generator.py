letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))\

#Easy Version
password = ''
import random

for char in range (0, nr_letters):
    password += random.choice(letters)

for char in range (0, nr_numbers):
    password += random.choice(numbers)

for char in range (0, nr_symbols):
    password += random.choice(symbols)

print(f"Easy Version: Your password could be: {password}")

#Hard Version
password_list = []
import random

for char in range (0, nr_letters):
    password_list.append(random.choice(letters))

for char in range (0, nr_numbers):
    password_list.append(random.choice(numbers))

for char in range (0, nr_symbols):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

final_password = ''
for char in password_list:
    final_password += char

print(f"Hard Version: Your password could be: {final_password}")

#No User Inputs
password_list = []
import random

for char in range (0, 5):
    password_list.append(random.choice(letters))

for char in range (0, 3):
    password_list.append(random.choice(numbers))

for char in range (0, 4):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

final_password = ''
for char in password_list:
    final_password += char

print(f"No Inputs Needed: Your password could be: {final_password}")