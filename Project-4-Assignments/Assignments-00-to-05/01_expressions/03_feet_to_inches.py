# Problem Statement
# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.



def main():
    print("This Program Converts Feet To Inches.")
    userInput = input("Enter Feet To Convert In Inches: ")
    userInput = int(userInput)
    answer = userInput * 12
    print(f"{userInput} Feet Is {answer} Inches.")



if __name__ == '__main__':
    main()