import random 

print("Welcome to the Password Generator!")

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+[]}{|;:,.<>?"
number = input("Amount of passwords to generate: ")
number = int(number)
length = input("Length of passwords: ")
length = int(length)

print("\nHere are your passwords: ")
for pwd in range(number):
    password = ""
    for c in range(length):
        password += random.choice(chars)
    print(password)