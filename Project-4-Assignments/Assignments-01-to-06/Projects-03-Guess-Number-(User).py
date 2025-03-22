

import random

print("Welcome to the Guess Number Game!")
print("I'm thinking of a number between 1 and 100.")
print("Can you guess what it is?")



def computer_guess_number():
    number = int(input("Enter a number between 1 and 100: "))
    low = 1
    high = 100
    guess = None
    attempts = 0
    while guess != number:
        guess = random.randint(low, high)
        attempts += 1
        print(f"The computer guesses: {guess}")
        if guess < number:
            print("Too low!")
            low = guess + 1
        elif guess > number:
            print("Too high!")
            high = guess - 1
    print(f"Congratulations! The computer guessed the number in {attempts} attempts.")


computer_guess_number()