import random
import time

import keyboard


def dice_roll():
    print("Rolling dices...")
    time.sleep(3)

    print("---------------------------------------------------")
    roll_1 = random.randint(1, 6)
    roll_2 = random.randint(1, 6)
    print(f"Number on Dice 1: \t{roll_1} \nNumber on Dice 2: \t{roll_2} \nCombined result: \t{roll_1 + roll_2}")
    print("---------------------------------------------------")
    print("Press any key to roll again...\n")
    keyboard.read_key()

    dice_roll()


dice_roll()
