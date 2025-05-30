import sys
from rps import rps
from guess_number import guess_number

#Arcade
def play_game(name='PlayerOne'):
    welcome_back = False

    while True:
        if welcome_back == True:
            print(f"\n{name}, welcome back to the arcade!.\n\n")
        
        playerchoice = input(
            "\nPlease choose a game:\n1 = Rock\ Paper Scissors\n2 = Guess My Number\n\nOr press \"x\" to exit the Arcade\n\n"
            )

        if (playerchoice not in ["1","2","x"]):
            print(f"{name}, please enter 1, 2, or x.\n")
            return play_game(name)

        welcome_back = True

        if playerchoice == "1":
            rock_paper_scissors = rps(name)
            rock_paper_scissors()
        elif playerchoice == "2":
            guess_my_number = guess_number(name)
            guess_my_number()
        else:
            print("\nThanks for playing, loser}!\n")
            sys.exit(f"Bye, {name}!\n")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description = "Provides a personalized game experience."
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required = True, help="The name of the person playing the game."
    )

    args = parser.parse_args()

    print(f"\n{args.name}, welcome to the Arcade!")
    play_game(args.name)


