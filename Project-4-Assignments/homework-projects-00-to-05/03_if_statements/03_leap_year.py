


def main():
    print("This program tells you that a leap year or not!")
    userInput = input("Plaese Enter The Year:")
    userInput = int(userInput)
    if userInput % 4 == 0:
        if userInput % 100 == 0:
            if userInput % 400 == 0:
                print("That's a Leap Year.")
            else :
                print("That's Not a Leap Year.")
        else :
            print("That's a Leap Year.")
    else : 
        print("That's Not a Leap Year.")



if __name__ == "__main__":
    main()        