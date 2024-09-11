import random
import string
import time


def generate_password(length, use_uppercase, use_numbers, use_special_characters):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special_characters:
        characters += string.punctuation

    return ''.join(random.choice(characters) for _ in range(0, length))


print("Password Generator")
print("------------------")

length = int(input("Set your password length: "))
use_uppercase = input("Do you want to include uppercase letters? (y/n): ").lower() == 'y'
use_numbers = input("Do you want to include numbers? (y/n): ").lower() == 'y'
use_special_characters = input("Do you want to include special characters? (y/n): ").lower() == 'y'

print("------------------")
print("Your generated password:")
print(generate_password(length, use_uppercase, use_numbers, use_special_characters))
print("------------------")
