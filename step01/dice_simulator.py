import random

num_sides = 6

def roll_dice():
    die1 = random.randint(1, num_sides)
    die2 = random.randint(1, num_sides)

    total = die1 + die2
    print("Total number of dice is: ", total)

def main():
    die1 = 7
    print("Die1 in main starts as ", str(die1))
    roll_dice()
    roll_dice()
    roll_dice()
    print("Die1 in main is ", str(die1))

if __name__ == "__main__":
    main()