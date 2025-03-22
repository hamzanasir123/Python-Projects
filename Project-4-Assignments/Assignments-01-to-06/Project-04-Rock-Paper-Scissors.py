

import random


def rock_paper_scissors():
    print("Welcome to the Rock, Paper, Scissors Game!")
    print("Choose rock, paper, or scissors.")
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    user_choice = input("Enter your choice: ").lower()
    print(f"The computer chooses: {computer_choice}")
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "rock":
        if computer_choice == "paper":
            print("You lose!")
        else:
            print("You win!")
    elif user_choice == "paper":
        if computer_choice == "scissors":
            print("You lose!")
        else:
            print("You win!")
    elif user_choice == "scissors":
        if computer_choice == "rock":
            print("You lose!")
        else:
            print("You win!")
    else:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        rock_paper_scissors()


rock_paper_scissors()