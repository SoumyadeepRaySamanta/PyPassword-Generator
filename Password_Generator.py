import random
import string

print("Welcome to the Password Generator!")
lowerCase = string.ascii_lowercase
upperCase = string.ascii_uppercase
numbers = string.digits
symbols = string.punctuation

userinput = int(input("Enter the length of the password: "))

lowerCase_letters = 0
upperCase_letters = 0
N_numbers = 0
N_symbols = 0

lowerCase_letters += random.randint(1, userinput+1)
userinput -= lowerCase_letters

upperCase_letters += random.randint(1, userinput+1)
userinput -= upperCase_letters

N_numbers += random.randint(1, userinput+1)
userinput -= N_numbers

N_symbols += random.randint(1, userinput+1)
userinput -= N_symbols

password_list = []

for char in range(0, lowerCase_letters):
    password_list += random.choice(lowerCase)

for char in range(0, upperCase_letters):
    password_list += random.choice(upperCase)

for char in range(0, N_numbers):
    password_list += random.choice(numbers)

for char in range(0, N_symbols):
    password_list += random.choice(symbols)

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")
print("Thank you for using Password Generator!")