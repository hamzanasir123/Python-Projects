
MAX_LENGHT = 5

def shorten(lis):
    while len(lis) > MAX_LENGHT:
        pop_last_element = lis.pop()
        print(f"Remove Elements = {pop_last_element}")



def getlist():
    lis = []
    userInput = input("Please Enter an Element Of The List Or Press Enter To Stop:")
    while userInput != "":
        lis.append(userInput)
        userInput = input("Please Enter an Element Of The List Or Press Enter To Stop:")
    return lis


def main():
    lis = getlist()
    shorten(lis)
    print(lis)


if __name__ == '__main__':
    main()   