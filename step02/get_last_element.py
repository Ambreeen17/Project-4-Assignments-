def get_lst():
    lst = [] 
    while True:
        elem = input("Please enter an element of the list or press enter to stop: ")
        if elem == "":  # If the user presses Enter, stop the loop
            break
        lst.append(elem)
    return lst

def get_last_element(lst):
    if lst:  # Check if the list is not empty
        print("The last element in the list is:", lst[-1])  # Print the last element
    else:
        print("The list is empty.")  # Handle the case where the list is empty

def main():
    lst = get_lst() 
    get_last_element(lst)

if __name__ == '__main__':
    main()