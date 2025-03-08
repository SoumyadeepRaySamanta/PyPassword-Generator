# This is a password generator based on Python 3.
# Written by Soumyadeep Ray Samanta.

import random
import string

# List of Characters
print("Welcome to the Password Generator!")
lowerCase = string.ascii_lowercase
upperCase = string.ascii_uppercase
numbers = string.digits
symbols = string.punctuation

# If user needs random number of characters:
userinput = int(input("Enter the length of the password: "))

# Ensuring at least one character from each category
lowerCase_letters = random.randint(1, userinput - 3)
upperCase_letters = random.randint(1, userinput - lowerCase_letters - 2)
N_numbers = random.randint(1, userinput - lowerCase_letters - upperCase_letters - 1)
N_symbols = userinput - (lowerCase_letters + upperCase_letters + N_numbers)  # Remaining characters

# If user needs particular number of characters:
# lowerCase_letters = int(input("Number of lowercase letters you like in your password: "))
# upperCase_letters = int(input("Number of uppercase letters you like in your password: "))
# N_numbers = int(input("Number of numbers you like in your password: "))
# N_symbols = int(input("Number of symbols you like in your password: "))

# Generate Password
password_list = []

for char in range(0, lowerCase_letters):
    password_list += random.choice(lowerCase)

for char in range(0, upperCase_letters):
    password_list += random.choice(upperCase)

for char in range(0, N_numbers):
    password_list += random.choice(numbers)

for char in range(0, N_symbols):
    password_list += random.choice(symbols)

# Shuffle Password
random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")
print("Thank you for using Password Generator!")
