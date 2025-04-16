import random
from words import words

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    used_letters = set()
    lives = 6  # Added lives counter

    while len(word_letters) > 0 and lives > 0:
        print('\nYou have', lives, 'lives left')
        print('Used letters:', ' '.join(sorted(used_letters)))
        current_word = [letter if letter in used_letters else '_' for letter in word]
        print('Current word:', ' '.join(current_word))

        user_letter = input("Guess a letter: ").upper()
        
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print('Letter is not in the word!')
        elif user_letter in used_letters:
            print("You've already guessed that letter. Try again.")
        else:
            print("Invalid input. Please enter a letter from A-Z.")

    if lives == 0:
        print('\nYou lost! The word was:', word)
    else:
        print('\nCongratulations! You guessed the word:', word)

if __name__ == "__main__":
    hangman()