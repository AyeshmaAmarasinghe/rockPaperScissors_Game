import random

choices = ["rock", "paper", "scissors"]

computer = random.choice(choices)
player = None

while player not in choices:
    player = input("rock, paper or scissors ? : ").lower()

if player == computer:
    print("Computer : ", computer)
    print("Player : ", player)
    print("Tie!")
elif player == "rock":
    if computer == "scissors":
        print("Computer : ", computer)
        print("Player : ", player)
        print("You win !")
    elif computer == "paper":
        print("Computer : ", computer)
        print("Player : ", player)
        print("You lose!")
elif player == "paper":
    if computer == "rock":
        print("Computer : ", computer)
        print("Player : ", player)
        print("You win")
    elif computer == "scissors":
        print("Computer : ", computer)
        print("Player : ", player)
        print("You win!")
elif player == "scissors":
    if computer == "rock":
        print("Computer : ", computer)
        print("Player : ", player)
        print("You lose!")
    elif computer == "paper":
        print("Computer : ", computer)
        print("Player : ", player)
        print("You win!")