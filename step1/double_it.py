def double_until_100():

    try:
        curr_value = int(input("Enter a number: "))

        if curr_value >= 100:
            print("The number is already 100 or greater.")
        else:
            while curr_value < 100:
                curr_value = curr_value * 2
                print(curr_value, end=" ")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

def main():
    double_until_100()
    
if __name__ == '__main__':
    main()