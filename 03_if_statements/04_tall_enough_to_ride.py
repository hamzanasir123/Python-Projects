



def main():
    print("This Program Tells You That You Are Enough Long To Ride Or Not!")
    userInput = input("How Long Are You In Foot:")
    userInput = float(userInput)
    minimumhight = 5
    if userInput >= minimumhight:
        print("You Are Tall Enough To Ride!")
    else :
        print("You Are Not Tall Enough To Ride!")


if __name__ == "__main__":
    main()        