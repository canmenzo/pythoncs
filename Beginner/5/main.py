
### One of the niches of computer science where rock paper and scissors
### game's output can be calculated by using remainders in math
### also known as modulo operator in python.
### Reference: https://www.geeksforgeeks.org/what-is-a-modulo-operator-in-python/
# Computer     Human       (computer - human) % 3
# 0 Rock       0 Rock                0        0 # Draw
# 0 Rock       1 Paper              -1        2 # Human
# 0 Rock       2 Scissors           -2        1 # Computer
# 1 Paper      0 Rock                1        1 # Computer
# 1 Paper      1 Paper               0        0 # Draw
# 1 Paper      2 Scissors           -1        2 # Human
# 2 Scissors   0 Rock                2        2 # Human
# 2 Scissors   1 Paper               1        1 # Computer
# 2 Scissors   2 Scissors            0        0 # 

# imports
import random
import getpass

# function for outcome computer vs player
def outcome(game, namePlayer1, namePlayer2, choiceHuman1, choiceHuman2):
    if game == 0:
        print(f"The {namePlayer1} has chosen `{choiceHuman1}`")
        print(f"The {namePlayer2} has chosen `{choiceHuman2}`")
        print("The game is a draw!")
    elif game == 1:
        print(f"The {namePlayer1} has chosen `{choiceHuman1}`")
        print(f"The {namePlayer2} has chosen `{choiceHuman2}`")
        print(f"The {namePlayer1} won!")
    elif game == 2:
        print(f"The {namePlayer1} has chosen `{choiceHuman1}`")
        print(f"The {namePlayer2} has chosen `{choiceHuman2}`")
        print(f"The {namePlayer2} won!")
    else:
        print("You have entered an invalid choice.")

# input/exit validation and assing int value to choice of RPS
def exitVal(z):
    try:
        if z == 'exit':
            print("Exiting...")
            exit()
        elif z.lower() == "rock":
            z = 0
            return z
        elif z.lower() == "paper":
            z = 1
            return z
        elif z.lower() == "scissors":
            z = 2
            return z
    except ValueError:
        print("Please enter a valid input.")

# welcome statement
print("Welcome to the Rock Paper Scissors Game!")

# main loop
while True:
    # getting input for vs player or vs npc/computer
    gameChoice = input("Would you like to play against the computer or against another player? (computer,player): \n")
    # playing against npc/computer
    if gameChoice == "computer":
          # player names if against computer, its generic variable.
        namePlayer1 = "Computer"
        namePlayer2 = "Human Player"

         # input for human1
        choiceHuman2 = input("Enter your choice (rock, paper, scissors) or (type 'exit' to quit):\n")
        answer2 = exitVal(choiceHuman2)

        # generate number between 0 and 2 (possibilities: 0,1,2)
        pcAnswer = random.randint(0, 2)

        # assign random num to a choice
        if pcAnswer == 0:
            choiceHuman1 = "rock"
        elif pcAnswer == 1:
            choiceHuman1 = "paper"
        elif pcAnswer == 2:
            choiceHuman1 = "scissors"

        # calculate game outcome
        game = (pcAnswer - answer2) % 3

        # call outcome function
        outcome(game, namePlayer1, namePlayer2, choiceHuman1, choiceHuman2)

    elif gameChoice == "player":

         # input names
        namePlayer1 = input("Enter name for Player 1:")
        namePlayer2 = input("Enter name for Player 2:")

        # player1 input
        choiceHuman1 = getpass.getpass(f"{namePlayer1}, Please enter your choice (rock, paper, scissors) or (type 'exit' to quit):\n")
        answer1 = exitVal(choiceHuman1)

        # player2 input
        choiceHuman2 = getpass.getpass(f"{namePlayer2}, Please enter your choice (rock, paper, scissors) or (type 'exit' to quit):\n")
        answer2 = exitVal(choiceHuman2)

        # calculate game outcome
        game = (answer1 - answer2) % 3

        # call outcome function
        outcome(game, namePlayer1, namePlayer2, choiceHuman1, choiceHuman2)
