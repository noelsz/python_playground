import random

random_number = random.randint(1, 100)

print("I thought of a number between 1 and 100, try to guess it!")


def guess_number(number):
    guess = int(input("Your guess: "))
    if guess < number:
        print("Higher!")
        return False
    elif guess > number:
        print("Lower!")
        return False
    else:
        print("Your guess is correct!")
        return True


found = False
while not found:
    found = guess_number(random_number)



