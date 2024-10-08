import random


def rps(player, computer):

    if player == computer:
        return 'Draw!'
    elif (player == 'rock' and computer == 'scissors') or (player == 'paper' and computer == 'rock') or (player == 'scissors' and computer == 'paper'):
        return 'Player wins!'
    else:
        return 'Computer wins!'

print('Rock, Paper, Scissors!')
player = input("Player: ")
computer = random.choice(['rock', 'paper', 'scissors'])
print('Computer: ' + computer)
print(rps(player, computer))