import random

def hangman():
    words = ['apple', 'banana', 'cherry', 'date', 'elder']
    word = random.choice(words)
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect = 6

    print("Welcome to Hangman!")
    print(f"You have {max_incorrect} incorrect guesses allowed.")

    while incorrect_guesses < max_incorrect:
        # Display the current state of the word
        display_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
        print("\nWord: ", ' '.join(display_word))

        # Check if the player has guessed the word
        if '_' not in display_word:
            print("Congratulations! You guessed the word correctly!")
            break

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetic character.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess not in word:
            incorrect_guesses += 1
            print(f"Incorrect! You have {max_incorrect - incorrect_guesses} guesses left.")

    else:
        print(f"Game over! The word was '{word}'.")

if __name__ == "__main__":
    hangman()