import random

def high_low_game():
    NUM_ROUNDS = 5
    score = 0
    
    print("Welcome to the High-Low Game!")
    print("--------------------------------")
    
    for round_num in range(1, NUM_ROUNDS + 1):
        # Generate numbers
        computer_num = random.randint(1, 100)
        your_num = random.randint(1, 100)
        
        print(f"\nRound {round_num}")
        print(f"Your number is {your_num}")
        
        # Get user input with validation
        while True:
            guess = input("Do you think your number is higher or lower than the computer's?: ").lower()
            if guess in ['higher', 'lower']:
                break
            print("Please enter either 'higher' or 'lower'")
        
        # Determine outcome
        if your_num > computer_num:
            correct_answer = 'higher'
        elif your_num < computer_num:
            correct_answer = 'lower'
        else:
            correct_answer = None  # tie goes to computer
        
        # Check if user was right
        if guess == correct_answer:
            score += 1
            print(f"You were right! The computer's number was {computer_num}")
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_num}")
        
        print(f"Your score is now {score}")
    
    # Final message with conditional ending
    print("\nThanks for playing!")
    
    if score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

# Run the game
high_low_game()