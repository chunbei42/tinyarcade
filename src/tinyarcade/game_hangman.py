import os
import random
import string
import time


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


EASY_WORDS = [
    "cat",
    "dog",
    "sun",
    "book",
    "apple",
    "house",
    "water",
    "happy",
    "green",
    "music",
]

NORMAL_WORDS = [
    "python",
    "github",
    "package",
    "terminal",
    "keyboard",
    "computer",
    "hangman",
    "library",
    "cityu",
    "student",
]

HARD_WORDS = [
    "algorithm",
    "repository",
    "debugging",
    "encryption",
    "framework",
    "interface",
    "javascript",
    "database",
    "variables",
    "exception",
]

DIFFICULTIES = {
    "1": ("Easy", EASY_WORDS, 5),
    "2": ("Normal", NORMAL_WORDS, 3),
    "3": ("Hard", HARD_WORDS, 0),
}

MAX_WRONG_GUESSES = 6

HANGMAN_STAGES = [
    """
      +---+
      |   |
          |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    """,
]


def choose_difficulty():
    while True:
        clear_screen()
        print("🎮 === HANGMAN === 🎮")
        print("Choose your difficulty:")

        print("\n[1] 🟢 Easy   - 5 hints")
        print("[2] 🟡 Normal - 3 hints")
        print("[3] 🔴 Hard   - 0 hints")
        print("[q] 🚪 Return to TinyArcade menu")

        choice = input("\n🎯 Choose a difficulty: ").strip().lower()

        if choice == "q":
            return None

        if choice in DIFFICULTIES:
            clear_screen()
            return DIFFICULTIES[choice]

        print("❌ Invalid choice. Please enter 1, 2, 3, or q.")


def choose_word(words):
    return random.choice(words)


def display_word(secret_word, guessed_letters):
    return " ".join(
        letter if letter in guessed_letters else "_"
        for letter in secret_word
    )


def show_hangman(wrong_guesses):
    print(HANGMAN_STAGES[wrong_guesses])


def get_hint_letter(secret_word, guessed_letters):
    alphabet = set(string.ascii_lowercase)
    letters_not_in_word = alphabet - set(secret_word)
    available_hints = letters_not_in_word - guessed_letters

    if not available_hints:
        return None

    return random.choice(sorted(available_hints))


def ask_for_hint(hints_left, secret_word, guessed_letters):
    if hints_left <= 0:
        print("🚫 You have no hints left.")
        return None

    hint_letter = get_hint_letter(secret_word, guessed_letters)

    if hint_letter is None:
        print("🤔 No useful hint is available.")
        return None

    print(f"💡 HINT: The letter '{hint_letter}' is NOT in the word.")
    return hint_letter


def play_round(difficulty_name, words, max_hints):
    secret_word = choose_word(words)
    guessed_letters = set()
    wrong_guesses = 0
    hints_left = max_hints

    print(f"🎮 === HANGMAN: {difficulty_name.upper()} === 🎮")
    print("🔤 Guess the secret word one letter at a time.")
    print(f"❤️ You can make {MAX_WRONG_GUESSES} wrong guesses.")
    print(f"💡 You have {max_hints} hint(s).")
    print("💬 Type 'hint' to reveal one letter that is not in the word.")
    print("🚪 Type 'quit' to return to the Hangman menu.")
    input("\n⏎ Press ENTER to start the game...")

    while wrong_guesses < MAX_WRONG_GUESSES:
        clear_screen()
        print(f"🔤 Word: {display_word(secret_word, guessed_letters)}")
        print(f"❌ Wrong guesses: {wrong_guesses}/{MAX_WRONG_GUESSES}")
        print(f"💡 Hints left: {hints_left}")
        print(
            "🔤 Guessed letters: "
            + (", ".join(sorted(guessed_letters)) if guessed_letters else "None")
        )

        show_hangman(wrong_guesses)

        guess = input(
            "\n🎯 Enter a letter, 'hint', or 'quit': "
        ).strip().lower()

        if guess == "quit":
            clear_screen()

            print("🚪 QUIT GAME")
            print("-----------------------------")
            print(f"🤫 The word was: {secret_word.upper()}")

            input("\n⏎ Press ENTER to continue...")

            return
        
        clear_screen()

        if guess == "hint":
            hint_letter = ask_for_hint(
                hints_left,
                secret_word,
                guessed_letters
            )

            if hint_letter is not None:
                hints_left -= 1
                guessed_letters.add(hint_letter)

            input("\n⏎ Press ENTER to continue...")
            continue

        if len(guess) != 1 or not guess.isalpha():
            print(
                "⚠️ Please enter one letter, 'hint', or 'quit'."
            )
            input("\n⏎ Press ENTER to continue...")
            continue

        if guess in guessed_letters:
            print("🔁 You already guessed that letter.")
            input("\n⏎ Press ENTER to continue...")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print("🎯 GUESS RESULT")
            print("-----------------------------")
            print(f"✅ '{guess}' is in the word!")

            input("\n⏎ Press ENTER to continue...")
        else:
            wrong_guesses += 1

            print("🎯 GUESS RESULT")
            print("-----------------------------")
            print(f"❌ '{guess}' is NOT in the word.")

            print("\n🎨 Drawing the hangman...")
            time.sleep(0.7)

            show_hangman(wrong_guesses)
            time.sleep(0.7)

            input("\n⏎ Press ENTER to continue...")
            

        if all(letter in guessed_letters for letter in secret_word):
            clear_screen()
            print("🎉🎉🎉 CONGRATULATIONS! 🎉🎉🎉")
            print(f"🏆 You guessed the word: {secret_word.upper()}")
            input("\n⏎ Press ENTER to continue...")
            clear_screen()
            return

    clear_screen()
    print("💀 GAME OVER 💀")
    print(f"😢 The word was: {secret_word.upper()}")
    show_hangman(MAX_WRONG_GUESSES)
    input("\n⏎ Press ENTER to continue...")
    clear_screen()


def ask_play_again():
    while True:
        print("🎮 What would you like to do?")
        print("[1] 🔁 Play Hangman again")
        print("[2] 🚪 Return to TinyArcade menu")

        choice = input("\n🎯 Choose an option: ").strip()

        if choice == "1":
            return True

        if choice == "2":
            return False

        print("❌ Invalid choice. Please enter 1 or 2.")


def play():
    while True:
        difficulty = choose_difficulty()

        if difficulty is None:
            break

        difficulty_name, words, max_hints = difficulty

        play_round(difficulty_name, words, max_hints)

        clear_screen()

        if not ask_play_again():
            break


if __name__ == "__main__":
    play()
