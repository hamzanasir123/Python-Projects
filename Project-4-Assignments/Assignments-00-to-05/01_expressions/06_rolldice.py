# Problem Statement
# Simulate rolling two dice, and prints results of each roll as well as the total.

import random

def rolling():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    print(f"""

Dice One is {dice1}
Dice Two is {dice2}
Total Is {dice1 + dice2}
""")

def main():
    rolling()



if __name__ == '__main__':
    main()