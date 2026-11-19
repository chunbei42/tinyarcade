import random

WORDS = [
    "python",
    "github",
    "package",
    "terminal",
    "keyboard",
    "computer",
    "hangman",
    "library",
    "cityu"
]

MAX_WRONG_GUESSES = 6


def choose_word():
    return random.choice(WORDS)


def display_word(secret_word, guessed_letters):
    return " ".join(
        letter if letter in guessed_letters else "_"
        for letter in secret_word
    )


def play():
    secret_word = choose_word()
    guessed_letters = set()
    wrong_guesses = 0

    print("\n=== Hangman ===")
    print("Guess the secret word one letter at a time.")

    while wrong_guesses < MAX_WRONG_GUESSES:
        print(f"\nWord: {display_word(secret_word, guessed_letters)}")
        print(f"Wrong guesses: {wrong_guesses}/{MAX_WRONG_GUESSES}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) or 'None'}")

        guess = input("Enter a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly one letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            wrong_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.")

        if all(letter in guessed_letters for letter in secret_word):
            print(f"\nYou win! The word was '{secret_word}'.")
            return

    print(f"\nGame over! The word was '{secret_word}'.")


if __name__ == "__main__":
    play()
