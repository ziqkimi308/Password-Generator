"""
********************************************************************************
* Project Name:  Password Generator
* Description:   This project generates a secure, random password based on user input
* Author:        ziqkimi308
* Created:       2024-12-05
* Updated:       2024-12-05
* Version:       1.0
********************************************************************************
"""

from password_bank import letters, symbols, numbers
import random

print("Welcome to the Password Generator!")
numb_letter = int(input("Enter number of letters: "))
numb_numbers = int(input("Enter number of numbers: "))
numb_symbols = int(input("Enter number of symbols: "))

password = []
for i in range(1, numb_letter + 1):
    password += random.choice(letters)

for i in range(1, numb_numbers + 1):
    password += random.choice(numbers)

for i in range(1, numb_symbols + 1):
    password += random.choice(symbols)

# Shuffle the password
random.shuffle(password)

# Convert list to string
password_string = ""
for char in password:
    password_string += char

# Print password string
print(f"Password: {password_string}")