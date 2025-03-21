# Problem Statement
# Use Python to calculate the number of seconds in a year, and tell the user what the result is in a nice print statement that looks like this (of course the value 5 should be the calculated number instead):

# There are 5 seconds in a year!

# You should use constants for this exercise -- there are 365 days in a year, 24 hours in a day, 60 minutes in an hour, and 60 seconds per minute.



def main():
    print("This Program Calculate The Seconds of The Given Years")
    userInput = input("Enter The Number Of Years To Convert Into Seconds:")
    userInput = int(userInput)
    days = 365
    hours = 24
    minutes = 60
    seconds = 60
    secondsInAYear = (hours * days) * (seconds * minutes)
    answer = userInput * secondsInAYear
    print(f"There Are {answer} Seconds In a Year!")

if __name__ == '__main__':
    main()

