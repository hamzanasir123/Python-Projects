# Problem Statement
# Guess My Number

# I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high

# Enter a new number: 25 Your guess is too low

# Enter a new number: 40 Your guess is too low

# Enter a new number: 45 Your guess is too low

# Enter a new number: 48 Congrats! The number was: 48

MY_NUMBER = 55

def main():
    print("Guess My Number!")
    print("I Am Thinking Of a Number between 0 and 99")
    while True:
        answer = int(input("Enter a Guess:"))

        if answer == "":
            break
        
        if answer == MY_NUMBER:
            print("Congrats! The Number Was: 55")
            break
        elif answer > MY_NUMBER:
            print("Your guess is too high;")
            # answer = int(input("Enter a Guess:"))
        elif answer < MY_NUMBER:
            print("Your guess is too low;")
            # answer = int(input("Enter a Guess:"))
            
        


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()