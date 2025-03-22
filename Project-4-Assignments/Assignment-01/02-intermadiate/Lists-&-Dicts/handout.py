# Problem #1: List Practice
# Now practice writing code with lists! Implement the functionality described in the comments below.

# def main(): # Create a list called fruit_list that contains the following fruits: # 'apple', 'banana', 'orange', 'grape', 'pineapple'.

# # Print the length of the list.


# # Add 'mango' at the end of the list. 


# # Print the updated list.
# Problem #2: Index Game
# As a warmup, read this code and play the game a few times. Use this mental model of the list:

# Objective:
# Create a Python program that helps you practice accessing and manipulating elements in a list. This exercise will help you get comfortable with indexing, slicing, and modifying list elements.

# Instructions:
# Initialize a List:
# Create a list with at least 5 different elements. They can be numbers, strings, or a mix of both.

# Accessing Elements:
# Write a function that:

# Accepts a list and an index as inputs.
# Returns the element at the specified index.
# If the index is out of range, return an appropriate message.
# Modifying Elements:
# Write a function that:

# Accepts a list, an index, and a new value as inputs.
# Replaces the element at the specified index with the new value.
# If the index is out of range, return an appropriate message.
# Slicing the List:
# Write a function that:

# Accepts a list, a start index, and an end index as inputs.
# Returns a new list containing the elements from the start index up to (but not including) the end index.
# Handles cases where the indices are out of range.
# Game Interaction:
# Create a simple text-based game that:

# Prompts the user to select an operation (access, modify, slice).
# Asks for the necessary inputs (index, new value, etc.).
# Displays the result and the updated list.





def main():
    # Problem 1
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    print(len(fruit_list))
    fruit_list.append('mango')
    print(fruit_list)

    # Problem 2
    lis = ["Hamza", "Nasir", 24, 5.5 , False ]
    print(lis)


    def access_element(lis, index):
        if index >= len(lis):
            return "Index out of range"
        return lis[index]



    def modify_elements(lis, index, new_value):
        if index >= len(lis):
            return "Index out of range"
        lis[index] = new_value
        return lis
    

    def slicing_list(lis, start, end):
        if start >= len(lis) or end >= len(lis):
            return "Index out of range"
        return lis[start:end]
    

    def game():
        print("Select an operation:")
        print("1. Access")
        print("2. Modify")
        print("3. Slice")
        choice = int(input())
        if choice == 1:
            index = int(input("Enter index: "))
            print(access_element(lis, index))
        elif choice == 2:
            index = int(input("Enter index: "))
            new_value = input("Enter new value: ")
            print(modify_elements(lis, index, new_value))
        elif choice == 3:
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            print(slicing_list(lis, start, end))
        else:
            print("Invalid choice")


    game()




if __name__ == "__main__":
    main()