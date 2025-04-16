def main():
    # Create a list called fruit_list that contains the following fruits:
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    
    # Print the length of the list
    print("Length of the list:", len(fruit_list))
    
    # Add 'mango' at the end of the list
    fruit_list.append('mango')
    
    # Print the updated list
    print("Updated list:", fruit_list)

if __name__ == "__main__":
    main()



def access_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Index out of range!"

def modify_element(lst, index, new_value):
    try:
        lst[index] = new_value
        return "Element modified successfully!"
    except IndexError:
        return "Index out of range!"

def slice_list(lst, start, end):
    try:
        return lst[start:end]
    except IndexError:
        return "Invalid indices for slicing!"

def main():
    # Initialize a list with 5 elements
    game_list = [10, 20, 30, 40, 50]
    
    print("Welcome to the List Indexing Game!")
    print("Starting list:", game_list)
    
    while True:
        print("\nOptions:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            index = int(input("Enter index to access: "))
            result = access_element(game_list, index)
            print("Result:", result)
            print("Current list:", game_list)
        
        elif choice == '2':
            index = int(input("Enter index to modify: "))
            new_value = input("Enter new value: ")
            result = modify_element(game_list, index, new_value)
            print(result)
            print("Updated list:", game_list)
        
        elif choice == '3':
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            result = slice_list(game_list, start, end)
            print("Slice result:", result)
            print("Original list remains:", game_list)
        
        elif choice == '4':
            print("Thanks for playing!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()