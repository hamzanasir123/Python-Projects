



def add_three_copies(mylist, data):
    for i in range(3):
        mylist.append(data)


def main():
    userInput = input("Enter AnyThing To Copy:")
    mylist = []
    add_three_copies(mylist,userInput)
    print(mylist)




if __name__ == '__main__':
    main()         
