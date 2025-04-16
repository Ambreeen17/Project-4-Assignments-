def main ():
    print("This program adds two numbers together");

    # Promt the user to enter two numbers
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    # calculate the sum of the two numbers
    sum = num1 + num2
    print(f"The sum of {num1} and {num2} is {sum}");


if __name__ == "__main__":
    main()