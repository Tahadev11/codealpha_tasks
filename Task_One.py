import random

def choose_word():
    # List of words to choose from
    words = ["python", "hangman", "developer", "computer", "programming", "algorithm", "function", "variable"]
    return random.choice(words)

def display_word(word, guessed_letters):
    # Display the word with underscores for unguessed letters
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def play_hangman():
    word = choose_word()
    guessed_letters = set()  # Set of letters guessed so far
    incorrect_guesses = 0
    max_incorrect_guesses = 6
    guessed_word = False
    
    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters.")
    
    while incorrect_guesses < max_incorrect_guesses and not guessed_word:
        print(f"\nCurrent word: {display_word(word, guessed_letters)}")
        print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")
        guess = input("Guess a letter: ").lower()

        # Validate the input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue
        
        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try again.")
            continue
        
        guessed_letters.add(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Oops! '{guess}' is not in the word.")
        
        # Check if the player has guessed all letters correctly
        guessed_word = all(letter in guessed_letters for letter in word)
        
    if guessed_word:
        print(f"\nCongratulations! You guessed the word '{word}' correctly!")
    else:
        print(f"\nGame Over! The word was '{word}'.")

if __name__ == "__main__":
    play_hangman()
