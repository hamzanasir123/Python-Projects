

def sum(numbers):
    total = 0
    for number in numbers:
        total += number

    return total



def main():
    listOfNumbers = [1,2,3,4,5,6,7,8,9]
    answer = sum(listOfNumbers)
    print(answer)



if __name__ == '__main__':
    main()    