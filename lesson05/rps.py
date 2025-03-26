import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

print('')

playerchoice = input('Enter ...\n1 for Rock\n2 for Paper\n3 for Scissors:\n\n')

player = int(playerchoice)

if player < 1 or player > 3:
    sys.exit("you must enter 1, 2, or 3.\n")

computerchoice = random.choice("123")

computer = int(computerchoice)

print("")
print("You chose " + str(RPS(player)).replace('RPS.', '') + ".")
print("Python chose " + str(RPS(computer)).replace('RPS.', '') + ".")
print("")

if player == computer:
    print("You Tied.")
elif player == ((computer + 1) % 3):
    print("You Win.")
else:
    print("You Lose.")

