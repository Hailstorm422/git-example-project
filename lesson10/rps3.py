import sys
import random
from enum import Enum

def play_rps():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3
        
    playerchoice = input('\nEnter ...\n1 for Rock\n2 for Paper\n3 for Scissors:\n\n')

    if (playerchoice not in ["1","2","3"]):
        print("you must enter 1, 2, or 3.\n")
        return play_rps()
    player = int(playerchoice)

    computerchoice = random.choice("123")

    computer = int(computerchoice)

    print("\nYou chose " + str(RPS(player)).replace('RPS.', '') + ".")
    print("Python chose " + str(RPS(computer)).replace('RPS.', '') + ".\n")

    if player == computer:
        print("You Tied.")
    elif player == ((computer + 1) % 3):
        print("You Win.")
    else:
        print("You Lose.")

    print("\nPlay again?")
    while True:
        playagain = input("\nY for Yes or \nQ to Quit \n")
        if playagain.lower() not in ["y", "q"]:
            continue
        else:
            break

    if playagain.lower() == "y":
        return play_rps()
    else:
        print("\nThanks for playing, loser!\n")
        sys.exit("Bye!\n")

play_rps()
