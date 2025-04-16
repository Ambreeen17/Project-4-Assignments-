import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors: ").lower()
    
    # Input validation
    while user not in ['r', 'p', 's']:
        print("Invalid choice. Please try again.")
        user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors: ").lower()
    
    computer = random.choice(['r', 'p', 's'])
    
    # Print choices
    print(f"\nYou chose: {get_choice_name(user)}")
    print(f"Computer chose: {get_choice_name(computer)}")
    
    if user == computer:
        result = 'Tie!'
    elif is_win(user, computer):
        result = 'You won!'
    else:
        result = 'You lost!'
    
    print(result)
    return result
    
def is_win(player, opponent):
    # return true if player wins
    # rock beats scissors, scissors beats paper, paper beats rock
    return (player == 'r' and opponent == 's') or \
           (player == 's' and opponent == 'p') or \
           (player == 'p' and opponent == 'r')

def get_choice_name(letter):
    # Helper function to convert letter to full name
    choices = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
    return choices.get(letter, 'Invalid choice')

if __name__ == "__main__":
    play()