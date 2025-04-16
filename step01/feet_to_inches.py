inches_feet = 12

def main():
    feet = float(input("Enter number of feet: "))
    inches = feet * inches_feet
    print("That is ", str(inches), " inches.")

if __name__ == '__main__':
    main()