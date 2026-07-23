#Rock Paper Scissors

import random

choices = ["rock", "paper", "scissors"]

while True:
    player = input("Enter rock, paper or scissors (or exit): ")
    if player == "exit":
        break

    computer = random.choice(choices)
    print(f"Computer choose : {computer}")

    if player == "rock" and computer == "scissors":
        print("Player wins")
    elif player == "scissors" and computer == "paper":
        print("Player wins")
    elif player == "paper" and computer == "rock":
        print("Player wins")
    elif player == "paper" and computer == "scissors":
        print("Computer wins")
    elif player == "scissors" and computer == "rock":
        print("Computer wins")
    elif player == "rock" and computer == "paper":
        print("Computer wins")
    elif player == computer:
        print("It's a draw")
        