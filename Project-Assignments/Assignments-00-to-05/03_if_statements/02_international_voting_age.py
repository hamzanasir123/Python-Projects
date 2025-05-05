


def main():
    print("This Program Tells You That You Can Vote Or Not!")
    userInput = input("How Old Are You: ")
    userInput = int(userInput)
    peturksbouipo = 16
    stanlau = 25
    mayengua = 48
    if userInput >= peturksbouipo:
        print("You can vote in Peturksbouipo where voting age is 16,")
    else :
        print("You cannot vote in Peturksbouipo where voting age is 16,")
    if userInput >= stanlau:
        print("You can vote in Stanlau where voting age is 25,")
    else :
        print("You cannot vote in Stanlau where voting age is 25,")
    if userInput >= mayengua:
        print("You can vote in Mayengua where voting age is 48,")
    else :
        print("You cannot vote in Mayengua where voting age is 48,")

if __name__ == "__main__":
    main()        