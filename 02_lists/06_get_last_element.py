

def get_last_element(lis):
    print(lis[-1])



def getlist():
    lis = []
    userInput = input("Please Enter an Element Of The List Or Press Enter To Stop:")
    while userInput != "":
        lis.append(userInput)
        userInput = input("Please Enter an Element Of The List Or Press Enter To Stop:")
    return lis


def main():
    lis = getlist()
    get_last_element(lis)


if __name__ == '__main__':
    main()   