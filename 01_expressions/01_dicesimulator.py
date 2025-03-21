
# Problem Statement

# Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works.

import random
NUM_SIDES = 6

def rolling():
    dice1 = random.randint(1, NUM_SIDES)
    dice2 = random.randint(1, NUM_SIDES)
    total = dice1 + dice2
    print(f"Dice One is {dice1},Dice Two is {dice2} Total Is {total}")


def main():
   rolling()
   rolling()
   rolling()




if __name__ == '__main__':
    main()