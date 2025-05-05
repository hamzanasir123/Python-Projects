

def get_first_element(lis):
    print(lis[0])



def getlist():
    lis = []
    userInput = input("Please Enter an Element Of The List Or Press Enter To Stop:")
    while userInput != "":
        lis.append(userInput)
        userInput = input("Please Enter an Element Of The List Or Press Enter To Stop:")
    return lis


def main():
    lis = getlist()
    get_first_element(lis)


if __name__ == '__main__':
    main()   