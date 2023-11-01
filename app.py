#

# import the random library
import random
# create a list of play options
play_options = ["rock", "paper", "scissors"]
# assign a random play to the computer
computer = random.choice(play_options)
# set player to False
player = False
# create a while loop to check the player input
while player == False:
    # set player to True
    player = input("rock, paper, scissors?")
    # check for a tie
    if player == computer:
        print("Tie!")
    # check for rock
    elif player == "rock":
        if computer == "paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    # check for paper
    elif player == "paper":
        if computer == "scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    # check for scissors
    elif player == "scissors":
        if computer == "rock":
            print("You lose!", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")
    # player was set to True, but we want it to be False so the loop continues
    player = False
    computer = random.choice(play_options)
