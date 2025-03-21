
# Problem Statement
# In this program we show an example of using dictionaries to keep track of information in a phonebook.

def get_phone_numbers():
    phone_book = {}
    while True:
        name = input("Enter Your Name:")
        if name == "":
            break

        phone_no = input("Enter Your Phone Number:")
        phone_book[name] = phone_no

    return phone_book

def print_phone_book(phonebook):
    for name in phonebook:
        print(str(name) + " -> " + str(phonebook[name]))



def lookup_numbers(phonebook):
    while True:
        name = input("Enter name to lookup:")
        if name == "":
            break

        if name not in phonebook:
            print(f"{name} is not in the phonebook!")
        else:
            print(phonebook[name])




def main():
    phonebook = get_phone_numbers()
    print_phone_book(phonebook)
    lookup_numbers(phonebook)
    
if __name__ == '__main__':
    main()