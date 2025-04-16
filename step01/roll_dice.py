import random

num_sides = 6

def main():
    die1 = random.randint(1, num_sides)
    die2 = random.randint(1, num_sides)
    
    total = die1 + die2
    
    print("Dice have", num_sides, "sides each.")
    print("First die:", die1)
    print("Second die:", die2)
    print("Total of two dice:", total)

if __name__ == '__main__':
    main()
