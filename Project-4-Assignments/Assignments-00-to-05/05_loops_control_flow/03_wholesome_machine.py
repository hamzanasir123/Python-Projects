# Problem Statement
# Write a program which prompts the user to type an affirmation of your choice (we'll use "I am capable of doing anything I put my mind to.") until they type it correctly. Sometimes, especially in the midst of such uncertain times, we just need to be reminded that we are resilient, capable, and strong; this little Python program may be able to help!

# Here's a sample run of the program (user input is in blue):

# Please type the following affirmation: I am capable of doing anything I put my mind to. Hmmm That was not the affirmation. Please type the following affirmation: I am capable of doing anything I put my mind to. I am capable of doing anything I put my mind to. That's right! :)

# Note that you can call input() with no prompt and it will still wait for a user to type something!


def main():
    affirmation = "I am capable of doing anything I put my mind to."
    user_input = input("Please type the following affirmation: ")

    while user_input != affirmation:
        print("Hmmm That was not the affirmation.")
        user_input = input("Please type the following affirmation: ")
        if user_input == "":
            break
        print("That's right! :)")
    
if __name__ == '__main__':
    main()