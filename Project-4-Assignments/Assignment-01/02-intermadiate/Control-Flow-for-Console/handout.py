# Problem: High Low
# We want you to gain more experience working with control flow and Booleans in Python. To do this, we are going to have you develop a game! The game is called High-Low and the way it's played goes as follows:

# Two numbers are generated from 1 to 100 (inclusive on both ends): one for you and one for a computer, who will be your opponent. You can see your number, but not the computer's!

# You make a guess, saying your number is either higher than or lower than the computer's number

# If your guess matches the truth (ex. you guess your number is higher, and then your number is actually higher than the computer's), you get a point!

# These steps make up one round of the game. The game is over after all rounds have been played.

# We've provided a sample run below.

import random

ROUNDS = 5

def main():
    print("Welcome to High Low!")
    print("You will be playing against the computer.")
    print("The game will consist of 5 rounds.")
    print("You will be given a number and you must guess if the computer's number is higher or lower.")
    print("If you guess correctly, you get a point!")
    print("\n")
    print("Let's begin!")
    print("\n")

    POINTS = 0

    while True:
        for i in range(ROUNDS):
            print(f"Round {i + 1}")
            user = random.randint(1, 100)
            computer = random.randint(1, 100)
            print("Your number is:", user)
            guess = input("Do you think the computer's number is higher or lower? (h/l) ")
            if guess == "h" and computer > user:
                print(f"You are correct! Computer's number was: {computer}")
                POINTS += 1
                print(f"Your points: {POINTS}")
            elif guess == "l" and computer < user:
                print(f"You are correct! Computer's number was: {computer}")
                POINTS += 1
                print(f"Your points: {POINTS}")
            else:
                print("You are incorrect.")
            if i > ROUNDS:
                break
        break
    print("\n")
    print("Game Over!")
    print(f"Your total points: {POINTS}")
    print("\n")
    if POINTS <= 2:
        print("Better luck next time!")
    elif POINTS == 5:
        print("Wow! You played perfectly!")
    else:
        print("Good job!")
    
    print("\n")
    print("Thanks for playing!")






if __name__ == "__main__":
    main()