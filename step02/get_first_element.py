def get_lst():
    lst = [] 
    while True:
        elem = input("Please enter an element of the list or press enter to stop: ")
        if elem == "":  # If the user presses Enter, stop the loop
            break
        lst.append(elem)
    return lst

def get_first_element(lst):
    if lst:  # Check if the list is not empty
        print("The first element in the list is:", lst[0])  # Print the first element
    else:
        print("The list is empty.")  # Handle the case where the list is empty

def main():
    lst = get_lst() 
    get_first_element(lst)

if __name__ == '__main__':
    main()