import random

# Word list for the game (who ever is incharge for this part replace and expand as neccesary)
words = ['visual', 'computer', 'coding', 'science', 'hello']

# Function to randomly select a word from the list
def get_word():
    return random.choice(words)

# Function to display the current state of the guessed word
def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

# Main game function that integrates all answer validation and game logic
def hangman():
    word = get_word()  # The word to be guessed
    guessed_letters = []  # Store all guessed letters
    attempts = 6  # Number of allowed wrong guesses
    correct_guesses = set()  # Store correctly guessed letters

    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters.")
    
    # Game loop
    while attempts > 0:
        # Show the current state of the word
        print(f"Word: {display_word(word, correct_guesses)}")
        print(f"Guessed Letters: {', '.join(guessed_letters)}")
        print(f"Remaining Attempts: {attempts}")

        # Get user input
        guess = input("Guess a letter: ").lower()

        # **Answer Part: Validating Input**
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print(f"You have already guessed '{guess}'. Try a different letter.")
            continue

        # Add the guess to the guessed_letters list
        guessed_letters.append(guess)

        # **Answer Part: Checking if the guess is correct**
        if guess in word:
            print(f"Good guess! The letter '{guess}' is in the word.")
            correct_guesses.add(guess)
        else:
            print(f"Sorry, the letter '{guess}' is not in the word.")
            attempts -= 1  # Decrease attempts on wrong guess

        # **Answer Part: Check for a Win**
        if all(letter in correct_guesses for letter in word):
            print(f"Congratulations! You guessed the word: {word}")
            break
    else:
        # Out of attempts, game over
        print(f"Game over! The correct word was: {word}") 

# Start the game
hangman()
