

import random

print("Welcome to the Guess Number Game!")


def guess_number():
    number = random.randint(1, 100)
    guess = None
    attempts = 0
    while guess != number:
        guess = int(input("Enter your guess: "))
        attempts += 1
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
    print(f"Congratulations! You guessed the number in {attempts} attempts.")


guess_number()