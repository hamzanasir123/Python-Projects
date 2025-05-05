# Problem Statement
# Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.

# Here's a sample run of the program (user input is in bold italics):

# Please enter an integer to be divided: 5

# Please enter an integer to divide by: 3

# The result of this division is 1 with a remainder of 2


def main():
    print("This Program Gives The Reminder Of Division!")
    num1 = input("Please enter an integer to be divided:")
    num1 = float(num1)
    num2 = input("Please enter an integer to divide by:")
    num2 = float(num2)
    answer = num1 // num2
    reminder = num1 % num2
    print(f"The Result Of This Division is {answer} with a Reminder Of {reminder}")






if __name__ == '__main__':
    main()