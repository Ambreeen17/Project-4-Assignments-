def main():
    print("This program converts temperature from Fahrenheit to Celsius");

    fahrenheit = float(input("Enter the temperature in Fahrenheit: "));
    celsius = (fahrenheit - 32) * 5.0/9.0;

    print(f"The temperature in Celsius is {celsius}");

if __name__ == "__main__":
    main()